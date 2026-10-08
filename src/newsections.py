"""Bilingual content for the sections and pages that are generated (not translated from src/sections)."""
import html

E = html.escape
GITHUB = "https://github.com/PINNeAPPle-Labs/PINNeAPPle"
LINKEDIN = "https://www.linkedin.com/in/yan-barros-yan"

T = {
    "pt": dict(
        entry_eyebrow="Por onde começar",
        entry_h2="Qual é o seu problema?",
        entry_p="Escolha o que mais se parece com a sua situação. Cada atalho leva a um projeto nosso, com vídeo, números medidos e limites.",
        entries=[
            ("Minha simulação demora demais para decidir", "heatsink-sizer", "Substitutos que respondem em milissegundos, conferidos contra a simulação real."),
            ("Preciso escolher entre muitos projetos possíveis", "aircraft-design-optimizer", "Otimização com compromissos reais, e o motivo de cada projeto rejeitado."),
            ("Não sei se posso confiar no resultado", "simulation-comparator", "Comparação, malha e verificação antes de uma decisão."),
            ("Meus dados de planta estão bagunçados", "engineering-data-health", "Diagnóstico de qualidade com a evidência de cada achado."),
            ("Tenho poucas medições e preciso estimar o resto", "inverse-heat-lab", "Do punhado de sensores ao campo inteiro, com o parâmetro que ninguém mediu."),
            ("Gasto horas copiando dados de datasheets", "form-compiler", "Formulários preenchidos, com a fonte de cada valor."),
        ],
        entry_open="Ver o projeto",
        pilot_eyebrow="O piloto",
        pilot_h2="O que acontece quando você decide testar.",
        pilot_p="Todo projeto começa por um piloto de escopo fechado. Sem surpresas: você sabe o que traz, o que recebe e em que condições.",
        pilot_cols=[
            ("O que você traz", ["O problema e a métrica de sucesso, em uma página.",
                                 "Uma amostra de dados, geometria ou documentos (pode ser anonimizada).",
                                 "Alguém da sua equipe técnica para validar o resultado."]),
            ("O que entregamos", ["Escopo fechado por escrito, antes da primeira linha de código.",
                                  "Uma ferramenta ou modelo funcionando sobre o seu caso.",
                                  "O resultado comparado ao método atual, com o ganho medido, os limites e a incerteza."]),
            ("Condições", ["NDA antes de qualquer dado.",
                           "Diagnóstico inicial sem custo; prazo e valor definidos no escopo fechado.",
                           "Na validação você paga só o custo aberto, sem margem; em produção, a remuneração acompanha o ganho."]),
        ],
        pilot_btn="Discutir um piloto",
        about_eyebrow="Quem somos",
        about_h2="Engenharia aplicada, com código aberto que você pode auditar.",
        about_p="Todos os projetos deste site são construídos sobre o PINNeAPPle, uma biblioteca de Physics AI de código aberto (licença Apache 2.0), publicada no PyPI, com repositório público, changelog e testes.",
        about_person="Yan Barros", about_role="autor e mantenedor do PINNeAPPle · Natal/RN",
        about_btn="Conhecer a equipe e a parceria", about_code="Ver o código no GitHub",
        # about page
        ab_title="Sobre a ChordIQ + Domus — equipe, propósito e parceria", ab_desc="Sobre a ChordIQ + Domus: o PINNeAPPle, uma biblioteca de Physics AI de código aberto, o propósito, o posicionamento e a parceria com a Domus.",
        ab_h1="Sobre a ChordIQ + Domus", ab_lead="Engenharia aplicada com IA científica, construída sobre uma biblioteca aberta que qualquer pessoa pode auditar.",
        who_h2="Quem está por trás", who_lines=[
            ("Código aberto", "O PINNeAPPle é uma biblioteca de Physics AI (redes informadas pela física, operadores neurais, solvers e pipelines reprodutíveis) sob licença Apache 2.0, publicada no PyPI, com repositório público, changelog e testes. Cada projeto do portfólio roda sobre ela."),
        ],
        # capabilities page
        cap_title="Capacidades — ChordIQ + Domus", cap_desc="Os formatos de aplicação que a ChordIQ + Domus já sabem construir, as chamadas reais por trás das entregas e a visualização 3D de resultados.",
        cap_h1="Capacidades", cap_lead="Os formatos de aplicação que já sabemos construir, as chamadas reais por trás de algumas entregas e como mostramos qualquer resultado de simulação em 3D.",
        studio_h2="Visualização 3D de qualquer resultado",
        studio_p="Resultados de OpenFOAM, CalculiX, Abaqus, Gmsh ou VTK viram cenas 3D (glTF, USD para Omniverse, visualizador web e renders em Blender). Abaixo, o corpo de Ahmed, uma referência de aerodinâmica veicular: escoamento em OpenFOAM (RANS k-ω SST, 40 m/s, inclinação de 25°), com CD de 0,298 contra cerca de 0,285 medido, em malha média de 0,20 milhão de células e 10 minutos em 2 núcleos.",
        studio=[("studio-ahmed-cp.jpg", "Corpo de Ahmed: pressão na superfície (Cp)"),
                ("studio-ahmed-streamlines.jpg", "Corpo de Ahmed: linhas de corrente por velocidade"),
                ("studio-ahmed-mid-plane-speed.jpg", "Corpo de Ahmed: velocidade no plano central"),
                ("studio-ahmed-wake-vorticity.jpg", "Corpo de Ahmed: vorticidade na esteira"),
                ("studio-airliner-cp.jpg", "Avião com o Cp calculado em OpenFOAM"),
                ("studio-cantilever-von-mises.jpg", "Viga em balanço com tensão de von Mises (CalculiX)")],
        # privacy
        pv_title="Política de privacidade — ChordIQ + Domus", pv_desc="Como este site trata dados pessoais.", pv_h1="Política de privacidade",
        legal=["Privacidade", "Sobre", "Capacidades"],
    ),
    "en": dict(
        entry_eyebrow="Where to start",
        entry_h2="What is your problem?",
        entry_p="Pick the one that looks most like your situation. Each shortcut leads to one of our projects, with video, measured numbers and limits.",
        entries=[
            ("My simulation takes too long to decide", "heatsink-sizer", "Surrogates that answer in milliseconds, checked against the real simulation."),
            ("I have to choose among many possible designs", "aircraft-design-optimizer", "Optimization with real trade-offs, and the reason each design was rejected."),
            ("I don't know if I can trust the result", "simulation-comparator", "Comparison, mesh and verification before a decision."),
            ("My plant data is a mess", "engineering-data-health", "A quality diagnosis with the evidence for each finding."),
            ("I have few measurements and need to estimate the rest", "inverse-heat-lab", "From a handful of sensors to the whole field, with the parameter nobody measured."),
            ("I spend hours copying data from datasheets", "form-compiler", "Filled forms, with the source of every value."),
        ],
        entry_open="See the project",
        pilot_eyebrow="The pilot",
        pilot_h2="What happens when you decide to test.",
        pilot_p="Every project starts with a closed-scope pilot. No surprises: you know what you bring, what you get and under what conditions.",
        pilot_cols=[
            ("What you bring", ["The problem and the success metric, on one page.",
                                "A sample of data, geometry or documents (it can be anonymized).",
                                "Someone from your technical team to validate the result."]),
            ("What we deliver", ["A closed scope in writing, before the first line of code.",
                                 "A working tool or model on your case.",
                                 "The result compared with your current method, with the gain measured, the limits and the uncertainty."]),
            ("Conditions", ["An NDA before any data.",
                            "Initial diagnosis at no cost; timeline and price set in the closed scope.",
                            "In validation you pay only the open cost, with no margin; in production, remuneration follows the gain."]),
        ],
        pilot_btn="Discuss a pilot",
        about_eyebrow="Who we are",
        about_h2="Applied engineering, with open-source code you can audit.",
        about_p="Every project on this site is built on PINNeAPPle, an open-source Physics AI library (Apache 2.0 licence), published on PyPI, with a public repository, a changelog and tests.",
        about_person="Yan Barros", about_role="author and maintainer of PINNeAPPle · Natal, Brazil",
        about_btn="Meet the team and the partnership", about_code="See the code on GitHub",
        ab_title="About ChordIQ + Domus — team, purpose and partnership", ab_desc="About ChordIQ + Domus: PINNeAPPle, an open-source Physics AI library, the purpose, the positioning and the partnership with Domus.",
        ab_h1="About ChordIQ + Domus", ab_lead="Applied engineering with scientific AI, built on an open library that anyone can audit.",
        who_h2="Who is behind it", who_lines=[
            ("Open source", "PINNeAPPle is a Physics AI library (physics-informed networks, neural operators, solvers and reproducible pipelines) under the Apache 2.0 licence, published on PyPI, with a public repository, a changelog and tests. Every project in the portfolio runs on it."),
        ],
        cap_title="Capabilities — ChordIQ + Domus", cap_desc="The application formats ChordIQ + Domus already know how to build, the real calls behind the deliverables and 3D visualization of results.",
        cap_h1="Capabilities", cap_lead="The application formats we already know how to build, the real calls behind some deliverables and how we show any simulation result in 3D.",
        studio_h2="3D visualization of any result",
        studio_p="Results from OpenFOAM, CalculiX, Abaqus, Gmsh or VTK become 3D scenes (glTF, USD for Omniverse, a web viewer and Blender renders). Below, the Ahmed body, a vehicle-aerodynamics reference: OpenFOAM flow (RANS k-ω SST, 40 m/s, 25° slant), with CD of 0.298 against about 0.285 measured, on a medium mesh of 0.20 million cells and 10 minutes on 2 cores.",
        studio=[("studio-ahmed-cp.jpg", "Ahmed body: surface pressure (Cp)"),
                ("studio-ahmed-streamlines.jpg", "Ahmed body: streamlines by speed"),
                ("studio-ahmed-mid-plane-speed.jpg", "Ahmed body: speed on the mid plane"),
                ("studio-ahmed-wake-vorticity.jpg", "Ahmed body: wake vorticity"),
                ("studio-airliner-cp.jpg", "An airliner with the Cp computed in OpenFOAM"),
                ("studio-cantilever-von-mises.jpg", "Cantilever beam with von Mises stress (CalculiX)")],
        pv_title="Privacy policy — ChordIQ + Domus", pv_desc="How this website handles personal data.", pv_h1="Privacy policy",
        legal=["Privacy", "About", "Capabilities"],
    ),
}

