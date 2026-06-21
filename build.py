#!/usr/bin/env python3
# personaltrainerinamstelveen.nl static site generator
import os, json, html, shutil, hashlib

def _ver(relpath):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),relpath),'rb').read()).hexdigest()[:8]
    except Exception: return "1"

BASE = "https://personaltrainerinamstelveen.nl"
SITE = "Personal Trainer in Amstelveen"
OUT = os.path.join(os.path.dirname(__file__), "site")
SRC = os.path.dirname(__file__)
EMAIL = "info@personaltrainerinamstelveen.nl"
CSS_VER = _ver("assets/css/style.css")

NAV = [
    ("Home", "/"),
    ("Soorten training", "/soorten-training/"),
    ("Keuzegids", "/beste-personal-trainer-kiezen/"),
    ("Contact", "/contact/"),
]

# ---- icons ----
IC = {
 "pin":'<svg viewBox="0 0 24 24" fill="none"><path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11Z" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="10" r="2.5" stroke="currentColor" stroke-width="1.8"/></svg>',
 "check":'<svg viewBox="0 0 24 24" fill="none"><path d="M5 12.5l4.5 4.5L19 7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "medal":'<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="9" r="6" stroke="currentColor" stroke-width="1.8"/><path d="M8.5 14l-1.5 7 5-3 5 3-1.5-7" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
 "target":'<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="3.5" stroke="currentColor" stroke-width="1.8"/></svg>',
 "chat":'<svg viewBox="0 0 24 24" fill="none"><path d="M4 5h16v11H8l-4 3V5Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.5" stroke="currentColor" stroke-width="1.8"/><path d="M12 7.5V12l3 2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 "dumbbell":'<svg viewBox="0 0 24 24" fill="none"><path d="M3 9v6M6 7v10M18 7v10M21 9v6M6 12h12" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>',
"play":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none"><circle cx="9" cy="8" r="3.2" stroke="currentColor" stroke-width="1.8"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0M16 5.5a3 3 0 0 1 0 5.8M16.5 19a5.5 5.5 0 0 0-2-3.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
}

def esc(s): return html.escape(s, quote=True)

ORG = {
 "@type":"Organization","@id":BASE+"/#org","name":SITE,"url":BASE+"/",
 "logo":{"@type":"ImageObject","url":BASE+"/assets/icons/logo-mark.png","width":512,"height":512},
 "email":EMAIL,
 "description":"Onafhankelijk overzicht van personal trainers in Amstelveen en omgeving.",
 "areaServed":{"@type":"City","name":"Amstelveen"},
}

