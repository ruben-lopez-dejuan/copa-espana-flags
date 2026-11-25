import math
import os

H = os.path.dirname(os.path.abspath(__file__))
U = '../..'
V = 'banderas'
T = {
    'an': ('Andalucía', 'Andalucía', [('Lorenzo Escobar Kraskouskaya', 6.10), ('Marisa Revaliente Ruiz', 7.05), ('Carlos Méndez García-Barroso', 7.12)]),
    'ct': ('Cataluña', 'Cataluña', [('Biel Salmons Gonzalez', 6.31), ('Arnau Tous Mateu', 7.31), ('Vidal Perea Cívico', 7.96)]),
    'pv': ('Euskadi', 'Euskadi', [('Aratz Larruzea', 7.10), ('Eder Olivencia González', 7.47), ('Óscar Gervasini Lois', 7.57)]),
    'md': ('Madrid', 'Comunidad de Madrid', [('Manuel Prieto de Antón', 7.25), ('Carlos Cascos González', 7.64), ('Raúl Martínez Redondo', 8.01)]),
    'vc': ('C. Valenciana', 'Comunidad Valenciana', [('Diego Serrano Martínez', 7.04), ('David Sánchez Peris', 7.17), ('Arnau López García', 9.18)]),
    'ar': ('Aragón', 'Aragón', [('Miguel Martínez Montañés', 7.36), ('Antonio López', 8.05), ('Marcos Plaza Nocito', 8.57)]),
    'nc': ('Navarra', 'Navarra', [('Julen Simon Iriarte', 7.72), ('Aitor Ibáñez Larrea', 7.81), ('José Miguel Beguiristain', 8.62)]),
    'cm': ('Castilla-La Mancha', 'Castilla-La Mancha', [('Raúl Cuevas Castillo', 8.23), ('Iker Carrasco Ruiz', 8.97), ('Nuria Soria García', 9.94)]),
    'cn': ('Canarias', 'Canarias', [('Gael Galeote Flores', 7.91), ('Jorge Darias Rodríguez', 9.49), ('Arturo José Sánchez Plaza', 12.55)]),
    'mc': ('Murcia', 'Región de Murcia', [('Pablo Amoraga Velasco', 8.18), ('Marcos Caballero Marsilla', 8.79), ('Jose Sánchez García', 9.44)]),
    'ga': ('Galicia', 'Galicia', [('Sergio Márquez Fernández-Jardón', 7.80), ('Yeray Varela Mouzo', 11.04), ('Fernando Lago Díaz', 11.85)]),
    'cl': ('Castilla y León', 'Castilla y León', [('Ismael Pérez Herrero', 10.50), ('Samuel María Liñares', 10.56), ('Diego Rodríguez Villafañe', 13.45)]),
}
B = ['an', 'ct', 'pv', 'md', 'vc', 'ar', 'nc', 'mc', 'cm', 'cn', 'ga', 'cl']  # según las medias actuales
BW, BH, G, SC = 540, 88, 8, 74

CSS = """@page{size:297mm 210mm;margin:0}*{margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}body{background:#fff}
section{width:297mm;height:210mm;overflow:hidden;break-after:page}section:last-child{break-after:auto}
svg{display:block;width:297mm;height:210mm;font-family:"Roboto Condensed","Arial Narrow",Arial,sans-serif}
.nm{font-size:38px;font-weight:700;fill:#fff}.sd{font-size:32px;font-weight:700;fill:#fff}.ph{font-size:30px;fill:#8b93a3}
.lb{font-size:29px;font-weight:700;fill:#fff;letter-spacing:1px}.fl{font-size:44px;font-weight:700;fill:#fff;letter-spacing:4px}
.t1{font-size:104px;font-weight:700;fill:#fff}.t2{font-size:58px;font-weight:700;fill:#fff;letter-spacing:2px}.cn{fill:none;stroke:#fff;stroke-width:4}
.s2{font-size:52px;font-weight:700;fill:#fff}.n2{font-size:47px;font-weight:700;fill:#fff}.p2{font-size:37px;fill:#14181f}
.v2{font-size:42px;font-weight:700;fill:#14181f}.m2{font-size:38px;font-weight:700;fill:#0a3f9c}.mv{font-size:52px;font-weight:700;fill:#0a3f9c}"""


