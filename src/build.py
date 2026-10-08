#!/usr/bin/env python3
"""Builds the bilingual site (pt at /, en at /en/) into the repository root.

Run from the repository root:  python3 src/build.py
Sources: src/sections/*.html (Portuguese home sections), src/en.json (English text for them),
src/projects.py (portfolio content in both languages).
"""
import html
import json
import urllib.parse
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from i18n import translate  # noqa: E402
from newsections import ANALYTICS_OFF, ANALYTICS_ON, GITHUB, LINKEDIN, PRIVACY, T  # noqa: E402
from projects import BY_SLUG, CATEGORIES, CATEGORY_ORDER, HOME_HIGHLIGHTS, P  # noqa: E402

EN = json.load(open(os.path.join(ROOT, "src", "en.json"), encoding="utf-8"))
CFG = json.load(open(os.path.join(ROOT, "src", "site.json"), encoding="utf-8"))
E = html.escape
SITE = "https://chordiq-tech.github.io"

UI = {
    "pt": dict(
        lang="pt-BR", prefix="", other="en", other_label="EN", other_title="Read in English",
        title="ChordIQ — Physics AI para engenharia industrial",
        desc="Transformamos simulações e processos industriais em modelos de IA rápidos, físicos e verificáveis. CFD, gêmeos digitais, modelos substitutos e verificação, com casos reais e número medido.",
        nav=[("servicos", "Serviços"), ("portfolio", "Portfólio"), ("casos", "Validações"), ("capacidades", "Capacidades"),
             ("metodo", "Como trabalhamos"), ("sobre", "Sobre"), ("contato", "Contato")],
        cta="Falar com a gente", menu="Menu", hero_media_label="Ver o projeto Aircraft Design Optimizer", hero_media_cap="Aircraft Design Optimizer · CFD 3D (OpenFOAM) · pressão na pele", demo_btn="Pedir acesso à demo", demo_subject="Acesso à demo: ", demo_body="Olá! Gostaria de testar o ", demo_note="Os apps de demonstração têm acesso restrito.",
        show_eyebrow="Veja funcionando", show_h2="Um avião comercial projetado por IA e física, em 96 segundos.",
        show_p="O Aircraft Design Optimizer voa 1.920 projetos de avião de corredor único, descarta os que não seriam certificáveis e confere os escolhidos em CFD 3D. Calibrado primeiro no A320, depois otimizado: até −13% de CO₂ por passageiro-km, dentro do portão de 36 m do aeroporto.",
        show_btn="Ver o projeto completo", show_cap="Demonstração em vídeo do Aircraft Design Optimizer.",
        hl_eyebrow="Portfólio", hl_h2="O que já construímos, funcionando.",
        hl_p="Ferramentas de engenharia que combinam física e IA, do dimensionamento térmico ao projeto de uma aeronave. Cada projeto traz o vídeo de uso, os números medidos e, quando existe, o limite do que ele ainda não cobre.",
        hl_all="Ver todos os projetos", hl_more="projetos no portfólio",
        pf_h1="Portfólio", pf_lead="Treze projetos de engenharia com física e IA, organizados por tema. Abra um para ver o vídeo, o problema que ele resolve, os números medidos e os limites.",
        crumb_home="Início", crumb_pf="Portfólio",
        problem="O problema", how="Como funciona", results="Resultados medidos", limit="Limite declarado", gallery="Imagens",
        tags="Temas", next="Próximo projeto", all="Todos os projetos",
        cta_h="Quer algo assim para a sua operação?", cta_p="Conte o problema. A gente volta com um escopo fechado e uma métrica de sucesso, sem compromisso.", cta_b="Discutir um piloto",
        ex_summary="Ver a chamada real por trás de quatro das nossas entregas",
        video_label="Demonstração em vídeo: ",
        pf_title="Portfólio — ChordIQ", pf_desc="Projetos de engenharia com física e IA: térmica, dados industriais, simulação e malha, rastreabilidade e aeroespacial.",
        proj_suffix=" — ChordIQ",
    ),
    "en": dict(
        lang="en", prefix="/en", other="pt", other_label="PT", other_title="Ler em português",
        title="ChordIQ — Physics AI for industrial engineering",
        desc="We turn industrial simulations and processes into fast, physical and verifiable AI models. CFD, digital twins, surrogate models and verification, with real cases and measured numbers.",
        nav=[("servicos", "Services"), ("portfolio", "Portfolio"), ("casos", "Validations"), ("capacidades", "Capabilities"),
             ("metodo", "How we work"), ("sobre", "About"), ("contato", "Contact")],
        cta="Talk to us", menu="Menu", hero_media_label="See the Aircraft Design Optimizer project", hero_media_cap="Aircraft Design Optimizer · 3D CFD (OpenFOAM) · skin pressure", demo_btn="Request demo access", demo_subject="Demo access: ", demo_body="Hello! I would like to try ", demo_note="The demo apps have restricted access.",
        show_eyebrow="See it working", show_h2="An airliner designed by AI and physics, in 96 seconds.",
        show_p="The Aircraft Design Optimizer flies 1,920 single-aisle airliner designs, discards the ones that would not be certifiable and checks the picks in 3D CFD. Calibrated on the A320 first, then optimized: up to −13% CO₂ per passenger-km, inside the 36 m airport gate.",
        show_btn="See the full project", show_cap="Video demonstration of the Aircraft Design Optimizer.",
        hl_eyebrow="Portfolio", hl_h2="What we've built, working.",
        hl_p="Engineering tools that combine physics and AI, from thermal sizing to the design of an aircraft. Each project comes with a video of it in use, the measured numbers and, where one exists, the limit of what it does not cover yet.",
        hl_all="See all projects", hl_more="projects in the portfolio",
        pf_h1="Portfolio", pf_lead="Thirteen engineering projects with physics and AI, organized by theme. Open one to see the video, the problem it solves, the measured numbers and the limits.",
        crumb_home="Home", crumb_pf="Portfolio",
        problem="The problem", how="How it works", results="Measured results", limit="Stated limit", gallery="Images",
        tags="Topics", next="Next project", all="All projects",
        cta_h="Want something like this for your operation?", cta_p="Tell us the problem. We come back with a closed scope and a success metric, no commitment.", cta_b="Discuss a pilot",
        ex_summary="See the real call behind four of our deliverables",
        video_label="Video demonstration: ",
        pf_title="Portfolio — ChordIQ", pf_desc="Engineering projects with physics and AI: thermal, industrial data, simulation and mesh, traceability and aerospace.",
        proj_suffix=" — ChordIQ",
    ),
}

