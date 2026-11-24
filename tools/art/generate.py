"""Regenerate the doodle illustrations in static/img/art/.

Run from the project folder:  python3 tools/art/generate.py
The drawings live in doodles.py and the scene layouts in scenes.py.
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
print(len(JOBS), "illustrations written to static/img/art/")
