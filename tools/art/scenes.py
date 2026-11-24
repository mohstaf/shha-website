import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from doodles import *

CHAR = {
 'girl-blue': lambda: hijab_girl('blue', 'sand', 'dots', 'smile', 'skin'),
 'girl-red':  lambda: hijab_girl('red', 'blue', 'zigzag', 'big', 'skin3', arm=wave_arm('blue')),
 'girl-sand': lambda: hijab_girl('sand', 'red', 'stripes', 'big', 'skin2'),
 'girl-flag': lambda: hijab_girl('red', 'green', 'dots', 'big', 'skin', arm=flag_arm('green')),
 'boy':       lambda: boy('blue'),
 'mother':    mother,
 'doctor':    doctor,
}
BG = {'girl-blue':'#eef4fb', 'girl-red':'#fdf0ea', 'girl-sand':'#eef6f0', 'girl-flag':'#eef4fb', 'boy':'#fdf6e8',
      'mother':'#fdf0ea', 'doctor':'#eef4fb', 'family':'#fdf6e8', 'hands':'#fdf0ea', 'city':'#eef4fb'}
RATIO = {'pill': 520/250, 'tall': 5/6, 'p910': 9/10, 'zig': 5/4, 'card': 4/3, 'wide': 21/8, 'lg': 16/7.2, 'article': 16/9}

def at(x, y, items, s=1): return g(f'translate({x:.1f} {y:.1f})' + (f' scale({s:.3f})' if s != 1 else ''), items)

def sky(W, H, seed=0, ground=True, wide=False):
    it = []
    it += at(W*0.80 if wide else W*0.82, H*0.2, sun(22 if wide else 18))
    it += at(W*0.10, H*0.16, cloud(0.8))
    if wide:
        it += at(W*0.56, H*0.1, cloud(0.6))
        it += at(W*0.30, H*0.2, bird()) + at(W*0.35, H*0.13, bird(), .7) + at(W*0.66, H*0.24, bird(), .8)
    if ground:
        it += hills(W, H*0.74)
    if wide:
        it += at(W*0.11, H*0.82, acacia(0.95)) + at(W*0.92, H*0.8, acacia(0.7))
        it += at(W*0.24, H*0.9, tuft()) + at(W*0.78, H*0.94, tuft()) + at(W*0.03, H*0.97, tuft())
    return it

def scene(key, rname, medical=None):
    r = RATIO[rname]; H = 240.0; W = H * r
    it = []
    wide = r > 1.9
    if key == 'city':
        it += at(W*0.82, H*0.2, sun(20)) + at(W*0.12, H*0.18, cloud(.8)) + at(W*0.6, H*0.12, cloud(.55))
        it += at(W*0.3, H*0.22, bird()) + at(W*0.36, H*0.15, bird(), .7)
        s = H*0.9/200; it += at(W/2 - 210*s, H - 200*s, city(420), s)
        return W, H, BG[key], it
    if rname == 'pill':
        it += at(W*0.12, H*0.3, sparkle(1.1)) + at(W*0.9, H*0.72, sparkle(0.9, 'blush')) + at(W*0.86, H*0.24, heart(0.7))
        s = 1.85
        items = CHAR[key]() if key in CHAR else hands_heart()
        it += at(W/2 - 100*s, H*0.6 - 88*s, items, s)
        return W, H, BG.get(key, '#fdf6e8'), it
    it += sky(W, H, wide=wide)
    if medical == 'cells':
        it += at(W*(0.2 if wide else 0.12), H*0.46, cells_cluster(), .9) + at(W*(0.8 if wide else 0.88), H*0.52, sickle())
    elif medical == 'drops':
        it += at(W*(0.22 if wide else 0.13), H*0.5, drop(.8)) + at(W*(0.79 if wide else 0.88), H*0.56, cells_cluster(), .7)
    if key == 'family':
        fw = 340; s = min(H*0.84/200, W*0.86/fw)
        it += at(W/2 - fw/2*s, H - 200*s + 4, family(), s)
        it += at(W/2, H*0.12 + 0, heart(0.8))
    elif key == 'hands':
        s = min(H*0.92/200, W*0.9/200)
        it += at(W/2 - 100*s, H - 192*s, hands_heart(), s)
    else:
        extra = 48 if key == 'girl-flag' else 0
        s = min(H*0.94/200, W*0.96/(200+extra))
        it += at(W/2 - (100 + extra/2)*s, H - 200*s, CHAR[key](), s)
        it += at(W/2 - 92*s, H - 188*s, sparkle(0.8))
    return W, H, BG[key], it

def make(key, rname, medical=None):
    W, H, bg, it = scene(key, rname, medical)
    return svg_doc(W, H, bg, it)
