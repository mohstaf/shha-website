# Offset-print doodle illustrations. Entries: (kind, colour, svg)
# kind: F = fill only (offset colour layer), S = navy stroke, T = thin navy stroke,
#       FS = fill + full outline, INK = navy fill, W = white fill, R = red stroke
NAVY = '#0e2a4f'
C = dict(skin='#d9935f', skin2='#c98352', skin3='#e3a676', hair='#3b2a22', blue='#7fb3ec', red='#f08a7f',
         sand='#f2c879', green='#8cc7a0', navy='#9db3d3', white='#ffffff', cream='#fff7ea', blush='#f0998a', deep='#e0554a',
         blueD='#5d97dc', redD='#dd6a5d', sandD='#e2ad4f', greenD='#6fae86', navyD='#7f98c0', skinD='#bd7642', skin2D='#a86a3c', skin3D='#c98b5a', lip='#b4554a', iris='#5a3522')

def g(transform, items): return [('G', transform, items)]

def face(cx, cy, s=1, mood='smile', skin='skin'):
    k = lambda v: round(v * s, 2)
    it = []
    sd = C.get(skin + 'D', C['skinD'])
    # soft shading on one side of the face and under the brow
    it += [('F', sd, f'<path d="M{cx+k(18)} {cy-k(34)} C {cx+k(26)} {cy-k(18)} {cx+k(27)} {cy+k(8)} {cx+k(20)} {cy+k(22)} C {cx+k(14)} {cy+k(30)} {cx+k(8)} {cy+k(33)} {cx+k(2)} {cy+k(34)} C {cx+k(14)} {cy+k(24)} {cx+k(20)} {cy+k(4)} {cx+k(18)} {cy-k(34)} Z"/>')]
    it += [('F', C['blush'], f'<ellipse cx="{cx-k(16)}" cy="{cy+k(13)}" rx="{k(6.5)}" ry="{k(4.2)}"/>'),
           ('F', C['blush'], f'<ellipse cx="{cx+k(16)}" cy="{cy+k(13)}" rx="{k(6.5)}" ry="{k(4.2)}"/>')]
    # brows
    it += [('S', None, f'<path d="M{cx-k(18)} {cy-k(10)} q{k(7)} {-k(5)} {k(13)} {-k(1)} M{cx+k(5)} {cy-k(11)} q{k(6)} {-k(4)} {k(13)} {k(1)}"/>')]
    if mood == 'closed':
        it += [('S', None, f'<path d="M{cx-k(16)} {cy} q{k(5.5)} {k(4.5)} {k(11)} 0 M{cx+k(5)} {cy} q{k(5.5)} {k(4.5)} {k(11)} 0"/>'),
               ('T', None, f'<path d="M{cx-k(14)} {cy+k(3)} l{-k(1.5)} {k(2.5)} M{cx-k(10)} {cy+k(4)} v{k(2.6)} M{cx+k(8)} {cy+k(4)} v{k(2.6)} M{cx+k(13)} {cy+k(3)} l{k(1.5)} {k(2.5)}"/>')]
    else:
        for ex in (-10.5, 10.5):
            x = cx + k(ex)
            it += [('W', None, f'<path d="M{x-k(6.5)} {cy} C {x-k(4)} {cy-k(4.6)} {x+k(4)} {cy-k(4.6)} {x+k(6.5)} {cy} C {x+k(4)} {cy+k(3.6)} {x-k(4)} {cy+k(3.6)} {x-k(6.5)} {cy} Z"/>'),
                   ('IRIS', None, f'<circle cx="{x}" cy="{cy}" r="{k(3.4)}"/>'),
                   ('INK', None, f'<circle cx="{x}" cy="{cy}" r="{k(1.7)}"/>'),
                   ('W', None, f'<circle cx="{x+k(1.2)}" cy="{cy-k(1.3)}" r="{k(0.9)}"/>'),
                   ('S', None, f'<path d="M{x-k(7)} {cy+k(0.4)} C {x-k(4)} {cy-k(5)} {x+k(4)} {cy-k(5)} {x+k(7.4)} {cy-k(0.6)}"/>')]
    # nose
    it += [('T', None, f'<path d="M{cx+k(1)} {cy+k(2)} C {cx+k(3)} {cy+k(7)} {cx+k(4)} {cy+k(9)} {cx+k(2)} {cy+k(11)} M{cx-k(4)} {cy+k(11)} q{k(2)} {k(1.6)} {k(4)} 0 M{cx+k(3)} {cy+k(11)} q{k(2)} {k(1.6)} {k(4)} 0"/>')]
    # mouth
    if mood == 'big':
        it += [('FS', C['lip'], f'<path d="M{cx-k(10)} {cy+k(18)} C {cx-k(6)} {cy+k(28)} {cx+k(6)} {cy+k(28)} {cx+k(10)} {cy+k(18)} C {cx+k(4)} {cy+k(20)} {cx-k(4)} {cy+k(20)} {cx-k(10)} {cy+k(18)} Z"/>'),
               ('W', None, f'<path d="M{cx-k(7)} {cy+k(19.6)} C {cx-k(3)} {cy+k(21)} {cx+k(3)} {cy+k(21)} {cx+k(7)} {cy+k(19.6)} L {cx+k(6)} {cy+k(22)} C {cx+k(2)} {cy+k(23)} {cx-k(2)} {cy+k(23)} {cx-k(6)} {cy+k(22)} Z"/>')]
    else:
        it += [('F', C['lip'], f'<path d="M{cx-k(8)} {cy+k(18)} C {cx-k(3)} {cy+k(24)} {cx+k(3)} {cy+k(24)} {cx+k(8)} {cy+k(18)} C {cx+k(3)} {cy+k(20)} {cx-k(3)} {cy+k(20)} {cx-k(8)} {cy+k(18)} Z"/>'),
               ('S', None, f'<path d="M{cx-k(9)} {cy+k(17.5)} C {cx-k(4)} {cy+k(21)} {cx+k(4)} {cy+k(21)} {cx+k(9)} {cy+k(17.5)}"/>')]
    return it

