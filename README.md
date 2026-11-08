# Plan de 90 días para meter la IA en tu negocio

El plan exacto para meter la IA en un negocio, en el orden que funciona. **Cinco fases, sesenta pasos, noventa días: un paso al día, de lunes a viernes, fines de semana libres.**

1. **Medición**: saber tus números (ingresos, márgenes, embudo, tiempos y dónde se va tu tiempo).
2. **Operaciones**: documentar procesos, automatizar lo repetitivo y poner a Claude a trabajar con tu equipo.
3. **Captación**: CRM, respuesta rápida, seguimiento y un setter con IA.
4. **Crecimiento**: contenido, anuncios, referidos, ventas adicionales y retención.
5. **Libertad**: cuadro de mando, delegar, agentes que trabajan solos y una revisión semanal de una hora.

La mayoría de dueños se van directos al crecimiento y echan gasolina a un motor roto. Este plan empieza por el motor.

Cada paso trae el objetivo, la herramienta y el prompt listo para pegar, una checklist y el error típico para que no lo cometas. Solo te cuesta tu tiempo y unos 200 € al mes en herramientas como mucho (el desglose, con fecha, está en `PLAN.md`; sin contar lo que inviertas en anuncios).

## Qué hay dentro

| Archivo | Qué es |
|---|---|
| `PLAN.md` | El plan completo: 60 pasos con prompts, checklists y errores típicos |
| `pdf/Plan-90-dias.pdf` | El mismo plan en PDF para leer o pasárselo a cualquier IA |
| `SKILL.md` | La skill `/plan-90` para Claude: te guía día a día y guarda tu progreso |
| `motor/progreso.py` | El motor del progreso (Python, sin dependencias) |

## Tres formas de usarlo

### 1. Con Claude Code (la skill te guía cada día)

```bash
git clone https://github.com/deniscorral3am/plan-skill ~/.claude/skills/plan-90
```

Abre Claude Code y escribe `/plan-90` o «qué toca hoy del plan». La primera vez te hace 4 preguntas sobre tu negocio; desde ahí, cada día te da el paso que toca adaptado a ti, comprueba la checklist antes de darlo por hecho y hace una revisión al final de cada fase. Tu progreso se guarda en `~/plan-90/progreso.json`.

### 2. Pasándole el PDF a cualquier IA

Sube `pdf/Plan-90-dias.pdf` a Claude, ChatGPT o la IA que uses y escribe:

> Eres mi guía para este plan. Pregúntame lo que necesites de mi negocio y dame cada día el paso que toca, adaptado a mí. No pases al siguiente hasta que te confirme la checklist.

### 3. Leyéndolo tú

Abre el PDF y haz un paso al día. Los prompts están listos para copiar y pegar.

## El motor, a mano

```bash
python3 motor/progreso.py empezar --negocio "..." --facturacion "..." --equipo "..." --objetivo "..."
python3 motor/progreso.py hoy                          # el paso de hoy
python3 motor/progreso.py hecho --checklist 1,2,3,4    # marcarlo (exige la checklist completa)
python3 motor/progreso.py saltar --motivo "..."        # si no aplica a tu negocio
python3 motor/progreso.py resumen                      # cómo vas
```

Otros: `paso N`, `revision --fase N`, `deshacer`, `perfil`. Para regenerar el PDF: `python3 motor/pdf.py` (necesita Google Chrome). Para comprobar el plan: `python3 motor/contar_pasos.py` y `bash motor/prueba.sh`.

---

Hecha por Denis Corral · Sell Your AI (https://sellyourai.io) · Licencia MIT
