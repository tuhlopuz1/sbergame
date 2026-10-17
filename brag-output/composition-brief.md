# Hyperframes Composition Brief: Лавка на один день

## Objective
Короткий промо-ролик игры «Лавка на один день», который открывает HTML-презентацию питча.

## Output
- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920x1080, 30fps
- Duration: 21s

## Source Material
- Project root: репозиторий sbergame
- Primary files read: `index.html` (вся игра), `docs/game.md`, `docs/task.md`
- Product name: Лавка на один день
- Tagline / strongest claim: «Открой лавку на ярмарке. Готовь заказы, считай сдачу и не попадись хитрецам!»
- Key UI to show: записанный геймплей (`work/clip-*.mp4`, 780×1688, реальная игра в Playwright) + SVG-персонажи, выгруженные из кода игры (`work/assets.json`)
- Copy that must appear verbatim:
  - «Скажи код из СМС — дадим 1000 алмазов» (реплика «Поддержки игры»)
  - «Закрашивай Лиса!»
  - «Лавка на один день»
  - «Ура!», «Обнимаю», «Я с тобой»
  - «Хозяин ярмарки»

## Creative Direction
- Tone preset: default
- Creative direction: яркая детская мобильная реклама в стиле СберKids
- Angle / Hook / Outro: см. `brag-plan.md`
- Avoid: общие фразы, абстрактные заливки, редизайн персонажей

## Visual Identity
- Background: #F2F3F7, небо #BFE8FF→#E8F7FF
- Text: #111216
- Accent: #C6F432; #FF5CE6, #2EC5FF, #FFDD2E, #FF7A1A
- Display font: Onest 800/900 (локальный @font-face), акцент Caveat 700
- References: Кляксик, клякса-splat, полосатый навес, флажки, телефон-чат, наклейки, медаль

## Storyboard
1. Hook — 3.7s — сообщение мошенника, клякса, «Закрашивай Лиса!»
2. Reveal — 2.6s — навес, название, три товара по биту
3. Финансы — 2.66s — запись «Дай сдачу»
4. Безопасность — 3.69s — запись «Лис в чате»
5. Мягкие навыки — 3.75s — запись «Друзья в чате», три наклейки
6. Outro — 4.6s — итоги дня, медаль, название

## Audio
- Music: `assets/music/happy-beats-business-moves-vol-11-by-ende-dot-app.mp3`, volume 0.55, fade-out в конце
- Cue locks: 3.70 reveal, 8.96 и 12.65 смены сцен, 17.91 медаль
- Audio-reactive: свечение/солнце за телефоном от баса (subtle)
- SFX: выбираются по готовой анимации из `<skill-dir>/assets/sfx/` (sfx-analysis.md), только low/medium HF risk

## Hyperframes Instructions
Composition built per hyperframes-core contract: один paused GSAP timeline на `window.__timelines["main"]`, `data-*` тайминги, видео — framework-owned `<video muted>` с собственными `data-start`, без вложенных таймированных обёрток. `npx hyperframes check` — единственный гейт перед рендером. Рендер локально.