def hijab_girl(hij='blue', dress='sand', pattern='dots', mood='smile', skin='skin', arm=None):
    """Girl in hijab, chest up, in 200x200 units, bottom at y=200."""
    it = []
    # dress
    it += [('F', C[dress], '<path d="M40 200 C 42 168 62 150 100 150 C 138 150 158 168 160 200 Z"/>'),
           ('S', None, '<path d="M40 200 C 42 176 52 162 66 155 M160 200 C 158 176 148 162 134 155"/>')]
    if pattern == 'dots':
        it += [('INK', None, ''.join(f'<circle cx="{x}" cy="{y}" r="1.9"/>' for x, y in [(62,178),(80,172),(98,180),(116,172),(134,178),(70,192),(90,190),(110,192),(130,190),(146,192),(54,192)]))]
    elif pattern == 'zigzag':
        it += [('T', None, '<path d="M52 180 l8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6"/>'),
               ('T', None, '<path d="M46 194 l8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6 8 -6 8 6"/>')]
    else:
        it += [('T', None, '<path d="M50 182 C 80 178 120 178 150 182 M45 194 C 80 190 120 190 155 194"/>')]
    if arm:
        it += arm
    it += [('F', C[dress+'D'] if dress+'D' in C else C['sandD'], '<path d="M126 152 C 144 158 156 172 160 200 L 136 200 C 136 180 132 164 126 152 Z"/>')]
    # hijab
    it += [('FS', C[hij], '<path d="M100 20 C 62 20 48 52 50 86 C 51 106 46 124 38 144 C 62 162 138 162 162 144 C 154 124 149 106 150 86 C 152 52 138 20 100 20 Z"/>'),
           ('F', C[hij+'D'], '<path d="M128 30 C 146 44 151 66 150 88 C 149 108 154 126 162 144 C 150 152 136 156 120 158 C 134 140 138 118 136 92 C 134 64 132 44 128 30 Z"/>'),
           ('T', None, '<path d="M56 112 C 62 128 72 140 86 150 M144 112 C 138 128 128 140 114 150 M100 138 C 99 146 99 152 100 158"/>'),
           ('T', None, '<path d="M64 58 C 70 40 84 32 100 31"/>')]
    # face opening band + face
    it += [('FS', C['cream'], '<path d="M100 43 C 77 43 70 63 71 88 C 72 112 86 126 100 126 C 114 126 128 112 129 88 C 130 63 123 43 100 43 Z"/>'),
           ('FS', C[skin], '<path d="M100 48 C 80 48 74 66 75 88 C 76 110 88 122 100 122 C 112 122 124 110 125 88 C 126 66 120 48 100 48 Z"/>')]
    it += face(100, 88, 1, mood)
    return it

