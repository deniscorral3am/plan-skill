#!/usr/bin/env python3
"""Comprueba que PLAN.md tiene exactamente 60 pasos bien formados (5 fases x 12)."""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PLAN = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "..", "PLAN.md")
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes"]
CAMPOS = ["**Objetivo:**", "**Cómo hacerlo con IA:**", "```text", "**Checklist:**", "**Error típico:**"]

texto = open(PLAN, encoding="utf-8").read()
partes = re.split(r"(?m)^### Paso (\d+) · (.+)$", texto)
nums = [int(partes[i]) for i in range(1, len(partes), 3)]
errores = []
if nums != list(range(1, 61)):
    errores.append(f"Numeración incorrecta: {nums}")
fases = re.findall(r"(?m)^## Fase (\d) · ", texto)
if fases != ["1", "2", "3", "4", "5"]:
    errores.append(f"Fases encontradas: {fases}")
for i in range(1, len(partes), 3):
    n, cuerpo = int(partes[i]), re.split(r"(?m)^## ", partes[i + 2])[0]
    for c in CAMPOS:
        if c not in cuerpo:
            errores.append(f"Paso {n}: falta {c}")
    casillas = len(re.findall(r"(?m)^- \[ \] ", cuerpo))
    if not 3 <= casillas <= 5:
        errores.append(f"Paso {n}: {casillas} casillas (deben ser 3-5)")
    meta = f"*Fase {(n - 1) // 12 + 1} · Semana {(n - 1) // 5 + 1}, {DIAS[(n - 1) % 5]} · "
    if meta not in cuerpo:
        errores.append(f"Paso {n}: cabecera de fase/semana/día/tiempo incorrecta (esperaba {meta!r})")
    if cuerpo.count("```") % 2:
        errores.append(f"Paso {n}: bloque de código sin cerrar")

print(f"Pasos encontrados: {len(nums)} · fases: {len(fases)}")
if errores:
    print("ERRORES:")
    print("\n".join("  " + e for e in errores))
    sys.exit(1)
print("OK: 60 pasos, 5 fases x 12, todos con objetivo, cómo con IA, prompt, checklist (3-5), error típico, tiempo y día.")
