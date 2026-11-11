# Generates fonts.html: 15 heading/body font pairings shown on the real page content.
# (heading family, heading spec, heading weight, has italic, body family, body spec, style, note)
P = [
 ("Playfair Display","ital,wght@0,500;0,600;1,500",500,1,"Source Sans 3","wght@400;600","Serif","Elegant and editorial, high contrast"),
 ("Lora","ital,wght@0,500;0,600;1,500",500,1,"Inter","wght@400;500;600","Serif","Warm, calm and very readable"),
 ("Libre Baskerville","ital,wght@0,400;0,700;1,400",400,1,"Open Sans","wght@400;600","Serif","Traditional and trustworthy"),
 ("DM Serif Display","ital@0;1",400,1,"DM Sans","wght@400;500;600","Serif","Bold and confident"),
 ("Merriweather","ital,wght@0,400;0,700;1,400",400,1,"Lato","wght@400;700","Serif","Sturdy and dependable"),
 ("EB Garamond","ital,wght@0,500;0,600;1,500",500,1,"Mulish","wght@400;600","Serif","Classic, bookish and refined"),
 ("Source Serif 4","ital,wght@0,500;0,600;1,500",600,1,"Source Sans 3","wght@400;600","Serif","Clean, modern serif"),
 ("Newsreader","ital,wght@0,500;0,600;1,500",500,1,"Inter","wght@400;500;600","Serif","Contemporary and thoughtful"),
 ("Marcellus","",400,0,"Karla","wght@400;600","Serif","Graceful, classical capitals"),
 ("Crimson Pro","ital,wght@0,500;0,600;1,500",500,1,"Work Sans","wght@400;600","Serif","Soft and approachable"),
 ("Montserrat","wght@500;600",600,0,"Open Sans","wght@400;600","Sans","Clean, modern and confident"),
 ("Poppins","wght@500;600",500,0,"Nunito Sans","wght@400;600","Sans","Friendly and rounded"),
 ("Raleway","wght@500;600",600,0,"Lato","wght@400;700","Sans","Light, airy and stylish"),
 ("Manrope","wght@400;500;600;700",600,0,"Manrope","","Sans","Crisp and contemporary"),
 ("Plus Jakarta Sans","wght@500;600;700",600,0,"Inter","wght@400;500;600","Sans","Smart and polished"),
]
fams = {}
for h, hs, hw, it, b, bs, st, note in P:
    fams.setdefault(h, hs)
    if bs: fams.setdefault(b, bs)
links = "\n".join(
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=%s%s&display=swap">'
    % (f.replace(" ", "+"), (":" + s) if s else "") for f, s in fams.items())
cards = ""
for i, (h, hs, hw, it, b, bs, st, note) in enumerate(P, 1):
    pair = h if h == b else "%s + %s" % (h, b)
    cards += f'''
<article class="opt" style="--h:'{h}';--b:'{b}';--hw:{hw};--it:{'italic' if it else 'normal'}">
  <header><span class="num">{i}</span><div><strong>{pair}</strong><small>{st} &middot; {note}</small></div></header>
  <div class="sample">
    <p class="brand">Marsha Hunter <span>Counselling</span></p>
    <h2>A safe space to feel <em>heard</em>.</h2>
    <p class="body">I'm Marsha Hunter, a qualified and experienced counsellor. I offer a welcoming, non-judgemental space where you can work through challenging feelings and situations.</p>
    <div class="row"><span class="btn">Arrange an initial session</span><span class="price"><b>£55</b> per session</span></div>
  </div>
</article>'''
html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Font options — Marsha Hunter Counselling</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{links}
<style>
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;background:#e9efe6;color:#555a56;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}}
.page{{max-width:1240px;margin:0 auto;padding:40px 20px 72px}}
.intro h1{{margin:0 0 6px;font-size:28px;line-height:1.2;color:#24392f}}
.intro p{{margin:0;max-width:60ch}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,440px),1fr));gap:20px;margin-top:28px}}
.opt{{background:#f5f5f1;border-radius:20px;overflow:hidden;border:1px solid #d9dbd6}}
.opt header{{display:flex;align-items:center;gap:14px;padding:14px 20px;background:#fff;border-bottom:1px solid #d9dbd6}}
.num{{flex:none;width:38px;height:38px;border-radius:50%;background:#35543f;color:#fff;font-weight:700;display:grid;place-items:center}}
.opt header strong{{display:block;color:#24392f;line-height:1.3}}
.opt header small{{display:block;font-size:13px}}
.sample{{padding:26px 26px 30px}}
.brand{{margin:0 0 22px;font-family:var(--h),serif;font-weight:var(--hw);font-size:21px;line-height:1.2;color:#24392f}}
.brand span{{display:block;margin-top:3px;font-family:var(--b),sans-serif;font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#6b8a6f}}
.sample h2{{margin:0;font-family:var(--h),serif;font-weight:var(--hw);font-size:40px;line-height:1.14;color:#24392f;text-wrap:balance}}
.sample h2 em{{font-style:var(--it);color:#35543f;background:linear-gradient(transparent 68%,#f5dc93 68%,#f5dc93 92%,transparent 92%)}}
.body{{margin:16px 0 0;font-family:var(--b),sans-serif;font-size:16.5px;line-height:1.65}}
.row{{display:flex;flex-wrap:wrap;align-items:center;gap:14px 24px;margin-top:22px}}
.btn{{font-family:var(--b),sans-serif;font-weight:600;font-size:15px;line-height:1.2;background:#ecc45a;color:#24392f;padding:13px 24px;border-radius:999px}}
.price{{font-family:var(--b),sans-serif;font-size:15px}}
.price b{{font-family:var(--h),serif;font-weight:var(--hw);font-size:34px;line-height:1;color:#24392f;margin-right:4px}}
</style>
</head>
<body>
<div class="page">
  <div class="intro">
    <h1>Font options for Marsha Hunter Counselling</h1>
    <p>Fifteen pairings, each shown on the real page content: the first font is for headings, the second for body text. Options 1–10 are serif headings, 11–15 are sans-serif. Pick a number.</p>
  </div>
  <div class="grid">{cards}
  </div>
</div>
</body>
</html>
'''
open("fonts.html", "w").write(html)
print("\n".join("https://fonts.googleapis.com/css2?family=%s%s&display=swap" % (f.replace(" ", "+"), (":" + s) if s else "") for f, s in fams.items()))