def boy(shirt='blue', skin='skin2', mood='big'):
    it = []
    it += [('F', C[shirt], '<path d="M40 200 C 42 166 62 146 100 146 C 138 146 158 166 160 200 Z"/>'),
           ('S', None, '<path d="M40 200 C 42 166 62 146 100 146 C 138 146 158 166 160 200"/>'),
           ('T', None, '<path d="M50 176 C 80 171 120 171 150 176 M44 190 C 80 185 120 185 156 190"/>')]
    it += [('FS', C[skin], '<path d="M88 126 h24 v24 c -8 6 -16 6 -24 0 Z"/>'),
           ('S', None, '<path d="M82 148 q18 14 36 0"/>')]
    it += [('FS', C[skin], '<circle cx="62" cy="94" r="10"/>'), ('FS', C[skin], '<circle cx="138" cy="94" r="10"/>')]
    it += [('FS', C[skin], '<path d="M100 54 C 76 54 64 72 64 94 C 64 118 80 134 100 134 C 120 134 136 118 136 94 C 136 72 124 54 100 54 Z"/>')]
    it += [('FS', C['hair'], '<path d="M62 90 C 56 58 80 42 100 44 C 122 42 146 58 138 90 C 134 76 124 68 112 70 C 104 64 94 64 86 70 C 76 68 66 76 62 90 Z"/>'),
           ('W', None, ''.join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for x, y in [(78,58),(92,52),(108,52),(122,58),(84,64),(116,64),(100,58)]))]
    it += face(100, 96, 1, mood)
    return it

def flag_arm(dress):
    return [('FS', C[dress], '<path d="M140 156 C 152 146 160 128 162 108 L 176 110 C 176 134 166 158 152 172 Z"/>'),
            ('S', None, '<path d="M168 200 L 182 14"/>'),
            ('FS', C['blue'], '<path d="M182 16 C 204 8 220 26 244 18 L 238 76 C 214 84 200 66 178 74 Z"/>'),
            ('W', None, '<path d="M209 34 l4.6 10 11 1.2 -8.2 7.4 2.4 10.8 -9.8 -5.6 -9.8 5.6 2.4 -10.8 -8.2 -7.4 11 -1.2 z"/>'),
            ('T', None, '<path d="M209 34 l4.6 10 11 1.2 -8.2 7.4 2.4 10.8 -9.8 -5.6 -9.8 5.6 2.4 -10.8 -8.2 -7.4 11 -1.2 z"/>'),
            ('FS', C['skin'], '<ellipse cx="172" cy="104" rx="10" ry="9"/>'),
            ('T', None, '<path d="M166 100 q6 -2 12 0 M166 106 q6 -2 12 0"/>')]