HOME_ORDER = ["hero", "SHOWCASE", "proof", "problema", "ENTRIES", "HIGHLIGHTS", "servicos", "casos",
              "principio", "validacao", "metodo", "PILOT", "ABOUT", "contato"]


def read(name):
    return open(os.path.join(ROOT, "src", "sections", name + ".html"), encoding="utf-8").read()


def absolutize(s):
    s = re.sub(r'(src|poster)="(img|videos)/', r'\1="/\2/', s)
    s = s.replace('href="styles.css"', 'href="/styles.css"').replace('src="script.js"', 'src="/script.js"')
    return s


PAGE_SLUGS = {"about": {"pt": "sobre", "en": "about"}, "capabilities": {"pt": "capacidades", "en": "capabilities"},
              "privacy": {"pt": "privacidade", "en": "privacy"}}


def path_for(lang, kind, slug=None):
    pre = UI[lang]["prefix"]
    if kind == "home":
        return pre + "/"
    if kind == "portfolio":
        return pre + "/portfolio/"
    if kind in PAGE_SLUGS:
        return f"{pre}/{PAGE_SLUGS[kind][lang]}/"
    return f"{pre}/portfolio/{slug}.html"


def jsonld(kind):
    if kind != "home":
        return ""
    data = {"@context": "https://schema.org", "@type": "Organization", "name": "ChordIQ", "url": SITE + "/",
            "logo": SITE + "/apple-touch-icon.png", "email": "yan@pinneapple.org",
            "sameAs": [LINKEDIN, GITHUB]}
    if CFG.get("legal_name"):
        data["legalName"] = CFG["legal_name"]
    return '\n  <script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def head(lang, title, desc, kind, slug=None):
    u = UI[lang]
    other = u["other"]
    here = SITE + path_for(lang, kind, slug)
    alt = SITE + path_for(other, kind, slug)
    pt_url = here if lang == "pt" else alt
    en_url = here if lang == "en" else alt
    return f'''<!doctype html>
<html lang="{u["lang"]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{E(title)}</title>
  <meta name="description" content="{E(desc)}">
  <link rel="canonical" href="{here}">
  <link rel="alternate" hreflang="pt-BR" href="{pt_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="x-default" href="{pt_url}">
  <meta property="og:title" content="{E(title)}">
  <meta property="og:description" content="{E(desc)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{here}">
  <meta property="og:image" content="{SITE}/img/og-{lang}.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="ChordIQ">
  <meta property="og:locale" content="{"pt_BR" if lang == "pt" else "en_US"}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{E(title)}">
  <meta name="twitter:description" content="{E(desc)}">
  <meta name="twitter:image" content="{SITE}/img/og-{lang}.jpg">
  <meta name="theme-color" content="#060910">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="48x48">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="preload" href="/fonts/k3kPo8UDI-1M0wlSV9XAw6lQkqWY8Q82sLydOxKsv4Rn.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/fonts.css">
  <link rel="stylesheet" href="/styles.css">{jsonld(kind)}
</head>
<body>
'''


