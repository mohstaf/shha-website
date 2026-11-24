"""Regenerate the doodle illustrations in static/img/art/.

Run from the project folder:  python3 tools/art/generate.py
The drawings live in doodles.py (cute, flat style) and the scene layouts in scenes.py.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from scenes import make
OUT = os.path.join(HERE, "..", "..", "static", "img", "art")
JOBS = [('boy', 'lg', 'drops'), ('boy', 'pill', None), ('boy', 'wide', 'drops'), ('city', 'article', None), ('city', 'card', None), ('doctor', 'article', None), ('doctor', 'card', None), ('doctor', 'wide', 'cells'), ('doctor', 'wide', None), ('doctor', 'zig', None), ('family', 'card', None), ('family', 'wide', None), ('family', 'zig', None), ('girl-blue', 'card', 'cells'), ('girl-blue', 'pill', None), ('girl-blue', 'wide', 'cells'), ('girl-blue', 'wide', None), ('girl-flag', 'card', None), ('girl-flag', 'pill', None), ('girl-flag', 'tall', None), ('girl-flag', 'zig', None), ('girl-red', 'card', 'cells'), ('girl-red', 'pill', None), ('girl-red', 'wide', 'cells'), ('girl-sand', 'pill', None), ('hands', 'wide', None), ('hands', 'zig', None), ('mother', 'card', 'drops'), ('mother', 'p910', None), ('mother', 'pill', None), ('mother', 'wide', 'drops')]
for key, ratio, medical in JOBS:
    name = "-".join(x for x in (key, ratio, medical) if x) + ".svg"
    with open(os.path.join(OUT, name), "w") as f:
        f.write(make(key, ratio, medical))
# Dark versions: same drawings on deep, tinted backgrounds for the dark theme.
import doodles, scenes
LIGHT_P = dict(doodles.P); LIGHT_BG = dict(scenes.BG)
DARK_P = dict(hill1="#1d3a2e", hill2="#244736", cloud="#2a3a56", sea="#1f3c63", wave="#2f5486",
              wall1="#3a3326", wall2="#2a3a56", wall3="#26385a", window="#3c5175")
DARK_BG = {k: {"#eef4fb": "#16233a", "#fdf0ea": "#2a1d22", "#eef6f0": "#142821", "#fdf6e8": "#272219"}.get(v, "#16233a") for k, v in LIGHT_BG.items()}
doodles.P.update(DARK_P); scenes.BG.clear(); scenes.BG.update(DARK_BG)
for key, ratio, medical in JOBS:
    name = "-".join(x for x in (key, ratio, medical) if x) + "-dark.svg"
    with open(os.path.join(OUT, name), "w") as f:
        f.write(make(key, ratio, medical))
doodles.P.clear(); doodles.P.update(LIGHT_P); scenes.BG.clear(); scenes.BG.update(LIGHT_BG)
print(len(JOBS), "illustrations written to static/img/art/, each with a dark version")
