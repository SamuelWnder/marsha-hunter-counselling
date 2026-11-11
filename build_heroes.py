# Generates hero-options.html: 15 decorative treatments for the hero, on the real content.
LEAF = "M0 0 C -18 -18, -18 -48, 0 -66 C 18 -48, 18 -18, 0 0 Z"
SPRIG = ('<svg class="sprig %s" viewBox="0 0 150 250" fill="none" stroke="#6b8a6f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
         '<path d="M60 240 C 58 160, 68 85, 100 22"/>'
         + "".join('<path d="%s" transform="translate(%d %d) rotate(%d) scale(%s)"/>' % (LEAF, x, y, r, s) for x, y, r, s in
                   [(60, 200, -58, 1), (61, 172, 52, 1), (64, 135, -52, .95), (69, 100, 54, .9), (78, 66, -46, .8), (88, 42, 58, .7), (100, 22, 18, .7)])
         + '</svg>')
WAVE = ('<svg class="wave" viewBox="0 0 1200 100" preserveAspectRatio="none">'
        '<path d="M0 50 C 200 0, 400 100, 620 48 S 1000 10, 1200 46 V100 H0 Z" fill="#cfdccc"/>'
        '<path d="M0 74 C 220 30, 420 110, 660 66 S 1020 44, 1200 70 V100 H0 Z" fill="#ffffff"/></svg>')