def header(lang, kind, slug=None):
    u = UI[lang]
    home = u["prefix"] + "/"
    base = "" if kind == "home" else home
    nav = []
    for anchor, label in u["nav"]:
        if anchor == "portfolio" and kind != "home":
            href = path_for(lang, "portfolio")
        elif anchor == "capacidades":
            href = path_for(lang, "capabilities")
        elif anchor == "sobre":
            href = path_for(lang, "about")
        else:
            href = f"{base}#{anchor}"
        nav.append(f'      <a href="{href}">{label}</a>')
    sw = path_for(u["other"], kind, slug)
    return f'''<header>
  <div class="bar">
    <a class="brand" href="{home}#top">
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M4.5 3 V19.5 H21" stroke="var(--on-surface-dim)" stroke-width="1.5" stroke-linecap="round"/>
        <path d="M6 16.5 C 9.5 16, 10.5 8.5, 14 7 S 18.5 4.5, 19.5 4.5" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" fill="none"/>
        <circle cx="14" cy="7" r="2" fill="var(--signal-tok)"/>
      </svg>
      ChordIQ <span class="div">+</span> <span class="partner">Domus</span>
    </a>
    <button class="menu-btn" type="button" aria-label="{u["menu"]}" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span></button>
    <nav id="site-nav">
{chr(10).join(nav)}
    </nav>
    <a class="lang-switch" href="{sw}" hreflang="{u["other"]}" lang="{u["other"]}" title="{u["other_title"]}">{u["other_label"]}</a>
    <a class="btn btn-ghost" href="{base}#contato" style="font-size:.78rem;padding:.55rem 1.05rem">{u["cta"]}</a>
  </div>
</header>
'''


def analytics_tag():
    code = CFG.get("analytics_goatcounter", "").strip()
    return f'\n<script data-goatcounter="https://{code}.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>' if code else ""


def tail(lang="pt", kind="home"):
    u = UI[lang]
    base = "" if kind == "home" else u["prefix"] + "/"
    return f'''
<a class="mobile-cta" href="{base}#contato">{u["cta"]}</a>{analytics_tag()}
<script src="/script.js"></script>
</body>
</html>
'''