def wave_arm(dress):
    return [('FS', C[dress], '<path d="M138 156 C 150 146 156 128 158 112 L 172 114 C 172 136 164 158 150 172 Z"/>'),
            ('FS', C['skin3'], '<path d="M160 112 C 154 104 156 90 160 84 C 162 80 166 82 166 86 L 167 96 L 170 82 C 172 78 176 80 176 84 L 174 98 L 180 88 C 182 84 186 86 185 90 L 176 112 C 172 118 164 118 160 112 Z"/>'),
            ('T', None, '<path d="M150 72 q-6 -6 -4 -14 M188 70 q6 -6 4 -14"/>')]

def mother():
    it = []
    # dress and shoulders
    it += [('F', C['red'], '<path d="M28 200 C 30 160 56 138 100 138 C 144 138 170 160 172 200 Z"/>'),
           ('F', C['redD'], '<path d="M138 146 C 158 156 168 174 172 200 L 148 200 C 148 178 144 160 138 146 Z"/>'),
           ('S', None, '<path d="M28 200 C 30 172 44 152 62 144 M172 200 C 170 172 156 152 138 144"/>')]
    # long hijab over shoulders
    it += [('FS', C['navy'], '<path d="M100 16 C 62 16 48 48 50 82 C 51 100 46 118 36 140 C 62 158 138 158 164 140 C 154 118 149 100 150 82 C 152 48 138 16 100 16 Z"/>'),
           ('F', C['navyD'], '<path d="M128 26 C 146 40 151 62 150 84 C 149 104 154 122 164 140 C 152 148 138 152 122 154 C 136 136 138 114 136 88 C 134 60 132 40 128 26 Z"/>'),
           ('T', None, '<path d="M64 54 C 70 36 84 28 100 27 M58 108 C 64 124 74 136 88 146 M142 108 C 136 124 126 136 112 146"/>'),
           ('FS', C['cream'], '<path d="M100 39 C 77 39 70 59 71 84 C 72 107 86 120 100 120 C 114 120 128 107 129 84 C 130 59 123 39 100 39 Z"/>'),
           ('FS', C['skin2'], '<path d="M100 44 C 80 44 74 62 75 84 C 76 104 88 116 100 116 C 112 116 124 104 125 84 C 126 62 120 44 100 44 Z"/>')]
    it += face(100, 82, 1, 'closed', 'skin2')
    # baby wrapped in a blanket, held across the chest
    it += [('FS', C['sand'], '<path d="M44 168 C 44 150 70 140 104 142 C 140 144 166 154 166 172 C 166 190 136 198 104 198 C 70 198 44 188 44 168 Z"/>'),
           ('F', C['sandD'], '<path d="M60 186 C 84 194 128 196 160 182 C 152 194 128 198 104 198 C 80 198 64 194 60 186 Z"/>'),
           ('INK', None, ''.join(f'<circle cx="{x}" cy="{y}" r="1.7"/>' for x, y in [(96,160),(114,156),(132,160),(148,166),(104,176),(122,172),(140,178),(112,188),(130,190),(90,186)])),
           ('T', None, '<path d="M84 150 C 92 166 92 182 84 196"/>')]
    it += [('FS', C['skin3'], '<circle cx="66" cy="160" r="20"/>'),
           ('F', C['skin3D'], '<path d="M76 144 C 86 152 88 166 80 176 C 76 170 78 156 76 144 Z"/>'),
           ('FS', C['hair'], '<path d="M47 156 C 46 140 58 136 66 138 C 76 138 86 146 85 156 C 80 148 72 146 66 148 C 58 146 50 150 47 156 Z"/>'),
           ('S', None, '<path d="M56 162 q3 3 6 0 M70 162 q3 3 6 0"/>'),
           ('T', None, '<path d="M62 171 q4 3 8 0 M66 165 v2"/>'),
           ('F', C['blush'], '<circle cx="55" cy="168" r="3.6"/><circle cx="78" cy="168" r="3.6"/>')]
    # mother's hands
    it += [('FS', C['skin2'], '<path d="M140 156 C 150 148 166 152 168 164 C 170 174 160 180 148 178 C 140 176 136 164 140 156 Z"/>'),
           ('T', None, '<path d="M150 154 q6 6 4 14 M157 154 q6 6 4 14"/>'),
           ('FS', C['skin2'], '<path d="M58 186 C 62 178 76 178 82 184 C 86 190 80 196 70 196 C 62 196 56 192 58 186 Z"/>'),
           ('F', C['deep'], '<path d="M100 120 c -3 -5 -11 -3 -8 3 l 8 8 l 8 -8 c 3 -6 -5 -8 -8 -3 z"/>')]
    return it

