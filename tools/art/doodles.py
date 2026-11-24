"""Cute, modern flat doodles for SHHA. Flat colour, round shapes, simple dot eyes.
Entries: (kind, colour, svg). kind: F fill, L line, T thin line, INK navy fill, W white fill, G group."""
import math, re
INK = '#1c2b45'
P = dict(
    skin='#c98a5e', skin2='#a96b42', skin3='#dba477', hair='#2b1d16',
    blue='#5b8def', blueL='#8fb2f5', coral='#ef6b5b', coralL='#f6988c', mustard='#f4b942', mustardL='#f8cf73',
    mint='#7cc6a4', mintL='#a9dcc3', navy='#2f4a7a', navyL='#5a74a3', lilac='#a99bea', white='#ffffff',
    cream='#fff6e9', blush='#f58f80', sun='#ffd36e', hill1='#d6eedd', hill2='#bfe3ca', sea='#9cc3f2', seaL='#bcd6f7',
    red='#e2483a', wall1='#fde7c4', wall2='#ffffff', wall3='#d9e6fb', dome='#5b8def', trunk='#8a6a52')

def g(tf, items): return [('G', tf, items)]
def at(x, y, items, s=1): return g(f'translate({x:.1f} {y:.1f})' + (f' scale({s:.3f})' if s != 1 else ''), items)

def eyes(cx, cy, gap=14, r=4.4, closed=False):
    if closed:
        return [('L', None, f'<path d="M{cx-gap-4} {cy} q4 4 8 0 M{cx+gap-4} {cy} q4 4 8 0"/>')]
    it = []
    for x in (cx - gap, cx + gap):
        it += [('INK', None, f'<ellipse cx="{x}" cy="{cy}" rx="{r*.86:.1f}" ry="{r*1.12:.1f}"/>'),
               ('W', None, f'<circle cx="{x+1.4}" cy="{cy-1.8}" r="1.5"/>')]
    return it

def cheeks(cx, cy, gap=25):
    return [('F', P['blush'], f'<ellipse cx="{cx-gap}" cy="{cy}" rx="7.5" ry="4.6" opacity=".55"/>'),
            ('F', P['blush'], f'<ellipse cx="{cx+gap}" cy="{cy}" rx="7.5" ry="4.6" opacity=".55"/>')]

def smile(cx, cy, w=7, open_=False):
    if open_:
        return [('F', '#8c2f2a', f'<path d="M{cx-w} {cy} q{w} {w*1.3:.1f} {2*w} 0 Z"/>'),
                ('F', '#f08a8a', f'<path d="M{cx-w*.55:.1f} {cy+w*.62:.1f} q{w*.55:.1f} {w*.5:.1f} {w*1.1:.1f} 0 q{-w*.55:.1f} {-w*.45:.1f} {-w*1.1:.1f} 0 Z"/>')]
    return [('L', None, f'<path d="M{cx-w} {cy} q{w} {w*.85:.1f} {2*w} 0"/>')]

def kid_hijab(hij='blue', dress='mustard', skin='skin', mood='smile', arm=None):
    it = []
    it += [('F', P[dress], '<path d="M54 200 C 54 172 74 152 100 152 C 126 152 146 172 146 200 Z"/>'),
           ('F', P[dress + 'L'] if dress + 'L' in P else P['white'], '<path d="M74 176 h10 M92 182 h10 M110 176 h10 M120 192 h10 M80 194 h10" stroke="' + (P[dress + 'L'] if dress + 'L' in P else '#fff') + '" stroke-width="5" stroke-linecap="round"/>')]
    if arm: it += arm
    it += [('F', P[hij], '<path d="M100 26 C 56 26 36 60 38 98 C 40 126 52 148 68 162 C 84 172 116 172 132 162 C 148 148 160 126 162 98 C 164 60 144 26 100 26 Z"/>'),
           ('F', P[hij + 'L'], '<path d="M70 44 C 80 34 92 31 104 31 C 92 36 80 44 74 56 Z" opacity=".9"/>'),
           ('F', P[skin], '<ellipse cx="100" cy="102" rx="40" ry="41"/>')]
    it += eyes(100, 100, closed=(mood == 'closed')) + cheeks(100, 116) + smile(100, 117, 7, mood == 'big')
    return it