def footer(lang):
    s = read("footer")
    s = translate(s, EN) if lang == "en" else s
    t = T[lang]
    links = " &middot; ".join(f'<a href="{path_for(lang, k)}">{lbl}</a>' for k, lbl in zip(("privacy", "about", "capabilities"), t["legal"]))
    ent = (f'ChordIQ &middot; {E(CFG["legal_name"])} &middot; CNPJ {CFG["cnpj"]}' if CFG.get("legal_name") else "")
    if CFG.get("partner_legal_name"):
        ent += f' &nbsp;|&nbsp; Domus &middot; {E(CFG["partner_legal_name"])} &middot; CNPJ {CFG["partner_cnpj"]} &middot; Volta Redonda/RJ'
    ent_html = f'<div class="wrap legal-entity">{ent}</div>\n  ' if ent else ""
    return s.replace("</footer>", f'  {ent_html}<div class="wrap legal-links">{links}</div>\n</footer>')


def card(lang, p):
    u = UI[lang]
    d = p[lang]
    url = path_for(lang, "project", p["slug"])
    cat = CATEGORIES[p["cat"]][lang]
    tags = "".join(f'<span class="tag">{E(t)}</span>' for t in p["tags"][lang][:3])
    return f'''      <a class="pf-card" href="{url}">
        <div class="pf-thumb"><img loading="lazy" decoding="async" src="/img/portfolio/{p.get("thumb", p["image"])}" alt="{E(p["name"])}"><span class="pf-play" aria-hidden="true">&#9654;</span></div>
        <div class="pf-body">
          <span class="card-k">{E(cat)}</span>
          <h3>{E(p["name"])}</h3>
          <p>{E(d["tagline"])}</p>
          <div class="tag-row">{tags}</div>
        </div>
      </a>'''


def showcase(lang):
    u = UI[lang]
    p = BY_SLUG["aircraft-design-optimizer"]
    url = path_for(lang, "project", p["slug"])
    imgs = "".join(
        f'<a href="{url}"><img loading="lazy" decoding="async" src="/img/portfolio/{f}" alt="{E(cap)}"></a>'
        for f, cap in (("13-aircraft-render-pressure.jpg", p["gallery"][0][2 if lang == "pt" else 3]),
                       ("13-aircraft-render-streamlines.jpg", p["gallery"][1][2 if lang == "pt" else 3]),
                       ("13-aircraft-render-friction.jpg", p["gallery"][2][2 if lang == "pt" else 3])))
    return f'''<section id="vitrine" class="showcase">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{u["show_eyebrow"]}</p>
      <h2>{u["show_h2"]}</h2>
      <p>{u["show_p"]}</p>
    </div>
    <div class="show-video">
      <video controls preload="none" playsinline poster="/videos/app13.jpg" aria-label="{E(u["video_label"] + p["name"])}">
        <source src="/videos/app13.mp4" type="video/mp4">
      </video>
    </div>
    <div class="show-imgs">{imgs}</div>
    <p class="show-cta"><a class="btn btn-primary" href="{url}">{u["show_btn"]} &rarr;</a></p>
  </div>
</section>

'''


def highlights(lang):
    u = UI[lang]
    cards = "\n".join(card(lang, BY_SLUG[s]) for s in HOME_HIGHLIGHTS)
    rest = len(P) - len(HOME_HIGHLIGHTS)
    return f'''<section id="portfolio">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{u["hl_eyebrow"]}</p>
      <h2>{u["hl_h2"]}</h2>
      <p>{u["hl_p"]}</p>
    </div>
    <div class="pf-grid">
{cards}
    </div>
    <p class="show-cta"><a class="btn btn-ghost" href="{path_for(lang, "portfolio")}">{u["hl_all"]} (+{rest}) &rarr;</a></p>
  </div>
</section>

'''