def doctor():
    it = []
    it += [('FS', C['white'], '<path d="M34 200 C 36 164 60 142 100 142 C 140 142 164 164 166 200 Z"/>'),
           ('FS', C['blue'], '<path d="M84 144 L 100 184 L 116 144 C 110 142 90 142 84 144 Z"/>'),
           ('S', None, '<path d="M84 144 L 100 184 L 116 144 M100 184 V 200"/>'),
           ('FS', C['white'], '<path d="M128 172 h22 v16 h-22 Z"/>'),
           ('S', None, '<path d="M134 172 v-10"/>'), ('FS', C['deep'], '<circle cx="134" cy="161" r="2.6"/>'),
           ('FS', C['sand'], '<path d="M56 160 h22 v10 h-22 Z"/>'),
           ('R', None, '<path d="M67 178 v12 M61 184 h12"/>')]
    it += [('FS', C['navy'], '<path d="M100 20 C 64 20 52 50 54 84 C 55 102 60 120 70 140 C 86 150 114 150 130 140 C 140 120 145 102 146 84 C 148 50 136 20 100 20 Z"/>'),
           ('T', None, '<path d="M66 58 C 72 40 86 32 100 31 M64 110 C 68 122 74 132 84 140 M136 110 C 132 122 126 132 116 140"/>'),
           ('FS', C['cream'], '<path d="M100 41 C 79 41 72 61 73 84 C 74 106 87 120 100 120 C 113 120 126 106 127 84 C 128 61 121 41 100 41 Z"/>'),
           ('FS', C['skin'], '<path d="M100 46 C 82 46 76 64 77 84 C 78 104 88 116 100 116 C 112 116 122 104 123 84 C 124 64 118 46 100 46 Z"/>')]
    it += face(100, 82, 0.95, 'smile')
    it += [('S', None, '<path d="M74 146 C 64 170 72 192 96 192 C 112 192 120 182 120 168"/>'),
           ('S', None, '<path d="M126 146 C 128 154 124 160 120 162"/>'),
           ('FS', C['sand'], '<circle cx="120" cy="168" r="7"/>'), ('T', None, '<circle cx="120" cy="168" r="3"/>')]
    return it

def man(shirt='green', skin='skin2'):
    it = [('F', C[shirt], '<path d="M44 200 C 46 166 66 148 100 148 C 134 148 154 166 156 200 Z"/>'),
          ('S', None, '<path d="M44 200 C 46 166 66 148 100 148 C 134 148 154 166 156 200"/>'),
          ('S', None, '<path d="M86 150 L 100 166 L 114 150 M100 166 V 200"/>'),
          ('INK', None, '<circle cx="100" cy="178" r="2"/><circle cx="100" cy="190" r="2"/>'),
          ('FS', C[skin], '<path d="M88 128 h24 v22 c -8 6 -16 6 -24 0 Z"/>'),
          ('FS', C[skin], '<circle cx="64" cy="92" r="9"/>'), ('FS', C[skin], '<circle cx="136" cy="92" r="9"/>'),
          ('FS', C[skin], '<path d="M100 50 C 78 50 66 68 66 92 C 66 118 82 136 100 136 C 118 136 134 118 134 92 C 134 68 122 50 100 50 Z"/>'),
          ('FS', C['hair'], '<path d="M66 84 C 64 56 82 46 100 46 C 120 46 138 56 134 84 C 128 70 116 64 100 66 C 86 64 72 70 66 84 Z"/>'),
          ('FS', C['hair'], '<path d="M74 112 C 80 134 120 134 126 112 C 120 124 112 128 100 128 C 88 128 80 124 74 112 Z"/>')]
    it += face(100, 94, 1, 'smile')
    return it