# ---------------------------------------------------------------- providers
PROVIDERS = [
 {
  "slug":"yourhealth-personal-training",
  "name":"YourHealth Personal Training",
  "cc":"var(--c1)",
  "badge":"Grootste netwerk",
  "badge_ic":"users",
  "tagline":"Personal training aan huis en buiten, actief sinds 2007.",
  "url":"https://www.yourhealthpt.nl/personal-trainer-amstelveen/",
  "home":"https://www.yourhealthpt.nl/",
  "domain":"yourhealthpt.nl",
  "anchor":"YourHealth in Amstelveen",
  "phone":"06 21264241","tel":"+31621264241","email":"info@yourhealthpt.nl","banner":"training-battle-ropes.jpg",
  "usp":[
    "Een van de grootste platforms voor personal training aan huis in Nederland, met een team van meer dan honderd trainers.",
    "Ruime keuze aan specialisaties, van kracht en conditie tot boksen, herstel en medische training.",
    "Trainen op een vaste of wisselende locatie, thuis, op het werk of buiten in de buurt.",
    "Werkt met strippenkaarten, dus zonder abonnement, en een tweede persoon traint zonder meerkosten mee.",
  ],
  "for":"Wie veel keuze wil uit trainers en specialisaties en flexibel wil trainen zonder vast abonnement.",
  "lead":"YourHealth Personal Training bestaat sinds 2007 en groeide uit tot een van de grootste aanbieders van personal training aan huis in Nederland. Door het grote team is er ook in Amstelveen vrijwel altijd een trainer beschikbaar die past bij het doel en de agenda.",
  "sections":[
    ("Een breed en ervaren team","Het team bestaat uit meer dan honderd trainers met uiteenlopende specialisaties. Daardoor is een gerichte match mogelijk, of het doel nu afvallen, spieropbouw, conditie of herstel na een blessure is. Naast reguliere training zijn er onder meer medische trainers en bokstrainers."),
    ("Trainen waar het uitkomt","De training vindt plaats op de plek die het beste past: thuis, in de tuin, op het werk of buiten in een park of op een sportveld in de buurt. De trainer neemt de sportmaterialen mee. Locaties afwisselen kan ook, bijvoorbeeld binnen bij slecht weer en buiten als het droog is."),
    ("Flexibel met strippenkaarten","YourHealth werkt met strippenkaarten in plaats van een abonnement. Een groter pakket geeft een lager uurtarief. Een tweede persoon kan zonder meerkosten meetrainen, wat de kosten per persoon verlaagt. Voor ondernemers zijn de kosten mogelijk fiscaal aftrekbaar."),
  ],
 },
 {
  "slug":"lets-do-it-personal-training",
  "name":"LET'S DO IT Personal Training",
  "cc":"var(--c2)",
  "badge":"Voor vrouwen, door vrouwen",
  "badge_ic":"check",
  "tagline":"Personal training speciaal voor vrouwen, met vrouwelijke trainers.",
  "url":"https://www.letsdoitpt.nl/personal-trainer-amstelveen/",
  "home":"https://www.letsdoitpt.nl/",
  "domain":"letsdoitpt.nl",
  "anchor":"LET'S DO IT in Amstelveen",
  "phone":"06 21264241","tel":"+31621264241","email":"info@letsdoitpt.nl","banner":"training-veld-lunges.jpg",
  "usp":[
    "Personal training volledig gericht op vrouwen, met uitsluitend vrouwelijke trainers.",
    "Kennis van de invloed van de menstruatiecyclus, een zwangerschap en de overgang op een training.",
    "Begeleiding voor vrouwen na een bevalling en voor vrouwen boven de veertig.",
    "Trainen aan huis of buiten in de buurt, in een vertrouwde omgeving.",
  ],
  "for":"Vrouwen die het prettig vinden om met een vrouwelijke trainer te werken en aandacht willen voor de eigen levensfase.",
  "lead":"LET'S DO IT Personal Training richt zich volledig op vrouwen en werkt uitsluitend met vrouwelijke trainers. De aanpak is afgestemd op het vrouwenlichaam en op de verschillende levensfases, van zwangerschap tot de overgang. Ook in Amstelveen is een vrouwelijke trainer beschikbaar.",
  "sections":[
    ("Volledig gericht op vrouwen","Waar veel aanbieders zich op iedereen richten, traint LET'S DO IT alleen vrouwen, en alleen met vrouwelijke trainers. Veel vrouwen ervaren dat als prettiger en vertrouwder, zeker omdat de training vaak in de eigen omgeving plaatsvindt."),
    ("Aandacht voor de levensfase","De trainers houden rekening met factoren die specifiek bij vrouwen spelen. Een menstruatiecyclus kan invloed hebben op een training, net als een zwangerschap of een hormonale verandering tijdens de overgang. Er is begeleiding voor zwangere vrouwen, voor vrouwen na een bevalling en voor vrouwen boven de veertig."),
    ("Aan huis of buiten","De trainingen vinden plaats aan huis of buiten op een plek in de buurt. Er is geen langdurig abonnement nodig en een sportmaatje kan meetrainen. Zo blijft de drempel laag om te beginnen en vol te houden."),
  ],
 },
 {
  "slug":"jouw-personal-trainer-aan-huis",
  "name":"Jouw Personal Trainer aan Huis",
  "cc":"var(--c3)",
  "badge":"Sterk in 40-plus",
  "badge_ic":"medal",
  "tagline":"Personal training aan huis met aandacht voor fit blijven na het veertigste.",
  "url":"https://www.jouwpersonaltraineraanhuis.nl/personal-trainer-amstelveen/",
  "home":"https://www.jouwpersonaltraineraanhuis.nl/",
  "domain":"jouwpersonaltraineraanhuis.nl",
  "anchor":"Jouw Personal Trainer aan Huis in Amstelveen",
  "phone":"06 21264241","tel":"+31621264241","email":"info@jouwpersonaltraineraanhuis.nl","banner":"training-50plus.jpg",
  "usp":[
    "Veel ervaring met 40-plussers en 50-plussers die fit willen blijven.",
    "Aandacht voor kracht, balans en soepel bewegen, met een geleidelijke opbouw.",
    "Geschikt bij stijfheid, klachten of een herstart na een periode van weinig beweging.",
    "Trainen aan huis of buiten, zonder langdurig abonnement, met een partner die kosteloos meetraint.",
  ],
  "for":"Veertig- en vijftigplussers die geleidelijk willen opbouwen en willen werken aan kracht, balans en energie.",
  "lead":"Jouw Personal Trainer aan Huis past goed bij veertig- en vijftigplussers die merken dat fit blijven om een andere aanpak vraagt dan vroeger. Door een groot team is er ook in Amstelveen vaak een trainer beschikbaar die aansluit bij het doel, de conditie en de planning.",
  "sections":[
    ("Gericht op fit blijven na het veertigste","Vanaf het veertigste levensjaar veranderen kracht, herstel en mobiliteit geleidelijk. Gericht trainen helpt om spiermassa te behouden, klachten te verminderen en energiek te blijven tijdens werk, hobby en dagelijkse bezigheden. De begeleiding heeft hier nadrukkelijk aandacht voor."),
    ("Geleidelijke opbouw met aandacht voor techniek","De training richt zich op kracht, balans en soepel bewegen, met een opbouw die past bij het uitgangspunt. Dat maakt het geschikt bij stijfheid, bestaande klachten of een herstart na een periode van weinig beweging. De belastbaarheid en de techniek staan centraal."),
    ("Aan huis of buiten in Amstelveen","De trainingen vinden plaats thuis, in de tuin of buiten in een park in Amstelveen. Er is geen langdurig abonnement nodig en een partner kan kosteloos meetrainen. Daarnaast is er ruimte voor voedingsadvies en oefeningen voor tussen de trainingen door."),
  ],
 },
]
PROV_BY = {p["slug"]:p for p in PROVIDERS}

CRITERIA = [
 ("medal","Ervaring en expertise","Een goede personal trainer heeft jarenlange ervaring en een gedegen opleiding, kan de training afstemmen op de fysieke mogelijkheden en helpt blessures te voorkomen."),
 ("target","Maatwerk en persoonlijke aanpak","De beste trainers stellen een plan op dat past bij het doel, de wensen en de huidige conditie, zodat de uitdaging klopt zonder overbelasting."),
 ("chat","Communicatie en motivatie","Een goede trainer luistert, begrijpt het doel en motiveert ook buiten de training, bijvoorbeeld rond voeding en leefstijl."),
 ("clock","Flexibiliteit in locatie en tijd","Een trainer die past bij het schema en de leefstijl biedt de ruimte om thuis, buiten of op een andere plek te trainen, op momenten die uitkomen."),
]