def home(lang):
    u = UI[lang]
    out = [head(lang, u["title"], u["desc"], "home"), header(lang, "home")]
    for name in HOME_ORDER:
        if name == "SHOWCASE":
            out.append(showcase(lang))
        elif name == "HIGHLIGHTS":
            out.append(highlights(lang))
        elif name == "ENTRIES":
            out.append(entries(lang))
        elif name == "PILOT":
            out.append(pilot(lang))
        elif name == "ABOUT":
            out.append(about_teaser(lang))
        else:
            s = read(name)
            if name == "exemplos":
                s = s.replace('<div class="wrap">', f'<div class="wrap">\n    <details class="more"><summary>{u["ex_summary"]}</summary>', 1)
                s = s.replace("  </div>\n</section>", "    </details>\n  </div>\n</section>")
            if name == "hero":
                s = s.replace("<!--HEROMEDIA-->", hero_media(lang))
            if name == "contato":
                bk = CFG.get("booking_url", "").strip()
                btn = f'<p><a class="btn btn-ghost" href="{E(bk)}" target="_blank" rel="noopener">{"Agendar uma conversa" if lang == "pt" else "Book a call"} &rarr;</a></p>' if bk else ""
                s = s.replace("<!--BOOKING-->", btn)
            out.append(translate(s, EN) if lang == "en" else s)
            out.append("\n")
    out.append(footer(lang))
    out.append(tail(lang, "home"))
    return absolutize("".join(out))


def portfolio(lang):
    u = UI[lang]
    sections = []
    for c in CATEGORY_ORDER:
        items = [p for p in P if p["cat"] == c]
        if not items:
            continue
        sections.append(f'''    <h2 class="pf-cat">{E(CATEGORIES[c][lang])}</h2>
    <div class="pf-grid">
{chr(10).join(card(lang, p) for p in items)}
    </div>''')
    home_url = u["prefix"] + "/"
    body = f'''<main class="page">
  <div class="wrap">
    <p class="crumbs"><a href="{home_url}">{u["crumb_home"]}</a> / {u["crumb_pf"]}</p>
    <div class="section-head">
      <p class="eyebrow">{u["hl_eyebrow"]}</p>
      <h1>{u["pf_h1"]}</h1>
      <p class="lead">{u["pf_lead"]}</p>
    </div>
{chr(10).join(sections)}
  </div>
</main>
'''
    return absolutize(head(lang, u["pf_title"], u["pf_desc"], "portfolio") + header(lang, "portfolio") + body + contact_cta(lang) + footer(lang) + tail(lang, "portfolio"))


def book_btn(lang):
    bk = CFG.get("booking_url", "").strip()
    if not bk:
        return ""
    return f' <a class="btn btn-ghost" href="{E(bk)}" target="_blank" rel="noopener">{"Agendar uma conversa" if lang == "pt" else "Book a call"} &rarr;</a>'


def contact_cta(lang):
    u = UI[lang]
    return f'''<section class="cta-band">
  <div class="wrap">
    <h2>{u["cta_h"]}</h2>
    <p>{u["cta_p"]}</p>
    <p><a class="btn btn-primary" href="{u["prefix"]}/#contato">{u["cta_b"]} &rarr;</a>{book_btn(lang)}</p>
  </div>
</section>
'''


def demo_href(lang, p):
    u = UI[lang]
    return "mailto:yan@pinneapple.org?subject=" + urllib.parse.quote(u["demo_subject"] + p["name"]) + "&body=" + urllib.parse.quote(u["demo_body"] + p["name"] + ".")


