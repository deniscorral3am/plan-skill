# Probado

Fecha: 8 de noviembre de 2026 · macOS · Python 3 (solo biblioteca estándar) · Google Chrome headless.

| Prueba | Cómo | Resultado |
|---|---|---|
| 60 pasos exactos | `python3 motor/contar_pasos.py` | OK: 60 pasos numerados del 1 al 60, 5 fases × 12; cada paso con objetivo, cómo con IA, prompt, checklist de 3 a 5 casillas, error típico, tiempo y día de la semana correcto |
| Motor, 3 días simulados | `bash motor/prueba.sh` (carpeta temporal, fechas simuladas con `PLAN90_HOY`; no toca `~/plan-90`) | OK: lunes da el paso 1 → hecho → martes da el paso 2 → hecho → miércoles da el paso 3 → hecho → siguiente paso 4; resumen «vas al día» |
| Checklist obligatoria | `hecho --checklist 1,2` en un paso de 4 casillas | OK: se niega (código 2) y lista las casillas que faltan |
| Saltar y deshacer | `saltar` y `deshacer` en el paso 3 | OK: el paso 3 vuelve a estar pendiente |
| Fin de semana | fecha simulada sábado | OK: «fin de semana libre» y el paso del lunes |
| Revisión de fase | fase 1 completa | OK: aviso «REVISIÓN DE FASE PENDIENTE»; tras `revision --fase 1` pasa al paso 13 |
| Sin plan empezado | `resumen` antes de `empezar` | OK: mensaje claro y código de error |
| PDF | `python3 motor/pdf.py` | OK: `pdf/Plan-90-dias.pdf`, 43 páginas A4, se abre (pdfinfo y pdftotext), Inter incrustada, portada negra con dorado, fases en negro y pasos en papel |
| Ortografía | corrector de macOS en español sobre PLAN.md y SKILL.md | OK: solo marca nombres de producto y anglicismos de uso habitual (leads, prompt, checklist, skill, pipeline); sin voseo |

Precios de herramientas consultados el 8/11/2026 (páginas de precios y comparativas de 2026): Claude Pro 20 $ + IVA (unos 22 €), n8n Cloud Starter 24 €/mes (20 € anual), HubSpot Starter unos 20 €/usuario (hay plan gratuito), ManyChat Pro 39 $/mes (29 $ anual). API de Claude con tope de 30 €. Total: 130-150 €/mes; unos 200 € con margen.
