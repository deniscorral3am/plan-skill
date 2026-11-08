#!/usr/bin/env python3
"""Genera plan-90-dias.html y Plan-90-dias.pdf a partir de PLAN.md (solo biblioteca estándar + Chrome headless).

Uso: python3 motor/pdf.py [--sin-pdf]
"""
import html
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, ".."))
PLAN = os.path.join(RAIZ, "PLAN.md")
HTML_OUT = os.path.join(RAIZ, "pdf", "plan-90-dias.html")
PDF_OUT = os.path.join(RAIZ, "pdf", "Plan-90-dias.pdf")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(https?://[^\s<)]+[^\s<).,])", r'<a href="\1">\1</a>', t)
    return t


def convertir(md):
    lineas = md.split("\n")
    # Saltar título, subtítulo y firma: van en la portada.
    i = next(k for k, l in enumerate(lineas) if l.strip() == "---") + 1
    out, lista, tabla, en_paso, en_fase = [], None, [], False, False

    def cerrar_lista():
        nonlocal lista
        if lista:
            out.append(f"</{lista}>")
            lista = None

    def cerrar_tabla():
        nonlocal tabla
        if tabla:
            filas = [[c.strip() for c in f.strip().strip("|").split("|")] for f in tabla
                     if not re.match(r"^\|[\s\-|]+\|$", f.strip())]
            h = "".join(f"<th>{inline(c)}</th>" for c in filas[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in f) + "</tr>" for f in filas[1:])
            out.append(f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>")
            tabla = []

    def cerrar_paso():
        nonlocal en_paso
        if en_paso:
            out.append("</section>")
            en_paso = False

    while i < len(lineas):
        l = lineas[i]
        s = l.strip()
        if s.startswith("```"):
            cerrar_lista(); cerrar_tabla()
            bloque = []
            i += 1
            while not lineas[i].strip().startswith("```"):
                bloque.append(lineas[i]); i += 1
            out.append('<div class="prompt"><span class="etq">Prompt para pegar</span><pre>'
                       + html.escape("\n".join(bloque)) + "</pre></div>")
        elif s.startswith("|"):
            cerrar_lista(); tabla.append(s)
        elif s == "---" or s == "":
            cerrar_lista(); cerrar_tabla()
        elif s.startswith("## "):
            cerrar_lista(); cerrar_tabla(); cerrar_paso()
            m = re.match(r"## Fase (\d) · (.+)", s)
            if m:
                intro = []
                i += 1
                while i < len(lineas) and not lineas[i].startswith("### "):
                    if lineas[i].strip():
                        intro.append(lineas[i].strip())
                    i += 1
                n = int(m.group(1))
                out.append(f'<section class="fase"><div class="fase-num">Fase {n} de 5</div>'
                           f'<h2>{inline(m.group(2))}</h2><div class="fase-pasos">Pasos {(n-1)*12+1} a {n*12}</div>'
                           f'<p class="fase-intro">{inline(" ".join(intro))}</p></section>')
                continue
            out.append(f'<h2 class="seccion">{inline(s[3:])}</h2>')
        elif s.startswith("### Paso"):
            cerrar_lista(); cerrar_tabla(); cerrar_paso()
            m = re.match(r"### Paso (\d+) · (.+)", s)
            out.append(f'<section class="paso"><div class="paso-num">{m.group(1)}</div>'
                       f'<h3>{inline(m.group(2))}</h3>')
            en_paso = True
        elif s.startswith("### "):
            cerrar_lista(); cerrar_tabla()
            out.append(f"<h3 class='sub'>{inline(s[4:])}</h3>")
        elif s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            out.append(f'<div class="meta">{inline(s[1:-1])}</div>')
        elif s.startswith("- [ ] "):
            if lista != "ul class=\"check\"":
                cerrar_lista(); out.append('<ul class="check">'); lista = 'ul class="check"'
            out.append(f"<li>{inline(s[6:])}</li>")
        elif s.startswith("- "):
            if lista != "ul":
                cerrar_lista(); out.append("<ul>"); lista = "ul"
            out.append(f"<li>{inline(s[2:])}</li>")
        elif re.match(r"^\d+\. ", s):
            if lista != "ol":
                cerrar_lista(); out.append("<ol>"); lista = "ol"
            item = re.sub(r"^\d+\. ", "", s)
            out.append(f"<li>{inline(item)}</li>")
        else:
            cerrar_lista()
            cls = ' class="error"' if s.startswith("**Error típico:**") else ""
            out.append(f"<p{cls}>{inline(s)}</p>")
        i += 1
    cerrar_lista(); cerrar_tabla(); cerrar_paso()
    # Las listas cierran con su etiqueta base
    return "\n".join(out).replace('</ul class="check">', "</ul>")


CSS = """
@page { size: A4; margin: 18mm 17mm 18mm 17mm; }
@page portada { margin: 0; }
:root { --negro:#0E0E0D; --papel:#F4F1EA; --oro:#A8884A; --gris:#5b5850; --linea:#d9d3c5; }
* { box-sizing: border-box; }
html { background: var(--papel); }
body { margin:0; font-family: 'Inter', -apple-system, 'Helvetica Neue', Arial, sans-serif; color: var(--negro);
  background: var(--papel); font-size: 10pt; line-height: 1.5; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
a { color: var(--oro); text-decoration: none; }
.portada { page: portada; width: 210mm; height: 297mm; background: var(--negro); color: var(--papel);
  padding: 26mm 22mm; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; }
.portada .marca { letter-spacing: .32em; text-transform: uppercase; font-size: 9pt; color: var(--oro); font-weight: 600; }
.portada h1 { font-size: 44pt; line-height: 1.02; letter-spacing: -0.035em; font-weight: 700; margin: 0 0 10mm; }
.portada h1 span { color: var(--oro); }
.portada .bajada { font-size: 13pt; color: #cfc9bc; max-width: 140mm; font-weight: 400; }
.portada .cifras { display: flex; gap: 12mm; margin-top: 14mm; }
.portada .cifras div { border-top: 1px solid var(--oro); padding-top: 3mm; }
.portada .cifras b { display:block; font-size: 26pt; font-weight: 700; letter-spacing: -0.03em; }
.portada .cifras small { color: #a9a395; font-size: 9pt; text-transform: uppercase; letter-spacing: .12em; }
.portada .orden { font-size: 9.5pt; color: #a9a395; letter-spacing: .04em; }
.portada .orden b { color: var(--papel); font-weight: 600; }
.portada .pie { display:flex; justify-content: space-between; align-items: flex-end; font-size: 9pt; color: #a9a395; }
.portada .pie strong { color: var(--papel); font-size: 12pt; letter-spacing: -0.01em; }
.contenido h2.seccion { font-size: 20pt; letter-spacing: -0.03em; margin: 8mm 0 3mm; }
.contenido h3.sub { font-size: 12.5pt; margin: 6mm 0 2mm; letter-spacing: -0.01em; }
.contenido h2.seccion:first-child { margin-top: 0; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0 4mm; font-size: 9pt; page-break-inside: avoid; }
th { text-align: left; background: var(--negro); color: var(--papel); font-weight: 600; padding: 2mm 2.5mm; }
td { border-bottom: 1px solid var(--linea); padding: 2mm 2.5mm; vertical-align: top; }
.fase { page-break-before: always; background: var(--negro); color: var(--papel); border-radius: 4mm;
  padding: 16mm 14mm; margin-bottom: 8mm; }
.fase-num { color: var(--oro); letter-spacing: .3em; text-transform: uppercase; font-size: 9pt; font-weight: 600; }
.fase h2 { font-size: 40pt; letter-spacing: -0.04em; margin: 3mm 0 1mm; line-height: 1; }
.fase-pasos { color: #a9a395; font-size: 10pt; margin-bottom: 6mm; }
.fase-intro { font-size: 11.5pt; color: #e3ded2; max-width: 150mm; margin: 0; }
.paso { position: relative; border-top: 2px solid var(--negro); padding: 4mm 0 2mm 16mm; margin: 0 0 6mm; }
.paso h3 { font-size: 14pt; letter-spacing: -0.02em; line-height: 1.2; margin: 0 0 1mm; page-break-after: avoid; }
.paso-num { position: absolute; left: 0; top: 4mm; width: 11mm; height: 11mm; border-radius: 50%;
  background: var(--oro); color: var(--negro); font-weight: 700; font-size: 11pt; display:flex; align-items:center; justify-content:center; }
.meta { color: var(--oro); font-size: 8.5pt; font-weight: 600; letter-spacing: .04em; text-transform: uppercase; margin-bottom: 2.5mm; }
.paso p { margin: 0 0 2mm; }
.prompt { background: var(--negro); color: var(--papel); border-radius: 2.5mm; padding: 3mm 4mm 3.5mm; margin: 1mm 0 3mm; page-break-inside: avoid; }
.prompt .etq { display:block; color: var(--oro); font-size: 7.5pt; letter-spacing: .2em; text-transform: uppercase; font-weight: 600; margin-bottom: 1.5mm; }
.prompt pre { margin: 0; white-space: pre-wrap; font-family: 'Inter', -apple-system, sans-serif; font-size: 8.8pt; line-height: 1.45; }
ul, ol { margin: 0 0 2.5mm; padding-left: 5mm; }
ul.check { list-style: none; padding-left: 0; page-break-inside: avoid; }
ul.check li { position: relative; padding-left: 6mm; margin-bottom: 1mm; }
ul.check li::before { content: ""; position: absolute; left: 0; top: 1.1mm; width: 3.2mm; height: 3.2mm; border: 1.3px solid var(--oro); border-radius: .7mm; }
p.error { border-left: 3px solid var(--oro); background: #ebe5d8; padding: 2mm 3mm; border-radius: 0 2mm 2mm 0; }
code { background: #e7e1d3; padding: 0 1mm; border-radius: 1mm; font-size: 9pt; }
strong { font-weight: 650; }
"""


def portada():
    return """
<section class="portada">
  <div class="marca">Sell Your AI · Recurso gratuito</div>
  <div>
    <h1>Plan de 90 días para meter la IA <span>en tu negocio</span></h1>
    <div class="bajada">El orden exacto, paso a paso, con la herramienta, el prompt listo para pegar, la checklist y el error típico de cada día.</div>
    <div class="cifras">
      <div><b>5</b><small>fases</small></div>
      <div><b>60</b><small>pasos</small></div>
      <div><b>90</b><small>días</small></div>
    </div>
  </div>
  <div class="orden"><b>Medición</b> → <b>Operaciones</b> → <b>Captación</b> → <b>Crecimiento</b> → <b>Libertad</b><br>Un paso al día, de lunes a viernes. Fines de semana libres.</div>
  <div class="pie"><div><strong>Sell Your AI</strong><br>Hecho por Denis Corral</div><div>sellyourai.io</div></div>
</section>"""


def main():
    md = open(PLAN, encoding="utf-8").read()
    cuerpo = convertir(md)
    doc = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>Plan de 90 días para meter la IA en tu negocio · Sell Your AI</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{portada()}<main class="contenido">{cuerpo}</main></body></html>"""
    os.makedirs(os.path.dirname(HTML_OUT), exist_ok=True)
    open(HTML_OUT, "w", encoding="utf-8").write(doc)
    print("HTML:", HTML_OUT)
    if "--sin-pdf" in sys.argv:
        return
    if not os.path.exists(CHROME):
        sys.exit("No encuentro Google Chrome; abre el HTML y usa Imprimir > Guardar como PDF.")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=10000", f"--print-to-pdf={PDF_OUT}", "file://" + HTML_OUT],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("PDF:", PDF_OUT, f"({os.path.getsize(PDF_OUT) // 1024} KB)")


if __name__ == "__main__":
    main()