def project(lang, p):
    u = UI[lang]
    d = p[lang]
    home_url = u["prefix"] + "/"
    cat = CATEGORIES[p["cat"]][lang]
    idx = P.index(p)
    nxt = P[(idx + 1) % len(P)]
    res = "\n".join(f"          <li>{E(r)}</li>" for r in d["results"])
    limit = f'\n      <div class="callout"><b>{u["limit"]}.</b> {E(d["limit"])}</div>' if d.get("limit") else ""
    tags = "".join(f'<span class="tag">{E(t)}</span>' for t in p["tags"][lang])
    gal = [(p["image"], p["name"], p["name"])] + [(g[0], g[2], g[3]) for g in p["gallery"]]
    gal_html = "\n".join(
        f'      <figure><img loading="lazy" decoding="async" src="/img/portfolio/{f}" alt="{E(cp_pt if lang == "pt" else cp_en)}">'
        + (f'<figcaption>{E(cp_pt if lang == "pt" else cp_en)}</figcaption>' if i else "") + "</figure>"
        for i, (f, cp_pt, cp_en) in enumerate(gal))
    body = f'''<main class="page project">
  <div class="wrap">
    <p class="crumbs"><a href="{home_url}">{u["crumb_home"]}</a> / <a href="{path_for(lang, "portfolio")}">{u["crumb_pf"]}</a> / {E(p["name"])}</p>
    <p class="eyebrow">{E(cat)}</p>
    <h1>{E(p["name"])}</h1>
    <p class="lead">{E(d["tagline"])}</p>
    <div class="show-video">
      <video controls preload="metadata" playsinline poster="/videos/app{p["n"]}.jpg" aria-label="{E(u["video_label"] + p["name"])}">
        <source src="/videos/app{p["n"]}.mp4" type="video/mp4">
      </video>
    </div>
    <div class="proj-grid">
      <div class="proj-text">
        <h2>{u["problem"]}</h2>
        <p>{E(d["problem"])}</p>
        <h2>{u["how"]}</h2>
        <p>{E(d["how"])}</p>
      </div>
      <aside class="proj-side">
        <h2>{u["results"]}</h2>
        <ul class="app-list">
{res}
        </ul>{limit}
        <p class="side-k">{u["tags"]}</p>
        <div class="tag-row">{tags}</div>
        <p class="demo-ask"><a class="btn btn-primary" href="{demo_href(lang, p)}">{u["demo_btn"]} &rarr;</a><span>{u["demo_note"]}</span></p>
      </aside>
    </div>
    <h2 class="gal-h">{u["gallery"]}</h2>
    <div class="gallery">
{gal_html}
    </div>
    <p class="proj-nav"><a href="{path_for(lang, "portfolio")}">&larr; {u["all"]}</a>
      <a href="{path_for(lang, "project", nxt["slug"])}">{u["next"]}: {E(nxt["name"])} &rarr;</a></p>
  </div>
</main>
'''
    title = p["name"] + " — " + d["tagline"].rstrip(".")
    return absolutize(head(lang, title + u["proj_suffix"], d["tagline"], "project", p["slug"]) + header(lang, "project", p["slug"]) + body + contact_cta(lang) + footer(lang) + tail(lang, "project"))


def hero_media(lang):
    u = UI[lang]
    p = BY_SLUG["aircraft-design-optimizer"]
    return f'''<a class="hero-media" href="{path_for(lang, "project", p["slug"])}">
      <video autoplay muted loop playsinline preload="auto" poster="/videos/hero-aero.jpg" aria-hidden="true">
        <source src="/videos/hero-aero.mp4" type="video/mp4">
      </video>
      <span class="hero-media-cap">{E(u["hero_media_cap"])}</span>
    </a>'''


def entries(lang):
    t = T[lang]
    cards = []
    for q, slug, hint in t["entries"]:
        cards.append(f'''      <a class="entry" href="{path_for(lang, "project", slug)}">
        <span class="entry-q">{E(q)}</span>
        <span class="entry-a">{E(hint)}</span>
        <span class="entry-go">{t["entry_open"]} &rarr;</span>
      </a>''')
    return f'''<section id="entradas">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t["entry_eyebrow"]}</p>
      <h2>{t["entry_h2"]}</h2>
      <p>{t["entry_p"]}</p>
    </div>
    <div class="entry-grid">
{chr(10).join(cards)}
    </div>
  </div>
</section>

'''


