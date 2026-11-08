#!/usr/bin/env python3
"""Progreso del Plan de 90 días (Sell Your AI). Solo biblioteca estándar.

Uso:
  progreso.py empezar --negocio "..." --facturacion "..." --equipo "..." --objetivo "..." [--inicio AAAA-MM-DD]
  progreso.py hoy                 Paso que toca hoy (completo)
  progreso.py hecho [--checklist 1,2,3] [--nota "..."] [--forzar]
  progreso.py saltar [--motivo "..."]
  progreso.py revision --fase N [--nota "..."]
  progreso.py deshacer            Deshace la última acción (hecho o saltar)
  progreso.py paso N              Muestra cualquier paso
  progreso.py resumen             Progreso por fase y ritmo
  progreso.py perfil              Datos del negocio guardados

Variables de entorno:
  PLAN90_DIR   carpeta del progreso (por defecto ~/plan-90)
  PLAN90_HOY   fecha de hoy simulada (AAAA-MM-DD), para pruebas
  PLAN90_PLAN  ruta a PLAN.md (por defecto, la del repositorio)
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
PLAN = os.environ.get("PLAN90_PLAN") or os.path.join(AQUI, "..", "PLAN.md")
DIR = os.path.expanduser(os.environ.get("PLAN90_DIR") or "~/plan-90")
ARCHIVO = os.path.join(DIR, "progreso.json")
FASES = {1: "Medición", 2: "Operaciones", 3: "Captación", 4: "Crecimiento", 5: "Libertad"}
TOTAL = 60
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def hoy():
    f = os.environ.get("PLAN90_HOY")
    return dt.date.fromisoformat(f) if f else dt.date.today()


def fase_de(n):
    return (n - 1) // 12 + 1


# ---------- PLAN.md ----------
def leer_pasos():
    if not os.path.exists(PLAN):
        sys.exit(f"No encuentro PLAN.md en {PLAN}")
    texto = open(PLAN, encoding="utf-8").read()
    partes = re.split(r"(?m)^### Paso (\d+) · (.+)$", texto)
    pasos = {}
    for i in range(1, len(partes), 3):
        n, titulo, cuerpo = int(partes[i]), partes[i + 1].strip(), partes[i + 2]
        cuerpo = re.split(r"(?m)^## ", cuerpo)[0]  # corta antes de la siguiente fase
        cuerpo = cuerpo.strip().rstrip("-").strip()
        checklist = re.findall(r"(?m)^- \[ \] (.+)$", cuerpo)
        pasos[n] = {"titulo": titulo, "cuerpo": cuerpo, "checklist": checklist}
    return pasos


# ---------- progreso.json ----------
def cargar(obligatorio=True):
    if not os.path.exists(ARCHIVO):
        if obligatorio:
            sys.exit("Aún no has empezado. Ejecuta primero: progreso.py empezar --negocio ... (ver --help)")
        return None
    with open(ARCHIVO, encoding="utf-8") as f:
        return json.load(f)


def guardar(datos):
    os.makedirs(DIR, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=DIR, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    os.replace(tmp, ARCHIVO)


def actual(datos):
    for n in range(1, TOTAL + 1):
        if str(n) not in datos["pasos"]:
            return n
    return None


def laborables(desde, hasta):
    """Días de lunes a viernes entre dos fechas, ambas incluidas."""
    if hasta < desde:
        return 0
    d, c = desde, 0
    while d <= hasta:
        if d.weekday() < 5:
            c += 1
        d += dt.timedelta(days=1)
    return c


def revision_pendiente(datos):
    for f in range(1, 6):
        ultimo = f * 12
        if all(str(n) in datos["pasos"] for n in range(ultimo - 11, ultimo + 1)) and str(f) not in datos["revisiones"]:
            return f
    return None


# ---------- comandos ----------
def cmd_empezar(a):
    if cargar(obligatorio=False) and not a.reiniciar:
        sys.exit(f"Ya hay un plan empezado en {ARCHIVO}. Usa --reiniciar para empezar de cero (se pierde el progreso).")
    inicio = dt.date.fromisoformat(a.inicio) if a.inicio else hoy()
    datos = {
        "version": 1,
        "inicio": inicio.isoformat(),
        "negocio": {"negocio": a.negocio, "facturacion": a.facturacion, "equipo": a.equipo, "objetivo": a.objetivo},
        "pasos": {},
        "revisiones": {},
        "historial": [],
    }
    guardar(datos)
    print(f"Plan empezado el {inicio.isoformat()} ({DIAS[inicio.weekday()]}). Progreso en {ARCHIVO}")
    print("Siguiente: progreso.py hoy")


def cmd_hoy(a):
    datos, pasos = cargar(), leer_pasos()
    f = hoy()
    pend = revision_pendiente(datos)
    if pend:
        print(f"REVISIÓN DE FASE PENDIENTE: has terminado la fase {pend} · {FASES[pend]}. "
              f"Haz la revisión y regístrala con: progreso.py revision --fase {pend} --nota \"...\"\n")
    n = actual(datos)
    if n is None:
        print("Has terminado los 60 pasos. Haz la revisión final (paso 60) y fija los siguientes 90 días.")
        return
    if f.weekday() >= 5:
        print(f"Hoy es {DIAS[f.weekday()]}: fin de semana libre. El lunes toca este paso:\n")
    hechos_hoy = sum(1 for h in datos["historial"] if h["fecha"] == f.isoformat() and h["accion"] == "hecho")
    if hechos_hoy:
        print(f"(Hoy ya has hecho {hechos_hoy} paso{'s' if hechos_hoy > 1 else ''}. El plan es uno al día; si sigues, que sea con calma.)\n")
    p = pasos[n]
    print(f"PASO {n} de {TOTAL} · Fase {fase_de(n)} · {FASES[fase_de(n)]}")
    print(f"{p['titulo']}\n")
    print(p["cuerpo"])
    print(f"\nCuando lo termines: progreso.py hecho --checklist {','.join(str(i + 1) for i in range(len(p['checklist'])))}")


def cmd_hecho(a, accion="hecho"):
    datos, pasos = cargar(), leer_pasos()
    n = actual(datos)
    if n is None:
        sys.exit("No queda ningún paso pendiente.")
    p = pasos[n]
    marcadas = []
    if accion == "hecho":
        total = len(p["checklist"])
        if a.checklist:
            try:
                marcadas = sorted({int(x) for x in a.checklist.split(",") if x.strip()})
            except ValueError:
                sys.exit("--checklist debe ser una lista de números, por ejemplo 1,2,3")
            fuera = [x for x in marcadas if not 1 <= x <= total]
            if fuera:
                sys.exit(f"El paso {n} tiene {total} casillas; no existen: {fuera}")
        faltan = [i for i in range(1, total + 1) if i not in marcadas]
        if faltan and not a.forzar:
            print(f"El paso {n} no está completo. Faltan estas casillas:")
            for i in faltan:
                print(f"  [{i}] {p['checklist'][i - 1]}")
            print("Termínalas y vuelve a marcarlo, o usa --forzar si de verdad no aplican a tu negocio.")
            sys.exit(2)
    f = hoy().isoformat()
    datos["pasos"][str(n)] = {"estado": accion, "fecha": f, "checklist": marcadas,
                              "nota": getattr(a, "nota", None) or getattr(a, "motivo", None)}
    datos["historial"].append({"fecha": f, "accion": accion, "paso": n})
    guardar(datos)
    verbo = "hecho" if accion == "hecho" else "saltado"
    print(f"Paso {n} {verbo}: {p['titulo']}")
    if n % 12 == 0:
        fa = fase_de(n)
        print(f"\nFin de la fase {fa} · {FASES[fa]}. Toca la revisión de fase antes de seguir "
              f"(progreso.py revision --fase {fa} --nota \"...\").")
    sig = actual(datos)
    if sig:
        print(f"Siguiente (próximo día laborable): paso {sig} · {pasos[sig]['titulo']}")
    else:
        print("Has terminado los 60 pasos.")


def cmd_saltar(a):
    cmd_hecho(a, accion="saltado")


def cmd_revision(a):
    datos = cargar()
    if a.fase not in FASES:
        sys.exit("La fase va de 1 a 5.")
    datos["revisiones"][str(a.fase)] = {"fecha": hoy().isoformat(), "nota": a.nota}
    datos["historial"].append({"fecha": hoy().isoformat(), "accion": "revision", "fase": a.fase})
    guardar(datos)
    print(f"Revisión de la fase {a.fase} · {FASES[a.fase]} registrada.")


def cmd_deshacer(a):
    datos = cargar()
    for i in range(len(datos["historial"]) - 1, -1, -1):
        h = datos["historial"][i]
        if h["accion"] in ("hecho", "saltado"):
            datos["pasos"].pop(str(h["paso"]), None)
            datos["historial"].pop(i)
            guardar(datos)
            print(f"Deshecho: el paso {h['paso']} vuelve a estar pendiente.")
            return
    print("No hay nada que deshacer.")


def cmd_paso(a):
    pasos = leer_pasos()
    if a.n not in pasos:
        sys.exit("El paso va de 1 a 60.")
    p = pasos[a.n]
    print(f"PASO {a.n} · Fase {fase_de(a.n)} · {FASES[fase_de(a.n)]}\n{p['titulo']}\n\n{p['cuerpo']}")


def cmd_resumen(a):
    datos = cargar()
    f = hoy()
    inicio = dt.date.fromisoformat(datos["inicio"])
    resueltos = len(datos["pasos"])
    hechos = sum(1 for v in datos["pasos"].values() if v["estado"] == "hecho")
    saltados = resueltos - hechos
    esperados = min(TOTAL, laborables(inicio, f))
    print(f"Plan de 90 días · empezado el {inicio.isoformat()} · hoy {f.isoformat()} ({DIAS[f.weekday()]})")
    print(f"Pasos: {hechos} hechos, {saltados} saltados, {TOTAL - resueltos} pendientes ({resueltos * 100 // TOTAL} %)\n")
    for fa, nombre in FASES.items():
        rango = range((fa - 1) * 12 + 1, fa * 12 + 1)
        h = sum(1 for n in rango if datos["pasos"].get(str(n), {}).get("estado") == "hecho")
        s = sum(1 for n in rango if datos["pasos"].get(str(n), {}).get("estado") == "saltado")
        barra = "".join("#" if datos["pasos"].get(str(n), {}).get("estado") == "hecho"
                        else ("~" if str(n) in datos["pasos"] else ".") for n in rango)
        rev = " · revisión hecha" if str(fa) in datos["revisiones"] else ""
        print(f"  Fase {fa} {nombre:<12} [{barra}] {h}/12" + (f" ({s} saltados)" if s else "") + rev)
    dif = resueltos - esperados
    if dif == 0:
        ritmo = "vas al día"
    elif dif > 0:
        ritmo = f"vas {dif} paso{'s' if dif > 1 else ''} por delante"
    else:
        ritmo = f"vas {-dif} paso{'s' if dif < -1 else ''} por detrás (sin drama: retoma con el de hoy)"
    print(f"\nDías laborables desde el inicio: {laborables(inicio, f)} · {ritmo}")
    n = actual(datos)
    if n:
        print(f"Toca: paso {n} · {leer_pasos()[n]['titulo']}")
    pend = revision_pendiente(datos)
    if pend:
        print(f"Pendiente: revisión de la fase {pend} · {FASES[pend]}")


def cmd_perfil(a):
    datos = cargar()
    for k, v in datos["negocio"].items():
        print(f"{k}: {v}")


def main():
    ap = argparse.ArgumentParser(description="Progreso del Plan de 90 días (Sell Your AI)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("empezar")
    e.add_argument("--negocio", required=True, help="A qué se dedica el negocio")
    e.add_argument("--facturacion", required=True, help="Facturación aproximada al mes")
    e.add_argument("--equipo", required=True, help="Quién trabaja en el negocio")
    e.add_argument("--objetivo", required=True, help="Qué quiere conseguir en 90 días o qué más le frena")
    e.add_argument("--inicio", help="Fecha de inicio AAAA-MM-DD (por defecto hoy)")
    e.add_argument("--reiniciar", action="store_true")
    sub.add_parser("hoy")
    h = sub.add_parser("hecho")
    h.add_argument("--checklist", help="Casillas completadas, por ejemplo 1,2,3,4")
    h.add_argument("--nota")
    h.add_argument("--forzar", action="store_true", help="Marcar hecho aunque falten casillas")
    s = sub.add_parser("saltar")
    s.add_argument("--motivo")
    r = sub.add_parser("revision")
    r.add_argument("--fase", type=int, required=True)
    r.add_argument("--nota")
    sub.add_parser("deshacer")
    p = sub.add_parser("paso")
    p.add_argument("n", type=int)
    sub.add_parser("resumen")
    sub.add_parser("perfil")
    a = ap.parse_args()
    {"empezar": cmd_empezar, "hoy": cmd_hoy, "hecho": cmd_hecho, "saltar": cmd_saltar,
     "revision": cmd_revision, "deshacer": cmd_deshacer, "paso": cmd_paso,
     "resumen": cmd_resumen, "perfil": cmd_perfil}[a.cmd](a)


if __name__ == "__main__":
    main()