def kid_boy(shirt='mint', skin='skin2'):
    it = [('F', P[shirt], '<path d="M56 200 C 56 172 76 152 100 152 C 124 152 144 172 144 200 Z"/>'),
          ('F', P[shirt + 'L'], '<path d="M86 154 q14 12 28 0 v8 q-14 10 -28 0 Z"/>'),
          ('F', P[skin], '<circle cx="58" cy="104" r="10"/>'), ('F', P[skin], '<circle cx="142" cy="104" r="10"/>'),
          ('F', P[skin], '<circle cx="100" cy="102" r="44"/>')]
    bumps = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(66,80,13),(78,66,14),(94,58,15),(110,58,15),(125,64,14),(136,78,13),(140,92,8),(60,92,8)])
    it += [('F', P['hair'], bumps)]
    it += eyes(100, 106) + cheeks(100, 122, 27) + smile(100, 122, 8, True)
    return it

def flag_arm(dress='mint'):
    return [('F', P[dress], '<path d="M132 168 C 146 160 152 140 154 118 L 166 120 C 166 146 158 168 144 180 Z"/>'),
            ('L', None, '<path d="M162 200 L 176 30"/>'),
            ('F', '#4189dd', '<path d="M176 32 C 194 26 208 40 228 34 L 223 80 C 204 86 190 72 172 78 Z"/>'),
            ('W', None, '<path d="M199 44 l4 9 10 1 -7.5 6.6 2.2 9.8 -8.7 -5 -8.7 5 2.2 -9.8 -7.5 -6.6 10 -1 z"/>'),
            ('F', P['skin'], '<circle cx="162" cy="114" r="9"/>')]

def wave_arm(dress='mint', skin='skin3'):
    return [('F', P[dress], '<path d="M132 168 C 146 160 152 140 154 122 L 166 124 C 166 148 158 168 144 180 Z"/>'),
            ('F', P[skin], '<ellipse cx="161" cy="112" rx="11" ry="13"/>'),
            ('T', None, '<path d="M146 90 q-5 -5 -3 -12 M178 88 q5 -5 3 -12"/>')]

def mom_baby():
    it = [('F', P['coral'], '<path d="M40 200 C 40 166 66 146 100 146 C 134 146 160 166 160 200 Z"/>'),
          ('F', P['navy'], '<path d="M100 22 C 56 22 38 56 40 94 C 42 122 52 144 66 158 C 82 168 118 168 134 158 C 148 144 158 122 160 94 C 162 56 144 22 100 22 Z"/>'),
          ('F', P['navyL'], '<path d="M70 40 C 80 30 92 27 104 27 C 92 32 80 40 74 52 Z"/>'),
          ('F', P['skin2'], '<ellipse cx="100" cy="96" rx="38" ry="39"/>')]
    it += eyes(100, 94, closed=True) + cheeks(100, 110, 24) + smile(100, 112, 6)
    it += [('F', P['mustard'], '<path d="M44 176 C 44 156 70 148 104 150 C 138 152 160 160 160 178 C 160 194 134 200 104 200 C 72 200 44 194 44 176 Z"/>'),
           ('F', P['mustardL'], ''.join(f'<circle cx="{x}" cy="{y}" r="3"/>' for x, y in [(96,166),(116,162),(136,168),(108,184),(128,186),(148,182)])),
           ('F', P['skin3'], '<circle cx="70" cy="164" r="20"/>'),
           ('F', P['hair'], '<path d="M52 160 C 52 146 62 142 70 143 C 80 143 88 150 88 160 C 82 152 74 150 70 152 C 62 150 56 154 52 160 Z"/>')]
    it += [('L', None, '<path d="M60 166 q3 3 6 0 M74 166 q3 3 6 0"/>'), ('F', P['blush'], '<ellipse cx="58" cy="174" rx="4" ry="2.6" opacity=".6"/><ellipse cx="82" cy="174" rx="4" ry="2.6" opacity=".6"/>'),
           ('F', P['skin2'], '<ellipse cx="150" cy="168" rx="12" ry="10"/>'),
           ('F', P['coral'], '<path d="M100 130 c -3 -5 -11 -3 -8 3 l 8 8 l 8 -8 c 3 -6 -5 -8 -8 -3 z"/>')]
    return it