def pilot(lang):
    t = T[lang]
    cols = []
    for h, items in t["pilot_cols"]:
        li = "\n".join(f"          <li>{E(i)}</li>" for i in items)
        cols.append(f'''      <div class="pilot-col">
        <h3>{E(h)}</h3>
        <ul>
{li}
        </ul>
      </div>''')
    return f'''<section id="piloto">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t["pilot_eyebrow"]}</p>
      <h2>{t["pilot_h2"]}</h2>
      <p>{t["pilot_p"]}</p>
    </div>
    <div class="pilot-grid">
{chr(10).join(cols)}
    </div>
    <p class="show-cta"><a class="btn btn-primary" href="#contato">{t["pilot_btn"]} &rarr;</a>{book_btn(lang)}</p>
  </div>
</section>

'''


def person_cards(lang):
    out = []
    for m in CFG.get("team", []):
        name = m["name"]
        initials = "".join(w[0] for w in name.split()[:2]).upper()
        mark = (f'<img class="person-photo" loading="lazy" decoding="async" src="/img/team/{E(m["photo"])}" alt="{E(name)}">' if m.get("photo")
                else f'<div class="person-mark" aria-hidden="true">{E(initials)}</div>')
        bio = m.get("bio_" + lang, "")
        bio_html = f'<p class="person-bio">{E(bio)}</p>' if bio else ""
        li = f'<a class="ext" href="{E(m["linkedin"])}" target="_blank" rel="noopener">LinkedIn &rarr;</a>' if m.get("linkedin") else ""
        out.append(f'''    <div class="person">
      {mark}
      <div><strong>{E(name)}</strong><span>{E(m.get("role_" + lang, ""))}</span>{bio_html}</div>
      {li}
    </div>''')
    return "\n".join(out)


def about_teaser(lang):
    t = T[lang]
    return f'''<section id="sobre">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t["about_eyebrow"]}</p>
      <h2>{t["about_h2"]}</h2>
      <p>{t["about_p"]}</p>
    </div>
{person_cards(lang)}
    <p class="show-cta"><a class="btn btn-primary" href="{path_for(lang, "about")}">{t["about_btn"]} &rarr;</a>
      <a class="btn btn-ghost" href="{GITHUB}" target="_blank" rel="noopener">{t["about_code"]} &rarr;</a></p>
  </div>
</section>

'''


def simple_page(lang, kind, title, desc, body):
    return absolutize(head(lang, title, desc, kind) + header(lang, kind) + body + contact_cta(lang) + footer(lang) + tail(lang, kind))


def tr(lang, name):
    s = read(name)
    return translate(s, EN) if lang == "en" else s


def about_page(lang):
    t = T[lang]
    u = UI[lang]
    lines = "".join(f'<div class="who-row"><span class="who-k">{E(k)}</span><p>{E(v)}</p></div>' for k, v in t["who_lines"])
    body = f'''<main class="page">
  <div class="wrap">
    <p class="crumbs"><a href="{u["prefix"]}/">{u["crumb_home"]}</a> / {t["about_eyebrow"]}</p>
    <div class="section-head">
      <p class="eyebrow">{t["about_eyebrow"]}</p>
      <h1>{t["ab_h1"]}</h1>
      <p class="lead">{t["ab_lead"]}</p>
    </div>
    <h2 class="gal-h">{t["who_h2"]}</h2>
    <div class="people">{person_cards(lang)}</div>
    <div class="who">{lines}</div>
    <p class="show-cta"><a class="btn btn-ghost" href="{GITHUB}" target="_blank" rel="noopener">{t["about_code"]} &rarr;</a>
      <a class="btn btn-ghost" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn &rarr;</a></p>
  </div>
</main>
{tr(lang, "proposito")}
{tr(lang, "position")}
{tr(lang, "setores")}
{tr(lang, "parceria")}
'''
    return simple_page(lang, "about", t["ab_title"], t["ab_desc"], body)


