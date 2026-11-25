Te paso el contexto de un proyecto a medias. Ayúdame a preparar lo que falta. Tú no tienes acceso a Singular ni a mi Drive: tu trabajo es generarme archivos y textos listos para copiar/subir, y decirme exactamente dónde pegarlos.

## Contexto

- Evento: Campeonato de España de Speedcubing 2026 (Barakaldo, Bizkaia). Retransmisión con el paquete gráfico de la WCA (Kevin Hays, WMCT) en Singular.live, usando el "control app" (no tocamos la composición).
- Dentro del campeonato hay una "Copa de España": 12 equipos por comunidades autónomas, eliminatoria, con el elemento "NationsCup" (3 tiempos por equipo, gana la suma más baja) y el elemento "Bracket" (datos desde una Google Sheet + Data Stream de Singular).
- Las imágenes en Singular tienen que ser URLs que devuelvan la imagen en crudo (raw.githubusercontent.com).
- Repo público mío para recursos: https://github.com/ruben-lopez-dejuan/recursos-streaming-nacional (rama main). Ahí están las banderas y el logo:
  - Logo símbolo: https://raw.githubusercontent.com/ruben-lopez-dejuan/recursos-streaming-nacional/main/logos/campeonato-espana-2026-simbolo.svg
  - Logo horizontal: https://raw.githubusercontent.com/ruben-lopez-dejuan/recursos-streaming-nacional/main/logos/campeonato-espana-2026-horizontal.svg
  - Logo completo: https://raw.githubusercontent.com/ruben-lopez-dejuan/recursos-streaming-nacional/main/logos/campeonato-espana-2026.svg
  - Los logos son la versión en blanco (para fondo oscuro).

## Ya hecho (no rehacer)

- Banderas de las 17 comunidades + Ceuta y Melilla en 4:3. En el campo "Team Flag" de NationsCup se escribe `../../../../../../../ruben-lopez-dejuan/recursos-streaming-nacional/main/es-md` (siete `../`, sin .svg). Códigos: es-an, es-ar, es-as, es-ib, es-cn, es-cb, es-cl, es-cm, es-ct, es-ex, es-ga, es-ri, es-md, es-mc, es-nc, es-pv, es-vc, es-ce, es-ml. Hay un PR abierto al repo oficial para que valgan los códigos cortos (es-md…); hasta que se acepte, ruta larga.
- Google Sheet del bracket (copia de la plantilla H2H de la WCA) con los 12 equipos, semillas y banderas, conectada a un Data Stream de Singular. Bracket visible en Singular con logo, título "CAMPEONATO DE ESPAÑA 2026" y evento "Copa de España".
- Cuadro (12 equipos, las semillas 1-4 pasan directas a cuartos):
  - Octavos: Murcia (8) – Castilla-La Mancha (9); C. Valenciana (5) – Castilla y León (12); Aragón (6) – Galicia (11); Navarra (7) – Canarias (10).
  - Cuartos esperan: Andalucía (1), Madrid (4), País Vasco (3), Cataluña (2).

## Lo que falta y en qué me tienes que ayudar

1. **Fact URL (datos curiosos de la Player Card).** Hay que generar un JSON donde la clave es el WCA ID (respetando mayúsculas) y el valor es una lista de frases cortas. Ejemplo del formato oficial:
   ```json
   {
     "2016KAMA04": ["Campeón de España de Megaminx 2024", "141 medallas WCA"],
     "2017MCKE02": ["186 medallas WCA"]
   }
   ```
   - Máximo 3-4 frases por persona, cortas (caben ~45 caracteres por línea; se puede forzar salto con `\n`).
   - Te pasaré una lista de competidores (nombre + WCA ID) y datos sueltos; tú me devuelves el JSON válido, en español, sin inventar datos: si no tienes un dato, no lo pongas.
   - El archivo se subirá al repo como `competitor_facts.json`, y en Singular (Global Data → Player Card Data → Fact URL) se pega su URL raw y se pulsa "Update Facts".

2. **Fotos de competidores (Player Card).** Las fotos van en una carpeta de un repo público de GitHub, cada archivo con nombre = WCA ID exacto (ej. `2015LOPE01.png`). En Global Data → Player Card Data se ponen cuenta, repo y carpeta, y se pulsa "Update Pictures". Si no hay foto, usa la del perfil WCA.
   - Ayúdame con un script (PowerShell, estoy en Windows) que renombre fotos a partir de un CSV `nombre_archivo,wca_id`, y con el mismo formato/recorte para todas.

3. **Global Data (ronda en directo).** Hay que poner el ID de la competición en WCA Live ("Live Comp ID" o elegirla en "Competition"), y en cada ronda cambiar Event y Round. Hazme una tabla del horario con evento + número de ronda para tenerla a mano (te pasaré el horario).
   - Opciones de nombre: "Name Override" y "Name Semifinals". Dime cómo dejarlo para que las rondas salgan en español si se puede (p. ej. "Final", "Semifinal").
   - El desplegable "Competitor" solo trae gente del top 1000 mundial; para el resto se usa "Manual WCA ID". Prepárame la lista de WCA IDs de finalistas probables para copiar rápido.

4. **Event Label, Logos y Fullscreen Logo.** Rellenar con el nombre de la competición y los logos (URLs de arriba). Si hay patrocinadores, me ayudas a preparar sus logos (SVG o PNG con fondo transparente, versión clara para fondo oscuro) para subirlos al repo en `logos/`.

5. **Caster Tags, Lower Third e Info Tag.** Prepárame los textos (nombres de comentaristas, cargos, rótulos del tipo "Copa de España · Octavos de final"), cortos y en el mismo estilo.

6. **Copa de España en directo (NationsCup).** Una entrada en la playlist por cada partido, con nombres y banderas ya puestos. Durante el partido se teclean los 3 tiempos por equipo (cada uno se emite al pulsar Tab). Nombres y banderas solo se emiten al pulsar "Update". Después se apunta el resultado en la Google Sheet (pestaña Bracket) y se pulsa "Update Bracket".
   - Hazme una chuleta de 1 página para el operador con este flujo y la tabla de partidos (nombre del equipo + código de bandera).
   - Pendiente de averiguar: cómo se marca un DNF en NationsCup (no hay campo; probar con un tiempo muy alto como 999 y ver qué pasa).

7. **Checklist del día** (antes de emitir): Global Data en ON (▶), token público puesto, test data desactivado, salida de Singular metida en OBS, prueba de cada elemento.

## Reglas

- No inventes datos de competidores ni récords.
- Nunca me pidas tokens ni los pongas en ningún archivo.
- No hay que modificar la plantilla oficial de la WCA ni la composición de Singular; todo se hace desde el control app y archivos propios.
- Respuestas prácticas: archivos completos listos para pegar, y dónde va cada cosa.

Empieza por decirme qué datos necesitas de mí para los puntos 1, 2 y 3, en una lista corta.