def extras_cells():
    return [('FS', C['red'], '<circle cx="0" cy="0" r="13"/>'), ('T', None, '<ellipse cx="0" cy="0" rx="6" ry="4.5"/>')]

def heart(s=1):
    return [('FS', C['deep'], f'<path transform="scale({s})" d="M0 -6 c -6 -10 -22 -6 -16 6 l 16 15 l 16 -15 c 6 -12 -10 -16 -16 -6 z"/>')]

def sparkle(s=1, col='sand'):
    return [('FS', C[col], f'<path transform="scale({s})" d="M0 -12 C 2 -3 3 -2 12 0 C 3 2 2 3 0 12 C -2 3 -3 2 -12 0 C -3 -2 -2 -3 0 -12 Z"/>')]

def sun(r=26):
    rays = ''.join(f'M{(r+8)*__import__("math").cos(a):.1f} {(r+8)*__import__("math").sin(a):.1f} L{(r+16)*__import__("math").cos(a):.1f} {(r+16)*__import__("math").sin(a):.1f} ' for a in [i*0.785 for i in range(8)])
    return [('FS', C['sand'], f'<circle cx="0" cy="0" r="{r}"/>'), ('T', None, f'<path d="{rays}"/>')]

def cloud(s=1):
    return [('FS', C['white'], f'<path transform="scale({s})" d="M0 0 C -2 -12 12 -18 20 -10 C 24 -24 46 -24 50 -8 C 60 -10 66 0 60 8 L 2 8 C -6 8 -8 2 0 0 Z"/>')]

def bird():
    return [('T', None, '<path d="M0 0 q6 -6 12 0 q6 -6 12 0"/>')]

def acacia(s=1):
    return g(f'scale({s})', [('S', None, '<path d="M0 0 C 2 -24 -4 -44 -18 -62 M-2 -30 C 8 -42 18 -52 22 -62 M-8 -46 C -2 -54 4 -58 8 -64"/>'),
           ('FS', C['green'], '<path d="M-56 -66 C -58 -84 -20 -92 0 -90 C 24 -94 60 -84 56 -66 C 40 -58 -40 -58 -56 -66 Z"/>'),
           ('T', None, '<path d="M-36 -74 q8 -4 16 0 M4 -78 q8 -4 16 0 M26 -70 q6 -3 12 0"/>')])

def tuft():
    return [('S', None, '<path d="M0 0 q-6 -14 -14 -18 M0 0 q-1 -18 3 -26 M0 0 q8 -12 16 -14"/>')]

def hills(W, y):
    return [('F', '#bfe0c9', f'<path d="M0 {y} C {W*.18} {y-26} {W*.36} {y-24} {W*.52} {y-6} C {W*.66} {y-30} {W*.86} {y-28} {W} {y-8} V 999 H 0 Z"/>')]

def cells_cluster():
    it = []
    for x, y, r in [(0, 0, 14), (30, 16, 10), (8, 34, 8)]:
        it += [('FS', C['red'], f'<circle cx="{x}" cy="{y}" r="{r}"/>'), ('T', None, f'<ellipse cx="{x}" cy="{y}" rx="{r*.45}" ry="{r*.32}"/>')]
    return it

def sickle():
    return [('FS', C['red'], '<path d="M-14 -10 C 12 -18 28 4 20 22 C 14 8 2 -4 -14 -10 Z"/>')]

