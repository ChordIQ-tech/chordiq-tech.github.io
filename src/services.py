"""Services page and the 'who does what' block (ChordIQ x Domus), bilingual."""

PDF = {"pt": "/downloads/chordiq-comercial-pt.pdf", "en": "/downloads/chordiq-commercial-en.pdf"}

S = {
    "pt": dict(
        title="Serviços — ChordIQ + Domus",
        desc="Cada projeto começa por uma conversa: um diagnóstico sob NDA, sem custo, e um escopo definido junto com você.",
        crumb="Serviços", eyebrow="Serviços",
        h1="Cada projeto começa pela conversa.",
        lead="Não vendemos pacote pronto. Escopo, entregáveis, formato e condições comerciais são definidos junto com você, a partir do seu problema.",
        formats_h2="Como começamos",
        formats=[
            ("01", "Diagnóstico", "Sob NDA, sem custo",
             "Entender o seu problema e dizer se há ganho claro antes de qualquer proposta.",
             ["Uma conversa de 30 minutos.", "Confidencialidade antes de qualquer dado."]),
            ("02", "Escopo", "Definido junto com você",
             "Combinar o que será feito, a métrica de sucesso e a forma de trabalho.",
             ["Escopo e métrica de sucesso por escrito.", "Formato e condições conforme o seu caso."]),
            ("03", "Projeto", "Ganho medido",
             "Executar e comparar o resultado com o método que você usa hoje.",
             ["Resultado comparado ao método atual.", "Limites e incerteza declarados."]),
        ],
        deliver="O que inclui", for_="Objetivo",
        limits_h="Condições dos testes e limites de validade",
        limits_p="Cada número que mostramos vem com as condições do teste e o limite de validade. Não prometemos a mesma aceleração ou precisão no seu caso sem antes avaliar o seu problema, a sua geometria e os seus dados.",
        diag_h="Fale com a gente", diag_p="Conte o problema. Voltamos com uma conversa de diagnóstico, sob NDA e sem custo, para definir juntos o melhor caminho.",
        diag_btn="Agendar diagnóstico", pdf_btn="Baixar o resumo em PDF (1 página)", wa_btn="Falar pelo WhatsApp",
    ),
    "en": dict(
        title="Services — ChordIQ + Domus",
        desc="Every project starts with a conversation: a free diagnosis under NDA and a scope defined together with you.",
        crumb="Services", eyebrow="Services",
        h1="Every project starts with a conversation.",
        lead="We do not sell a ready-made package. Scope, deliverables, format and commercial terms are defined together with you, starting from your problem.",
        formats_h2="How we start",
        formats=[
            ("01", "Diagnosis", "Under NDA, free of charge",
             "Understand your problem and tell you whether there is a clear gain before any proposal.",
             ["A 30-minute conversation.", "Confidentiality before any data."]),
            ("02", "Scope", "Defined together with you",
             "Agree on what will be done, the success metric and the way of working.",
             ["Scope and success metric in writing.", "Format and terms according to your case."]),
            ("03", "Project", "Measured gain",
             "Execute and compare the result with the method you use today.",
             ["Result compared with the current method.", "Limits and uncertainty stated."]),
        ],
        deliver="What it includes", for_="Goal",
        limits_h="Test conditions and validity limits",
        limits_p="Every number we show comes with the test conditions and its validity limit. We do not promise the same speed-up or accuracy on your case without first assessing your problem, geometry and data.",
        diag_h="Talk to us", diag_p="Tell us the problem. We come back with a diagnosis conversation, under NDA and free of charge, to define the best path together.",
        diag_btn="Book a diagnosis", pdf_btn="Download the 1-page PDF summary", wa_btn="Talk on WhatsApp",
    ),
}

R = {
    "pt": dict(
        eyebrow="Quem faz o quê", h2="ChordIQ desenvolve. Domus entrega.",
        p="Duas empresas, um projeto só do ponto de vista do cliente.",
        rows=[("ChordIQ", "Desenvolve", "Constrói a tecnologia de Physics AI: modelos físicos, modelos substitutos, verificação e o código aberto PINNeAPPle."),
              ("Domus", "Entrega", "Leva a tecnologia para a operação da engenharia industrial: implantação, agentes e o modelo comercial por ganho."),
              ("Contratação", "Definida com você", "Como o projeto é contratado é combinado na conversa comercial, conforme o seu caso.")],
    ),
    "en": dict(
        eyebrow="Who does what", h2="ChordIQ builds. Domus delivers.",
        p="Two companies, one project from the customer's point of view.",
        rows=[("ChordIQ", "Builds", "Builds the Physics AI technology: physics-based models, surrogate models, verification and the open-source PINNeAPPle."),
              ("Domus", "Delivers", "Takes the technology into industrial engineering operations: deployment, agents and the gain-based commercial model."),
              ("Contracting", "Defined with you", "How the project is contracted is agreed in the commercial conversation, according to your case.")],
    ),
}