def doctor():
    it = [('F', P['white'], '<path d="M44 200 C 44 168 68 150 100 150 C 132 150 156 168 156 200 Z"/>'),
          ('F', P['blueL'], '<path d="M86 152 L 100 184 L 114 152 Z"/>'),
          ('T', None, '<path d="M86 152 L 100 184 L 114 152 M100 184 V 200"/>'),
          ('T', None, '<path d="M44 200 C 44 168 68 150 100 150 C 132 150 156 168 156 200"/>'),
          ('F', P['red'], '<path d="M62 172 h4 v-5 h4 v5 h4 v4 h-4 v5 h-4 v-5 h-4 Z"/>'),
          ('F', P['navy'], '<path d="M100 24 C 58 24 40 56 42 94 C 44 120 54 140 68 154 C 84 162 116 162 132 154 C 146 140 156 120 158 94 C 160 56 142 24 100 24 Z"/>'),
          ('F', P['navyL'], '<path d="M70 42 C 80 32 92 29 104 29 C 92 34 80 42 74 54 Z"/>'),
          ('F', P['skin'], '<ellipse cx="100" cy="98" rx="38" ry="39"/>')]
    it += eyes(100, 96) + cheeks(100, 112, 24) + smile(100, 113, 6)
    it += [('L', None, '<path d="M78 156 C 70 174 78 190 98 190 C 112 190 120 182 120 172"/>'),
           ('F', P['mustard'], '<circle cx="120" cy="170" r="7"/>'), ('W', None, '<circle cx="120" cy="170" r="3"/>')]
    return it

def man(shirt='blue', skin='skin2'):
    it = [('F', P[shirt], '<path d="M54 200 C 54 170 76 150 100 150 C 124 150 146 170 146 200 Z"/>'),
          ('F', P[shirt + 'L'], '<path d="M88 152 L 100 166 L 112 152 Z"/>'),
          ('F', P[skin], '<circle cx="58" cy="100" r="9"/>'), ('F', P[skin], '<circle cx="142" cy="100" r="9"/>'),
          ('F', P[skin], '<circle cx="100" cy="98" r="42"/>'),
          ('F', P['hair'], '<path d="M60 92 C 56 58 80 48 100 48 C 122 48 146 58 140 92 C 132 74 118 68 100 70 C 84 68 68 74 60 92 Z"/>'),
          ('F', P['hair'], '<path d="M70 116 C 78 142 122 142 130 116 C 124 130 112 134 100 134 C 88 134 76 130 70 116 Z"/>')]
    it += eyes(100, 100) + cheeks(100, 114, 26) + smile(100, 116, 6)
    return it

def family():
    it = []
    it += at(-8, 22, man(), .82)
    it += at(150, 14, kid_hijab('coral', 'navy', 'skin'), .86)
    it += at(94, 74, kid_boy('mustard', 'skin3'), .6)
    it += at(214, 78, kid_hijab('blue', 'mustard', 'skin3', 'big'), .58)
    return it

def hands_heart():
    """Two friends sharing a big heart."""
    it = []
    it += at(-34, 40, kid_hijab('mustard', 'blue', 'skin2', 'big'), .8)
    it += at(74, 40, kid_boy('coral', 'skin'), .8)
    it += at(100, 40, [('F', P['coral'], '<path d="M0 -6 c -6 -10 -22 -6 -16 6 l 16 15 l 16 -15 c 6 -12 -10 -16 -16 -6 z"/>'), ('F', P['coralL'], '<path d="M-12 -6 c 2 -3 6 -3 8 -1 c -3 0 -6 2 -7 5 z"/>')], 1.7)
    return it