PRIVACY = {
    "pt": [
        ("Quem somos", "Este site é da ChordIQ + Domus{legal}. Para qualquer pedido sobre dados pessoais, escreva para <a href=\"mailto:yan@pinneapple.org\">yan@pinneapple.org</a>."),
        ("O que o site coleta", "O site é estático e não define cookies. O formulário de contato não envia nada para um servidor nosso: ele monta a mensagem no seu navegador e abre o seu WhatsApp ou o seu aplicativo de e-mail, e só vai adiante se você confirmar o envio. Os dados que você escrever (nome, e-mail, empresa e descrição do problema) só chegam até nós por esse canal, e só se você enviar."),
        ("Para que usamos", "Os dados que você nos envia servem apenas para responder ao seu contato e para preparar uma proposta ou um escopo, se houver interesse. Não vendemos nem compartilhamos esses dados."),
        ("Estatísticas de acesso", "{analytics}"),
        ("Hospedagem e fontes", "O site é hospedado no GitHub Pages, que pode registrar o endereço IP de quem acessa, conforme a política de privacidade do GitHub. As fontes de texto e os vídeos são servidos pelo próprio site, sem serviços de terceiros."),
        ("Seus direitos", "Pela LGPD, você pode pedir acesso, correção ou exclusão dos dados que nos enviou, e a revogação de qualquer consentimento. Escreva para <a href=\"mailto:yan@pinneapple.org\">yan@pinneapple.org</a>."),
    ],
    "en": [
        ("Who we are", "This site belongs to ChordIQ + Domus{legal}. For any request about personal data, write to <a href=\"mailto:yan@pinneapple.org\">yan@pinneapple.org</a>."),
        ("What the site collects", "The site is static and sets no cookies. The contact form does not send anything to a server of ours: it builds the message in your browser and opens your WhatsApp or e-mail app, and it only goes further if you confirm the sending. The data you write (name, e-mail, company and a description of the problem) reaches us only through that channel, and only if you send it."),
        ("What we use it for", "The data you send us is used only to answer your contact and to prepare a proposal or a scope, if there is interest. We do not sell or share it."),
        ("Visit statistics", "{analytics}"),
        ("Hosting and fonts", "The site is hosted on GitHub Pages, which may log the IP address of visitors, according to GitHub's privacy policy. Text fonts and videos are served by the site itself, with no third-party services."),
        ("Your rights", "Under Brazil's LGPD you may ask for access to, correction of or deletion of the data you sent us, and to withdraw any consent. Write to <a href=\"mailto:yan@pinneapple.org\">yan@pinneapple.org</a>."),
    ],
}
ANALYTICS_OFF = {"pt": "No momento o site não usa ferramenta de análise de visitas.",
                 "en": "At the moment the site uses no visit-analytics tool."}
ANALYTICS_ON = {"pt": "Usamos o GoatCounter, uma ferramenta de contagem de visitas que não usa cookies e não identifica pessoas, só conta páginas vistas, país e tipo de dispositivo.",
                "en": "We use GoatCounter, a visit-counting tool that sets no cookies and does not identify people; it only counts page views, country and device type."}
