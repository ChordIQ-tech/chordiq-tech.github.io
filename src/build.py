#!/usr/bin/env python3
"""Builds the bilingual site (pt at /, en at /en/) into the repository root.

Run from the repository root:  python3 src/build.py
Sources: src/sections/*.html (Portuguese home sections), src/en.json (English text for them),
src/projects.py (portfolio content in both languages).
"""
import html
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from i18n import translate  # noqa: E402
from projects import BY_SLUG, CATEGORIES, CATEGORY_ORDER, HOME_HIGHLIGHTS, P  # noqa: E402

EN = json.load(open(os.path.join(ROOT, "src", "en.json"), encoding="utf-8"))
E = html.escape
SITE = "https://chordiq-tech.github.io"

UI = {
    "pt": dict(
        lang="pt-BR", prefix="", other="en", other_label="EN", other_title="Read in English",
        title="ChordIQ — Physics AI para engenharia industrial",
        desc="Transformamos simulações e processos industriais em modelos de IA rápidos, físicos e verificáveis. CFD, gêmeos digitais, modelos substitutos e verificação, com casos reais e número medido.",
        nav=[("servicos", "Serviços"), ("portfolio", "Portfólio"), ("casos", "Casos reais"), ("capacidades", "Capacidades"),
             ("principio", "Princípio"), ("metodo", "Como trabalhamos"), ("parceria", "Parceria"), ("contato", "Contato")],
        cta="Falar com a gente", menu="Menu",
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
        nav=[("servicos", "Services"), ("portfolio", "Portfolio"), ("casos", "Real cases"), ("capacidades", "Capabilities"),
             ("principio", "Principle"), ("metodo", "How we work"), ("parceria", "Partnership"), ("contato", "Contact")],
        cta="Talk to us", menu="Menu",
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

HOME_ORDER = ["hero", "SHOWCASE", "proof", "problema", "HIGHLIGHTS", "servicos", "casos", "capacidades", "exemplos", "setores",
              "principio", "validacao", "metodo", "proposito", "position", "parceria", "contato"]


def read(name):
    return open(os.path.join(ROOT, "src", "sections", name + ".html"), encoding="utf-8").read()


def absolutize(s):
    s = re.sub(r'(src|poster)="(img|videos)/', r'\1="/\2/', s)
    s = s.replace('href="styles.css"', 'href="/styles.css"').replace('src="script.js"', 'src="/script.js"')
    return s


def path_for(lang, kind, slug=None):
    pre = UI[lang]["prefix"]
    if kind == "home":
        return pre + "/"
    if kind == "portfolio":
        return pre + "/portfolio/"
    return f"{pre}/portfolio/{slug}.html"


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
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap">
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
'''


def header(lang, kind, slug=None):
    u = UI[lang]
    home = u["prefix"] + "/"
    base = "" if kind == "home" else home
    nav = []
    for anchor, label in u["nav"]:
        href = f"{home}portfolio/" if (anchor == "portfolio" and kind != "home") else f"{base}#{anchor}"
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


def tail(lang="pt", kind="home"):
    u = UI[lang]
    base = "" if kind == "home" else u["prefix"] + "/"
    return f'''
<a class="mobile-cta" href="{base}#contato">{u["cta"]}</a>
<script src="/script.js"></script>
</body>
</html>
'''


def footer(lang):
    s = read("footer")
    return translate(s, EN) if lang == "en" else s


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
        else:
            s = read(name)
            if name == "exemplos":
                s = s.replace('<div class="wrap">', f'<div class="wrap">\n    <details class="more"><summary>{u["ex_summary"]}</summary>', 1)
                s = s.replace("  </div>\n</section>", "    </details>\n  </div>\n</section>")
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


def contact_cta(lang):
    u = UI[lang]
    return f'''<section class="cta-band">
  <div class="wrap">
    <h2>{u["cta_h"]}</h2>
    <p>{u["cta_p"]}</p>
    <p><a class="btn btn-primary" href="{u["prefix"]}/#contato">{u["cta_b"]} &rarr;</a></p>
  </div>
</section>
'''


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


def write(path, content):
    full = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)


def main():
    # clean generated output
    for d in ("portfolio", "en"):
        shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)
    missing = set()
    # dry run for missing translations (home sections)
    for name in HOME_ORDER:
        if name in ("SHOWCASE", "HIGHLIGHTS"):
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
    print("built", 2 * (2 + len(P)), "pages")


if __name__ == "__main__":
    main()
