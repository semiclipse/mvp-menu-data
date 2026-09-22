"""Validate the public feed and immutable releases; Python 3.9+, no dependencies."""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
INGREDIENTS = {'Meat', 'Vegetables', 'Pasta', 'Seafood', 'Cheese', 'Sauce'}
def keys(obj, required):
    assert isinstance(obj, dict) and set(obj) == set(required.split()), 'Missing or unknown fields'
def number(n, lo, hi):
    assert type(n) is int and lo <= n <= hi, 'Number outside allowed range'
def text(s, maximum, empty=False):
    assert isinstance(s,str) and len(s.encode('utf-16-le'))//2 <= maximum and (empty or s.strip()), 'Invalid text'
    assert not any(ord(c)<32 and c!='\n' or 127<=ord(c)<160 for c in s), 'Control character'
def validate(m):
    keys(m, 'schemaVersion menuId revision version title notes recipes columnNames rowNames columnIngredients scoring')
    assert type(m['schemaVersion']) is int and m['schemaVersion']==1 and m['menuId']=='italian', 'Unsupported schema/menu'
    number(m['revision'],1,2147483647)
    text(m['version'],24); assert re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*',m['version'])
    text(m['title'],80);text(m['notes'],400,True)
    for name in ['columnNames','rowNames']:
        assert isinstance(m[name],list) and len(m[name])==3
        for s in m[name]:text(s,32)
    assert isinstance(m['columnIngredients'],list) and len(m['columnIngredients'])==3
    assert all(s in INGREDIENTS for s in m['columnIngredients'])
    r=m['scoring']; keys(r,'wastePenalty closingThreshold rowBonus columnBonus firstServiceBonus ruinedCountsForCollections allResolvedTriggersClosing')
    for k in ['wastePenalty','rowBonus','columnBonus','firstServiceBonus']:number(r[k],0,1000)
    number(r['closingThreshold'],1,20)
    for k in ['ruinedCountsForCollections','allResolvedTriggersClosing']:assert type(r[k]) is bool
    assert isinstance(m['recipes'],list) and len(m['recipes'])==9
    ids=set()
    for r in m['recipes']:
        keys(r,'id title description points costs');text(r['id'],64)
        assert re.fullmatch('[a-z0-9][a-z0-9_-]*',r['id']) and r['id'] not in ids
        ids.add(r['id']);text(r['title'],64);text(r['description'],400,True);number(r['points'],0,1000)
        assert isinstance(r['costs'],list) and 1<=len(r['costs'])<=6
        ingredients=set();total=0
        for c in r['costs']:
            keys(c,'ingredient amount');assert c['ingredient'] in INGREDIENTS and c['ingredient'] not in ingredients
            ingredients.add(c['ingredient']);number(c['amount'],1,12);total+=c['amount']
        assert total<=24,'Too many ingredient marks'
    return m

def read(path):
    data=path.read_bytes();assert len(data)<=131072,'Menu exceeds 128 KiB'
    def pairs(items):
        result={}
        for k,v in items:
            assert k not in result,'Duplicate JSON key: '+k
            result[k]=v
        return result
    return validate(json.loads(data, object_pairs_hook=pairs))
def main():
    latest=read(ROOT/'latest.json');revisions=[]
    for path in sorted((ROOT/'releases').glob('*.json')):
        release=read(path);rev=release['revision'];revisions.append(rev)
        assert path.name==f'italian-r{rev:06d}.json','Release filename mismatch'
    assert len(revisions)==len(set(revisions)) and latest['revision']==max(revisions),'Latest must be highest revision'
    assert latest==read(ROOT/'releases'/f"italian-r{latest['revision']:06d}.json"),'Latest/archive mismatch'
    # CI passes its previous commit or PR base: reject rewritten archives and rollback in place.
    if len(sys.argv)>1 and sys.argv[1] != '0'*40:
        base=sys.argv[1];assert re.fullmatch('[0-9a-f]{40}',base),'Expected commit SHA'
        paths=subprocess.check_output(['git','ls-tree','-r','--name-only',base],cwd=ROOT,text=True).splitlines()
        for p in paths:
            if p.startswith('releases/') and p.endswith('.json'):
                old=subprocess.check_output(['git','show',base+':'+p],cwd=ROOT)
                assert (ROOT/p).exists() and (ROOT/p).read_bytes()==old,'Published release rewritten: '+p
        if 'latest.json' in paths:
            previous=json.loads(subprocess.check_output(['git','show',base+':latest.json'],cwd=ROOT))
            assert latest['revision']>=previous['revision'],'Revision cannot decrease'
            if latest['revision']==previous['revision']:assert latest==previous,'Changed menu needs a new revision'
    print(f"PASS: {len(revisions)} release(s); latest {latest['version']} / revision {latest['revision']}")
if __name__=='__main__':main()
