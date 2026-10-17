#!/usr/bin/env python3
"""Собирает pitch/index.html: подставляет настоящие SVG игры (из composition/assets/assets.json)."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent
A = json.load(open(ROOT / 'composition/assets/assets.json'))
ic = lambda n: f'<svg viewBox="0 0 24 24" aria-hidden="true">{A["IC"][n]}</svg>'
fonts = open(ROOT / 'composition/assets/fonts/fonts.css').read().replace('assets/fonts/', 'fonts/')
flags = ''.join(
    f'<path d="M{40 + i * 96} {28 + round(26 * (1 - ((i - 9.5) / 9.5) ** 2))}l40 0-20 50z" fill="{["#C6F432", "#FF5CE6", "#2EC5FF", "#FFDD2E", "#A77BFF"][i % 5]}"/>'
    for i in range(20))
medals = ''.join(f'<div data-a="pop" style="--d:{.2 + k * .08:.2f}" title="{t}">{m}</div>' for k, (m, t) in enumerate(zip(A['medals'], A['titles'])))
R = {
    'FONTS': fonts, 'FLAGS': flags, 'MEDALS': medals,
    'KLX': A['klx'], 'KLX_CAN': A['klxCan'], 'FOX': A['c_fox_sly'], 'RACCOON': A['c_raccoon_sly'],
    'FROG': A['c_frog_happy'], 'BUNNY': A['c_bunny_happy'],
    'LEMON': A['prod_lemon'], 'DONUT': A['prod_donut'], 'SLIME': A['prod_slime'],
    'PHONE_ART': A['phone'], 'MEDAL_SM': A['medals'][0],
    'ST_JOY': A['st_joy'], 'ST_SAD': A['st_sad'], 'ST_ANGRY': A['st_angry'],
    'AV_ROBOT': A['av_robot'], 'SPLAT': A['splat'],
    'IC_LEMONI': f'<svg viewBox="0 0 24 24">{A["IC"]["i_lemon"]}</svg>',
}
for n in ['coin', 'shield', 'heart', 'phone', 'clock', 'repeat', 'keypad', 'qr', 'coinsBack', 'hug', 'box', 'spark', 'user',
          'cashfly', 'magnifier', 'gift', 'link', 'zip', 'handshake', 'wallet', 'play', 'stop', 'crown', 'check', 'chat']:
    R['IC_' + n.upper()] = ic(n)
html = open(ROOT / 'pitch-template.html').read()
html = re.sub(r'\{\{(\w+)\}\}', lambda m: R[m.group(1)], html)
(ROOT.parent / 'pitch/index.html').write_text(html)
print('ok', len(html))