def capabilities_page(lang):
    t = T[lang]
    u = UI[lang]
    figs = "\n".join(f'      <figure><img loading="lazy" decoding="async" src="/img/portfolio/{f}" alt="{E(c)}"><figcaption>{E(c)}</figcaption></figure>' for f, c in t["studio"])
    ex = tr(lang, "exemplos")
    body = f'''<main class="page">
  <div class="wrap">
    <p class="crumbs"><a href="{u["prefix"]}/">{u["crumb_home"]}</a> / {t["cap_h1"]}</p>
    <div class="section-head">
      <h1>{t["cap_h1"]}</h1>
      <p class="lead">{t["cap_lead"]}</p>
    </div>
  </div>
</main>
{tr(lang, "capacidades")}
{ex}
<section id="studio">
  <div class="wrap">
    <div class="section-head">
      <h2>{t["studio_h2"]}</h2>
      <p>{t["studio_p"]}</p>
    </div>
    <div class="gallery">
{figs}
    </div>
  </div>
</section>
'''
    return simple_page(lang, "capabilities", t["cap_title"], t["cap_desc"], body)


def privacy_page(lang):
    t = T[lang]
    u = UI[lang]
    legal = ""
    if CFG.get("legal_name"):
        legal = f" ({E(CFG['legal_name'])}" + (f", CNPJ {E(CFG['cnpj'])}" if CFG.get("cnpj") else "") + ")"
    analytics = (ANALYTICS_ON if CFG.get("analytics_goatcounter", "").strip() else ANALYTICS_OFF)[lang]
    secs = "\n".join(f"    <h2>{E(h)}</h2>\n    <p>{b.format(legal=legal, analytics=analytics)}</p>" for h, b in PRIVACY[lang])
    body = f'''<main class="page legal">
  <div class="wrap">
    <p class="crumbs"><a href="{u["prefix"]}/">{u["crumb_home"]}</a> / {t["pv_h1"]}</p>
    <h1>{t["pv_h1"]}</h1>
{secs}
  </div>
</main>
'''
    return absolutize(head(lang, t["pv_title"], t["pv_desc"], "privacy") + header(lang, "privacy") + body + footer(lang) + tail(lang, "privacy"))


def not_found():
    body = '''<main class="page"><div class="wrap">
  <p class="eyebrow">404</p>
  <h1>Página não encontrada · Page not found</h1>
  <p class="lead"><a href="/">Voltar ao início</a> · <a href="/en/">Back to the home page</a></p>
</div></main>
'''
    return absolutize(head("pt", "404 — ChordIQ", "Página não encontrada.", "home").replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n  <link rel="canonical"') + header("pt", "home") + body + footer("pt") + tail("pt", "home"))


def sitemap(urls):
    rows = "\n".join(f"  <url><loc>{SITE}{u}</loc></url>" for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n'


def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)


def main():
    # clean generated output
    for d in ("portfolio", "en", "sobre", "capacidades", "privacidade"):
        shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)
    missing = set()
    # dry run for missing translations (home sections)
    for name in HOME_ORDER:
        if name in ("SHOWCASE", "HIGHLIGHTS", "ENTRIES", "PILOT", "ABOUT"):
            continue
        translate(read(name), EN, missing)
    translate(read("footer"), EN, missing)
    if missing:
        print("MISSING EN TRANSLATIONS:")
        for k, t in sorted(missing):
            print(f"  {k}\t{t[:100]}")
        sys.exit(1)
    for lang in ("pt", "en"):
        write(path_for(lang, "home") + "index.html", home(lang))
        write(path_for(lang, "portfolio") + "index.html", portfolio(lang))
        for p in P:
            write(path_for(lang, "project", p["slug"]), project(lang, p))
        write(path_for(lang, "about") + "index.html", about_page(lang))
        write(path_for(lang, "capabilities") + "index.html", capabilities_page(lang))
        write(path_for(lang, "privacy") + "index.html", privacy_page(lang))
    write("/404.html", not_found())
    urls = []
    for lang in ("pt", "en"):
        urls += [path_for(lang, k) for k in ("home", "portfolio", "about", "capabilities", "privacy")]
        urls += [path_for(lang, "project", p["slug"]) for p in P]
    write("/sitemap.xml", sitemap(urls))
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("built", len(urls) + 1, "pages")


if __name__ == "__main__":
    main()