def drop(s=1):
    return [('FS', C['deep'], f'<path transform="scale({s})" d="M0 -30 C 0 -30 -22 0 -22 16 A 22 22 0 0 0 22 16 C 22 0 0 -30 0 -30 Z"/>'), ('W', None, f'<path transform="scale({s})" d="M-12 14 q0 8 7 12 l2 -3 q-5 -3 -5 -9 Z"/>')]

def city(W=420):
    it = []
    it += [('FS', C['sand'], '<path d="M30 160 V 100 H 80 V 160 Z"/>'), ('FS', C['white'], '<path d="M80 160 V 76 H 130 V 160 Z"/>'),
           ('FS', C['blue'], '<path d="M130 160 V 110 H 172 V 160 Z"/>')]
    win = ''.join(f'M{x} {y} h10 v12 h-10 Z ' for x, y in [(40,112),(60,112),(40,134),(60,134),(90,88),(110,88),(90,110),(110,110),(90,132),(110,132),(140,122),(156,122)])
    it += [('T', None, f'<path d="{win}"/>')]
    it += [('FS', C['white'], '<path d="M186 160 V 120 H 262 V 160 Z"/>'),
           ('FS', C['blue'], '<path d="M194 120 C 194 82 254 82 254 120 Z"/>'),
           ('S', None, '<path d="M224 88 V 70"/>'), ('FS', C['sand'], '<path d="M220 64 a 7 7 0 1 0 9 -7 a 6 6 0 1 1 -9 7 z"/>'),
           ('T', None, '<path d="M200 160 v -16 a 8 8 0 0 1 16 0 v 16 M232 160 v -16 a 8 8 0 0 1 16 0 v 16"/>'),
           ('FS', C['white'], '<path d="M270 160 V 66 H 286 V 160 Z"/>'), ('FS', C['red'], '<path d="M266 66 L 278 44 L 290 66 Z"/>'),
           ('T', None, '<path d="M270 90 H 286 M270 114 H 286 M270 138 H 286"/>'),
           ('FS', C['white'], '<path d="M300 160 V 104 H 340 V 160 Z"/>'),
           ('T', None, '<path d="M306 160 v -14 a 7 7 0 0 1 14 0 v 14 M322 120 h10 v10 h-10 Z M308 116 h8 v12 h-8 Z"/>')]
    it += [('S', None, '<path d="M372 160 C 368 130 376 112 372 94"/>'),
           ('FS', C['green'], '<path d="M372 94 c -16 -10 -34 -4 -40 6 c 14 -2 28 -4 40 -6 z M372 94 c 16 -10 34 -4 40 6 c -14 -2 -28 -4 -40 -6 z M372 94 c -8 -18 -26 -22 -34 -16 c 12 2 24 8 34 16 z M372 94 c 8 -18 26 -22 34 -16 c -12 2 -24 8 -34 16 z"/>')]
    it += [('S', None, f'<path d="M0 160 H {W}"/>'), ('F', C['blue'], f'<path d="M0 160 H {W} V 999 H 0 Z"/>'),
           ('T', None, '<path d="' + ''.join(f'M{x} 178 q 10 -6 20 0 ' for x in range(10, W, 46)) + '"/>'),
           ('T', None, '<path d="' + ''.join(f'M{x+22} 196 q 10 -6 20 0 ' for x in range(10, W, 46)) + '"/>')]
    # boat
    it += [('FS', C['red'], '<path d="M120 182 h46 l-8 12 h-30 Z"/>'), ('S', None, '<path d="M142 182 V 160"/>'), ('FS', C['white'], '<path d="M144 162 L 160 178 H 144 Z"/>')]
    return it

def family():
    it = []
    it += g('translate(-6 18) scale(.84)', man('green'))
    it += g('translate(150 10) scale(.86)', hijab_girl('red', 'navy', 'dots', 'smile', 'skin'))
    it += g('translate(92 70) scale(.62)', boy('sand', 'skin3', 'big'))
    it += g('translate(214 74) scale(.6)', hijab_girl('blue', 'sand', 'zigzag', 'big', 'skin3'))
    return it  # width ~ 340

