# Plan de 90 días para meter la IA en tu negocio

**Cinco fases, sesenta pasos, noventa días. Un paso al día, de lunes a viernes. Fines de semana libres.**

Hecho por Denis Corral · Sell Your AI (https://sellyourai.io)

---

## Antes de empezar

La mayoría de dueños de negocio empiezan la IA por el final: anuncios, contenido, más clientes. Es echar gasolina a un motor roto. Si no sabes tus números, si tus procesos viven en tu cabeza y si los leads se te enfrían en el WhatsApp, más clientes solo traen más caos.

Este plan va en el orden contrario, el que funciona:

1. **Medición** (pasos 1 a 12): saber tus números de verdad.
2. **Operaciones** (pasos 13 a 24): que el negocio funcione sin que lo sostengas tú a mano.
3. **Captación** (pasos 25 a 36): que ningún lead se pierda por no contestar a tiempo.
4. **Crecimiento** (pasos 37 a 48): ahora sí, más clientes y que se queden.
5. **Libertad** (pasos 49 a 60): que el negocio te dé tiempo para decidir, no que te lo quite.

### Cómo se usa

- **Un paso al día, de lunes a viernes.** 12 semanas = 60 días laborables, unos 90 días naturales. Los fines de semana no se toca.
- **Cada paso trae lo mismo:** objetivo, cómo hacerlo con IA (la herramienta y el prompt listo para pegar), una checklist y el error típico para que no lo cometas. El tiempo estimado está al lado del título.
- **Si un paso no aplica a tu negocio,** adáptalo o sáltalo y sigue. Mejor un paso adaptado hecho que uno perfecto pendiente.
- **Si no te apetece leerlo,** pásale este documento entero a tu IA (Claude, ChatGPT o la que uses) y dile: «Eres mi guía para este plan. Pregúntame lo que necesites de mi negocio y dame cada día el paso que toca». Si usas Claude Code, instala la skill y lo hace ella sola (mira el README).
- **En los prompts,** lo que va entre corchetes `[así]` lo cambias por tus datos. Antes de pegar datos de clientes en cualquier IA, quita nombres, teléfonos y DNI si no hacen falta.

### Calendario

| Semanas | Fase | Pasos |
|---|---|---|
| 1 a 3 (hasta el martes) | 1 · Medición | 1 a 12 |
| 3 (miércoles) a 5 (jueves) | 2 · Operaciones | 13 a 24 |
| 5 (viernes) a 8 (lunes) | 3 · Captación | 25 a 36 |
| 8 (martes) a 10 (miércoles) | 4 · Crecimiento | 37 a 48 |
| 10 (jueves) a 12 (viernes) | 5 · Libertad | 49 a 60 |

### Herramientas y lo que cuestan

Solo te cuesta tu tiempo y las herramientas. Precios aproximados consultados el 8 de noviembre de 2026 en las páginas de precios y en comparativas de 2026. Cambian a menudo y dependen del país y de si pagas al mes o al año: compruébalos antes de contratar.

| Herramienta | Para qué | Precio aproximado al mes |
|---|---|---|
| Claude Pro | El cerebro de todo: análisis, documentos, skills, Claude Code | 20 $ + IVA, unos 22 € |
| n8n Cloud Starter | Automatizaciones que conectan tus herramientas | 24 € (20 € pagando al año). Alternativa: instalarlo en un servidor propio por unos 5-10 € |
| HubSpot Sales Hub Starter | CRM: dónde vive cada lead y cada cliente | unos 20 € por usuario (hay plan gratuito para empezar) |
| ManyChat Pro | Responder en Instagram, Facebook y WhatsApp de forma automática | 39 $ (unos 34 €) con 2.500 contactos activos; 29 $ pagando al año |
| API de Claude (pago por uso) | Que tus automatizaciones y agentes piensen solos | pon un tope de 30 € al mes en la consola de Anthropic |
| Google Sheets y Looker Studio | Hojas de números y cuadro de mando | gratis con cuenta de Google |
| Fathom | Grabar y resumir llamadas | plan gratuito |

**Total: entre 130 y 150 € al mes** con un solo usuario en el CRM, o unos 100 € si empiezas con HubSpot gratis y n8n en tu propio servidor. Con margen para más consumo de API, más usuarios o una herramienta de diseño, te quedas en **unos 200 € al mes**. No incluye lo que inviertas en anuncios (paso 43): eso es presupuesto de publicidad, aparte.

### Una regla antes del paso 1

La IA se equivoca. Revisa siempre lo que te devuelve antes de mandarlo a un cliente, y no dejes que ningún agente cobre, pague, borre o envíe nada importante sin tu permiso hasta que lleve semanas funcionando bien (lo verás en la fase 5).

---
## Fase 1 · Medición

Sin números, cualquier decisión es una opinión. En estas dos semanas y media vas a saber cuánto ganas de verdad, qué te deja cada cosa que vendes, por dónde entran los clientes y, sobre todo, dónde se te va el tiempo. Al final tendrás tus tres fugas más caras: lo que vas a arreglar con IA en el resto del plan.

### Paso 1 · Tus ingresos reales de los últimos 12 meses
*Fase 1 · Semana 1, lunes · 45 min*

**Objetivo:** tener en una sola hoja lo que ha entrado cada mes durante el último año, separado por producto o servicio.

**Cómo hacerlo con IA:** descarga de tu banco o de tu programa de facturación los movimientos o facturas del último año en CSV o Excel. Ábrelo en Claude (arrastra el archivo al chat) y pega este prompt. Pide que te devuelva la tabla y pásala a Google Sheets.

```text
Te paso las facturas/movimientos de mi negocio de los últimos 12 meses. Mi negocio es [qué vendes].
1. Quédate solo con los ingresos de clientes (quita traspasos, devoluciones de Hacienda, préstamos).
2. Agrúpalos por mes y por producto o servicio: [lista de lo que vendes].
3. Devuélveme una tabla: mes | servicio | ingresos sin IVA | número de ventas.
4. Debajo, el total del año, la media mensual, el mejor y el peor mes.
Si hay movimientos que no sabes clasificar, ponlos aparte en una lista y pregúntame. No inventes nada.
```

**Checklist:**
- [ ] Tengo el archivo de los últimos 12 meses descargado
- [ ] La tabla por mes y servicio está en Google Sheets
- [ ] He revisado los movimientos dudosos que la IA no supo clasificar
- [ ] Sé mi media mensual de ingresos sin IVA

**Error típico:** mezclar ingresos con IVA y sin IVA, o contar como venta un traspaso entre tus cuentas. Todo sin IVA y solo dinero de clientes.

---

### Paso 2 · Lo que te deja cada cosa que vendes
*Fase 1 · Semana 1, martes · 60 min*

**Objetivo:** saber el margen real de cada producto o servicio, no solo lo que facturas.

**Cómo hacerlo con IA:** reúne los costes directos de cada servicio (material, horas de empleados, comisiones, plataformas, desplazamientos). Si no los tienes apuntados, estímalos con la IA, que te hará las preguntas.

```text
Quiero calcular el margen de cada cosa que vendo. Mis servicios y precios son: [lista con precios].
Hazme las preguntas que necesites, una a una, para estimar el coste directo de cada uno
(materiales, horas de personal y su coste por hora, comisiones, envíos, software que se usa solo para ese servicio).
Al final dame una tabla: servicio | precio sin IVA | coste directo | margen en € | margen en % | ventas al año | margen total al año.
Ordénala por margen total al año y dime en dos frases qué te llama la atención.
```

**Checklist:**
- [ ] Tengo el coste directo de cada servicio (real o estimado y marcado como estimado)
- [ ] Sé el margen en euros y en porcentaje de cada uno
- [ ] Sé qué servicio me deja más dinero al año y cuál menos
- [ ] La tabla está en la misma hoja que el paso 1

**Error típico:** no contar tus propias horas como coste. Si un servicio te come 10 horas a ti, esas horas valen dinero aunque no te las pagues.

---

### Paso 3 · Costes fijos y punto de equilibrio
*Fase 1 · Semana 1, miércoles · 45 min*

**Objetivo:** saber cuánto necesitas facturar cada mes solo para cubrir gastos.

**Cómo hacerlo con IA:** saca del banco los gastos fijos de los últimos 3 meses (alquiler, nóminas, seguros, gestoría, software, cuota de autónomos). Pásaselos a Claude con este prompt.

```text
Estos son los gastos de mi negocio de los últimos 3 meses: [pega o adjunta].
1. Separa gastos fijos (se pagan vendas o no) de variables (dependen de las ventas).
2. Calcula la media mensual de gastos fijos.
3. Con mi margen medio del [X] % (sale de mi tabla de márgenes), calcula cuánto tengo que facturar al mes para no perder dinero.
4. Lista las suscripciones y servicios que se repiten cada mes, con su importe, para revisarlas después.
```

**Checklist:**
- [ ] Gastos fijos separados de los variables
- [ ] Sé mi gasto fijo mensual medio
- [ ] Sé mi punto de equilibrio en euros al mes
- [ ] Tengo la lista de suscripciones guardada para el paso 10

**Error típico:** olvidar los pagos trimestrales o anuales (seguros, impuestos, dominios). Divídelos entre los meses que cubren y súmalos.

---

### Paso 4 · Dibuja tu embudo de principio a fin
*Fase 1 · Semana 1, jueves · 45 min*

**Objetivo:** tener por escrito el camino que hace una persona desde que te descubre hasta que paga y repite.

**Cómo hacerlo con IA:** cuéntaselo a Claude en voz alta (usa el dictado del móvil o del ordenador) como si se lo explicaras a un socio nuevo. Que te lo ordene.

```text
Te voy a contar cómo me llegan los clientes y qué pasa hasta que me pagan. Escúchame entero y luego:
1. Dibuja mi embudo como una lista de etapas (por ejemplo: me descubre, me escribe, le respondo, presupuesto, compra, repite).
2. Para cada etapa: qué hace el cliente, qué hago yo, qué herramienta uso y cuánto tardo.
3. Marca las etapas donde depende solo de mí y las que no tengo medidas.
4. Hazme 3 preguntas sobre lo que no te ha quedado claro.
Mi explicación: [habla o escribe aquí].
```

**Checklist:**
- [ ] Mi embudo está escrito en etapas
- [ ] Cada etapa tiene responsable y herramienta
- [ ] He marcado las etapas que dependen solo de mí
- [ ] He marcado las etapas de las que no tengo ningún dato

**Error típico:** dibujar el embudo que te gustaría tener, no el que tienes. Si los presupuestos se mandan «cuando puedo», se escribe así.

---

### Paso 5 · Cuántos pasan de cada etapa a la siguiente
*Fase 1 · Semana 1, viernes · 60 min*

**Objetivo:** poner un número a cada etapa del embudo del último trimestre: cuántos te escriben, cuántos piden presupuesto, cuántos compran.

**Cómo hacerlo con IA:** cuenta lo que puedas de tus fuentes (WhatsApp, correo, Instagram, agenda, facturas). Donde no haya datos, haz una estimación honesta y márcala. Claude te ayuda a calcular.

```text
Este es mi embudo: [pega el del paso 4]. Datos de los últimos 3 meses:
- Contactos o mensajes nuevos: [nº o estimación]
- Presupuestos o llamadas: [nº]
- Ventas: [nº]
- Clientes que repitieron: [nº]
Calcula la conversión entre cada etapa, dime cuál es la etapa donde más gente se pierde
y cuánto facturaría de más al mes si esa etapa mejorara 5 puntos, con mi ticket medio de [X] €.
Marca qué números son estimaciones mías.
```

**Checklist:**
- [ ] Tengo un número (real o estimado) en cada etapa
- [ ] Sé la conversión entre etapas
- [ ] Sé en qué etapa se me escapa más gente
- [ ] He anotado qué datos me faltan para medirlos a partir de ahora

**Error típico:** saltarte el paso porque «no tengo datos». Una estimación honrada hoy vale más que un dato perfecto dentro de seis meses.

---

### Paso 6 · Lo que te cuesta un cliente y lo que te deja
*Fase 1 · Semana 2, lunes · 45 min*

**Objetivo:** saber cuánto te cuesta conseguir un cliente nuevo y cuánto dinero te deja a lo largo del tiempo.

**Cómo hacerlo con IA:** suma lo que gastaste en conseguir clientes el último trimestre (anuncios, comisiones, ferias, tu tiempo de venta) y cruza con las ventas de clientes nuevos.

```text
En los últimos 3 meses gasté en captar clientes: [anuncios X €, comisiones X €, otros X €]
y dediqué unas [X] horas a vender (valora mi hora en [X] €). Conseguí [X] clientes nuevos.
Mi ticket medio es [X] €, mi margen medio [X] % y un cliente me compra de media [X] veces en [X] meses.
1. Calcula el coste de conseguir un cliente, con y sin mis horas.
2. Calcula el margen que me deja un cliente durante toda su relación conmigo.
3. Dime la relación entre las dos cifras y si me puedo permitir gastar más en captar.
Explica cada cálculo en una línea.
```

**Checklist:**
- [ ] Sé lo que me cuesta un cliente nuevo
- [ ] Sé el margen que me deja un cliente durante toda la relación
- [ ] He incluido mis horas de venta en el cálculo
- [ ] Sé si puedo invertir más en captación o no

**Error típico:** calcular con la facturación en vez de con el margen. Un cliente que te paga 1.000 € con un 20 % de margen te deja 200 €, no 1.000 €.

---

### Paso 7 · Reconstruye tu última semana hora a hora
*Fase 1 · Semana 2, martes · 60 min*

**Objetivo:** ver en qué se te fueron de verdad las horas la semana pasada.

**Cómo hacerlo con IA:** abre tu calendario, tu correo enviado, los chats de WhatsApp y el historial de llamadas de la semana pasada. Con eso, Claude te monta la semana. Si prefieres, exporta el calendario y adjúntalo.

```text
Ayúdame a reconstruir mi semana pasada. Te paso mi calendario y lo que recuerdo de cada día: [pega o adjunta].
Pregúntame día por día por los huecos que no estén en el calendario (mensajes, llamadas, tareas sueltas).
Al final, dame una tabla: día | franja horaria | tarea | categoría (vender, atender clientes, producir/entregar,
administración, gestionar equipo, apagar fuegos, otros) | horas.
Y un resumen con las horas totales por categoría y el porcentaje de cada una.
```

**Checklist:**
- [ ] Tengo la semana reconstruida con todas las franjas
- [ ] Cada tarea tiene categoría
- [ ] Sé cuántas horas trabajé en total
- [ ] Sé en qué categoría se me va más tiempo

**Error típico:** apuntar solo las reuniones. Lo que se come el tiempo son los cinco minutos de WhatsApp repetidos cuarenta veces al día.

---

### Paso 8 · Solo yo, delegable o automatizable
*Fase 1 · Semana 2, miércoles · 45 min*

**Objetivo:** clasificar cada tarea de tu semana según quién debería hacerla.

**Cómo hacerlo con IA:** pásale la tabla del paso 7 a Claude.

```text
Esta es mi semana real: [pega la tabla del paso 7]. Mi negocio es [qué haces] y mi equipo es [quién hay].
Clasifica cada tarea en:
- SOLO YO: necesita mi criterio, mi relación o mi firma.
- DELEGABLE: la podría hacer una persona con un buen procedimiento.
- AUTOMATIZABLE: la puede hacer una herramienta o la IA con poca supervisión.
Para las automatizables, di con qué tipo de herramienta (IA, automatización, CRM, plantilla).
Total de horas por grupo y las 5 tareas automatizables o delegables que más horas suman.
Sé estricto: si dudo de que algo sea «solo yo», ponlo en delegable y explícame por qué.
```

**Checklist:**
- [ ] Todas las tareas están clasificadas
- [ ] Sé cuántas horas a la semana podría quitarme de encima
- [ ] Tengo el top 5 de tareas que más tiempo me roban
- [ ] He discutido con la IA las que yo creía «solo yo»

**Error típico:** creer que casi todo es «solo yo». Casi nunca lo es; lo que pasa es que no está escrito cómo se hace. Eso lo arreglas en la fase 2.

---

### Paso 9 · Cuánto tardas en contestar
*Fase 1 · Semana 2, jueves · 45 min*

**Objetivo:** medir cuánto tarda tu negocio en responder a un cliente o a alguien que pregunta por primera vez.

**Cómo hacerlo con IA:** revisa los últimos 20 mensajes de gente nueva (WhatsApp, Instagram, correo, formulario web) y apunta la hora del mensaje y la de tu respuesta. Haz una prueba: escríbete desde otro número o pide a un amigo que pregunte como cliente. Luego, que Claude lo analice.

```text
Estos son los tiempos de respuesta de mi negocio a 20 contactos nuevos: [canal | hora de su mensaje | hora de mi respuesta | ¿compró?].
1. Calcula el tiempo medio y el peor caso por canal.
2. Mira si los que compraron recibieron respuesta más rápida que los que no.
3. Dime en qué franjas horarias o días respondemos peor.
No saques conclusiones fuertes si hay pocos datos; dímelo.
```

**Checklist:**
- [ ] He medido 20 respuestas reales
- [ ] He hecho la prueba de cliente misterioso
- [ ] Sé mi tiempo medio de respuesta por canal
- [ ] Sé en qué momentos se quedan mensajes sin contestar

**Error típico:** medir solo el horario de oficina. Mucha gente escribe por la noche y en fin de semana, y ese mensaje sin contestar hasta el lunes también cuenta.

---

### Paso 10 · Qué herramientas pagas y cuáles sobran
*Fase 1 · Semana 2, viernes · 30 min*

**Objetivo:** revisar todo el software que pagas, cortar lo que no usas y liberar presupuesto para las herramientas de este plan.

**Cómo hacerlo con IA:** usa la lista de suscripciones del paso 3.

```text
Estas son las suscripciones y programas que pago cada mes: [lista con importe].
Para cada una, pregúntame si la uso, cuánto y para qué. Después:
1. Marca las que puedo cancelar, las que se solapan entre sí y las que debería mantener.
2. Calcula el ahorro mensual si cancelo las que sobran.
3. Dime cuáles podrían sustituirse por Claude, n8n, HubSpot o Google Sheets sin perder nada.
```

**Checklist:**
- [ ] Tengo la lista completa de lo que pago
- [ ] He cancelado (o apuntado para cancelar) lo que no uso
- [ ] Sé cuánto ahorro al mes
- [ ] Sé qué herramientas actuales se quedan en el plan

**Error típico:** contratar las herramientas nuevas sin cancelar las viejas. Acabas pagando dos CRM y no usando ninguno.

---

### Paso 11 · Tus 5 números de cada semana
*Fase 1 · Semana 3, lunes · 45 min*

**Objetivo:** elegir los cinco números que vas a mirar cada lunes y montar la hoja donde se apuntan.

**Cómo hacerlo con IA:** con todo lo que has medido, Claude te propone los números y la hoja.

```text
Este es el resumen de mis números: [ingresos, márgenes, embudo, coste por cliente, tiempo de respuesta, horas del dueño].
Propón los 5 números que debería revisar cada semana para saber si el negocio va bien
(al menos uno de dinero, uno de captación, uno de clientes y uno de mi tiempo).
Para cada uno: cómo se calcula, de dónde saco el dato y qué valor sería una señal de alarma.
Después dame la estructura de una hoja de Google Sheets con una fila por semana para apuntarlos,
con las fórmulas exactas para las columnas que se calculan solas.
```

**Checklist:**
- [ ] He elegido mis 5 números
- [ ] Sé de dónde sale cada dato
- [ ] La hoja semanal está creada en Google Sheets
- [ ] He apuntado los valores de esta semana como punto de partida

**Error típico:** elegir quince números. Con quince no miras ninguno. Cinco, y que cada uno te diga qué hacer si se tuerce.

---

### Paso 12 · Revisión de la fase 1: tus tres fugas más caras
*Fase 1 · Semana 3, martes · 60 min*

**Objetivo:** cerrar la fase con un diagnóstico claro: las tres cosas que más dinero o tiempo te cuestan y que vas a arreglar en las fases siguientes.

**Cómo hacerlo con IA:** junta todo lo de esta fase en un documento y pásaselo a Claude.

```text
Te paso todo lo que he medido de mi negocio estas dos semanas: [pega o adjunta los resultados de los pasos 1 a 11].
Actúa como un consultor directo que no me quiere caer bien:
1. Dime las 3 fugas que más me cuestan, en euros al mes o en horas a la semana, con el cálculo a la vista.
2. Para cada una, en qué fase del plan se arregla (operaciones, captación, crecimiento o libertad).
3. Dime qué dato importante sigue faltando.
4. Escribe un resumen de media página de cómo está mi negocio hoy para compararlo dentro de 90 días.
```

**Checklist:**
- [ ] Tengo mis 3 fugas con su coste calculado
- [ ] He guardado el resumen del «antes» para el paso 60
- [ ] Mi hoja de números está completa y la entiendo
- [ ] He bloqueado en el calendario una hora cada lunes para revisar mis 5 números

**Error típico:** pasar a la siguiente fase sin terminar esta porque «ya me hago una idea». Sin el «antes», en el paso 60 no podrás demostrar qué ha cambiado.

---

## Fase 2 · Operaciones

Ahora que sabes dónde se va el tiempo, toca recuperarlo. En esta fase sacas los procesos de tu cabeza, los conviertes en documentos que cualquiera (persona o IA) puede seguir y automatizas las tareas que se repiten. Es la fase que más horas te devuelve.

### Paso 13 · La lista de todo lo que se repite
*Fase 2 · Semana 3, miércoles · 45 min*

**Objetivo:** tener la lista completa de procesos de tu negocio: todo lo que se hace más de una vez al mes.

**Cómo hacerlo con IA:** usa tu semana del paso 7 y tu embudo del paso 4 como punto de partida.

```text
Mi negocio es [qué haces]. Te paso mi semana real y mi embudo: [pega pasos 4 y 7].
Haz la lista de todos los procesos que se repiten en un negocio como el mío, agrupados en:
captación, venta, entrega del servicio, atención al cliente, cobros y administración, equipo.
Para cada uno: quién lo hace hoy, cada cuánto y cuánto tarda (pregúntame lo que no sepas).
Añade los que probablemente hago sin darme cuenta (por ejemplo, perseguir pagos o pasar datos de una app a otra).
```

**Checklist:**
- [ ] Tengo la lista de procesos agrupada por área
- [ ] Cada proceso tiene responsable, frecuencia y duración
- [ ] He añadido los procesos «invisibles» que hago sin pensar
- [ ] La lista está guardada en un documento compartido

**Error típico:** listar solo los procesos grandes. Los que más tiempo comen suelen ser pequeños y frecuentes: copiar datos, mandar recordatorios, responder lo mismo.

---

### Paso 14 · Los 5 procesos que más horas te comen
*Fase 2 · Semana 3, jueves · 30 min*

**Objetivo:** elegir los cinco procesos que vas a documentar y automatizar primero.

**Cómo hacerlo con IA:** cruza la lista del paso 13 con la clasificación del paso 8.

```text
Esta es mi lista de procesos con su frecuencia y duración: [pega paso 13].
Y esta mi clasificación de tareas (solo yo, delegable, automatizable): [pega paso 8].
Calcula las horas al mes de cada proceso y elige los 5 que más tiempo me devolverían si los documento y automatizo.
Ordénalos por horas recuperadas y dificultad (fácil, media, difícil). Empieza por los fáciles que más horas suman.
```

**Checklist:**
- [ ] Tengo las horas al mes de cada proceso
- [ ] He elegido 5 procesos prioritarios
- [ ] Están ordenados por impacto y dificultad
- [ ] Sé cuántas horas al mes suman entre los 5

**Error típico:** empezar por el proceso más complicado porque es el que más molesta. Empieza por el fácil que más horas suma: ganarás confianza y tiempo para los difíciles.

---

### Paso 15 · Documenta el primer proceso hablando
*Fase 2 · Semana 3, viernes · 45 min*

**Objetivo:** convertir el proceso número 1 en un procedimiento escrito, paso a paso, que otra persona pueda seguir sin preguntarte.

**Cómo hacerlo con IA:** la próxima vez que hagas ese proceso, grábate la pantalla o el móvil mientras lo explicas en voz alta. Si no puedes, dicta la explicación. Pasa la transcripción (o el audio, si tu herramienta lo admite) a Claude.

```text
Esta es la transcripción de cómo hago este proceso: [pega].
Conviértela en un procedimiento claro con este formato:
- Nombre del proceso y para qué sirve
- Cuándo se hace y quién lo hace
- Qué hace falta antes de empezar (accesos, datos, plantillas)
- Pasos numerados, uno por acción, con el resultado esperado de cada paso
- Errores frecuentes y cómo evitarlos
- Cómo se sabe que está bien hecho
Si hay huecos en mi explicación, pregúntame antes de rellenarlos. No inventes pasos.
```

**Checklist:**
- [ ] He grabado o dictado el proceso mientras lo hacía
- [ ] El procedimiento escrito tiene todos los apartados
- [ ] He respondido a las dudas de la IA
- [ ] Alguien de mi equipo (o yo, fingiendo no saber) lo ha seguido sin preguntar

**Error típico:** escribir el procedimiento de memoria en vez de mientras lo haces. Siempre se te olvidan los pasos que haces en automático.

---

### Paso 16 · Documenta los otros cuatro
*Fase 2 · Semana 4, lunes · 90 min*

**Objetivo:** tener por escrito los cinco procesos prioritarios.

**Cómo hacerlo con IA:** repite el método del paso 15 con los procesos 2 a 5. Puedes grabar los cuatro en una tarde y pedírselos a Claude en una sola conversación, usando el primero como modelo.

```text
Este es un procedimiento que ya tengo bien escrito: [pega el del paso 15].
Ahora te paso las transcripciones de otros 4 procesos: [pega].
Escribe los 4 con el mismo formato y el mismo nivel de detalle.
Al final de cada uno, añade una línea: «Se puede automatizar: sí / en parte / no» y qué parte exactamente.
```

**Checklist:**
- [ ] Los 5 procesos están escritos con el mismo formato
- [ ] Cada uno indica qué parte se puede automatizar
- [ ] Están guardados en una carpeta compartida con nombre claro
- [ ] He corregido los pasos que la IA interpretó mal

**Error típico:** guardar cada procedimiento en un sitio distinto. Una sola carpeta, «Procesos», y un documento por proceso.

---

### Paso 17 · El proyecto de Claude con todo tu negocio
*Fase 2 · Semana 4, martes · 45 min*

**Objetivo:** crear en Claude un espacio con el contexto de tu negocio para que cada conversación empiece sabiendo quién eres, qué vendes y cómo hablas.

**Cómo hacerlo con IA:** en Claude, crea un Proyecto llamado con el nombre de tu negocio. Sube los procedimientos, tu lista de precios, tu resumen de la fase 1 y dos o tres mensajes que hayas escrito tú a clientes. En las instrucciones del proyecto pega esto, adaptado:

```text
Trabajas para [nombre del negocio], que [qué hace] para [qué clientes] en [zona].
Precios y servicios: están en los documentos del proyecto; no inventes precios que no estén ahí.
Tono: cercano y directo, de tú, frases cortas, sin tecnicismos ni emojis.
Cuando escribas a clientes, usa como modelo mis mensajes de ejemplo.
Si te falta un dato, pregunta antes de suponerlo.
Nunca prometas plazos, descuentos ni resultados que no estén en los documentos.
```

**Checklist:**
- [ ] El proyecto está creado con instrucciones
- [ ] He subido procedimientos, precios, resumen y mensajes de ejemplo
- [ ] He probado a pedirle un mensaje a un cliente y suena como yo
- [ ] He corregido las instrucciones con lo que no me gustó

**Error típico:** empezar cada conversación de cero y explicar tu negocio una y otra vez. El contexto se escribe una vez y se reutiliza siempre.

---

### Paso 18 · Las 20 preguntas que te hacen siempre
*Fase 2 · Semana 4, miércoles · 45 min*

**Objetivo:** tener respondidas, con tu tono, las preguntas que más se repiten de clientes y de gente interesada.

**Cómo hacerlo con IA:** copia de WhatsApp, Instagram y correo las preguntas que más te hacen (exporta un par de chats si hace falta, quitando datos personales). Dentro de tu proyecto de Claude:

```text
Estas son preguntas reales que me hacen clientes y gente interesada: [pega].
1. Agrúpalas y quédate con las 20 más frecuentes.
2. Para cada una, escribe la respuesta como la escribiría yo, usando los documentos del proyecto.
3. Si una respuesta necesita un dato que no tienes, márcala con [FALTA] en vez de inventarlo.
4. Termina cada respuesta con una pregunta o un siguiente paso que acerque a la venta, sin presionar.
```

**Checklist:**
- [ ] Tengo las 20 preguntas más frecuentes
- [ ] Cada una tiene su respuesta con mi tono
- [ ] He completado los huecos marcados con [FALTA]
- [ ] Las respuestas están guardadas en el proyecto y como respuestas rápidas en WhatsApp Business

**Error típico:** respuestas que contestan y se quedan ahí. Cada respuesta debe proponer el siguiente paso: una llamada, un presupuesto, una cita.

---

### Paso 19 · Tu primera skill: una tarea repetitiva que ya no haces a mano
*Fase 2 · Semana 4, jueves · 60 min*

**Objetivo:** convertir una tarea que repites (presupuestos, propuestas, informes, fichas de cliente) en una skill de Claude que la hace siempre igual y bien.

**Cómo hacerlo con IA:** una skill es un archivo de instrucciones que Claude sigue cada vez que haces esa tarea. Puedes subirla en la app de Claude desde los ajustes (apartado de capacidades) o instalarla en Claude Code. Elige la tarea del top 5 que tenga un resultado más estándar y pide que te la escriba:

```text
Quiero crear una skill de Claude para esta tarea: [por ejemplo, hacer presupuestos].
Así la hago hoy: [pega el procedimiento del paso 15 o 16]. Aquí tienes 2 ejemplos buenos ya hechos: [pega].
Escribe el archivo SKILL.md con:
- name y description en el encabezado (la description dice cuándo usarla, con las frases que yo diría)
- qué datos debe pedirme antes de empezar
- los pasos exactos y el formato del resultado
- comprobaciones antes de darme el resultado (precios del documento, sin errores de cálculo)
Después pruébala conmigo con un caso real.
```

**Checklist:**
- [ ] La skill está creada e instalada
- [ ] La he probado con un caso real
- [ ] El resultado es igual o mejor que el que hago a mano
- [ ] He apuntado cuánto tardaba antes y cuánto tardo ahora

**Error típico:** crear la skill sin ejemplos buenos. La IA copia el nivel de los ejemplos que le das; si no le das ninguno, se lo inventa.

---

### Paso 20 · Tu primera automatización en n8n
*Fase 2 · Semana 4, viernes · 60 min*

**Objetivo:** tener funcionando una automatización sencilla que te quite una tarea de copiar y pegar.

**Cómo hacerlo con IA:** crea tu cuenta en n8n Cloud (o instálalo en tu servidor). Empieza por algo simple: cuando alguien rellena el formulario de tu web, sus datos se guardan en una hoja de Google y te llega un aviso. Pide a Claude que te guíe clic a clic.

```text
Soy principiante en n8n. Quiero esta automatización: [cuando pase X, que se haga Y y me avise por Z].
Uso estas herramientas: [formulario de la web, Google Sheets, correo/Telegram/Slack].
Guíame paso a paso, nodo por nodo: qué nodo añadir, qué poner en cada campo y cómo conectar cada cuenta.
Dime cómo probarla con un dato de prueba antes de activarla.
Si es más fácil con otro enfoque, dímelo antes de empezar.
```

**Checklist:**
- [ ] Tengo cuenta en n8n
- [ ] La automatización funciona con un dato de prueba
- [ ] Está activada
- [ ] He comprobado durante el día que salta con datos reales

**Error típico:** querer automatizar el proceso entero el primer día. Primero una pieza pequeña que funcione; luego le añades más.

---

### Paso 21 · Cobros y facturas que se persiguen solos
*Fase 2 · Semana 5, lunes · 60 min*

**Objetivo:** dejar de perseguir pagos a mano: recordatorios automáticos antes y después del vencimiento.

**Cómo hacerlo con IA:** si tu programa de facturación ya manda recordatorios, actívalos y redacta los textos con Claude. Si no, monta en n8n un flujo que lea una hoja de facturas pendientes cada mañana y mande el recordatorio que toque.

```text
Quiero automatizar los recordatorios de pago. Mis facturas pendientes están en [programa u hoja] con estas columnas: [columnas].
1. Escribe 3 mensajes de recordatorio con mi tono: 3 días antes del vencimiento, el día del vencimiento y 7 días después.
   Amables, claros, con el importe, la fecha y cómo pagar. El tercero, firme pero educado.
2. Guíame para montarlo en n8n: cada mañana, leer las facturas, ver cuál toca y enviar el correo correspondiente.
3. Que me avise a mí de las que lleven más de 15 días vencidas para llamar yo.
```

**Checklist:**
- [ ] Tengo los 3 mensajes de recordatorio escritos y revisados
- [ ] El flujo funciona con una factura de prueba
- [ ] Me llega el aviso de las facturas muy atrasadas
- [ ] He apuntado cuánto dinero tengo hoy pendiente de cobro

**Error típico:** mandar el recordatorio a quien ya ha pagado. Antes de activarlo, asegúrate de que la hoja o el programa marcan las facturas cobradas el mismo día.

---

### Paso 22 · Reuniones que se resumen solas
*Fase 2 · Semana 5, martes · 30 min*

**Objetivo:** que cada llamada con clientes o con el equipo acabe con un resumen y una lista de tareas sin que tengas que escribir nada.

**Cómo hacerlo con IA:** instala Fathom (plan gratuito) y conéctalo a tu calendario y a Zoom, Google Meet o Teams. Avisa siempre a la otra persona de que la llamada se graba. Después, pasa los resúmenes por tu proyecto de Claude con este prompt:

```text
Este es el resumen y la transcripción de una reunión: [pega].
Dame:
1. Tres líneas con lo que se ha decidido.
2. Tareas: quién, qué y para cuándo.
3. Lo que el cliente ha dicho con sus palabras sobre sus problemas y objeciones (literal, para usarlo en ventas).
4. El correo de seguimiento para mandarle hoy, con mi tono.
```

**Checklist:**
- [ ] Fathom está instalado y conectado al calendario
- [ ] Aviso del grabado al empezar cada llamada
- [ ] He probado el prompt con una reunión real
- [ ] El correo de seguimiento sale el mismo día de la llamada

**Error típico:** grabar sin avisar. Además de ser poco elegante, en España necesitas informar a la otra persona. Una frase al empezar basta.

---

### Paso 23 · Claude para tu equipo, con normas
*Fase 2 · Semana 5, miércoles · 60 min*

**Objetivo:** que tu equipo use la IA bien y con las mismas reglas, en vez de que cada uno haga la guerra por su cuenta.

**Cómo hacerlo con IA:** prepara una sesión de una hora con tu equipo. Pide a Claude el guion y las normas. Si sois varios, valora el plan de equipo de Claude (comprueba su precio actual) o empieza compartiendo el proyecto.

```text
Tengo un equipo de [nº] personas que hacen [roles]. Quiero formarles en una hora para usar Claude en su trabajo.
1. Escribe un guion de 60 minutos: qué es, 3 ejercicios prácticos con tareas reales de su puesto, y dudas.
2. Escribe una página de normas de uso: qué datos nunca se meten (DNI, datos de salud, contraseñas, datos bancarios),
   qué hay que revisar siempre antes de mandar algo, y a quién preguntar.
3. Para cada rol, 3 prompts listos para usar en su día a día.
```

**Checklist:**
- [ ] He hecho la sesión con el equipo
- [ ] Las normas de uso están escritas y compartidas
- [ ] Cada persona tiene sus 3 prompts para su puesto
- [ ] He fijado una fecha dentro de dos semanas para ver cómo lo están usando

**Error típico:** dar acceso sin normas. El primer problema serio suele ser alguien pegando datos de clientes que no debería o mandando un texto sin revisar.

---

### Paso 24 · Revisión de la fase 2: horas recuperadas
*Fase 2 · Semana 5, jueves · 45 min*

**Objetivo:** medir cuántas horas te ha devuelto esta fase y decidir qué sigue en la cola.

**Cómo hacerlo con IA:**

```text
Hace tres semanas mi semana era así: [pega el resumen del paso 7].
Esto es lo que he montado en la fase de operaciones: [procedimientos, proyecto de Claude, respuestas, skill, automatizaciones, recordatorios, resúmenes, formación].
Esta semana he trabajado así: [horas por categoría, aunque sea estimado].
1. Calcula las horas a la semana recuperadas y su valor en euros con mi hora a [X] €.
2. Dime qué de lo montado no se está usando y por qué puede ser.
3. Propón los 3 siguientes procesos a documentar o automatizar cuando tenga un rato.
```

**Checklist:**
- [ ] Sé cuántas horas a la semana he recuperado
- [ ] He detectado lo que no se está usando
- [ ] Tengo la cola de los siguientes procesos a automatizar
- [ ] He apuntado el resultado junto al resumen del «antes»

**Error típico:** montar cosas y no comprobar si se usan. Una automatización apagada o una skill que nadie abre no te devuelve ni un minuto.

---

## Fase 3 · Captación

Con los números claros y las operaciones en orden, ya puedes recibir más clientes sin ahogarte. Esta fase no va de conseguir más leads todavía: va de no perder los que ya te llegan. Que cada contacto entre en un sitio, reciba respuesta rápida y tenga seguimiento hasta que diga sí o no.

### Paso 25 · Tu cliente ideal, con datos y no con intuición
*Fase 3 · Semana 5, viernes · 45 min*

**Objetivo:** describir a tu mejor cliente a partir de tus clientes reales, no de lo que te gustaría.

**Cómo hacerlo con IA:** saca de tus facturas los 10 clientes que más margen te han dejado y los 5 que más problemas te han dado. Quita los nombres si quieres.

```text
Estos son mis 10 mejores clientes por margen y mis 5 peores (más problemas, impagos, regateos): [datos: sector, tamaño, de dónde vino, qué compró, cuánto, cuánto tardó en decidir].
1. Encuentra qué tienen en común los mejores y qué los diferencia de los peores.
2. Describe a mi cliente ideal en un párrafo: quién es, qué problema tiene, qué le hace decidirse y dónde está.
3. Dame 5 señales para detectar en la primera conversación si un lead se parece a los mejores o a los peores.
```

**Checklist:**
- [ ] He analizado mis 10 mejores y 5 peores clientes
- [ ] Tengo descrito a mi cliente ideal en un párrafo
- [ ] Tengo 5 señales para reconocerlo pronto
- [ ] Lo he guardado en mi proyecto de Claude

**Error típico:** describir al cliente que te gustaría tener en vez de al que ya te compra y te deja margen. Empieza por los datos.

---

### Paso 26 · De dónde te llegan los leads y cuánto vale cada fuente
*Fase 3 · Semana 6, lunes · 45 min*

**Objetivo:** saber qué canales te traen clientes de verdad y cuáles solo te traen mensajes.

**Cómo hacerlo con IA:** para los clientes del último semestre, apunta por dónde llegaron (recomendación, Google, Instagram, anuncios, web, ferias). Si no lo sabes, pregúntaselo a los más recientes.

```text
Estos son mis clientes de los últimos 6 meses con su fuente de origen y lo que facturaron: [tabla].
Y esto es lo que gasto en cada canal (dinero y horas): [lista].
1. Ordena las fuentes por clientes conseguidos, por facturación y por coste.
2. Dime qué fuente me da los mejores clientes y cuál me da más trabajo para menos venta.
3. Propón cómo apuntar a partir de hoy la fuente de cada lead nuevo sin que se me olvide.
```

**Checklist:**
- [ ] Sé de dónde vino cada cliente del último semestre
- [ ] Tengo las fuentes ordenadas por resultado
- [ ] Sé qué canal me trae los mejores clientes
- [ ] He decidido cómo registrar la fuente de cada lead nuevo

**Error típico:** fiarte de la memoria. «Casi todos vienen por recomendación» suele ser falso cuando miras los datos.

---

### Paso 27 · Monta el CRM con tus etapas
*Fase 3 · Semana 6, martes · 60 min*

**Objetivo:** tener un CRM donde cada lead y cada cliente tiene su ficha y su etapa.

**Cómo hacerlo con IA:** crea tu cuenta de HubSpot (empieza con el plan gratuito; pasa a Starter cuando necesites automatizaciones o más funciones). Configura un pipeline con las etapas de tu embudo del paso 4. Si ya usas otro CRM que te funcione, quédate con él.

```text
Voy a configurar HubSpot para mi negocio. Mi embudo es: [pega paso 4]. Mi cliente ideal: [pega paso 25].
1. Propón las etapas del pipeline de ventas (máximo 7) y qué tiene que pasar para mover un lead de una a otra.
2. Propón las propiedades personalizadas que necesito en cada contacto (fuente, servicio de interés, presupuesto, etc.), sin pasarte.
3. Guíame clic a clic para crearlas en HubSpot.
```

**Checklist:**
- [ ] Tengo la cuenta del CRM creada
- [ ] El pipeline tiene mis etapas
- [ ] He creado las propiedades necesarias (y no más)
- [ ] He metido a mano un lead de prueba y lo he movido por todas las etapas

**Error típico:** crear veinte campos y doce etapas. Un CRM que da pereza rellenar se abandona en dos semanas.

---

### Paso 28 · Mete tus contactos y limpia la base
*Fase 3 · Semana 6, miércoles · 60 min*

**Objetivo:** tener en el CRM todos tus clientes y leads, sin duplicados y con su etapa.

**Cómo hacerlo con IA:** exporta contactos del móvil, del correo, de tu programa de facturación y de cualquier hoja que tengas. Junta todo en un CSV y pídele a Claude que lo limpie antes de importarlo.

```text
Te paso varios archivos de contactos de mi negocio: [adjunta].
1. Únelos en una sola tabla con estas columnas: nombre, apellidos, empresa, email, teléfono, fuente, etapa, última interacción, notas.
2. Elimina duplicados (mismo email o mismo teléfono) quedándote con el dato más completo.
3. Normaliza los teléfonos al formato +34 y pon en minúsculas los emails.
4. Marca la etapa según lo que sepas: cliente, lead activo, lead frío o presupuesto no cerrado.
5. Devuélveme un CSV listo para importar en HubSpot y una lista de los contactos dudosos.
```

**Checklist:**
- [ ] Todos los contactos están en un solo archivo limpio
- [ ] No hay duplicados
- [ ] Los he importado en el CRM con su etapa
- [ ] He revisado a mano los contactos dudosos

**Error típico:** importar contactos a los que luego vas a mandar comunicaciones comerciales sin que te hayan dado permiso. Distingue clientes y personas que te escribieron de listas compradas o sacadas de internet.

---

### Paso 29 · Que todos los leads entren solos al CRM
*Fase 3 · Semana 6, jueves · 60 min*

**Objetivo:** que cada persona que te escribe por la web, un formulario o un anuncio aparezca en el CRM sin que nadie copie nada.

**Cómo hacerlo con IA:** usa las integraciones nativas de HubSpot para tu formulario web y para los formularios de anuncios de Meta. Para el resto de canales, amplía la automatización de n8n del paso 20.

```text
Mis leads llegan por: [web, formulario de anuncios, Instagram, WhatsApp, correo, teléfono].
Uso HubSpot y n8n.
1. Para cada canal, dime la forma más sencilla de que el lead entre en HubSpot automáticamente (integración nativa o n8n).
2. Guíame para montar la del canal que más leads trae.
3. Que cada lead entre con su fuente rellenada y en la primera etapa, y que me llegue un aviso.
4. Para los canales que no se puedan automatizar, dame un procedimiento de 2 minutos para meterlos a mano.
```

**Checklist:**
- [ ] El canal principal mete los leads solo en el CRM
- [ ] Cada lead entra con su fuente
- [ ] Me llega un aviso por cada lead nuevo
- [ ] Hay un procedimiento para los canales que siguen siendo manuales

**Error típico:** automatizar la entrada y no la fuente. Sin saber de dónde viene cada lead, en la fase 4 no sabrás qué canal funciona.

---

### Paso 30 · Respuesta en minutos, también de noche
*Fase 3 · Semana 6, viernes · 60 min*

**Objetivo:** que nadie que te escribe espere horas a una primera respuesta útil.

**Cómo hacerlo con IA:** monta en n8n una respuesta automática para el canal que más leads trae: cuando entra un lead, Claude (vía API, con tope de gasto puesto en la consola de Anthropic) lee su mensaje y redacta una respuesta personalizada con tus preguntas frecuentes del paso 18. Empieza enviándote el borrador a ti para aprobarlo; cuando confíes, actívala sola.

```text
Quiero que cada lead nuevo de [canal] reciba en minutos una primera respuesta útil escrita por Claude.
Datos: mis preguntas frecuentes y respuestas [pega paso 18], mi cliente ideal [pega paso 25] y mi tono [describe].
1. Escribe el prompt de sistema para el nodo de Claude: responde a lo que pregunta, se presenta, hace UNA pregunta de cualificación
   y propone el siguiente paso. Nunca da precios cerrados que no estén en los documentos ni promete plazos.
2. Guíame para montarlo en n8n: entrada del lead, nodo de Claude, envío del borrador a mi Telegram o correo para aprobar.
3. Dime cómo pasarlo a envío automático cuando lo haya revisado durante una semana.
```

**Checklist:**
- [ ] El flujo genera una respuesta para cada lead nuevo
- [ ] Reviso los borradores antes de que salgan
- [ ] He corregido el prompt con los fallos de la primera semana
- [ ] He vuelto a medir mi tiempo de respuesta (compáralo con el paso 9)

**Error típico:** que la respuesta automática suene a robot o diga algo falso. Revisa una semana entera de borradores antes de dejarla sola.

---

### Paso 31 · El guion que separa curiosos de compradores
*Fase 3 · Semana 7, lunes · 45 min*

**Objetivo:** tener las preguntas exactas que te dicen, en tres o cuatro mensajes, si un lead merece una llamada.

**Cómo hacerlo con IA:**

```text
Mi cliente ideal: [pega paso 25]. Mi servicio y precios: [resumen]. Las objeciones que más oigo: [lista].
1. Escribe un guion de cualificación de 4 preguntas por mensaje, una cada vez, en este orden: situación, problema, urgencia, capacidad de inversión.
   Que suenen naturales, no a formulario.
2. Para cada respuesta posible, di si el lead sigue, se aparca o se descarta, y qué contestar.
3. Respuestas a las 5 objeciones más comunes con mi tono, sin presionar.
4. El mensaje para proponer la llamada a los que encajan, con enlace a mi agenda.
```

**Checklist:**
- [ ] Tengo las 4 preguntas de cualificación
- [ ] Sé qué hacer con cada tipo de respuesta
- [ ] Tengo respuestas a las 5 objeciones más comunes
- [ ] He creado un enlace de agenda (Google Calendar, HubSpot o la herramienta que uses)

**Error típico:** preguntar el presupuesto lo primero. Primero entiende su problema; cuando le importa, el dinero se habla con naturalidad.

---

### Paso 32 · Un setter con IA en Instagram y WhatsApp
*Fase 3 · Semana 7, martes · 90 min*

**Objetivo:** que los mensajes de Instagram y WhatsApp reciban respuesta, cualificación y propuesta de llamada aunque estés ocupado.

**Cómo hacerlo con IA:** en ManyChat Pro, conecta tu Instagram y, si lo usas, WhatsApp Business. Monta un flujo que salude, haga las preguntas del paso 31 y mande tu agenda a quien encaje. Para respuestas libres, ManyChat tiene funciones de IA de pago aparte, o puedes conectarlo con n8n y Claude. Deja siempre la opción de hablar con una persona.

```text
Voy a montar un setter en ManyChat para Instagram y WhatsApp. Mi guion de cualificación es: [pega paso 31].
1. Diseña el flujo: mensaje de bienvenida, cada pregunta con sus botones o respuesta libre, ramas según la respuesta,
   mensaje con la agenda y salida a una persona si lo pide o si no entiende algo.
2. Escribe todos los mensajes con mi tono, cortos, de tú.
3. Dime qué etiquetas poner en ManyChat para pasar luego cada lead al CRM con su etapa.
4. Escribe 10 mensajes de prueba raros (insultos, preguntas fuera de tema, audios) y cómo debe reaccionar el flujo.
```

**Checklist:**
- [ ] ManyChat está conectado a Instagram (y a WhatsApp si lo uso)
- [ ] El flujo cualifica y manda la agenda a quien encaja
- [ ] Siempre hay salida a una persona
- [ ] He probado los 10 mensajes raros antes de activarlo

**Error típico:** dejar que el bot finja ser una persona. Di que es un asistente y ofrece hablar contigo; la gente lo agradece y te ahorras malos ratos.

---

### Paso 33 · Seguimiento de cinco toques para los que no contestan
*Fase 3 · Semana 7, miércoles · 60 min*

**Objetivo:** que ningún lead se quede sin seguimiento porque se te olvidó escribirle.

**Cómo hacerlo con IA:** con HubSpot Starter puedes crear secuencias de correos; si estás en el plan gratuito, usa tareas recordatorio o un flujo de n8n que te avise cada mañana de a quién toca escribir y con qué mensaje.

```text
Quiero una secuencia de seguimiento para leads que no contestan o no han decidido. Mi servicio: [resumen]. Mi cliente ideal: [pega].
Escribe 5 mensajes: día 1, día 3, día 7, día 14 y día 30.
- Cada uno aporta algo distinto: una pregunta, un caso o ejemplo real mío [pega uno], una respuesta a una objeción, un recurso útil y una despedida que deja la puerta abierta.
- Máximo 5 líneas, con mi tono, sin «solo quería saber si...».
- Versión para correo y versión corta para WhatsApp.
```

**Checklist:**
- [ ] Tengo los 5 mensajes escritos y revisados
- [ ] La secuencia o los recordatorios están montados
- [ ] La secuencia se para sola cuando el lead responde
- [ ] He metido en la secuencia a los leads abiertos de este mes

**Error típico:** mandar cinco veces el mismo «¿has podido verlo?». Si cada mensaje no aporta algo nuevo, es spam.

---

### Paso 34 · Despierta la base dormida
*Fase 3 · Semana 7, jueves · 60 min*

**Objetivo:** recuperar ventas de antiguos clientes y presupuestos que no se cerraron.

**Cómo hacerlo con IA:** filtra en el CRM los presupuestos no cerrados de los últimos 12 meses y los clientes que no te compran desde hace más de 6. Que Claude te prepare mensajes personalizados.

```text
Te paso una lista de contactos dormidos: [nombre, qué pidió o compró, cuándo, por qué no siguió si lo sé].
Para cada uno, escribe un mensaje corto y personal para WhatsApp o correo:
- Recuerda en una frase qué hablamos.
- Da un motivo real para volver a hablar ahora: [novedad, hueco en la agenda, nuevo servicio, mejora].
- Una sola pregunta fácil de contestar al final.
Nada de descuentos salvo que yo te diga uno. Agrúpalos para que pueda mandarlos en 30 minutos.
```

**Checklist:**
- [ ] He sacado la lista de presupuestos no cerrados y clientes inactivos
- [ ] Cada contacto tiene su mensaje personalizado
- [ ] He enviado los mensajes
- [ ] He apuntado las respuestas en el CRM

**Error típico:** mandar el mismo mensaje genérico a todos. Una sola frase personal multiplica las respuestas frente a un «hola, ¿qué tal?».

---

### Paso 35 · Llega a cada llamada sabiendo todo del lead
*Fase 3 · Semana 7, viernes · 45 min*

**Objetivo:** preparar cada llamada de venta en 5 minutos con una ficha del lead.

**Cómo hacerlo con IA:** crea una skill o guarda este prompt en tu proyecto de Claude. Antes de cada llamada, pégale lo que tengas del lead (mensajes, web, ficha del CRM).

```text
Tengo una llamada de venta con este lead: [pega mensajes, ficha del CRM y su web o Instagram].
Prepárame una ficha de una página:
1. Quién es y qué hace su negocio (solo lo que se pueda comprobar; si algo es suposición, márcalo).
2. Su problema probable y cuánto le puede estar costando.
3. Las 5 preguntas que le haría para entender su situación.
4. Qué servicio mío encaja y por qué, y qué objeción es más probable.
5. Cómo propondría el siguiente paso al final de la llamada.
```

**Checklist:**
- [ ] El prompt o la skill está guardado
- [ ] He preparado con él mi siguiente llamada
- [ ] Después de la llamada, he pasado el resumen de Fathom al CRM
- [ ] He anotado si la llamada fue mejor que las que hacía sin preparar

**Error típico:** creerte todo lo que dice la ficha. La IA puede mezclar datos de otra empresa con el mismo nombre; comprueba lo importante antes de decirlo en la llamada.

---

### Paso 36 · Revisión de la fase 3: respuesta y conversión
*Fase 3 · Semana 8, lunes · 45 min*

**Objetivo:** comprobar si ahora pierdes menos leads que hace un mes.

**Cómo hacerlo con IA:**

```text
Antes de esta fase: tiempo medio de respuesta [paso 9], conversión del embudo [paso 5].
Ahora: tiempo de respuesta [medido de nuevo], leads de este periodo [nº], llamadas [nº], ventas [nº], respuestas de la base dormida [nº].
1. Compara antes y después y dime qué ha mejorado y qué no.
2. Revisa 10 conversaciones del setter y la respuesta automática [pega] y dime qué falla.
3. Dame los 3 ajustes con más impacto para el próximo mes.
Si los datos son pocos para sacar conclusiones, dilo.
```

**Checklist:**
- [ ] He comparado el tiempo de respuesta con el del paso 9
- [ ] He comparado la conversión con la del paso 5
- [ ] He revisado 10 conversaciones reales de los automatismos
- [ ] Tengo 3 ajustes apuntados y fechados

**Error típico:** juzgar la fase por las ventas de una semana. Mira la tendencia y los tiempos de respuesta; las ventas tardan más en reflejarlo.

---

## Fase 4 · Crecimiento

Ahora sí. Con el motor arreglado, cada euro y cada hora que metas en crecer rinde. En esta fase pones a trabajar el contenido, los anuncios y los referidos, y aprendes a vender más a quien ya te compra y a que no se vaya.

### Paso 37 · Tu oferta en una frase y en una página
*Fase 4 · Semana 8, martes · 60 min*

**Objetivo:** que cualquiera entienda en diez segundos qué vendes, a quién y qué consigue.

**Cómo hacerlo con IA:** dentro de tu proyecto de Claude, que ya conoce tu negocio y tu cliente ideal:

```text
Con lo que sabes de mi negocio y mi cliente ideal, y con estas frases literales de clientes sobre su problema [pega de los resúmenes de llamadas del paso 22]:
1. Escribe 10 versiones de mi oferta en una frase: para quién, qué resultado, en cuánto tiempo o con qué garantía (solo si la doy).
2. Elige las 3 mejores y explica por qué.
3. Con la que yo elija, escribe una página de oferta: problema, solución, cómo trabajo paso a paso, qué incluye, precio o desde cuánto, preguntas frecuentes y siguiente paso.
Usa las palabras de mis clientes, no jerga de marketing. No inventes testimonios ni cifras.
```

**Checklist:**
- [ ] Tengo mi oferta en una frase
- [ ] La he probado con 3 personas que no me conocen y la han entendido
- [ ] Tengo la página de oferta escrita
- [ ] La frase está en mi web, mi bio de Instagram y mi firma de correo

**Error típico:** describir lo que haces en vez de lo que consigue el cliente. «Hacemos reformas» no vende; «tu baño nuevo en dos semanas sin que tengas que estar en casa» sí.

---

### Paso 38 · Treinta ideas de contenido sacadas de tus clientes
*Fase 4 · Semana 8, miércoles · 45 min*

**Objetivo:** tener un banco de ideas de contenido basado en las preguntas y problemas reales de tus clientes.

**Cómo hacerlo con IA:**

```text
Estas son las preguntas que me hacen [pega paso 18], las objeciones que oigo [pega paso 31]
y frases literales de clientes [pega de los resúmenes de llamadas].
Dame 30 ideas de contenido para [Instagram / LinkedIn / TikTok / YouTube], repartidas en:
10 que resuelven una duda, 10 que rompen una creencia equivocada de mi cliente y 10 que enseñan cómo trabajo o un caso real.
Para cada una: título o gancho de una línea, la idea en dos frases y el formato (vídeo corto, carrusel, texto).
```

**Checklist:**
- [ ] Tengo 30 ideas apuntadas en una hoja
- [ ] Cada idea sale de algo que dijo un cliente real
- [ ] He marcado las 10 que más me apetece grabar
- [ ] Sé en qué red me voy a centrar (una, no cinco)

**Error típico:** inventarte los temas pensando en lo que te gustaría contar. El contenido que vende responde a lo que tu cliente ya se pregunta.

---

### Paso 39 · Una grabación a la semana, varias piezas
*Fase 4 · Semana 8, jueves · 60 min*

**Objetivo:** montar un sistema para producir el contenido de la semana en una sola sesión.

**Cómo hacerlo con IA:** elige un día fijo. Graba 20-30 minutos respondiendo 4 o 5 ideas del banco, o graba una charla con un cliente (con su permiso). Pasa la transcripción a Claude.

```text
Esta es la transcripción de mi grabación de esta semana: [pega].
1. Encuentra los 5 fragmentos con más fuerza para vídeos cortos: dónde empieza y acaba cada uno y el gancho para los primeros 3 segundos.
2. Escribe 2 carruseles de 7 diapositivas con las ideas principales.
3. Escribe 2 publicaciones de texto y el correo semanal para mi lista.
Mantén mis palabras; corrige solo lo necesario para que se entienda.
```

**Checklist:**
- [ ] Tengo un día fijo de grabación en el calendario
- [ ] He hecho la primera grabación
- [ ] He sacado al menos 5 piezas de ella
- [ ] He apuntado cuánto tiempo me ha llevado todo

**Error típico:** grabar cada pieza por separado cada día. Te come la semana y lo acabas dejando. Una sesión, muchas piezas.

---

### Paso 40 · Calendario y publicación programada
*Fase 4 · Semana 8, viernes · 45 min*

**Objetivo:** dejar el contenido de las próximas dos semanas programado para que salga solo.

**Cómo hacerlo con IA:** usa el programador gratuito de tu red (Meta Business Suite para Instagram y Facebook, el de LinkedIn o el de YouTube). Pide a Claude el calendario.

```text
Tengo estas piezas listas: [lista]. Publico en [red] y puedo publicar [X] veces por semana.
1. Repártelas en un calendario de 2 semanas alternando tipos (duda, creencia, caso).
2. Escribe el texto de cada publicación con una llamada a la acción distinta: comentar una palabra, escribir por privado, ir a la web.
3. Dime cómo medir en 2 semanas qué tipo de pieza funciona mejor con los datos de la propia red.
```

**Checklist:**
- [ ] Tengo el calendario de 2 semanas
- [ ] Las publicaciones están programadas
- [ ] Cada pieza tiene una llamada a la acción
- [ ] He puesto un recordatorio para revisar los datos en 2 semanas

**Error típico:** publicar sin llamada a la acción. Si nadie sabe qué hacer después de verte, el contenido entretiene pero no trae clientes.

---

### Paso 41 · Testimonios y casos de verdad
*Fase 4 · Semana 9, lunes · 45 min*

**Objetivo:** reunir testimonios y casos reales de tus clientes para usarlos en tu web, contenido y ventas.

**Cómo hacerlo con IA:** elige 5 clientes contentos. Pide a Claude el mensaje para pedirles el testimonio y, cuando te respondan, que lo convierta en un caso.

```text
1. Escribe un mensaje corto para pedir a un cliente contento un testimonio. Que le ponga fácil responder:
   3 preguntas (cómo estaba antes, qué cambió, qué le diría a alguien que duda) y la opción de responder con un audio.
2. Cuando te pase sus respuestas, conviértelas en un caso: situación de partida, qué hicimos, resultado.
   Usa sus palabras literales y no añadas cifras ni resultados que no haya dicho.
3. Recuérdame pedirle permiso por escrito para publicarlo con su nombre.
```

**Checklist:**
- [ ] He pedido testimonio a 5 clientes
- [ ] Tengo al menos 2 respuestas convertidas en caso
- [ ] Tengo permiso por escrito para publicarlas
- [ ] Están en mi web y en mi proyecto de Claude para usarlas en ventas

**Error típico:** «mejorar» el testimonio con cifras que el cliente no dijo. Un testimonio inventado o exagerado te quita toda la credibilidad cuando se descubre.

---

### Paso 42 · Un programa de referidos sencillo
*Fase 4 · Semana 9, martes · 45 min*

**Objetivo:** que tus clientes contentos te traigan a otros como ellos, de forma ordenada.

**Cómo hacerlo con IA:**

```text
Mi negocio: [resumen]. Mi cliente ideal: [pega]. Mi margen medio por cliente: [pega paso 6].
1. Propón 3 formas de recompensar a quien me recomienda (descuento, servicio extra, regalo, donación), con su coste para mí.
2. Elige la más sencilla de gestionar y escribe las reglas en 5 líneas.
3. Escribe el mensaje para presentárselo a mis clientes actuales y el momento ideal para pedirlo (justo después de un buen resultado).
4. Dime cómo registrar en el CRM quién recomendó a quién.
```

**Checklist:**
- [ ] Tengo las reglas del programa escritas
- [ ] La recompensa es rentable según mi margen
- [ ] He enviado el mensaje a mis clientes actuales
- [ ] Las recomendaciones quedan registradas en el CRM

**Error típico:** pedir recomendaciones a todo el mundo en cualquier momento. Pide justo después de que el cliente note el resultado, cuando está más contento.

---

### Paso 43 · Tu primera campaña de anuncios, pequeña y medida
*Fase 4 · Semana 9, miércoles · 90 min*

**Objetivo:** lanzar una campaña de prueba con un presupuesto que puedas perder sin problema, para aprender qué funciona.

**Cómo hacerlo con IA:** elige una sola plataforma (Meta para Instagram y Facebook, o Google si te buscan por lo que vendes). Decide el presupuesto de prueba antes de empezar: es inversión en publicidad y va aparte de las herramientas. Con tu coste máximo por cliente del paso 6:

```text
Quiero lanzar mi primera campaña en [Meta / Google]. Vendo [oferta del paso 37] a [cliente ideal] en [zona].
Puedo gastar como máximo [X] € en la prueba y un cliente me deja [X] € de margen (paso 6).
1. Dime qué objetivo de campaña elegir y por qué.
2. Propón la segmentación más sencilla (zona, edad, intereses o palabras clave).
3. Calcula a partir de qué coste por lead la campaña no me sale rentable con mi conversión actual [paso 5].
4. Guíame para crearla paso a paso y para conectar los leads con mi CRM (paso 29).
```

**Checklist:**
- [ ] He fijado el presupuesto máximo de prueba
- [ ] Sé a partir de qué coste por lead no compensa
- [ ] La campaña está lanzada en una sola plataforma
- [ ] Los leads de la campaña entran solos en el CRM con su fuente

**Error típico:** lanzar anuncios sin saber cuánto puedes pagar por un cliente. Sin esa cifra, no sabrás si la campaña va bien o te está quemando dinero.

---

### Paso 44 · Creatividades y textos de anuncios con IA
*Fase 4 · Semana 9, jueves · 60 min*

**Objetivo:** tener varias versiones de anuncios para probar cuál funciona, en vez de apostar todo a una.

**Cómo hacerlo con IA:**

```text
Mi oferta: [paso 37]. Mi cliente ideal: [paso 25]. Frases literales de clientes: [pega].
1. Escribe 5 ganchos distintos para anuncios: uno de dolor, uno de deseo, uno de objeción, uno de caso real y uno de curiosidad.
2. Para cada gancho, un texto de anuncio de 3-5 líneas y un titular.
3. Para 2 de ellos, un guion de vídeo de 20-30 segundos que pueda grabar yo con el móvil.
No prometas resultados que no pueda demostrar ni uses testimonios que no te haya pasado.
```

**Checklist:**
- [ ] Tengo 5 versiones de anuncio
- [ ] He grabado al menos un vídeo con el móvil
- [ ] Están subidas a la campaña como anuncios distintos
- [ ] He apuntado en 7 días cuál tiene mejor coste por lead

**Error típico:** cambiarlo todo a los dos días. Deja que cada anuncio acumule datos (unos días y un mínimo de impresiones) antes de decidir.

---

### Paso 45 · Qué más le puedes vender a quien ya te compra
*Fase 4 · Semana 9, viernes · 45 min*

**Objetivo:** diseñar una venta adicional o una mejora para tus clientes actuales.

**Cómo hacerlo con IA:**

```text
Mis servicios y márgenes: [pega paso 2]. Lo que mis clientes me piden y no ofrezco: [lista]. Problemas que tienen después de comprarme: [lista].
1. Propón 3 ofertas para clientes actuales: una mejora del servicio, un complemento y una cuota mensual de mantenimiento o soporte.
2. Para cada una: qué incluye, precio orientativo según mi margen, cuánto trabajo me supone y a qué clientes ofrecérsela.
3. Elige la más fácil de vender y escribe cómo ofrecerla en una conversación natural, no como un vendedor.
```

**Checklist:**
- [ ] Tengo 3 ideas de venta adicional
- [ ] He elegido una y le he puesto precio
- [ ] Se la he ofrecido a 5 clientes actuales
- [ ] He apuntado las respuestas en el CRM

**Error típico:** ofrecer la mejora antes de que el cliente haya visto el primer resultado. Primero cumple; luego ofrece más.

---

### Paso 46 · Detecta a los clientes que se te van a ir
*Fase 4 · Semana 10, lunes · 60 min*

**Objetivo:** ver antes de que pase qué clientes están a punto de dejarte, para actuar a tiempo.

**Cómo hacerlo con IA:** exporta del CRM o de tu facturación tus clientes recurrentes con la fecha de su última compra, su frecuencia habitual, sus quejas y sus pagos atrasados.

```text
Estos son mis clientes recurrentes: [nombre, frecuencia habitual de compra, última compra, quejas o incidencias, pagos atrasados, última vez que hablamos].
1. Marca cada cliente en verde, amarillo o rojo según el riesgo de que se vaya y explica el motivo en una línea.
2. Para los rojos y amarillos, escribe un mensaje personal para retomar el contacto (no para venderles).
3. Propón una regla para que el CRM o n8n me avise solo cuando un cliente pase de su frecuencia habitual sin comprar.
```

**Checklist:**
- [ ] Tengo a mis clientes clasificados por riesgo
- [ ] He contactado a los rojos esta semana
- [ ] Tengo la alerta automática montada o apuntada para montarla
- [ ] He apuntado cuántos clientes perdí el último trimestre como referencia

**Error típico:** enterarte de que un cliente se ha ido cuando ya se ha ido. Casi siempre hay señales antes: compra menos, tarda en responder, se queja.

---

### Paso 47 · Opiniones y reseñas que se piden solas
*Fase 4 · Semana 10, martes · 45 min*

**Objetivo:** pedir opinión y reseña a cada cliente en el mejor momento, de forma automática.

**Cómo hacerlo con IA:** monta en n8n o en el CRM un flujo que, unos días después de terminar el servicio, mande una pregunta corta de satisfacción. A quien responda bien, se le pide la reseña en Google; a quien responda mal, te avisa a ti para llamarle.

```text
Quiero automatizar las opiniones de mis clientes. El servicio termina cuando [momento] y lo registro en [CRM/hoja].
1. Escribe el mensaje de satisfacción: una sola pregunta del 1 al 10 y un hueco para comentarios.
2. Escribe el mensaje para pedir la reseña en Google a quien ponga 9 o 10, con el enlace directo.
3. Escribe el aviso que me llega a mí si alguien pone 6 o menos, con sus datos para llamarle hoy.
4. Guíame para montarlo en n8n.
```

**Checklist:**
- [ ] El flujo de satisfacción está montado
- [ ] Tengo el enlace directo para dejar reseña en Google
- [ ] Me llega el aviso de los clientes descontentos
- [ ] He respondido a todas las reseñas recientes de Google

**Error típico:** pedir reseñas solo a los contentos y no hacer nada con los descontentos. El cliente al que llamas tras una mala nota a menudo se queda; el que ignoras se va y lo cuenta.

---

### Paso 48 · Revisión de la fase 4: qué canal crece y cuál cortar
*Fase 4 · Semana 10, miércoles · 60 min*

**Objetivo:** decidir dónde poner más tiempo y dinero y qué dejar de hacer.

**Cómo hacerlo con IA:**

```text
Resultados de la fase de crecimiento:
- Contenido: [publicaciones, alcance, mensajes o leads que generó]
- Anuncios: [gasto, leads, coste por lead, ventas]
- Referidos: [recomendaciones recibidas, ventas]
- Venta adicional: [ofertas hechas, aceptadas]
- Retención: [clientes en riesgo contactados, recuperados]
Mi coste máximo por cliente es [X] € (paso 6).
1. Ordena los canales por rentabilidad.
2. Dime cuál escalar, cuál mantener y cuál cortar, con el porqué en una línea.
3. Avísame si los datos son demasiado pocos para decidir alguno.
```

**Checklist:**
- [ ] Tengo los resultados de cada canal en una tabla
- [ ] He decidido qué escalar, qué mantener y qué cortar
- [ ] He actualizado mis 5 números semanales con lo que ahora sí mido
- [ ] He apuntado el resultado junto a las revisiones anteriores

**Error típico:** seguir en un canal porque «hay que estar». Si no te trae clientes y te come horas, se corta o se cambia.

---

## Fase 5 · Libertad

El objetivo nunca fue tener más herramientas. Era que el negocio funcione sin que estés encima de todo y te deje tiempo para decidir qué quieres hacer con él. En esta última fase ves el negocio de un vistazo, delegas lo que queda, pones agentes a trabajar solos con límites claros y lo dejas todo en una revisión de una hora a la semana.

### Paso 49 · Tu cuadro de mando en una pantalla
*Fase 5 · Semana 10, jueves · 60 min*

**Objetivo:** ver tus 5 números y su evolución en una sola pantalla, sin abrir cinco programas.

**Cómo hacerlo con IA:** conecta Looker Studio (gratis) a tu hoja de números semanales y, si quieres, a HubSpot. Pide a Claude que te diseñe el panel.

```text
Mis 5 números semanales son: [pega paso 11] y están en una hoja de Google con estas columnas: [columnas].
1. Diseña un cuadro de mando de una sola pantalla: qué gráfico para cada número y dónde colocarlo.
2. Añade una marca de alarma para cada número con el umbral que fijé.
3. Guíame clic a clic para montarlo en Looker Studio conectado a mi hoja.
4. Dime qué datos que hoy apunto a mano podría traer n8n solo a la hoja.
```

**Checklist:**
- [ ] El cuadro de mando está montado y conectado
- [ ] Se ven mis 5 números y su evolución
- [ ] Cada número tiene su umbral de alarma
- [ ] Lo tengo en favoritos y lo he compartido con quien lo necesite

**Error típico:** un panel precioso con datos que nadie actualiza. Si la hoja de origen no se rellena cada semana, el cuadro de mando miente.

---

### Paso 50 · El informe del lunes que se escribe solo
*Fase 5 · Semana 10, viernes · 60 min*

**Objetivo:** recibir cada lunes por la mañana un resumen de la semana con lo que importa y lo que tienes que decidir.

**Cómo hacerlo con IA:** monta en n8n un flujo programado para el lunes a primera hora: lee la hoja de números, los datos del CRM y las facturas pendientes, se los pasa a Claude por API y te manda el informe por correo o Telegram.

```text
Quiero un informe automático cada lunes a las 8:00. Fuentes: [hoja de números, CRM, facturas pendientes].
1. Escribe el prompt para el nodo de Claude: resumen de la semana en 5 líneas, comparación con la semana anterior,
   números en alarma, leads calientes sin seguimiento, cobros atrasados y las 3 decisiones que debería tomar esta semana.
   Solo con los datos recibidos; si falta uno, que lo diga en vez de inventarlo.
2. Guíame para montarlo en n8n: disparador semanal, lectura de cada fuente, nodo de Claude y envío.
```

**Checklist:**
- [ ] El flujo está montado y programado
- [ ] He recibido el primer informe de prueba
- [ ] He comprobado los números del informe contra la hoja
- [ ] He ajustado el prompt con lo que sobraba o faltaba

**Error típico:** fiarte del informe sin comprobarlo las primeras semanas. Compara los números con la hoja hasta estar seguro de que lee bien los datos.

---

### Paso 51 · Lo que solo puedes hacer tú
*Fase 5 · Semana 11, lunes · 45 min*

**Objetivo:** reducir tu lista de tareas a lo que de verdad necesita tu criterio y decidir a quién va el resto.

**Cómo hacerlo con IA:** repite la reconstrucción de la semana del paso 7 con tu semana actual y compárala.

```text
Mi semana del paso 7 era así: [pega]. Mi semana actual es así: [pega].
Lo que ya está automatizado o documentado: [lista].
1. Compara las dos semanas: horas recuperadas y en qué.
2. Lista las tareas que sigo haciendo yo y clasifícalas otra vez: solo yo, delegar a una persona, pasar a un agente de IA.
3. Para cada tarea a delegar, dime a quién o a qué y qué necesita esa persona o agente para hacerla sin mí.
Sé exigente: lo que pongo como «solo yo» tiene que serlo de verdad.
```

**Checklist:**
- [ ] He comparado mi semana actual con la del paso 7
- [ ] Tengo la lista de lo que solo puedo hacer yo
- [ ] Cada tarea a delegar tiene destino: persona o agente
- [ ] He elegido la primera tarea que voy a traspasar mañana

**Error típico:** delegar solo lo que no te gusta. Delega lo que otro puede hacer igual de bien, aunque te guste hacerlo.

---

### Paso 52 · Traspasa la primera tarea a una persona
*Fase 5 · Semana 11, martes · 60 min*

**Objetivo:** que alguien de tu equipo (o un colaborador externo) se quede una tarea entera, con su procedimiento y su forma de medir si está bien hecha.

**Cómo hacerlo con IA:**

```text
Voy a traspasar esta tarea: [tarea] a [persona y rol]. El procedimiento está aquí: [pega].
1. Escribe un plan de traspaso de 2 semanas: primero lo hago yo y mira, después lo hace y reviso, y al final lo hace sola.
2. Define cómo sé que está bien hecha sin revisarlo todo: 2 o 3 indicadores.
3. Escribe el mensaje para explicárselo: qué espero, qué decide sola y cuándo me tiene que preguntar.
```

**Checklist:**
- [ ] El plan de traspaso está escrito y compartido
- [ ] La persona sabe qué decide sola y qué no
- [ ] Hay 2 o 3 indicadores para saber si está bien hecha
- [ ] He puesto en el calendario la revisión del traspaso dentro de 2 semanas

**Error típico:** delegar y volver a hacerlo tú en cuanto algo sale distinto a como lo harías. Si el resultado es bueno, aunque el camino sea otro, déjalo estar.

---

### Paso 53 · Un agente que ordena tu bandeja de entrada
*Fase 5 · Semana 11, miércoles · 60 min*

**Objetivo:** que cada correo nuevo llegue clasificado y con un borrador de respuesta listo para revisar.

**Cómo hacerlo con IA:** monta en n8n un flujo que lea cada correo nuevo, lo pase a Claude por API para que lo clasifique (cliente, lead, proveedor, administración, ruido) y deje un borrador de respuesta en Gmail u Outlook. Los borradores no se envían solos: los revisas tú o alguien del equipo.

```text
Quiero un agente para mi correo con n8n y Claude. Uso [Gmail / Outlook].
1. Escribe el prompt de sistema: clasificar cada correo en una de estas categorías [lista], marcar urgencia (alta, media, baja)
   y escribir un borrador de respuesta con mi tono y mis documentos solo cuando tenga sentido responder.
   Nunca aceptar compromisos, precios ni fechas en mi nombre: en esos casos, el borrador dice [REVISAR].
2. Guíame para montarlo: disparador de correo nuevo, nodo de Claude, etiqueta en el correo y borrador guardado.
3. Dime cómo excluir correos con datos sensibles (bancos, salud, Hacienda) para que no pasen por la IA.
```

**Checklist:**
- [ ] El agente clasifica los correos nuevos
- [ ] Los borradores aparecen en la carpeta de borradores, sin enviarse
- [ ] Los correos sensibles quedan fuera
- [ ] He revisado 20 clasificaciones y he corregido el prompt

**Error típico:** dejar que envíe solo desde el primer día. Un mal correo enviado en tu nombre cuesta más que todo el tiempo que ahorra en un mes.

---

### Paso 54 · Un agente de seguimiento comercial que trabaja solo
*Fase 5 · Semana 11, jueves · 60 min*

**Objetivo:** que cada mañana tengas preparados los seguimientos del día sin abrir el CRM.

**Cómo hacerlo con IA:** monta en n8n un flujo diario que lea de HubSpot los leads y presupuestos sin actividad desde hace días, pase cada caso a Claude con su historial y te deje la lista de a quién escribir y el mensaje listo.

```text
Quiero un agente diario de seguimiento comercial con n8n, HubSpot y Claude.
1. Define qué leads entran cada día: etapa [X] sin actividad desde hace [X] días, presupuestos enviados sin respuesta, llamadas sin cerrar.
2. Escribe el prompt para que Claude, con el historial de cada lead, decida el siguiente paso (mensaje, llamada o descartar)
   y escriba el mensaje con mi tono y mi secuencia del paso 33.
3. Que el resultado me llegue a las 9:00 como lista ordenada por probabilidad de cerrar, con el mensaje listo para copiar.
4. Guíame para montarlo.
```

**Checklist:**
- [ ] El agente se ejecuta cada mañana
- [ ] Recibo la lista ordenada con los mensajes listos
- [ ] Los seguimientos que hago quedan registrados en el CRM
- [ ] Después de una semana, he comprobado que no se queda ningún lead sin seguimiento

**Error típico:** que el agente lea datos del CRM desactualizados. Si el equipo no mueve los leads de etapa, el agente sugerirá escribir a quien ya ha comprado.

---

### Paso 55 · Un agente que vigila la caja
*Fase 5 · Semana 11, viernes · 60 min*

**Objetivo:** enterarte a tiempo de cobros atrasados, gastos raros o semanas en las que vas a ir justo de caja.

**Cómo hacerlo con IA:** con tu hoja de facturas y la exportación del banco (o la conexión que te ofrezca tu programa de facturación), monta en n8n un flujo semanal que se las pase a Claude.

```text
Quiero un agente semanal de caja. Datos: facturas emitidas y su estado, gastos fijos del paso 3 y saldo del banco.
1. Escribe el prompt para Claude: calcular la caja prevista para las próximas 4 semanas, listar cobros atrasados por importe
   y detectar gastos nuevos o que han subido respecto al mes anterior.
2. Que me avise solo si hay algo que mirar (caja por debajo de [X] €, cobro atrasado de más de [X] días, gasto nuevo); si todo está bien, una línea.
3. Guíame para montarlo en n8n. Que solo lea datos: nada de pagos ni transferencias.
```

**Checklist:**
- [ ] El agente se ejecuta cada semana
- [ ] Me avisa solo cuando hay algo que mirar
- [ ] Solo tiene permiso de lectura, nunca de pago
- [ ] He comprobado la previsión de caja con mis números reales

**Error típico:** dar a un agente acceso para mover dinero. Que lea y avise; los pagos los apruebas tú.

---

### Paso 56 · Límites, permisos y registro de errores
*Fase 5 · Semana 12, lunes · 45 min*

**Objetivo:** dejar por escrito qué puede hacer cada agente y automatización sin tu permiso, y qué pasa cuando se equivoca.

**Cómo hacerlo con IA:**

```text
Estos son los agentes y automatizaciones que tengo funcionando: [lista con qué hace cada uno].
1. Haz una tabla: agente | qué hace solo | qué necesita mi aprobación | qué nunca puede hacer | quién lo revisa | cada cuánto.
2. Propón un registro sencillo de errores (hoja con fecha, agente, qué pasó, cómo se arregló) y cómo apuntar cada fallo en 1 minuto.
3. Dime qué agente tiene más riesgo si falla y qué control le añadirías.
4. Recuérdame revisar los topes de gasto de la API y quién tiene acceso a cada cuenta.
```

**Checklist:**
- [ ] Tengo la tabla de permisos de cada agente
- [ ] El registro de errores está creado
- [ ] He revisado el tope de gasto de la API de Claude
- [ ] He revisado quién tiene acceso a n8n, HubSpot y ManyChat

**Error típico:** montar agentes y olvidarse de ellos. Sin un responsable y una revisión fija, un fallo puede repetirse semanas sin que nadie lo vea.

---

### Paso 57 · Tu revisión semanal de una hora
*Fase 5 · Semana 12, martes · 45 min*

**Objetivo:** convertir todo el plan en un único hábito: una hora a la semana para revisar el negocio y decidir.

**Cómo hacerlo con IA:** guarda esta plantilla en tu proyecto de Claude y úsala cada lunes con el informe automático del paso 50.

```text
Revisión semanal. Te paso el informe del lunes [pega], mi cuadro de mando [pega números] y el registro de errores [pega].
Guíame en 60 minutos con este orden:
1. Números (10 min): qué ha cambiado y por qué.
2. Captación (10 min): leads, respuestas, seguimientos pendientes.
3. Clientes (10 min): riesgo de bajas, quejas, reseñas.
4. Agentes y automatizaciones (10 min): errores y ajustes.
5. Decisiones (15 min): las 3 cosas más importantes de esta semana, con responsable.
6. Cierre (5 min): qué dejo de hacer.
Hazme las preguntas una a una y al final dame el resumen para compartir con mi equipo.
```

**Checklist:**
- [ ] La plantilla está guardada en mi proyecto de Claude
- [ ] Tengo una hora fija cada semana en el calendario
- [ ] He hecho la primera revisión completa
- [ ] El resumen ha llegado a mi equipo

**Error típico:** saltarte la revisión cuando la semana va bien. Es justo cuando va bien cuando tienes la cabeza fría para decidir lo importante.

---

### Paso 58 · Qué pasa si algo falla o tú no estás
*Fase 5 · Semana 12, miércoles · 45 min*

**Objetivo:** que el negocio aguante si una herramienta se cae o si tú te vas dos semanas.

**Cómo hacerlo con IA:**

```text
Estas son mis herramientas, automatizaciones y agentes: [lista]. Y estas las tareas que siguen dependiendo de mí: [pega paso 51].
1. Para cada herramienta crítica: qué pasa si deja de funcionar un día, cómo me entero y cuál es el plan manual mientras tanto.
2. Escribe un documento «Si no estoy»: quién hace qué, qué puede decidir cada persona, a quién llamar y dónde están los accesos (sin escribir contraseñas).
3. Dime cómo hacer copias de seguridad de mis flujos de n8n, del CRM y de mis documentos, y cada cuánto.
```

**Checklist:**
- [ ] Tengo un plan manual para cada herramienta crítica
- [ ] El documento «Si no estoy» está escrito y compartido
- [ ] Las contraseñas están en un gestor de contraseñas, no en documentos
- [ ] He hecho la primera copia de seguridad de los flujos de n8n

**Error típico:** que todo el sistema dependa de una cuenta personal tuya. Las herramientas del negocio, a nombre del negocio y con acceso de al menos dos personas.

---

### Paso 59 · La prueba de fuego: un día entero sin tocar el negocio
*Fase 5 · Semana 12, jueves · todo el día (y 30 min de revisión al día siguiente)*

**Objetivo:** comprobar que el negocio funciona un día laborable completo sin ti.

**Cómo hacerlo con IA:** avisa a tu equipo, deja el documento «Si no estoy» a mano y desconecta: ni correo, ni WhatsApp del negocio, ni CRM. Al día siguiente, revisa qué pasó con Claude.

```text
Ayer hice un día sin tocar el negocio. Esto es lo que ha pasado: [mensajes recibidos, lo que resolvió el equipo, lo que resolvieron los agentes, lo que se quedó esperando].
1. Clasifica lo que pasó en: resuelto solo, resuelto por el equipo, esperó sin problema, esperó y fue un problema.
2. Para cada cosa del último grupo, dime qué falta: un procedimiento, un permiso, una automatización o una persona.
3. Dame la lista de ajustes para que la próxima vez puedan ser dos días.
```

**Checklist:**
- [ ] He pasado un día laborable sin tocar el negocio
- [ ] He revisado qué pasó al día siguiente
- [ ] Tengo la lista de lo que falta para aguantar más días
- [ ] He fijado la fecha de la próxima prueba, con dos días

**Error típico:** mirar el móvil «solo un momento». Si miras, no sabes si el sistema aguanta solo o si lo estás sosteniendo tú otra vez.

---

### Paso 60 · Revisión final y los siguientes 90 días
*Fase 5 · Semana 12, viernes · 90 min*

**Objetivo:** comparar tu negocio de hoy con el del paso 12 y decidir, con tiempo y datos, qué quieres hacer en los próximos 90 días.

**Cómo hacerlo con IA:**

```text
Hace 90 días mi negocio estaba así: [pega el resumen del «antes» del paso 12].
Hoy está así: [mis 5 números, horas a la semana, tiempo de respuesta, conversión, clientes, lo montado en cada fase].
1. Compara antes y después, número a número, sin adornar: qué ha mejorado, qué sigue igual y qué ha empeorado.
2. Dime cuántas horas a la semana he recuperado y qué estoy haciendo con ellas.
3. Hazme 5 preguntas para decidir hacia dónde llevar el negocio: crecer, mantener con menos horas, lanzar algo nuevo o prepararlo para venderlo.
4. Con mis respuestas, propón las 3 prioridades de los próximos 90 días y qué fase de este plan conviene repetir primero.
```

**Checklist:**
- [ ] He comparado el antes y el después con números
- [ ] Sé cuántas horas a la semana he recuperado
- [ ] He decidido hacia dónde llevar el negocio los próximos 90 días
- [ ] He bloqueado en el calendario la próxima revisión trimestral

**Error típico:** terminar el plan y dejar de revisar. Lo que montaste funciona mientras alguien lo mira una hora a la semana; sin eso, en tres meses vuelves al caos.

---

## Y ahora qué

Has medido, ordenado, captado, crecido y te has dado tiempo para decidir. Lo que montaste en estos 90 días es tuyo: tus números, tus procesos, tus agentes. Sigue con la revisión semanal y repite las fases que más te han costado.

Si quieres que te ayudemos a montarlo en tu negocio o a dedicarte a montarlo para otros, escríbenos en https://sellyourai.io.

Hecho por Denis Corral · Sell Your AI
