#!/usr/bin/env bash
# Prueba real del motor: simula 3 días laborables en una carpeta temporal (no toca ~/plan-90).
set -u
cd "$(dirname "$0")/.."
export PLAN90_DIR="$(mktemp -d)/plan-90"
p() { python3 motor/progreso.py "$@"; }
falla() { echo "FALLO: $*"; exit 1; }
echo "Carpeta temporal: $PLAN90_DIR"

echo; echo "== Antes de empezar"
p resumen && falla "resumen debería fallar sin plan empezado"

export PLAN90_HOY=2026-11-09   # lunes
echo; echo "== Empezar (lunes 9/11/2026)"
p empezar --negocio "Clínica de fisioterapia en Valencia" --facturacion "unos 18.000 €/mes" \
  --equipo "La dueña y 3 fisios" --objetivo "Dejar de contestar WhatsApp a las once de la noche" || falla empezar

echo; echo "== DÍA 1 · hoy"
p hoy | head -3
p hoy | grep -q "PASO 1 de 60" || falla "el día 1 no da el paso 1"
echo "-- hecho con casillas sin completar (debe negarse)"
p hecho --checklist 1,2; [ $? -eq 2 ] || falla "aceptó un paso con la checklist incompleta"
echo "-- hecho con la checklist completa"
p hecho --checklist 1,2,3,4 --nota "Media mensual sin IVA calculada" || falla hecho1

export PLAN90_HOY=2026-11-10   # martes
echo; echo "== DÍA 2 · hoy"
p hoy | head -2
p hoy | grep -q "PASO 2 de 60" || falla "el día 2 no avanza al paso 2"
p hecho --checklist 1,2,3,4 || falla hecho2

export PLAN90_HOY=2026-11-11   # miércoles
echo; echo "== DÍA 3 · hoy"
p hoy | grep -q "PASO 3 de 60" || falla "el día 3 no avanza al paso 3"
echo "-- saltar y deshacer"
p saltar --motivo "prueba" && p deshacer
p hoy | grep -q "PASO 3 de 60" || falla "deshacer no devuelve el paso 3"
p hecho --checklist 1,2,3,4 || falla hecho3
p hoy | grep -q "PASO 4 de 60" || falla "no avanza al paso 4"

echo; echo "== Resumen tras 3 días"
p resumen
p resumen | grep -q "vas al día" || falla "el ritmo debería ser 'vas al día'"

export PLAN90_HOY=2026-11-14   # sábado
echo; echo "== Sábado"
p hoy | head -1 | grep -q "fin de semana libre" || falla "no avisa del fin de semana"
p hoy | head -1

echo; echo "== Revisión de fase (forzando el resto de la fase 1)"
export PLAN90_HOY=2026-11-16
for i in $(seq 4 12); do p hecho --forzar --nota "simulado" > /dev/null || falla "forzar $i"; done
p hoy | grep -q "REVISIÓN DE FASE PENDIENTE" || falla "no pide la revisión de la fase 1"
p revision --fase 1 --nota "Fugas: WhatsApp sin contestar y cancelaciones" || falla revision
p hoy | grep -q "REVISIÓN DE FASE PENDIENTE" && falla "sigue pidiendo la revisión ya hecha"
p hoy | grep -q "PASO 13 de 60" || falla "no pasa a la fase 2"
p resumen | grep "Fase 1"

echo; echo "== progreso.json"
python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print('pasos resueltos:', len(d['pasos']), '· revisiones:', list(d['revisiones']))" "$PLAN90_DIR/progreso.json"
echo; echo "TODO OK"