V = [
 ("Clean and simple", "No decoration, just a soft shadow under the photo", ""),
 ("Yellow block", "Solid yellow block offset behind the photo", ""),
 ("Arch", "Photo in an arch shape with a fine green outline", ""),
 ("Circle", "Round photo with a thin ring and a yellow dot", ""),
 ("Soft blobs", "Organic green and yellow shapes behind the photo", ""),
 ("Dotted background", "Fine dot pattern across the right-hand side", ""),
 ("Diagonal split", "Deep green diagonal panel behind the photo", ""),
 ("Deep green", "Dark green hero with white text", ""),
 ("Waves", "Pale green hero with a wave along the bottom", WAVE),
 ("Ripples", "Concentric rings peeking out from behind the photo", ""),
 ("Fine stripes", "Diagonal pinstripe panels in green and yellow", ""),
 ("Botanical line art", "Outlined leaf sprigs in the corners", SPRIG % "s1" + SPRIG % "s2"),
 ("Sage panel", "Solid sage band down the right, photo overlapping it", ""),
 ("Soft glow", "Blurred yellow and green glows, no hard shapes", ""),
 ("Outline frame", "Fine dark green frame offset behind the photo, yellow corner", ""),
]
cards = ""
for i, (name, note, extra) in enumerate(V, 1):
    cards += f'''
<article class="opt">
  <header><span class="num">{i}</span><div><strong>{name}</strong><small>{note}</small></div></header>
  <div class="h v{i}">
    <span class="d a"></span><span class="d b"></span>{extra}
    <div class="h-text">
      <h2>A safe space<br>to feel <em>heard</em>.</h2>
      <p>I'm Marsha Hunter, a qualified and experienced counsellor. I offer a welcoming, non-judgemental space where you can work through challenging feelings and situations.</p>
      <div class="btns"><span class="btn p">Arrange an initial session</span><span class="btn g">Session fees</span></div>
      <ul><li>Registered with the BACP</li><li>Individuals and couples</li><li>Sessions via Zoom</li></ul>
    </div>
    <div class="h-art"><span class="d c"></span><span class="d e"></span><img src="theme/images/marsha-hunter.jpg" alt=""></div>
  </div>
</article>'''
html = '''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hero options — Marsha Hunter Counselling</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Inter:wght@400;500;600&display=swap">
<style>
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:#dfe5dc;color:#555a56;font:16px/1.6 "Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.page{max-width:1220px;margin:0 auto;padding:40px 20px 72px}
.intro h1{margin:0 0 6px;font:700 28px/1.2 "Plus Jakarta Sans",sans-serif;color:#24392f}
.intro p{margin:0;max-width:62ch}
.opt{margin-top:28px;border-radius:20px;overflow:hidden;border:1px solid #c9d1c6;background:#fff}
.opt header{display:flex;align-items:center;gap:14px;padding:14px 20px;border-bottom:1px solid #d9dbd6}
.num{flex:none;width:38px;height:38px;border-radius:50%;background:#35543f;color:#fff;font-weight:700;display:grid;place-items:center}
.opt header strong{display:block;color:#24392f;line-height:1.3}
.opt header small{display:block;font-size:13px}

/* shared hero */
.h{position:relative;isolation:isolate;overflow:hidden;background:#f5f5f1;display:grid;grid-template-columns:1.15fr .85fr;gap:48px;align-items:center;padding:60px 64px;min-height:460px}
.h-text{position:relative;z-index:2}
.h h2{margin:0;font:600 48px/1.14 "Plus Jakarta Sans",sans-serif;letter-spacing:-.02em;color:#24392f}
.h h2 em{font-style:normal;color:#35543f;background:linear-gradient(transparent 68%,#f5dc93 68%,#f5dc93 92%,transparent 92%)}
.h p{margin:18px 0 0;font-size:17px;max-width:32em}
.btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.btn{font-weight:600;font-size:15px;line-height:1.2;padding:13px 24px;border-radius:999px;color:#24392f}
.btn.p{background:#ecc45a}
.btn.g{box-shadow:inset 0 0 0 1.5px #6b8a6f}
.h ul{display:flex;flex-wrap:wrap;gap:8px 22px;list-style:none;padding:0;margin:26px 0 0;font-size:14px;font-weight:500;color:#2b2e2c}
.h li{display:flex;align-items:center;gap:8px}
.h li::before{content:"";width:8px;height:8px;border-radius:50%;background:#ecc45a}
.h-art{position:relative;z-index:1;width:100%;max-width:330px;margin:0 auto}
.h-art img{position:relative;z-index:1;display:block;width:100%;aspect-ratio:1;object-fit:cover;border-radius:24px}
.d{position:absolute;pointer-events:none;z-index:0}
.sprig,.wave{position:absolute;pointer-events:none;z-index:0}

.v1 img,.v6 img,.v12 img,.v13 img,.v14 img{box-shadow:0 24px 48px rgba(36,57,47,.18)}

.v2 img{box-shadow:16px 16px 0 #f5dc93}

.v3 .h-art{max-width:300px}
.v3 img{aspect-ratio:4/5;border-radius:999px 999px 24px 24px}
.v3 .c{inset:0;transform:translate(16px,16px);border:2px solid #6b8a6f;border-radius:999px 999px 24px 24px}

.v4 img{border-radius:50%}
.v4 .c{inset:-18px;border:2px solid #b9cbb6;border-radius:50%}
.v4 .e{z-index:2;width:58px;height:58px;right:6px;top:6px;border-radius:50%;background:#ecc45a}

.v5 .c{inset:-36px -42px -32px -38px;background:#cfdccc;border-radius:58% 42% 55% 45% / 48% 58% 42% 52%}
.v5 .e{z-index:2;width:96px;height:92px;left:-46px;bottom:-22px;background:#f5dc93;border-radius:60% 40% 52% 48% / 50% 56% 44% 50%}

.v6{background-image:radial-gradient(#b9cbb6 1.6px,transparent 2.1px);background-size:22px 22px}
.v6 .a{inset:0;background:linear-gradient(90deg,#f5f5f1 38%,rgba(245,245,241,0) 72%)}

.v7{background:linear-gradient(105deg,#f5f5f1 0 64%,#35543f 64% 100%)}
.v7 img{border:6px solid #fff;box-shadow:0 24px 48px rgba(0,0,0,.25)}

.v8{background:#24392f}
.v8 h2{color:#fff}
.v8 h2 em{color:#f5dc93;background:none}
.v8 p{color:#cfdccc}
.v8 .btn.g{color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.5)}
.v8 ul{color:#e9efe6}
.v8 .a{right:-140px;top:-150px;width:600px;height:600px;border-radius:50%;background:#2d4739}

.v9{background:#e9efe6;padding-bottom:120px}
.v9 .wave{left:0;bottom:0;width:100%;height:96px}
.v9 img{border:6px solid #fff;box-shadow:0 24px 48px rgba(36,57,47,.16)}

.v10 .c{width:280px;height:280px;right:-96px;top:-84px;border-radius:50%;background:repeating-radial-gradient(circle,transparent 0 16px,#b9cbb6 16px 18px)}
.v10 .e{width:170px;height:170px;left:-70px;bottom:-60px;border-radius:50%;background:repeating-radial-gradient(circle,transparent 0 12px,#ecc45a 12px 14px)}

.v11 .c{top:-28px;right:-36px;width:72%;height:72%;border-radius:16px;background:repeating-linear-gradient(135deg,#9fb59c 0 2px,transparent 2px 12px)}
.v11 .e{left:-32px;bottom:-28px;width:48%;height:48%;border-radius:16px;background:repeating-linear-gradient(135deg,#ecc45a 0 2px,transparent 2px 12px)}

.v12 .s1{right:14px;top:10px;width:150px;transform:rotate(14deg)}
.v12 .s2{left:57%;bottom:-70px;width:120px;transform:rotate(-24deg) scaleX(-1);stroke:#c9a53f}

.v13{background:linear-gradient(90deg,#f5f5f1 0 71%,#cfdccc 71% 100%)}
.v13 .c{right:-24px;bottom:-24px;width:112px;height:112px;background-image:radial-gradient(#35543f 2px,transparent 2.6px);background-size:16px 16px}

.v14{background:radial-gradient(420px 320px at 80% 26%,rgba(245,220,147,.75),transparent 70%),radial-gradient(540px 400px at 94% 90%,#cfdccc,transparent 70%),radial-gradient(420px 300px at 4% 100%,#e2eadf,transparent 70%),#f5f5f1}

.v15 .c{inset:0;transform:translate(-16px,-16px);border:2px solid #35543f;border-radius:24px}
.v15 .e{right:-18px;bottom:-18px;width:76px;height:76px;border-radius:18px;background:#ecc45a}

@media (max-width:820px){
  .h{grid-template-columns:1fr;padding:40px 24px;gap:44px}
  .h h2{font-size:36px}
  .v7{background:linear-gradient(170deg,#f5f5f1 0 62%,#35543f 62% 100%)}
  .v13{background:linear-gradient(180deg,#f5f5f1 0 66%,#cfdccc 66% 100%)}
  .v6 .a{background:linear-gradient(180deg,#f5f5f1 40%,rgba(245,245,241,0) 75%)}
}
</style>
</head>
<body>
<div class="page">
  <div class="intro">
    <h1>Hero options for Marsha Hunter Counselling</h1>
    <p>Fifteen ways to dress the top of the page, each shown with the real headline, photo and colours. Pick a number, or mix two (for example "3 with the background from 14").</p>
  </div>''' + cards + '''
</div>
</body>
</html>
'''
open("hero-options.html", "w").write(html)