# props
def sun(r=24): return [('F', P['sun'], f'<circle r="{r*1.45:.0f}" opacity=".35"/>'), ('F', P['sun'], f'<circle r="{r}"/>')]
def cloud(s=1): return [('F', P['white'], f'<path transform="scale({s})" d="M0 0 C -2 -12 12 -18 20 -10 C 24 -24 46 -24 50 -8 C 60 -10 66 0 60 8 L 2 8 C -6 8 -8 2 0 0 Z"/>')]
def bird(): return [('T', None, '<path d="M0 0 q6 -6 12 0 q6 -6 12 0"/>')]
def sparkle(s=1, col='sun'): return [('F', P[col], f'<path transform="scale({s})" d="M0 -12 C 2 -3 3 -2 12 0 C 3 2 2 3 0 12 C -2 3 -3 2 -12 0 C -3 -2 -2 -3 0 -12 Z"/>')]
def heart(s=1): return [('F', P['coral'], f'<path transform="scale({s})" d="M0 -6 c -6 -10 -22 -6 -16 6 l 16 15 l 16 -15 c 6 -12 -10 -16 -16 -6 z"/>')]
def acacia(s=1):
    return g(f'scale({s})', [('F', 'none', '<path d="M0 0 C 2 -24 -4 -44 -18 -62 M-2 -30 C 8 -42 18 -52 22 -62" stroke="#8a6a52" stroke-width="5" stroke-linecap="round" fill="none"/>'),
                             ('F', P['mint'], '<path d="M-56 -66 C -58 -86 -20 -94 0 -92 C 24 -96 60 -86 56 -66 C 40 -56 -40 -56 -56 -66 Z"/>'),
                             ('F', P['mintL'], '<path d="M-40 -76 C -30 -84 -10 -86 4 -84 C -12 -80 -26 -78 -40 -76 Z"/>')])
def tuft(): return [('F', 'none', '<path d="M0 0 q-6 -14 -14 -18 M0 0 q-1 -18 3 -26 M0 0 q8 -12 16 -14" stroke="#7cc6a4" stroke-width="3.2" stroke-linecap="round" fill="none"/>')]
def hills(W, y):
    return [('F', P['hill1'], f'<path d="M0 {y-10} C {W*.2} {y-40} {W*.4} {y-36} {W*.55} {y-14} C {W*.7} {y-40} {W*.88} {y-38} {W} {y-16} V 999 H 0 Z"/>'),
            ('F', P['hill2'], f'<path d="M0 {y+14} C {W*.25} {y-6} {W*.5} {y+4} {W*.7} {y+10} C {W*.85} {y} {W*.95} {y+2} {W} {y+8} V 999 H 0 Z"/>')]
def cells_cluster():
    it = []
    for x, y, r in [(0, 0, 14), (30, 16, 10), (8, 34, 8)]:
        it += [('F', P['coral'], f'<circle cx="{x}" cy="{y}" r="{r}"/>'), ('F', P['coralL'], f'<ellipse cx="{x}" cy="{y}" rx="{r*.5:.1f}" ry="{r*.36:.1f}"/>')]
    return it
def sickle(): return [('F', P['coral'], '<path d="M-14 -10 C 12 -18 28 4 20 22 C 14 8 2 -4 -14 -10 Z"/>')]
def drop(s=1): return [('F', P['red'], f'<path transform="scale({s})" d="M0 -30 C 0 -30 -22 0 -22 16 A 22 22 0 0 0 22 16 C 22 0 0 -30 0 -30 Z"/>'), ('W', None, f'<path transform="scale({s})" d="M-12 14 q0 8 7 12 l2 -3 q-5 -3 -5 -9 Z" opacity=".8"/>')]