STEPS = [
 ("Bepaal het doel","Helder hebben wat de training moet opleveren: afvallen, spieropbouw, een betere conditie of herstel na een blessure. Het doel bepaalt de aanpak."),
 ("Kies de juiste locatie","Thuis, in de tuin, op het werk of buiten in een park. De plek waar het sporten het prettigst voelt, helpt om vol te houden."),
 ("Bekijk de specialisaties","Kies een trainer met ervaring die past bij het doel, van krachttraining tot herstel na een blessure of begeleiding in een bepaalde levensfase."),
 ("Vraag een proefles aan","Een intake met proefles laat zien of er een klik is met de trainer, zonder meteen een langdurige verplichting aan te gaan."),
 ("Vergelijk tarieven en flexibiliteit","Let op het verschil tussen strippenkaart en abonnement, op de tarieven en op de beschikbaarheid door de week."),
]

MISTAKES = [
 ("Geen duidelijke doelen stellen","Maak vooraf duidelijk wat het doel is."),
 ("Onvoldoende communicatie","Zorg voor goede communicatie met de trainer."),
 ("Te snel te veel willen","Begin geleidelijk en bouw de intensiteit op."),
 ("Onrealistische verwachtingen","Wees realistisch over het doel en de tijdlijn."),
]

FAQ = [
 ("Waar moet een goede personal trainer aan voldoen?","Ervaring en een gedegen opleiding, een aanpak op maat, goede communicatie en motivatie, en flexibiliteit in locatie en tijd. Die combinatie maakt het verschil tussen een willekeurige trainer en een trainer die echt past."),
 ("Kan personal training ook aan huis of buiten?","Ja. De aanbevolen aanbieders trainen aan huis, op het werk of buiten in de buurt, zoals in een park of op een sportveld. De trainer neemt de benodigde materialen mee."),
 ("Is er een proefles mogelijk?","Bij de aanbevolen aanbieders is een intake met proefles gebruikelijk. Zo wordt vooraf duidelijk of er een klik is met de trainer en of de werkwijze past."),
 ("Wat kost een personal trainer in Amstelveen?","Tarieven verschillen per aanbieder en per pakket. Veel trainers werken met strippenkaarten, waarbij een groter pakket vaak een lager uurtarief geeft. Actuele tarieven staan op de site van de aanbieder."),
 ("Kan er samen met een partner of vriend worden getraind?","Bij de aanbevolen aanbieders kan een tweede persoon vaak zonder meerkosten meetrainen. Dat verlaagt de kosten per persoon en werkt voor veel mensen motiverend."),
 ("Kan er getraind worden met fysieke klachten of een blessure?","Ja. Trainers met ervaring in hersteltraining kunnen de training aanpassen. Het is belangrijk om klachten vooraf te melden, zodat de training daarop wordt afgestemd."),
]

# ---------------------------------------------------------------- helpers
def head(title, desc, path, jsonld=None, article=False):
    canonical = BASE + path
    blocks = ""
    if jsonld:
        if isinstance(jsonld, dict): jsonld=[jsonld]
        for o in jsonld:
            blocks += '<script type="application/ld+json">'+json.dumps(o,ensure_ascii=False)+'</script>\n'
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="L9e-TNNMkNa6xWaECQt9L1AyQr6Dazfpp-A8KYZbh18">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}/assets/img/og-default.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/icons/logo-mark.png" sizes="any">
<link rel="apple-touch-icon" href="/assets/icons/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Hanken+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{blocks}</head>
<body>
"""

def header(current):
    links=""
    for label,href in NAV:
        cur=' aria-current="page"' if href==current else ""
        links+=f'<li><a href="{href}"{cur}>{label}</a></li>'
    links+=f'<li><a class="nav-cta" href="/#trainers">Aanbevolen trainers</a></li>'
    return f"""<header class="site-header">
  <nav class="nav" aria-label="Hoofdmenu">
    <a class="brand" href="/"><img src="/assets/icons/logo-mark.png" alt="" width="38" height="38"><span>Personal Trainer<small>in Amstelveen</small></span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="menu" aria-label="Menu openen">
      <svg viewBox="0 0 24 24" fill="none"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
    <ul class="nav-links" id="menu">{links}</ul>
  </nav>
</header>
<main>
"""

def footer():
    prov_links="".join(f'<li><a href="/aanbieders/{p["slug"]}/">{esc(p["name"])}</a></li>' for p in PROVIDERS)
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="/"><img src="/assets/icons/logo-mark.png" alt="" width="38" height="38"><span>Personal Trainer<small>in Amstelveen</small></span></a>
        <p>Onafhankelijk overzicht dat helpt bij het vinden van een passende personal trainer in Amstelveen en omgeving.</p>
        <span class="footer-flag"><span class="flagchip sm"><img src="/assets/img/amstelveen-vlag.svg" alt="Vlag van Amstelveen"></span> Lokaal in Amstelveen</span>
      </div>
      <div>
        <h4>Aanbieders</h4>
        <ul>{prov_links}</ul>
      </div>
      <div>
        <h4>Info</h4>
        <ul>
          <li><a href="/soorten-training/">Soorten training</a></li>
          <li><a href="/beste-personal-trainer-kiezen/">Keuzegids</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/privacybeleid/">Privacybeleid</a></li>
          <li><a href="/cookiebeleid/">Cookiebeleid</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 {SITE}</span>
      <span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span>
    </div>
  </div>
</footer>
<script>
(function(){{var t=document.querySelector('.nav-toggle'),m=document.getElementById('menu');if(t&&m){{t.addEventListener('click',function(){{var o=m.classList.toggle('open');t.setAttribute('aria-expanded',o);}});}}
function loadVid(el){{var id=el.getAttribute('data-yt');if(!id||el.dataset.loaded)return;var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0';f.title=el.getAttribute('aria-label')||'YouTube-video';f.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';f.setAttribute('allowfullscreen','');f.loading='lazy';el.innerHTML='';el.appendChild(f);el.dataset.loaded='1';el.classList.add('playing');el.removeAttribute('role');el.removeAttribute('tabindex');}}
document.querySelectorAll('.video[data-yt]').forEach(function(el){{el.addEventListener('click',function(){{loadVid(el);}});el.addEventListener('keydown',function(e){{if(e.key==='Enter'||e.key===' '){{e.preventDefault();loadVid(el);}}}});}});}})();
</script>
</body>
</html>"""

