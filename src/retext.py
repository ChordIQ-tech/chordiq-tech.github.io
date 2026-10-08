"""Helper used while editing: change a Portuguese text node in a section file and re-key its English translation."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from i18n import key, norm
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_PATH = os.path.join(ROOT, "src", "en.json")

def load(): return json.load(open(EN_PATH, encoding="utf-8"))
def save(d): json.dump(d, open(EN_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def put_en(pt, en):
    d = load(); d[key(pt)] = en; save(d)

def sec(name): return os.path.join(ROOT, "src", "sections", name + ".html")
