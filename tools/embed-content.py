#!/usr/bin/env python3
"""Кладёт content.json в index.html как встроенную запасную копию (<script id="content-default">).

Запускать после правки content.json, чтобы игра без файла или с битым файлом играла на свежем контенте:
    python3 tools/embed-content.py
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))   # битый JSON не попадёт в игру
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
tag = f'<script type="application/json" id="content-default">{blob}</script>'
html = (ROOT / 'index.html').read_text(encoding='utf-8')
pat = re.compile(r'<script type="application/json" id="content-default">.*?</script>', re.S)
if pat.search(html):
    html = pat.sub(lambda _: tag, html, count=1)
else:
    html = html.replace('<div id="app"></div>', tag + '\n<div id="app"></div>', 1)
(ROOT / 'index.html').write_text(html, encoding='utf-8')
print('ok: встроено', len(blob), 'байт')