def write(path, content):
    full = os.path.join(OUT,"index.html") if path=="/" else os.path.join(OUT,path.strip("/"),"index.html")
    os.makedirs(os.path.dirname(full),exist_ok=True)
    open(full,"w",encoding="utf-8").write(content)

def breadcrumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList",
            "itemListElement":[{"@type":"ListItem","position":i,"name":n,"item":BASE+p} for i,(n,p) in enumerate(items,1)]}

def crumbs_html(items):
    parts=[]
    for i,(n,p) in enumerate(items):
        parts.append(f'<a href="{p}">{n}</a>' if i<len(items)-1 else f'<span>{n}</span>')
    return '<nav class="crumbs wrap" aria-label="Kruimelpad">'+' / '.join(parts)+'</nav>'

def ext(url, anchor, cc=None):
    style=f' style="--cc:{cc}"' if cc else ""
    return f'<a href="{url}" target="_blank" rel="noopener"{style}>{anchor}</a>'

def video(vid, title, label=None):
    lab=f'<span class="vlabel">{esc(label)}</span>' if label else ''
    return f'''<div class="video" data-yt="{vid}" role="button" tabindex="0" aria-label="Video afspelen: {esc(title)}">
        <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">
        <span class="play"><span><svg width="30" height="30" viewBox="0 0 24 24" fill="#ffffff" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span></span>{lab}
      </div>'''

