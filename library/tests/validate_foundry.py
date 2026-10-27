from pathlib import Path
from collections import Counter
from html.parser import HTMLParser
import json
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/"registry.json").read_text(encoding="utf-8"))["items"]
assert len(items)==44,len(items)
ids=[i["id"] for i in items]
assert len(ids)==len(set(ids))
new=[i for i in items if i.get("version")=="0.2.0"]
assert len(new)==27,len(new)
c=Counter(i["group"] for i in new)
assert all(c[g]==3 for g in ["headers","navigation","heroes","pricing","testimonials","portfolio","products","booking","landing-pages"]),c
class Check(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.label_targets=[];self.hrefs=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if "id" in d:self.ids.append(d["id"])
  if tag=="label" and "for" in d:self.label_targets.append(d["for"])
  if tag=="a" and "href" in d:self.hrefs.append(d["href"])
for item in items:
 assert item["status"]=="draft-demo" and item["verified"] is False,item["id"]
 assert item["html"].startswith("<"),item["id"]
 if item not in new:continue
 assert item["props"] and item["variant"] and item["contract"],item["id"]
 for prop in item["props"]:
  assert all(k in prop for k in ("name","type","default","description"))
 scan=Check();scan.feed(item["html"])
 assert len(scan.ids)==len(set(scan.ids)),item["id"]
 assert set(scan.label_targets).issubset(set(scan.ids)),item["id"]
 assert all(x.startswith(("#","./","mailto:")) for x in scan.hrefs),(item["id"],scan.hrefs)
WEB=ROOT.parents[1]/"website"/"library"
paths=["registry.json","styles/library.css","scripts/interactions.js"]+["templates/"+n+".html" for n in ("agency","portfolio","saas","local","commerce")]
for path in paths:
 dest="data/registry.json" if path=="registry.json" else path
 assert (ROOT/path).read_bytes()==(WEB/dest).read_bytes(),path
js=(ROOT/"scripts/interactions.js").read_text(encoding="utf-8")
assert "fetch(" not in js and "preventDefault()" in js
print("PASS: 44 unique canonical IDs")
print("PASS: 9 families × 3 variants = 27 new")
print("PASS: props, labels, hrefs, demo-only status")
print("PASS: source and website snapshots identical (8/8)")
