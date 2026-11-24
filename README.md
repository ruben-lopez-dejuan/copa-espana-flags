# Banderas Copa de España — paquete gráfico WMCT (Singular)

Banderas de las comunidades y ciudades autónomas en formato **4:3 (640×480)**, que es la proporción
a la que las estira el paquete gráfico (`object-fit: fill`). Si se usan en 3:2 salen deformadas.

![preview](preview.png)

## Cómo usarlas en Singular

El campo **Team Flag** (Nations Cup) no admite URLs: el gráfico construye
`https://raw.githubusercontent.com/wca-major-championships-team/graphics_package_resources/refs/heads/main/flags/4x3/<CÓDIGO>.svg`.

Escribiendo `../` siete veces se "sube" hasta la raíz de `raw.githubusercontent.com`
y se puede apuntar a **este repo** (público, rama `main`, archivos en la raíz):

```
../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-md
```

→ carga `https://raw.githubusercontent.com/ruben-lopez-dejuan/copa-espana-flags/main/es-md.svg`

> Probado en el control app del Campeonato de España (noviembre 2026) con el elemento NationsCup.

### Chuleta de códigos

| Comunidad | Archivo | Código corto (repo WMCT) | Código para Singular (este repo) |
|---|---|---|---|
| Andalucía | es-an.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-an` |
| Aragón | es-ar.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-ar` |
| Asturias | es-as.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-as` |
| Illes Balears | es-ib.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-ib` |
| Canarias | es-cn.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-cn` |
| Cantabria | es-cb.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-cb` |
| Castilla y León | es-cl.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-cl` |
| Castilla-La Mancha | es-cm.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-cm` |
| Cataluña | es-ct.svg | `es-ct` | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-ct` |
| Extremadura | es-ex.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-ex` |
| Galicia | es-ga.svg | `es-ga` | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-ga` |
| La Rioja | es-ri.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-ri` |
| Comunidad de Madrid | es-md.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-md` |
| Región de Murcia | es-mc.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-mc` |
| Navarra | es-nc.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-nc` |
| País Vasco | es-pv.svg | `es-pv` | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-pv` |
| Comunitat Valenciana | es-vc.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-vc` |
| Ceuta | es-ce.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-ce` |
| Melilla | es-ml.svg | — | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es-ml` |
| España | es.svg | `es` | `../../../../../../../ruben-lopez-dejuan/copa-espana-flags/main/es` |

Consejo: usar siempre la columna de este repo para todas (también Cataluña, Galicia y País Vasco),
así todas las banderas vienen del mismo sitio y si una falla, fallan todas igual.

## Cómo se han hecho

- Fuente: SVG de Wikimedia Commons (y `es-ct`, `es-ga`, `es-pv`, `es` de
  [lipis/flag-icons](https://github.com/lipis/flag-icons), que ya son 4:3).
- Conversión 3:2 → 4:3 recortando ~5,5 % por cada lado (centrado). En Aragón, Baleares y
  Comunitat Valenciana el recorte se hace solo por el lado del vuelo para no cortar el cantón/escudo.
  Murcia se encaja entera y se rellena arriba/abajo con su mismo granate (#9c1f2d).
- Cantabria y Extremadura: versión sin escudo (se ven mejor a ~18 px). La Rioja: con escudo
  (es la única versión disponible en Commons).

## Licencias de origen

| Archivo | Licencia (Wikimedia Commons) |
|---|---|
| es-an | CC BY-SA 4.0 |
| es-ar | CC BY-SA 3.0 |
| es-as, es-cm, es-cn, es-ex, es-nc, es-vc | Dominio público |
| es-cb | CC BY-SA 2.5 |
| es-cl | CC BY 3.0 |
| es-ce | CC BY-SA 4.0 |
| es-ib, es-md, es-mc | CC0 |
| es-ml | CC BY-SA 3.0 |
| es-ri | CC BY 2.5 |
| es-ct, es-ga, es-pv, es | MIT (lipis/flag-icons) |

Los archivos CC BY / CC BY-SA requieren atribución a sus autores en Wikimedia Commons
(página del archivo "Flag of …"). Si se publica el repo, enlazar a esas páginas.