def city(W=420):
    it = [('F', P['wall1'], '<rect x="30" y="100" width="50" height="60" rx="4"/>'), ('F', P['wall2'], '<rect x="80" y="76" width="50" height="84" rx="4"/>'),
          ('F', P['wall3'], '<rect x="130" y="110" width="42" height="50" rx="4"/>')]
    it += [('F', '#c9d8ef', ''.join(f'<rect x="{x}" y="{y}" width="10" height="12" rx="2"/>' for x, y in [(40,112),(60,112),(40,134),(60,134),(90,88),(110,88),(90,110),(110,110),(90,132),(110,132),(140,122),(156,122)]))]
    it += [('F', P['wall2'], '<rect x="186" y="120" width="76" height="40" rx="4"/>'), ('F', P['dome'], '<path d="M194 120 C 194 82 254 82 254 120 Z"/>'),
           ('F', P['mustard'], '<path d="M220 72 a 7 7 0 1 0 9 -7 a 6 6 0 1 1 -9 7 z"/>'),
           ('F', '#c9d8ef', '<path d="M200 160 v -16 a 8 8 0 0 1 16 0 v 16 Z M232 160 v -16 a 8 8 0 0 1 16 0 v 16 Z"/>'),
           ('F', P['wall2'], '<rect x="270" y="66" width="16" height="94" rx="3"/>'), ('F', P['coral'], '<path d="M266 68 L 278 44 L 290 68 Z"/>'),
           ('F', P['wall1'], '<rect x="300" y="104" width="40" height="56" rx="4"/>'),
           ('F', 'none', '<path d="M372 160 C 368 130 376 112 372 94" stroke="#8a6a52" stroke-width="5" stroke-linecap="round" fill="none"/>'),
           ('F', P['mint'], '<path d="M372 94 c -16 -10 -34 -4 -40 6 c 14 -2 28 -4 40 -6 z M372 94 c 16 -10 34 -4 40 6 c -14 -2 -28 -4 -40 -6 z M372 94 c -8 -18 -26 -22 -34 -16 c 12 2 24 8 34 16 z M372 94 c 8 -18 26 -22 34 -16 c -12 2 -24 8 -34 16 z"/>'),
           ('F', P['sea'], f'<path d="M0 160 H {W} V 999 H 0 Z"/>'),
           ('F', 'none', '<path d="' + ''.join(f'M{x} 178 q 10 -6 20 0 ' for x in range(10, W, 46)) + '" stroke="#bcd6f7" stroke-width="3" stroke-linecap="round" fill="none"/>'),
           ('F', P['coral'], '<path d="M120 182 h46 l-8 12 h-30 Z"/>'), ('F', P['white'], '<path d="M144 160 L 162 178 H 144 Z"/>')]
    return it

# render
def _scale(tf):
    k = 1.0
    for m in re.findall(r'scale\(([0-9.]+)', tf): k *= float(m)
    return k
def flatten(items, out, tf=''):
    for e in items:
        if e[0] == 'G': flatten(e[2], out, (tf + ' ' + e[1]).strip())
        else: out.append((e[0], e[1], e[2], tf))
    return out
def render(items):
    out = []
    for kind, col, svg, tf in flatten(items, []):
        k = _scale(tf)
        if kind == 'F': a = f'fill="{col}"' if col != 'none' else ''
        elif kind == 'L': a = f'fill="none" stroke="{INK}" stroke-width="{2.6/k:.2f}" stroke-linecap="round" stroke-linejoin="round"'
        elif kind == 'T': a = f'fill="none" stroke="{INK}" stroke-width="{1.8/k:.2f}" stroke-linecap="round" stroke-linejoin="round"'
        elif kind == 'INK': a = f'fill="{INK}"'
        elif kind == 'W': a = 'fill="#fff"'
        el = svg.replace('/>', f' {a}/>') if a and 'fill="' not in svg.split('/>')[0] else svg
        if a and 'fill="' in svg.split('/>')[0] and kind != 'F': el = svg.replace('/>', f' {a}/>')
        out.append(f'<g transform="{tf}">{el}</g>' if tf else el)
    return ''.join(out)
def svg_doc(W, H, bg, items):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" preserveAspectRatio="xMidYMid slice">'
            f'<rect width="100%" height="100%" fill="{bg}"/>' + render(items) + '</svg>')