def faq_block(items):
    inner="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in items)
    return f'<div class="faq">{inner}</div>', {
        "@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}

def provider_card(p):
    usp="".join(f'<li>{IC["check"]}<span>{esc(u)}</span></li>' for u in p["usp"])
    return f"""<article class="provider" style="--cc:{p['cc']}">
  <div class="pinner">
    <div class="pmain">
      <span class="badge" style="--cc:{p['cc']}">{IC[p['badge_ic']]}{esc(p['badge'])}</span>
      <p class="logo-slot">{esc(p['name'])}</p>
      <p class="tagline">{esc(p['tagline'])}</p>
      <ul class="usp">{usp}</ul>
    </div>
    <div class="pside">
      <span class="for-who">Past goed bij</span>
      <p class="for-text">{esc(p['for'])}</p>
      <div class="links">
        <a class="btn btn-primary" style="background:{p['cc']};border-color:{p['cc']}" href="{p['url']}" target="_blank" rel="noopener">{esc(p['anchor'])} {IC['arrow']}</a>
        <a href="/aanbieders/{p['slug']}/">Meer over {esc(p['name'])}</a>
      </div>
    </div>
  </div>
</article>"""

# ---------------------------------------------------------------- pages
def home():
    path="/"
    crit="".join(f'<div class="crit"><div class="ic">{IC[ic]}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for ic,t,d in CRITERIA)
    cards="".join(provider_card(p) for p in PROVIDERS)
    steps="".join(f'<div class="step"><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></div>' for t,d in STEPS[:3])
    fhtml,fld = faq_block(FAQ[:4])
    itemlist={"@context":"https://schema.org","@type":"ItemList","name":"Aanbevolen personal trainers in Amstelveen",
              "itemListElement":[{"@type":"ListItem","position":i,"name":p["name"],"url":p["url"]} for i,p in enumerate(PROVIDERS,1)]}
    website={"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":SITE,"inLanguage":"nl-NL","publisher":{"@id":BASE+"/#org"}}
    org=dict(ORG); org["@context"]="https://schema.org"
    h=head(f"{SITE} | Vind een passende personal trainer",
           "Op zoek naar een personal trainer in Amstelveen? Lees waar een goede trainer aan voldoet en bekijk drie aanbevolen aanbieders voor training aan huis en buiten.",
           path,[website,org,itemlist,fld])
    h+=header("/")
    h+=f"""<section class="hero">
  <div class="hero-inner hero-grid">
    <div>
    <span class="eyebrow"><span class="flagchip"><img src="/assets/img/amstelveen-vlag.svg" alt="Vlag van Amstelveen"></span>Amstelveen en omgeving</span>
    <h1>De beste <em>personal trainer</em> in Amstelveen vinden</h1>
    <p class="lead">Een goede personal trainer maakt het verschil tussen afzien en volhouden. Dit overzicht legt uit waar een trainer aan moet voldoen en licht drie aanbevolen aanbieders uit, voor training aan huis en buiten.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#trainers">Bekijk de aanbevolen trainers {IC['arrow']}</a>
      <a class="btn btn-ghost" style="color:#fff;border-color:#3a4754" href="/beste-personal-trainer-kiezen/">Naar de keuzegids</a>
    </div>
    <div class="hero-meta">
      <span>{IC['check']}Training aan huis en buiten</span>
      <span>{IC['check']}Proefles mogelijk</span>
      <span>{IC['check']}Geen abonnement nodig</span>
    </div>
    </div>
    <div class="hero-media">
      <img src="/assets/img/foto/hero-training.jpg" alt="Personal training buiten in Amstelveen" width="960" height="1280">
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['medal']}Aandachtspunten</span>
      <h2>Waar een goede personal trainer aan voldoet</h2>
      <p>Het gaat niet alleen om ervaring en kennis, maar ook om hoe goed een trainer zich kan afstemmen op een persoonlijke situatie. Vier kenmerken komen steeds terug.</p>
    </div>
    <div class="criteria">{crit}</div>
  </div>
</section>

<section class="section sand" id="trainers">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['pin']}Aanbevolen in Amstelveen</span>
      <h2>Drie aanbevolen personal trainers</h2>
      <p>Drie aanbieders die personal training aan huis en buiten verzorgen in Amstelveen, elk met een eigen accent. De keuze hangt af van het doel en de voorkeur.</p>
    </div>
    <div class="providers">{cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow" style="justify-content:center">{IC['play']}Op video</span>
      <h2>Zo ziet personal training eruit</h2>
      <p>Een korte introductie over wat personal training inhoudt en hoe een traject verloopt.</p>
    </div>
    <div class="video-intro">
      {video('5zxbknolK-4','Introductie personal training')}
      <p class="video-note">De video laadt pas na een klik. Tot die tijd worden er geen YouTube-cookies geplaatst.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['target']}In het kort</span>
      <h2>De juiste trainer kiezen</h2>
      <p>Een korte aanpak om tot een goede keuze te komen. De volledige uitleg staat in de keuzegids.</p>
    </div>
    <div class="steps">{steps}</div>
    <p style="margin-top:24px"><a class="btn btn-ghost" href="/beste-personal-trainer-kiezen/">Lees de volledige keuzegids {IC['arrow']}</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow"><span class="flagchip"><img src="/assets/img/amstelveen-vlag.svg" alt="Vlag van Amstelveen"></span>In en om Amstelveen</span>
      <h2>Training in beeld</h2>
      <p>Personal training speelt zich af waar het past: in het park, langs het water, in de duinen of gewoon thuis in de tuin.</p>
    </div>
    <div class="gallery">
      <img src="/assets/img/foto/training-water-zonsondergang.jpg" alt="Personal training langs het water bij zonsondergang" loading="lazy">
      <img src="/assets/img/foto/training-veld-lunges.jpg" alt="Lunges tijdens een buitentraining" loading="lazy">
      <img src="/assets/img/foto/training-agility.jpg" alt="Loopladder tijdens training in het park" loading="lazy">
      <img src="/assets/img/foto/training-park-bankjes.jpg" alt="Oefeningen op een parkbankje" loading="lazy">
      <img src="/assets/img/foto/training-polder.jpg" alt="Rekoefening in een Hollands polderlandschap" loading="lazy">
      <img src="/assets/img/foto/training-kettlebell.jpg" alt="Kettlebell-oefening buiten" loading="lazy">
    </div>
  </div>
</section>

<section class="section sand">
  <div class="wrap narrow">
    <div class="section-head center">
      <span class="eyebrow" style="justify-content:center">{IC['chat']}Veelgestelde vragen</span>
      <h2>Veelgestelde vragen</h2>
    </div>
    {fhtml}
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="cta-band">
      <h2>Klaar om te beginnen in Amstelveen?</h2>
      <p>Bekijk de aanbevolen aanbieders, vergelijk de aanpak en vraag een proefles aan bij de trainer die het beste past.</p>
      <a class="btn btn-dark" href="#trainers">Naar de aanbevolen trainers {IC['arrow']}</a>
    </div>
  </div>
</section>"""
    h+=footer()
    write(path,h)

def guide():
    path="/beste-personal-trainer-kiezen/"
    crumbs=[("Home","/"),("Keuzegids",path)]
    crit="".join(f'<h3>{esc(t)}</h3><p>{esc(d)}</p>' for ic,t,d in CRITERIA)
    steps="".join(f'<div class="step"><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></div>' for t,d in STEPS)
    rows="".join(f'<tr><td>{esc(f)}</td><td>{esc(o)}</td></tr>' for f,o in MISTAKES)
    fhtml,fld=faq_block(FAQ)
    art={"@context":"https://schema.org","@type":"Article","mainEntityOfPage":{"@type":"WebPage","@id":BASE+path},
         "headline":"Beste personal trainer in Amstelveen kiezen","description":"Een gids over waar een goede personal trainer aan voldoet en hoe de keuze voor een trainer in Amstelveen tot stand komt.",
         "image":BASE+"/assets/img/og-default.png","datePublished":"2026-02-10T08:00:00+01:00","dateModified":"2026-06-01T08:00:00+02:00",
         "author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"},"inLanguage":"nl-NL"}
    h=head("Beste personal trainer in Amstelveen kiezen | "+SITE,
           "Waar moet een goede personal trainer aan voldoen en hoe komt de keuze tot stand? Een gids met criteria, stappen en veelgemaakte fouten.",
           path,[art,breadcrumb(crumbs),fld],article=True)
    h+=header("/beste-personal-trainer-kiezen/")
    h+=crumbs_html(crumbs)
    h+=f"""<article class="article">
  <div class="wrap narrow prose">
    <span class="eyebrow">{IC['medal']}Keuzegids</span>
    <h1>De beste personal trainer in Amstelveen kiezen</h1>
    <p class="lead">Personal training is een goede manier om gezondheid en fitheid een stap verder te brengen. In Amstelveen en omgeving zijn er meerdere aanbieders. Deze gids helpt bij het maken van een weloverwogen keuze.</p>
    <p>Of het doel nu afvallen, sterker worden, een betere conditie of herstel na een blessure is, een passende trainer vergroot de kans op resultaat en op plezier tijdens het sporten. De vraag is hoe de trainer te vinden die past bij de eigen situatie, wensen en doelen.</p>
    <h2>Waar een goede personal trainer aan voldoet</h2>
    <p>Een aantal factoren onderscheidt een goede personal trainer van de rest. Het gaat om de juiste mix van kennis, aanpak en flexibiliteit.</p>
    {crit}
    <h2>De trainer vinden die past</h2>
    <p>Het vinden van de juiste trainer begint met heldere eigen wensen en doelen. De volgende stappen helpen om tot een goede match te komen.</p>
    <div class="steps">{steps}</div>
    <h2>Veelgemaakte fouten</h2>
    <p>Bij het kiezen van een personal trainer komen een paar fouten vaak voor. Met deze aandachtspunten zijn ze te voorkomen.</p>
    <table class="tbl"><thead><tr><th>Fout</th><th>Oplossing</th></tr></thead><tbody>{rows}</tbody></table>
    <h2>Realistische verwachtingen</h2>
    <p>Resultaat hangt af van veel factoren, zoals het doel, de trainingsfrequentie, voeding, slaap en herstel. Een serieuze aanbieder belooft geen vaste resultaten binnen een vaste periode, maar werkt aan duurzame vooruitgang met begeleiding en training op maat. Dat is een gezond uitgangspunt om op te letten.</p>
    <h2>Veelgestelde vragen</h2>
    {fhtml}
    <div class="callout"><p><strong>Concreet aan de slag in Amstelveen?</strong> Bekijk de <a href="/#trainers">drie aanbevolen aanbieders</a> en vergelijk welke het beste past bij het doel en de voorkeur.</p></div>
  </div>
</article>"""
    h+=footer()
    write(path,h)

def provider_page(p):
    path=f"/aanbieders/{p['slug']}/"
    crumbs=[("Home","/"),("Aanbieders","/#trainers"),(p["name"],path)]
    usp="".join(f'<li>{IC["check"]}<span>{esc(u)}</span></li>' for u in p["usp"])
    secs="".join(f'<h2>{esc(t)}</h2><p>{esc(d)}</p>' for t,d in p["sections"])
    ld=[breadcrumb(crumbs),{
        "@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,
        "name":f"{p['name']} in Amstelveen","inLanguage":"nl-NL","isPartOf":{"@id":BASE+"/#website"}}]
    h=head(f"{p['name']} in Amstelveen | {SITE}",
           f"{p['name']}: {p['tagline']} Lees waar dit bedrijf sterk in is en wat het biedt voor personal training in Amstelveen.",
           path,ld)
    h+=header("/")
    h+=crumbs_html(crumbs)
    h+=f"""<article class="article">
  <div class="wrap narrow prose">
    <span class="eyebrow" style="color:{p['cc']}">{IC[p['badge_ic']]}{esc(p['badge'])}</span>
    <h1>{esc(p['name'])} in Amstelveen</h1>
    <p class="lead">{esc(p['lead'])}</p>
    <div class="prov-banner"><img src="/assets/img/foto/{p['banner']}" alt="Personal training in Amstelveen" loading="lazy"></div>
    <ul class="usp" style="--cc:{p['cc']};margin:24px 0 6px">{usp}</ul>
    {secs}
    <div class="callout" style="background:var(--paper-2);border-left:5px solid {p['cc']}">
      <p><strong>Past dit bij het doel?</strong> Bekijk het aanbod en de tarieven rechtstreeks bij {ext(p['url'], p['anchor'], p['cc'])}.</p>
      <p style="margin-bottom:0">Direct contact: <a href="tel:{p['tel']}">{p['phone']}</a> of <a href="mailto:{p['email']}">{p['email']}</a>.</p>
    </div>
    <p><a href="/#trainers">Terug naar alle aanbevolen trainers</a></p>
  </div>
</article>
<section class="section tight">
  <div class="wrap">
    <div class="cta-band" style="background:{p['cc']}">
      <h2>{esc(p['name'])} in Amstelveen</h2>
      <p>Vraag een intake met proefles aan en ervaar of de werkwijze en de trainer passen.</p>
      <a class="btn btn-dark" href="{p['url']}" target="_blank" rel="noopener">Naar {esc(p['domain'])} {IC['arrow']}</a>
    </div>
  </div>
</section>"""
    h+=footer()
    write(path,h)

def soorten_training():
    path="/soorten-training/"
    crumbs=[("Home","/"),("Soorten training",path)]
    TYPES=[
     ("dumbbell","Personal training aan huis","Een trainer komt met de materialen naar het adres. Trainen kan binnen of in de tuin, op een vast moment dat in de week past."),
     ("pin","Outdoor personal training","Buiten trainen op een plek in de buurt, zoals het Amsterdamse Bos, het Broersepark of het Jac. P. Thijssepark. Frisse lucht en wisselende oefeningen houden de training afwisselend."),
     ("users","Duo training","Samen trainen met een partner, vriend of collega. Bij de aanbevolen aanbieders traint een tweede persoon vaak zonder meerkosten mee."),
     ("dumbbell","Personal boxing","Een intensieve workout waarbij het hele lichaam in actie is. Goed voor kracht en conditie, en een prettige uitlaatklep na een werkdag. Er wordt met en niet tegen elkaar getraind."),
     ("medal","Medische en hersteltraining","Training bij of na een blessure, of ter voorbereiding op een operatie. De oefeningen worden afgestemd op de klachten. Ook training vanuit een rolstoel hoort tot de mogelijkheden."),
     ("target","Training rond de zwangerschap","Verantwoord bewegen tijdens en na de zwangerschap, afgestemd op de fase. Dit helpt klachten te beperken en ondersteunt het herstel na de bevalling."),
     ("clock","Training bij 40-plus en de overgang","Gericht werken aan kracht, balans en energie vanaf het veertigste, met aandacht voor de veranderingen rond de overgang."),
     ("chat","Personal coaching","Naast de fysieke training aandacht voor mindset en balans, voor het verminderen van stress en het stellen van grenzen."),
     ("users","Bedrijfsfitness","Met collega's buiten in groepsverband werken aan kracht en conditie, toegankelijk ongeacht niveau of leeftijd."),
    ]
    cards="".join(f'<div class="crit"><div class="ic">{IC[ic]}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for ic,t,d in TYPES)
    ld=[breadcrumb(crumbs),
        {"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Soorten personal training in Amstelveen","inLanguage":"nl-NL","isPartOf":{"@id":BASE+"/#website"}},
        {"@context":"https://schema.org","@type":"ItemList","name":"Soorten personal training","itemListElement":[{"@type":"ListItem","position":i,"name":t} for i,(ic,t,d) in enumerate(TYPES,1)]}]
    h=head("Soorten personal training in Amstelveen | "+SITE,
           "Van training aan huis en outdoor training tot duo, boksen, herstel, zwangerschap, 40-plus en coaching. Een overzicht van de soorten personal training in Amstelveen.",
           path,ld)
    h+=header("/soorten-training/")
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow"><span class="flagchip"><img src="/assets/img/amstelveen-vlag.svg" alt="Vlag van Amstelveen"></span>Soorten training</span>
      <h1>Soorten personal training</h1>
      <p>Personal training kent veel vormen. De aanbevolen aanbieders in Amstelveen bieden onder meer de onderstaande soorten, aan huis en buiten. Welke vorm past, hangt af van het doel, de conditie en de voorkeur.</p>
    </div>
    <div class="prov-banner"><img src="/assets/img/foto/training-duo-park.jpg" alt="Duo personal training in een park in Amstelveen" loading="lazy"></div>
    <div class="types">{cards}</div>
    <div class="callout" style="margin-top:36px">
      <p><strong>Niet zeker welke vorm past?</strong> De <a href="/beste-personal-trainer-kiezen/">keuzegids</a> helpt bij het kiezen, of neem rechtstreeks contact op via de <a href="/contact/">contactpagina</a>.</p>
    </div>
  </div>
</section>
<section class="section sand">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow" style="justify-content:center">{IC['play']}Workouts</span>
      <h2>Workouts om mee te doen</h2>
      <p>Twee voorbeeldworkouts geven een indruk van het soort oefeningen tijdens een training.</p>
    </div>
    <div class="video-grid">
      {video('XmJ0CBz_yx0','Workout om mee te doen')}
      {video('UF2TX53ifjc','Workout om mee te doen')}
    </div>
    <p class="video-note">De videos laden pas na een klik. Tot die tijd worden er geen YouTube-cookies geplaatst.</p>
  </div>
</section>
<section class="section tight">
  <div class="wrap">
    <div class="gallery">
      <img src="/assets/img/foto/training-herstel.jpg" alt="Hersteltraining met weerstandsband vanuit een rolstoel" loading="lazy">
      <img src="/assets/img/foto/training-aan-huis.jpg" alt="Personal training aan huis in de tuin" loading="lazy">
      <img src="/assets/img/foto/training-battle-ropes.jpg" alt="Training met battle ropes" loading="lazy">
    </div>
  </div>
</section>"""
    h+=footer()
    write(path,h)

def contact():
    path="/contact/"
    crumbs=[("Home","/"),("Contact",path)]
    icons={"phone":'<svg viewBox="0 0 24 24" fill="none"><path d="M6.5 4h3l1.5 4-2 1.5a11 11 0 0 0 5 5l1.5-2 4 1.5v3a2 2 0 0 1-2 2A15 15 0 0 1 4.5 6a2 2 0 0 1 2-2Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
           "mail":'<svg viewBox="0 0 24 24" fill="none"><rect x="3.5" y="5.5" width="17" height="13" rx="2" stroke="currentColor" stroke-width="1.8"/><path d="M4 7l8 6 8-6" stroke="currentColor" stroke-width="1.8"/></svg>'}
    cards=""
    for p in PROVIDERS:
        cards+=f"""<div class="ccard" style="--cc:{p['cc']}">
        <span class="tag">{esc(p['badge'])}</span>
        <h3>{esc(p['name'])}</h3>
        <a class="row" href="tel:{p['tel']}">{icons['phone']}{p['phone']}</a>
        <a class="row" href="mailto:{p['email']}">{icons['mail']}{p['email']}</a>
        <div class="ext"><a href="{p['url']}" target="_blank" rel="noopener">{esc(p['anchor'])} {IC['arrow']}</a></div>
      </div>"""
    ld=[breadcrumb(crumbs),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    h=head("Contact | "+SITE,"Een afspraak of vraag over personal training in Amstelveen? Neem rechtstreeks contact op met een van de drie aanbevolen aanbieders.",path,ld)
    h+=header("/contact/")
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow"><span class="flagchip"><img src="/assets/img/amstelveen-vlag.svg" alt="Vlag van Amstelveen"></span>Contact</span>
      <h1>Contact opnemen</h1>
      <p>Voor een afspraak, een proefles of een vraag over personal training is het het handigst om rechtstreeks contact op te nemen met een van de drie aanbevolen aanbieders. Hieronder staan de gegevens op een rij.</p>
    </div>
    <div class="contact-cards">{cards}</div>
  </div>
</section>"""
    h+=footer()
    write(path,h)

def privacy():
    path="/privacybeleid/"
    crumbs=[("Home","/"),("Privacybeleid",path)]
    h=head("Privacybeleid | "+SITE,"Hoe personaltrainerinamstelveen.nl omgaat met persoonsgegevens.",path,[breadcrumb(crumbs)])
    h+=header("/")
    h+=crumbs_html(crumbs)
    h+=f"""<section class="article">
  <div class="wrap narrow prose">
    <span class="eyebrow">{IC['check']}Privacy</span>
    <h1>Privacybeleid</h1>
    <p class="updated">Laatst bijgewerkt: 1 juni 2026</p>
    <p>Deze site hecht waarde aan de privacy van bezoekers. Dit beleid legt uit welke gegevens worden verwerkt en met welk doel, in lijn met de Algemene verordening gegevensbescherming (AVG).</p>
    <h2>Welke gegevens</h2>
    <p>De site verzamelt zelf geen persoonsgegevens via een formulier, want er staat geen contactformulier op de site. Bij contact per e-mail worden het e-mailadres en de inhoud van het bericht gedeeld.</p>
    <h2>Doel van de verwerking</h2>
    <p>Een e-mailadres en bericht worden alleen gebruikt om de vraag te beantwoorden of op een verzoek te reageren. Deze gegevens worden niet voor andere doeleinden gebruikt en niet aan derden verkocht.</p>
    <h2>Bewaartermijn</h2>
    <p>E-mailcorrespondentie wordt niet langer bewaard dan nodig is voor de afhandeling van de vraag of zolang dat wettelijk verplicht is.</p>
    <h2>Externe links</h2>
    <p>De site verwijst naar de websites van de aanbevolen aanbieders. Op die websites geldt het privacybeleid van de betreffende partij. Deze site is niet verantwoordelijk voor de gegevensverwerking op externe sites.</p>
    <h2>Rechten</h2>
    <p>Er bestaat recht op inzage, correctie of verwijdering van persoonsgegevens. Een verzoek daartoe kan per e-mail worden ingediend via <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    <h2>Cookies</h2>
    <p>Informatie over cookies staat in het <a href="/cookiebeleid/">cookiebeleid</a>.</p>
  </div>
</section>"""
    h+=footer()
    write(path,h)

def cookies():
    path="/cookiebeleid/"
    crumbs=[("Home","/"),("Cookiebeleid",path)]
    h=head("Cookiebeleid | "+SITE,"Hoe personaltrainerinamstelveen.nl omgaat met cookies.",path,[breadcrumb(crumbs)])
    h+=header("/")
    h+=crumbs_html(crumbs)
    h+=f"""<section class="article">
  <div class="wrap narrow prose">
    <span class="eyebrow">{IC['check']}Cookies</span>
    <h1>Cookiebeleid</h1>
    <p class="updated">Laatst bijgewerkt: 1 juni 2026</p>
    <p>Dit cookiebeleid legt uit hoe de site omgaat met cookies en vergelijkbare technieken.</p>
    <h2>Wat zijn cookies</h2>
    <p>Cookies zijn kleine bestanden die een website op een apparaat kan plaatsen, bijvoorbeeld om voorkeuren te onthouden of om bezoek te meten.</p>
    <h2>Welke cookies deze site gebruikt</h2>
    <p>Deze site is opgezet als eenvoudige informatieve website zonder trackingcookies en zonder advertentienetwerken. Er worden geen cookies geplaatst die bezoekers volgen voor advertentiedoeleinden.</p>
    <p>Wel kan het hostingplatform technische gegevens verwerken die nodig zijn om de site veilig en betrouwbaar te tonen. Dat gebeurt op basis van een gerechtvaardigd belang en zonder het volgen van individuele bezoekers.</p>
    <h2>Externe content</h2>
    <p>Voor de weergave van lettertypen maakt de site gebruik van een externe bron, waarbij een verzoek naar die dienst gaat om de lettertypen te laden. Bij het volgen van een link naar een externe website gelden de cookieregels van die website.</p>
    <h2>Video van YouTube</h2>
    <p>Op enkele pagina's staan videos van YouTube. Deze laden bewust pas na een klik op de afspeelknop. Tot dat moment wordt alleen een voorbeeldafbeelding van YouTube getoond en wordt er geen YouTube-cookie geplaatst. Na een klik laadt de video via youtube-nocookie.com, de privacyvriendelijke variant van YouTube. Vanaf dat moment kan YouTube cookies plaatsen voor de werking van de speler. Wie dat wil voorkomen, klikt de video niet aan.</p>
    <h2>Cookies beheren</h2>
    <p>Cookies zijn via de browserinstellingen te bekijken en te verwijderen. In de meeste browsers is het mogelijk om cookies te blokkeren of een melding te krijgen voordat een cookie wordt geplaatst.</p>
  </div>
</section>"""
    h+=footer()
    write(path,h)

def not_found():
    h=head("Pagina niet gevonden | "+SITE,"Deze pagina bestaat niet of is verplaatst.","/404",None)
    h+=header("/")
    h+=f"""<section class="section"><div class="wrap narrow" style="text-align:center;padding:40px 0">
    <span class="eyebrow" style="justify-content:center">404</span>
    <h1>Deze pagina is er niet</h1>
    <p>De opgevraagde pagina bestaat niet of is verplaatst.</p>
    <p style="margin-top:24px"><a class="btn btn-primary" href="/">Naar de homepage</a> <a class="btn btn-ghost" href="/beste-personal-trainer-kiezen/">Naar de keuzegids</a></p>
    </div></section>"""
    h+=footer()
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h)

def extras():
    urls=["/","/soorten-training/","/beste-personal-trainer-kiezen/","/contact/","/privacybeleid/","/cookiebeleid/"]
    urls+=[f"/aanbieders/{p['slug']}/" for p in PROVIDERS]
    body='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        pr="1.0" if u=="/" else "0.8"
        body+=f"  <url><loc>{BASE}{u}</loc><lastmod>2026-06-01</lastmod><priority>{pr}</priority></url>\n"
    body+="</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8").write(body)
    open(os.path.join(OUT,"robots.txt"),"w",encoding="utf-8").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w",encoding="utf-8").write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: geolocation=(), microphone=(), camera=()\n\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n")
    open(os.path.join(OUT,"_redirects"),"w",encoding="utf-8").write("https://www.personaltrainerinamstelveen.nl/* https://personaltrainerinamstelveen.nl/:splat 301!\n")

def copy_assets():
    dst=os.path.join(OUT,"assets")
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(os.path.join(SRC,"assets"),dst)

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT,exist_ok=True)
    copy_assets()
    home(); guide(); soorten_training()
    for p in PROVIDERS: provider_page(p)
    contact(); privacy(); cookies(); not_found(); extras()
    print("Build klaar in",OUT)

if __name__=="__main__":
    main()