def build(seed, out):
    S = []
    a = S.append
    s = lambda n: seed[n - 1]

    def flag(c, x, y, w, h):
        return f'<image href="{V}/es-{c}.png" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="none"/>'

    def bar(x, y, right, team=None, ph=''):
        sx = x if right else x + BW - SC
        fill = '#05070c' if team else '#fff'
        a(f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="6" fill="{fill}" stroke="#fff" stroke-width="3"/>')
        a(f'<rect x="{sx}" y="{y}" width="{SC}" height="{BH}" rx="6" fill="#e6e2da" stroke="#fff" stroke-width="3"/>')
        if not team:
            tx, an = (x + BW - 20, 'end') if right else (x + 20, 'start')
            a(f'<text x="{tx}" y="{y+53}" class="ph" text-anchor="{an}">{ph}</text>')
            return
        n, cy = seed.index(team) + 1, y + 56
        if right:
            a(f'<text x="{x+BW-36}" y="{cy-2}" class="sd" text-anchor="middle">{n}</text>' + flag(team, x + BW - 132, y + 19, 62, 46))
            a(f'<text x="{x+BW-150}" y="{cy}" class="nm" text-anchor="end">{T[team][0]}</text>')
        else:
            a(f'<text x="{x+36}" y="{cy-2}" class="sd" text-anchor="middle">{n}</text>' + flag(team, x + 70, y + 19, 62, 46))
            a(f'<text x="{x+146}" y="{cy}" class="nm">{T[team][0]}</text>')

    def pair(x, c, right, t1, t2, lab, p1='', p2=''):
        y = c - BH - G / 2
        bar(x, y, right, t1, p1)
        bar(x, c + G / 2, right, t2, p2)
        tx, an = (x + BW, 'end') if right else (x, 'start')
        a(f'<text x="{tx}" y="{y-14}" class="lb" text-anchor="{an}">{lab}</text>')

    cs = [600, 875, 1150, 1425, 1700]
    L = [100, 320, 540]
    RX = [2970 - x - BW for x in L]

    def con(xe, c, cn, right):
        m = xe + (-26 if right else 26)
        yl = cn + (-1 if cn > c else 1) * (BH + G / 2)
        a(f'<path d="M{xe} {c-48} H{m} V{c+48} H{xe} M{m} {c} V{yl}" class="cn"/>')

    for right in (False, True):
        X = RX if right else [x + BW for x in L]
        con(X[0], cs[0], cs[1], right)
        con(X[0], cs[4], cs[3], right)
        con(X[1], cs[1], cs[2], right)
        con(X[1], cs[3], cs[2], right)
        m = X[2] + (-15 if right else 15)
        f = 1860 if right else 1110
        a(f'<path d="M{X[2]} {cs[2]-48} H{m} V{cs[2]+48} H{X[2]} M{m} {cs[2]} H{f}" class="cn"/>')

    pair(L[0], cs[0], False, s(8), s(9), 'PRIMERA RONDA · P1')
    pair(L[0], cs[4], False, s(5), s(12), 'PRIMERA RONDA · P2')
    pair(RX[0], cs[0], True, s(6), s(11), 'PRIMERA RONDA · P3')
    pair(RX[0], cs[4], True, s(7), s(10), 'PRIMERA RONDA · P4')
    pair(L[1], cs[1], False, s(1), None, 'CUARTOS · C1', p2='Ganador P1')
    pair(L[1], cs[3], False, None, s(4), 'CUARTOS · C2', p1='Ganador P2')
    pair(RX[1], cs[1], True, s(3), None, 'CUARTOS · C3', p2='Ganador P3')
    pair(RX[1], cs[3], True, None, s(2), 'CUARTOS · C4', p1='Ganador P4')
    pair(L[2], cs[2], False, None, None, 'SEMIFINAL · S1', 'Ganador C1', 'Ganador C2')
    pair(RX[2], cs[2], True, None, None, 'SEMIFINAL · S2', 'Ganador C3', 'Ganador C4')
    for x, p in ((1110, 'Ganador S1'), (1500, 'Ganador S2')):
        a(f'<rect x="{x}" y="1040" width="360" height="220" rx="6" fill="#fff" stroke="#fff" stroke-width="3"/>'
          f'<rect x="{x}" y="1040" width="360" height="66" rx="6" fill="#e6e2da"/>'
          f'<text x="{x+180}" y="1238" class="ph" text-anchor="middle">{p}</text>')
    a('<text x="1485" y="1012" class="fl" text-anchor="middle">FINAL</text>')
    a('<text x="1485" y="1752" class="lb" text-anchor="middle">TERCER Y CUARTO PUESTO</text>')
    bar(930, 1776, False, None, 'Perdedor S1')
    bar(1500, 1776, True, None, 'Perdedor S2')

    hx = ''
    for x, y, r in [(330, 300, 230), (800, 560, 180), (2350, 330, 260), (2700, 1050, 230), (420, 1500, 260),
                    (1500, 1500, 320), (2250, 1750, 230), (1250, 820, 200), (1900, 900, 240), (160, 1000, 170)]:
        P = [(x + r * math.sin(math.pi / 3 * k), y - r * math.cos(math.pi / 3 * k)) for k in range(6)]
        hx += '<path d="M' + ' L'.join(f'{px:.0f} {py:.0f}' for px, py in P) + 'Z '
        hx += ' '.join(f'M{x} {y} L{P[k][0]:.0f} {P[k][1]:.0f}' for k in (1, 3, 5)) + '"/>'

    def page(body, i):
        return (f'<section><svg viewBox="0 0 2970 2100"><defs><linearGradient id="g{i}" x1="0" y1="1" x2="1" y2="0">'
                f'<stop offset="0" stop-color="#062d72"/><stop offset="1" stop-color="#0a55c9"/></linearGradient>'
                f'<clipPath id="k{i}"><rect x="60" y="60" width="2850" height="1980" rx="30"/></clipPath></defs>'
                f'<rect x="60" y="60" width="2850" height="1980" rx="30" fill="url(#g{i})"/>'
                f'<g fill="#fff" fill-opacity=".035" stroke="#fff" stroke-opacity=".09" stroke-width="5" clip-path="url(#k{i})">{hx}</g>'
                f'{body}</svg></section>')

    logo = U + '/logos/campeonato-espana-2026-horizontal.svg'
    head = (f'<image href="{logo}" x="1185" y="84" width="600" height="222"/>'
            '<rect x="1105" y="330" width="760" height="270" fill="#05070c" stroke="#fff" stroke-width="7"/>'
            '<text x="1485" y="450" class="t1" text-anchor="middle">NACIONAL 2026</text><path d="M1165 494 H1805" stroke="#fff" stroke-width="3"/>'
            '<text x="1485" y="564" class="t2" text-anchor="middle">COPA DE ESPAÑA</text>')

    C = []
    cw, ch, gx, gy, y0 = 670, 500, 30, 34, 350
    x0 = (2970 - 4 * cw - 3 * gx) / 2
    f2 = lambda v: f'{v:.2f}'.replace('.', ',')
    for k, c in enumerate(seed):
        x, y = x0 + (k % 4) * (cw + gx), y0 + (k // 4) * (ch + gy)
        _, full, m = T[c]
        C.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="#fff"/>'
                 f'<path d="M{x} {y+110} V{y+12} a12 12 0 0 1 12 -12 H{x+cw-12} a12 12 0 0 1 12 12 V{y+110}Z" fill="#05070c"/>'
                 f'<text x="{x+46}" y="{y+74}" class="s2" text-anchor="middle">{k+1}</text>' + flag(c, x + 96, y + 26, 78, 58) +
                 f'<text x="{x+196}" y="{y+73}" class="n2">{full}</text>')
        for j, (p, v) in enumerate(m):
            yy = y + 110 + j * 94
            C.append(f'<text x="{x+26}" y="{yy+62}" class="p2">{p}</text><text x="{x+cw-26}" y="{yy+62}" class="v2" text-anchor="end">{f2(v)}</text>'
                     f'<path d="M{x+24} {yy+94} H{x+cw-24}" stroke="#c9ced8" stroke-width="3"/>')
        C.append(f'<text x="{x+30}" y="{y+462}" class="m2">Media del equipo</text>'
                 f'<text x="{x+cw-30}" y="{y+464}" class="mv" text-anchor="end">{f2(sum(v for _, v in m) / 3)}</text>')
    h2 = (f'<image href="{logo}" x="130" y="102" width="560" height="207"/>'
          '<text x="2840" y="200" class="t1" text-anchor="end">COPA DE ESPAÑA</text>'
          '<text x="2840" y="276" class="t2" text-anchor="end">EQUIPOS Y PARTICIPANTES</text>')
    html = ('<!doctype html><html lang="es"><meta charset="utf-8"><title>Copa de España 2026</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&display=block" rel="stylesheet">'
            f'<style>{CSS}</style>' + page(head + ''.join(S), 1) + page(h2 + ''.join(C), 2) + '</html>')
    open(os.path.join(H, out), 'w', encoding='utf8').write(html)


m = lambda c: sum(v for _, v in T[c][2]) / 3
assert B == sorted(T, key=m), 'orden de semillas'
build(B, 'bracket.html')