def hands_heart():
    it = []
    it += [('FS', C['skin2'], '<path d="M20 120 C 34 112 48 120 56 132 C 68 146 84 152 100 152 L 100 180 C 66 182 34 168 20 142 Z"/>'),
           ('FS', C['skin3'], '<path d="M180 120 C 166 112 152 120 144 132 C 132 146 116 152 100 152 L 100 180 C 134 182 166 168 180 142 Z"/>'),
           ('T', None, '<path d="M56 132 c 4 -12 16 -14 20 -4 M144 132 c -4 -12 -16 -14 -20 -4 M38 148 c 14 12 30 18 46 20 M162 148 c -14 12 -30 18 -46 20"/>'),
           ('FS', C['blue'], '<path d="M8 150 L 20 142 C 28 160 40 172 54 180 L 46 200 L 4 200 Z"/>'),
           ('FS', C['navy'], '<path d="M192 150 L 180 142 C 172 160 160 172 146 180 L 154 200 L 196 200 Z"/>')]
    it += g('translate(100 90) scale(2.3)', heart())
    return it

# ---------- render ----------
def flatten(items, out, tf=''):
    for e in items:
        if e[0] == 'G':
            flatten(e[2], out, (tf + ' ' + e[1]).strip())
        else:
            out.append((e[0], e[1], e[2], tf))
    return out

import re as _re
def _scale(tf):
    k = 1.0
    for m in _re.findall(r'scale\(([0-9.]+)', tf): k *= float(m)
    return k
def wrap(svg, tf, attrs):
    k = _scale(tf)
    attrs = _re.sub(r'stroke-width="([0-9.]+)"', lambda m: f'stroke-width="{float(m.group(1))/k:.2f}"', attrs)
    el = svg.replace('/>', f' {attrs}/>')
    return f'<g transform="{tf}">{el}</g>' if tf else el

def render_layers(items, off=(3, 2.5)):
    flat = flatten(items, [])
    fill = []; line = []
    for kind, col, svg, tf in flat:
        if not svg: continue
        if kind in ('F', 'FS') and col:
            fill.append(wrap(svg, tf, f'fill="{col}"'))
        if kind == 'FS':
            line.append(wrap(svg, tf, f'fill="none" stroke="{NAVY}" stroke-width="2.6"'))
        elif kind == 'S':
            line.append(wrap(svg, tf, f'fill="none" stroke="{NAVY}" stroke-width="2.6"'))
        elif kind == 'T':
            line.append(wrap(svg, tf, f'fill="none" stroke="{NAVY}" stroke-width="1.6"'))
        elif kind == 'R':
            line.append(wrap(svg, tf, 'fill="none" stroke="#c8291d" stroke-width="2.8"'))
        elif kind == 'INK':
            line.append(wrap(svg, tf, f'fill="{NAVY}"'))
        elif kind == 'W':
            line.append(wrap(svg, tf, 'fill="#fff"'))
        elif kind == 'IRIS':
            line.append(wrap(svg, tf, f'fill="{C["iris"]}"'))
    return (f'<g transform="translate({off[0]} {off[1]})" filter="url(#grain)">' + ''.join(fill) + '</g>'
            + '<g stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke">' + ''.join(line) + '</g>')

GRAIN = ('<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.3" numOctaves="1" seed="7" result="n"/>'
         '<feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  -1.1 0 0 0 1.42" result="m"/>'
         '<feComposite in="SourceGraphic" in2="m" operator="in"/></filter>')

def svg_doc(W, H, bg, items):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" preserveAspectRatio="xMidYMid slice"><defs>{GRAIN}</defs>'
            f'<rect width="100%" height="100%" fill="{bg}"/>' + render_layers(items) + '</svg>')
