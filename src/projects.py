"""Portfolio content, in Portuguese (pt) and English (en). One entry per project."""

CATEGORIES = {
    "thermal": {"pt": "Térmica e inversão", "en": "Thermal and inversion"},
    "data": {"pt": "Dados industriais", "en": "Industrial data"},
    "sim": {"pt": "Simulação e malha", "en": "Simulation and mesh"},
    "trace": {"pt": "Documentos e rastreabilidade", "en": "Documents and traceability"},
    "aero": {"pt": "Aeroespacial e otimização", "en": "Aerospace and optimization"},
}
CATEGORY_ORDER = ["aero", "thermal", "data", "sim", "trace"]

P = []


def add(**kw):
    P.append(kw)


add(
    slug="aircraft-design-optimizer", n=13, cat="aero", name="Aircraft Design Optimizer",
    image="13-aircraft-design-optimizer.jpg", thumb="13-aircraft-render-pressure.jpg",
    gallery=[("13-aircraft-render-pressure.jpg", "Cp", "Pressão na pele (Cp), calculada em OpenFOAM 3D", "Skin pressure (Cp), computed in 3D OpenFOAM"),
             ("13-aircraft-render-streamlines.jpg", "stream", "Linhas de corrente coloridas por velocidade", "Streamlines coloured by speed"),
             ("13-aircraft-render-friction.jpg", "Cf", "Atrito na pele (Cf)", "Skin friction (Cf)"),
             ("13-aircraft-render-flight.jpg", "flight", "Projeto escolhido, renderizado em voo", "The chosen design, rendered in flight"),
             ("aero_pareto.jpg", "pareto", "1.920 projetos voados, com os motivos de rejeição", "1,920 designs flown, with the reasons for rejection"),
             ("aero_blender.jpg", "blender", "Renders em Blender: classe A320 e escolha equilibrada", "Blender renders: A320 class and the balanced pick")],
    tags={"pt": ["CFD", "NSGA-II", "Otimização", "OpenFOAM"], "en": ["CFD", "NSGA-II", "Optimization", "OpenFOAM"]},
    pt=dict(
        tagline="1.920 projetos de avião comercial voados antes do almoço, e quais seriam certificáveis.",
        problem="Projetar a asa de um avião de corredor único é um jogo de compromissos que se contradizem: menos CO₂ por passageiro, cruzeiro mais rápido, aproximação mais lenta. Avaliar cada candidato com CFD completo é inviável; avaliar só com uma fórmula esconde os defeitos.",
        how="Um algoritmo genético (NSGA-II) varia a asa (área, envergadura, afilamento, enflechamento, torção, posição) e o Mach de cruzeiro, para um avião da classe A320 / 737 com mais de 150 assentos. Cada projeto voa uma missão completa: vortex lattice compressível, arrasto de onda transônico, pesos de categoria transporte, alcance de Breguet, velocidade de aproximação com slats e flaps, margens de estabilidade e de buffet. Os projetos escolhidos são conferidos em OpenFOAM 3D, e cada um exporta para glTF, USD (Omniverse) e STL.",
        results=["Calibrado primeiro no A320, antes de qualquer otimização: MTOW 73,5 t, L/D 16,4, Vref 131 kt",
                 "Três objetivos que realmente brigam: menos CO₂ por passageiro-km, Mach de cruzeiro mais alto e aproximação mais lenta",
                 "Projeto mais verde viável: −13% de CO₂ por passageiro-km, em Mach 0,735 e ainda dentro do portão de aeroporto de 36 m",
                 "Escolha equilibrada: −7,5% de CO₂ em Mach 0,80, com a mesma aproximação de 130 kt",
                 "Os projetos que falham dizem por quê: envergadura no portão, margem de buffet, volume de combustível, estol de ponta, margem estática, trimagem",
                 "Verificado em OpenFOAM 3D: pressão na pele, linhas de corrente e esteira, em escala do azul (baixo) ao vermelho (alto)"],
        limit="Ferramenta de projeto conceitual, não certificada: um engenheiro ainda precisa assumir os números."),
    en=dict(
        tagline="1,920 airliner designs flown before lunch, and which of them would actually be certifiable.",
        problem="Designing the wing of a single-aisle airliner is a game of competing goals: less CO₂ per passenger, faster cruise, slower approach. Evaluating every candidate with full CFD is not feasible; evaluating with a formula alone hides the flaws.",
        how="A genetic algorithm (NSGA-II) varies the wing (area, span, taper, sweep, twist, position) and the cruise Mach, for an A320 / 737-class airliner with 150+ seats. Every design flies a full mission: compressible vortex lattice, transonic wave drag, transport-category weights, Breguet range, approach speed with slats and flaps, stability and buffet margins. The picks are checked in 3D OpenFOAM, and every design exports to glTF, USD (Omniverse) and STL.",
        results=["Calibrated on the A320 first, before any optimization: MTOW 73.5 t, L/D 16.4, Vref 131 kt",
                 "Three goals that really fight: less CO₂ per passenger-km, higher cruise Mach, slower approach",
                 "Greenest feasible design: −13% CO₂ per passenger-km, at Mach 0.735 and still inside the 36 m airport gate",
                 "Balanced pick: −7.5% CO₂ at Mach 0.80, with the same 130 kt approach",
                 "Designs that fail say why: gate span, buffet margin, fuel volume, tip stall, static margin, trim",
                 "Checked in 3D OpenFOAM: pressure on the skin, streamlines and wake, coloured from blue (low) to red (high)"],
        limit="A conceptual-design tool, not a certified one: an engineer still has to own the numbers."),
)

add(
    slug="pcb-hotspot", n=2, cat="thermal", name="PCB Hotspot", image="02-pcb-hotspot.jpg", gallery=[],
    tags={"pt": ["Eletrônica", "Calibração", "EKI"], "en": ["Electronics", "Calibration", "EKI"]},
    pt=dict(
        tagline="Temperatura de junção de cada componente da placa em cerca de um segundo.",
        problem="Muita equipe ainda confere a térmica da placa com uma planilha de valores de θJA. Esse número vem de uma placa de teste JEDEC, não do seu layout, e pode errar feio num produto real. A alternativa é esperar dias por um especialista em CFD.",
        how="Você descreve a placa (tamanho, camadas de cobre, componentes e potência, vias térmicas, fluxo de ar) e recebe um modelo volumétrico em camadas, com cobre e dielétrico, em que cada encapsulamento entra como modelo JEDEC de duas resistências. Se você tiver algumas temperaturas medidas (termopar, ponto de IR, sensor no die), a Ensemble Kalman Inversion calibra o resfriamento real e o espalhamento de cobre da sua placa e refaz a previsão com faixa de incerteza.",
        results=["Reproduz o θJA publicado dentro de 8% em oito famílias de encapsulamento, do SOIC-8 a um BGA de 35 mm",
                 "Componente crítico sinalizado, mapa de temperatura das duas faces, vista 3D e para onde o calor realmente vai (placa, ar, chassi)",
                 "Lista ordenada de “e se”: vias térmicas, cobre de 2 oz, mais planos, fluxo de ar, fixação ao chassi, cada uma com os graus que ganha",
                 "No exemplo, o modelo sem calibrar põe a FPGA a 99 °C, no limite de 100 °C; calibrado com sete leituras, ela chega a 111 °C, acima do limite",
                 "Se as medições contradizem o modelo, ele diz isso em vez de fingir"],
        limit=None),
    en=dict(
        tagline="Junction temperature of every component on the board in about a second.",
        problem="Many teams still check board thermals with a spreadsheet of θJA values. That number comes from a standard JEDEC test board, not from your layout, so it can be badly off on a real product. The alternative is waiting days for a CFD specialist.",
        how="You describe the board (size, copper layers, components and their power, thermal vias, airflow) and get a layered 3D finite-volume model of the copper and dielectric, with each package as a JEDEC two-resistor model. Give it a few measured temperatures (a thermocouple, an IR spot, an on-die sensor) and Ensemble Kalman Inversion calibrates the real cooling and copper spreading of your board, then re-predicts every junction with an uncertainty band.",
        results=["Reproduces published θJA within 8% for eight package families, from SOIC-8 to a 35 mm BGA",
                 "The critical part flagged, a temperature map of both faces, a 3D view and where the heat actually goes (board, air, chassis)",
                 "A ranked \"what-if\" list: thermal vias, 2 oz copper, more planes, airflow, clamping to the chassis, each with the degrees it buys",
                 "In the example, the uncalibrated model puts the FPGA at 99 °C, right at its 100 °C limit; calibrated with seven readings it lands at 111 °C, above the limit",
                 "If your measurements contradict the model, it says so instead of pretending"],
        limit=None),
)

add(
    slug="inverse-heat-lab", n=7, cat="thermal", name="Inverse Heat Lab", image="07-inverse-heat-lab.jpg", gallery=[],
    tags={"pt": ["PINN", "Problema inverso", "Térmica"], "en": ["PINN", "Inverse problem", "Thermal"]},
    pt=dict(
        tagline="Do punhado de leituras de termopar ao coeficiente de transferência de calor h, ao campo inteiro e às temperaturas que ninguém mediu.",
        problem="O coeficiente h é o número de que todo cálculo térmico depende, e ninguém o mede diretamente. As correlações costumam prometer ±25%. Termopares, por outro lado, são baratos.",
        how="Uma rede neural informada pela física, construída com o PINNeAPPle: você escreve a equação como texto, h vira um parâmetro treinável e a rede aprende o campo e h juntos. Cada caso vem com o script completo, preenchido com os seus dados: instalou o pacote, rodou, obteve a mesma resposta.",
        results=["Aleta 1D: h em cerca de 20 s, conferido com a solução analítica",
                 "Placa 2D: h = 14,8 ± 0,3 para um valor verdadeiro de 15; ponto quente a 79,2 °C contra 79,1 °C de um solver de volumes finitos independente",
                 "Bloco 3D: a temperatura do chip, que nenhum sensor alcança, sai a 74,6 °C contra 74,5 °C, só com termopares no topo"],
        limit=None),
    en=dict(
        tagline="From a handful of thermocouple readings to the heat-transfer coefficient h, the whole field and the temperatures nobody measured.",
        problem="h is the number every thermal calculation depends on, and nobody can measure it directly. Correlations typically promise ±25%. Thermocouples, on the other hand, are cheap.",
        how="A physics-informed neural network built with PINNeAPPle: you write the equation as text, h becomes a trainable parameter, and the network learns the field and h together. Every case comes with its complete script filled with your inputs: install the package, run it, get the same answer.",
        results=["1D fin: h in about 20 s, cross-checked against the analytic solution",
                 "2D plate: h = 14.8 ± 0.3 for a true 15; hot spot at 79.2 °C vs 79.1 °C from an independent finite-volume solver",
                 "3D block: the chip's temperature, which no sensor reaches, comes out at 74.6 °C vs 74.5 °C, from thermocouples on top only"],
        limit=None),
)

add(
    slug="heatsink-sizer", n=1, cat="thermal", name="HeatSink Sizer", image="01-heatsink-sizer.jpg", gallery=[],
    tags={"pt": ["Térmica", "Substituto neural"], "en": ["Thermal", "Neural surrogate"]},
    pt=dict(
        tagline="Dimensionamento de dissipadores de calor em segundos, com a confiança declarada.",
        problem="Dimensionar um dissipador costuma seguir o ritual de sempre: planilha, chute informado, simulação lenta, ajuste, simulação de novo.",
        how="Você informa a potência do componente, a temperatura máxima, o espaço disponível e o tipo de resfriamento (ar natural ou forçado). A ferramenta varre milhares de geometrias de aletas com um modelo substituto de rede neural treinado na física e confere o melhor candidato com correlações clássicas e publicadas de transferência de calor.",
        results=["Temperatura, perda de carga e margem térmica, com vista 3D do dissipador e do campo de temperatura",
                 "Física conferida contra métodos independentes da literatura, com concordância de 0 a 5%",
                 "Substituto com 4,5% de erro médio contra elementos finitos 3D, em casos que não viu no treino",
                 "Diz até onde o modelo merece confiança e o que ainda não cobre"],
        limit=None),
    en=dict(
        tagline="Heat-sink sizing in seconds, with the confidence stated.",
        problem="Sizing a heat sink usually goes the usual way: spreadsheet, educated guess, slow simulation, tweak, simulate again.",
        how="You enter the component's power, its maximum allowed temperature, the space available and the cooling mode (natural or forced air). The tool screens thousands of fin geometries with a neural surrogate trained on the physics and verifies the best candidate with published, classical heat-transfer correlations.",
        results=["Temperature, pressure drop and thermal margin, with a 3D view of the heat sink and its temperature field",
                 "Physics cross-checked against independent methods from the literature, agreeing within 0–5%",
                 "A surrogate with 4.5% mean error against 3D finite-element simulation, on cases it never saw in training",
                 "States how far the model can be trusted and what it doesn't cover yet"],
        limit=None),
)

add(
    slug="engineering-data-health", n=3, cat="data", name="Engineering Data Health", image="03-engineering-data-health.jpg", gallery=[],
    tags={"pt": ["Qualidade de dados", "Eficiência energética"], "en": ["Data quality", "Energy efficiency"]},
    pt=dict(
        tagline="Diagnóstico de dados de planta antes que eles contaminem qualquer modelo.",
        problem="Dados industriais parecem bons numa planilha e ainda assim quebram tudo adiante: um sensor congelado por seis horas, um −999 onde o logger perdeu o link, um medidor de vazão que derivou, uma coluna que trocou de °C para kelvin depois de uma atualização de firmware.",
        how="Sobe-se um CSV, Excel, Parquet, JSON ou HDF5. A ferramenta reconhece a grandeza física e a unidade de cada coluna pelo cabeçalho e verifica o tempo (buracos, duplicatas, relógio voltando), a física (valores abaixo do zero absoluto, umidade acima de 100%, códigos de erro, unidades trocadas), os sensores (congelados, com picos, saturados) e o balanço de energia ρ·V·cp·ΔT entre temperatura de suprimento e retorno, vazão e carga reportada, o que pega um medidor derivando que parece normal sozinho. Cada achado traz a evidência, a correção sugerida e uma nota de 0 a 100. Com os dados limpos, aprendizado de máquina simples (sem PINN) aprende como a potência da planta depende dos setpoints e recomenda ajustes dentro de limites seguros.",
        results=["Em uma semana de dados de uma planta de água gelada com 8 falhas injetadas de propósito, encontrou as 8; a mesma planta sem falhas recebe 99,8",
                 "Numa planta simulada com física conhecida, previu 8,3% de economia e o valor real era 9,0%; em mais 8 simulações, 9,8% previstos contra 9,7% reais"],
        limit="É uma estimativa do modelo a partir de dados históricos, não uma garantia: confirme com um teste A/B antes de automatizar."),
    en=dict(
        tagline="Plant-data diagnosis before it contaminates any model.",
        problem="Industrial datasets can look fine in a spreadsheet and still break everything downstream: a sensor frozen for six hours, a −999 where the logger lost its link, a flow meter that drifted, a column that quietly switched from °C to kelvin after a firmware update.",
        how="Upload a CSV, Excel, Parquet, JSON or HDF5 file. The tool recognises each column's physical quantity and unit from its header, then checks time (gaps, duplicates, clocks going backwards), physics (values below absolute zero, humidity above 100%, error codes, wrong or switching units), sensors (frozen, spiking, saturated) and the energy balance ρ·V·cp·ΔT between supply and return temperature, flow and reported load, which catches a drifting flow meter that looks perfectly normal on its own. Every finding comes with its evidence, a suggested fix and a score from 0 to 100. With clean data, plain machine learning (no PINNs) learns how plant power depends on the setpoints and recommends better setpoints within safe limits.",
        results=["On a week of chilled-water plant data with 8 faults injected on purpose, it found all 8; the same plant without faults scores 99.8",
                 "On a simulated plant with known physics, it predicted an 8.3% saving and the true figure was 9.0%; over 8 more simulations, 9.8% predicted against 9.7% true"],
        limit="It is a model estimate from historical data, not a guarantee: confirm with an A/B trial before automating."),
)

add(
    slug="engineering-data-standardizer", n=4, cat="data", name="Engineering Data Standardizer", image="04-data-standardizer.jpg", gallery=[],
    tags={"pt": ["Interoperabilidade", "Dados industriais"], "en": ["Interoperability", "Industrial data"]},
    pt=dict(
        tagline="Várias fontes, uma única tabela limpa, em UTC e com unidades coerentes.",
        problem="Um sistema de gestão predial exporta CSV em horário local, °C e vírgula decimal. Uma API SCADA devolve JSON com milissegundos Unix, °F, galões por minuto e toneladas de refrigeração. Uma bancada de teste grava Excel em kelvin, litros por segundo e watts. Antes de comparar, alguém gasta um dia em conversões e fusos. No mês seguinte, de novo.",
        how="Com até 8 arquivos, a ferramenta propõe o mapeamento de cada coluna (grandeza física, nome canônico, unidade-alvo), deixa você revisar e editar, converte tudo para um esquema único em UTC (métrico, SI ou unidades dos EUA) e confere se as fontes concordam onde duas delas medem a mesma coisa. A saída é CSV, Parquet ou HDF5 com as unidades nos metadados e um manifesto com cada conversão aplicada. O mapeamento revisado vira uma receita em JSON, reaplicável por API nas exportações seguintes.",
        results=["No exemplo, as 9 comparações entre fontes concordam após a conversão, com diferenças medianas de 0,01 a 0,04 na unidade-alvo",
                 "Quando um arquivo foi declarado no fuso errado, a ferramenta apontou: as séries casam melhor deslocadas em 3 horas"],
        limit="As unidades vêm dos cabeçalhos ou do seu mapeamento: um cabeçalho errado é convertido fielmente e errado. É exatamente por isso que existe a checagem de concordância."),
    en=dict(
        tagline="Many sources, one clean table, in UTC and with consistent units.",
        problem="A building management system exports CSV in local time, °C and decimal commas. A SCADA API returns JSON with Unix milliseconds, °F, gallons per minute and tons of refrigeration. A test rig writes Excel in kelvin, litres per second and watts. Before anyone can compare them, someone spends a day on conversions and time zones. Next month, they do it again.",
        how="With up to 8 files, the tool proposes a mapping for every column (physical quantity, canonical name, target unit), lets you review and edit it, converts everything to one schema in UTC (metric, SI or US units) and checks that the sources agree wherever two of them measure the same thing. Output is CSV, Parquet or HDF5 with the units stored in the metadata, plus a manifest listing every conversion applied. The mapping you reviewed is saved as a recipe (JSON), so the next exports go through an API call.",
        results=["In the example, all 9 cross-source comparisons agree after conversion, with median differences of 0.01 to 0.04 in the target unit",
                 "When one file was declared in the wrong time zone, the tool flagged it: the series match best when shifted by 3 hours"],
        limit="Units come from headers or from your mapping: a wrong header is converted faithfully, and wrongly. That is exactly why the agreement check exists."),
)

add(
    slug="simulation-metadata", n=5, cat="data", name="Simulation Metadata API", image="05-simulation-metadata.jpg", gallery=[],
    tags={"pt": ["CFD", "FEA", "Rastreabilidade"], "en": ["CFD", "FEA", "Traceability"]},
    pt=dict(
        tagline="Um registro estruturado de cada simulação: o que rodou e se convergiu.",
        problem="Meses depois de um estudo de CFD ou FEA, ninguém lembra qual malha, passo de tempo ou modelo de turbulência produziu um resultado, nem se a execução tinha de fato convergido. A resposta está espalhada em uma dúzia de arquivos de texto.",
        how="Sobe-se um caso OpenFOAM (zip), um deck CalculiX ou Abaqus com os arquivos de saída, ou um histórico de resíduos. A API devolve um registro estruturado com solver (aplicação, versão, tempo de execução), malha (células, qualidade, patches), passo de tempo (Δt, Courant, passos executados), condições de contorno de cada campo em cada patch (e cargas e apoios, no caso de FEA), parâmetros e numérica (viscosidade, velocidade de entrada, materiais, esquemas, tolerâncias) e um veredito de convergência com os motivos e o que fazer em seguida. Só lê os arquivos, nunca os executa.",
        results=["Testada em cinco execuções reais com OpenFOAM v1912 e CalculiX 2.21: um caso turbulento convergido (282 iterações), o mesmo caso cortado em 60 iterações (ainda caindo), um que divergiu com exceção de ponto flutuante após 5 iterações, uma cavidade transiente (completa, Courant máximo 0,85) e uma viga em balanço não linear (convergiu em 6 incrementos)",
                 "Os vereditos batem com o que o solver fez; as contagens de malha batem com o checkMesh",
                 "Flecha da ponta da viga lida do arquivo de saída, 7,58 mm, dentro de 1% do valor de Euler–Bernoulli, 7,62 mm",
                 "Serve para indexar um acervo de simulações, documentar um estudo ou garantir que cada amostra com que você treina um substituto vem de uma execução convergida"],
        limit="Resíduos estáveis não provam que grandezas como arrasto ou perda de carga estabilizaram. Fluent, STAR-CCM+ e SU2 são lidos, por ora, só pelo histórico de resíduos."),
    en=dict(
        tagline="A structured record of every simulation: what ran and whether it converged.",
        problem="Months after a CFD or FEA study, nobody remembers which mesh, time step or turbulence model produced a result, or whether the run had actually converged. The answer is scattered across a dozen text files.",
        how="Upload an OpenFOAM case (zip), a CalculiX or Abaqus deck with its output files, or a residual history. The API returns one structured record: solver (application, version, run time), mesh (cells, quality, patches), time stepping (Δt, Courant, steps actually run), boundary conditions (every field on every patch, plus loads and supports for FEA), parameters and numerics (viscosity, inlet velocity, materials, schemes, tolerances) and a convergence verdict with the reasons and what to do next. It only reads the files; it never runs them.",
        results=["Tested on five real runs made with OpenFOAM v1912 and CalculiX 2.21: a converged turbulent case (282 iterations), the same case cut at 60 iterations (still falling), one that diverged with a floating-point exception after 5 iterations, a transient cavity (completed, max Courant 0.85) and a nonlinear cantilever (converged in 6 increments)",
                 "The verdicts match what the solver did; mesh counts match checkMesh",
                 "Beam tip deflection read from the output file, 7.58 mm, within 1% of the Euler–Bernoulli value, 7.62 mm",
                 "Useful to index a simulation archive, document a study, or make sure every sample you train a surrogate on comes from a converged run"],
        limit="Flat residuals don't prove that quantities like drag or pressure drop have settled. Fluent, STAR-CCM+ and SU2 are read from their residual history only, for now."),
)

add(
    slug="simulation-preflight", n=8, cat="sim", name="Simulation Preflight", image="08-simulation-preflight.jpg", gallery=[],
    tags={"pt": ["CFD", "FEA", "Qualidade"], "en": ["CFD", "FEA", "Quality"]},
    pt=dict(
        tagline="Todos os problemas de um caso apontados antes de rodar a simulação.",
        problem="Quantas horas você já perdeu com uma simulação que rodou até o fim e estava errada desde o começo?",
        how="Sobe-se um caso OpenFOAM ou um deck CalculiX e recebe-se um checklist exportável com PASS, WARNING ou FAIL, o arquivo e a linha, por que importa e como corrigir.",
        results=["Viga sem apoios: o CalculiX diz “Job finished” e reporta um deslocamento de 1,8e11 mm; o Preflight marca FAIL",
                 "Unidades misturadas: a primeira frequência sai 0,16 Hz em vez de 209 Hz; o Preflight pega antes da execução"],
        limit=None),
    en=dict(
        tagline="Every problem in a case flagged before you run the simulation.",
        problem="How many hours have you lost to a simulation that ran to the end and was wrong from the start?",
        how="Upload an OpenFOAM case or a CalculiX deck and get an exportable checklist with PASS, WARNING or FAIL, the file and line, why it matters and how to fix it.",
        results=["A beam with no supports: CalculiX says \"Job finished\" and reports a displacement of 1.8e11 mm; Preflight flags it as FAIL",
                 "Mixed units: the first frequency comes out at 0.16 Hz instead of 209 Hz; Preflight catches it before the run"],
        limit=None),
)

add(
    slug="mesh-quality", n=9, cat="sim", name="Mesh Quality", image="09-mesh-quality.jpg", gallery=[],
    tags={"pt": ["Malha", "CFD", "FEA"], "en": ["Mesh", "CFD", "FEA"]},
    pt=dict(
        tagline="A malha é boa o bastante? E, se não, onde exatamente ela é ruim?",
        problem="Uma malha ruim custa uma execução do solver para você descobrir. Aqui você descobre em segundos, antes.",
        how="Aceita malhas OpenFOAM, Gmsh, VTK, Abaqus/CalculiX ou STL. Entrega as métricas de qualidade, histogramas, um mapa de calor 3D, os piores elementos, as regiões problemáticas e o que fazer em cada uma.",
        results=["Métricas de volumes finitos idênticas às do checkMesh do OpenFOAM (pitzDaily: skewness 0,260575, não ortogonalidade 5,95°)",
                 "Jacobiano escalado, skewness e razão de arestas para malhas de elementos finitos"],
        limit=None),
    en=dict(
        tagline="Is your mesh good enough, and if not, where exactly is it bad?",
        problem="A bad mesh costs a solver run to find out. Here you find out in seconds, before.",
        how="Upload an OpenFOAM, Gmsh, VTK, Abaqus/CalculiX or STL mesh. You get the quality metrics, histograms, a 3D heatmap, the worst elements, the problem regions and what to do about each.",
        results=["Finite-volume metrics identical to OpenFOAM's checkMesh (pitzDaily: skewness 0.260575, non-orthogonality 5.95°)",
                 "Scaled Jacobian, skewness and edge ratio for finite-element meshes"],
        limit=None),
)

add(
    slug="simulation-comparator", n=10, cat="sim", name="Simulation Comparator", image="10-simulation-comparator.jpg", gallery=[],
    tags={"pt": ["Verificação", "Validação"], "en": ["Verification", "Validation"]},
    pt=dict(
        tagline="Quão distantes estão dois resultados, campo a campo e ponto a ponto?",
        problem="Comparar uma simulação com outra, com um experimento ou com um modelo de IA costuma virar um script feito sob medida, e a comparação em malhas diferentes é a parte mais fácil de errar.",
        how="Referência contra candidato: simulação e simulação, simulação e experimento, simulação e IA, IA e experimento. A ferramenta devolve o erro global e por campo e um mapa de erro, mesmo quando as malhas são diferentes.",
        results=["Cavidade com tampa móvel contra Ghia et al.: de 1,26% para 0,19% de erro com o refinamento da malha",
                 "Uma PINN contra volumes finitos: 0,39% de erro (máximo de 0,67 °C)"],
        limit=None),
    en=dict(
        tagline="How far apart are two results, field by field and point by point?",
        problem="Comparing a simulation with another one, with an experiment or with an AI model usually turns into a one-off script, and comparing across different meshes is the easiest part to get wrong.",
        how="Reference vs candidate: simulation/simulation, simulation/experiment, simulation/AI, AI/experiment. The tool returns global and per-field error and an error map, even on different meshes.",
        results=["Lid-driven cavity vs Ghia et al.: error from 1.26% to 0.19% with mesh refinement",
                 "A PINN vs finite volumes: 0.39% error (max 0.67 °C)"],
        limit=None),
)

add(
    slug="interoperability-hub", n=12, cat="sim", name="Simulation Interoperability Hub", image="12-interoperability-hub.jpg", gallery=[],
    tags={"pt": ["Interoperabilidade", "CAE"], "en": ["Interoperability", "CAE"]},
    pt=dict(
        tagline="Resultados de simulação em um conjunto de dados neutro, sem perder as unidades.",
        problem="Um script por par de formatos, e as unidades se perdendo no caminho.",
        how="Sobe-se um resultado OpenFOAM, CalculiX, VTK ou Gmsh e recebe-se um conjunto de dados físico neutro: geometria, malha, campos com grandeza e unidade, e metadados. Dali exporta-se para VTK, HDF5, Parquet, CSV, NPZ, JSON ou um dataset do PINNeAPPle, pronto para treinar modelos.",
        results=["OpenFOAM para VTU, relido pelo VTK com o mesmo volume que o checkMesh reporta"],
        limit=None),
    en=dict(
        tagline="Simulation results in one neutral dataset, with the units kept.",
        problem="One script per pair of formats, and the units get lost on the way.",
        how="Upload an OpenFOAM, CalculiX, VTK or Gmsh result and get one neutral physical dataset: geometry, mesh, fields with quantity and unit, and metadata. Then export to VTK, HDF5, Parquet, CSV, NPZ, JSON or a PINNeAPPle dataset, ready to train models on.",
        results=["OpenFOAM to VTU, reread by VTK with the same volume checkMesh reports"],
        limit=None),
)

add(
    slug="model-lineage", n=11, cat="trace", name="Engineering Model Lineage", image="11-model-lineage.jpg", gallery=[],
    tags={"pt": ["Rastreabilidade", "Fio digital"], "en": ["Traceability", "Digital thread"]},
    pt=dict(
        tagline="Qual revisão da geometria gerou esta previsão?",
        problem="Quando um modelo de IA ou uma simulação dá um resultado, a pergunta que não pode ficar sem resposta é de onde ele veio: qual CAD, qual malha, qual execução, qual conjunto de dados.",
        how="Solta-se uma pasta de projeto e a ferramenta monta o fio digital: CAD, malha, simulação, conjunto de dados, modelo e previsão. Cada etapa carrega arquivo, versão, software, parâmetros, data, hash, responsável e origem. A saída exporta para W3C PROV-JSON.",
        results=["Detecta um arquivo que mudou depois de registrado, resultados mais velhos que seus insumos e conjuntos de dados que misturam revisões"],
        limit=None),
    en=dict(
        tagline="Which geometry revision produced this prediction?",
        problem="When an AI model or a simulation gives a result, the question that cannot go unanswered is where it came from: which CAD, which mesh, which run, which dataset.",
        how="Drop a project folder and the tool builds the digital thread: CAD, mesh, simulation, dataset, model, prediction. Each step carries its file, version, software, parameters, timestamp, hash, owner and origin. The output exports to W3C PROV-JSON.",
        results=["It catches a file that changed since it was recorded, results older than their inputs, and datasets that mix revisions"],
        limit=None),
)

add(
    slug="form-compiler", n=6, cat="trace", name="Form Compiler", image="06-form-compiler.jpg", gallery=[],
    tags={"pt": ["Documentos", "OCR", "Projeto de processo"], "en": ["Documents", "OCR", "Process design"]},
    pt=dict(
        tagline="Datasheets e especificações viram o formulário preenchido, com a fonte de cada valor.",
        problem="Já passou uma tarde inteira copiando números de cinco datasheets para um formulário só, para o fornecedor perguntar duas semanas depois porque dois deles discordavam?",
        how="Escolhe-se o formato do documento, soltam-se os datasheets e as especificações e o formulário sai compilado. Cada valor traz o documento, a página e o texto exato de onde foi lido. Conflitos entre documentos são apontados (vale o documento mais alto na sua lista, e os outros aparecem), e os itens obrigatórios que faltam são listados, para você saber a quem perguntar antes do fornecedor. PDFs escaneados são lidos por OCR, com as linhas de grade apagadas antes para que bordas de tabela não virem dígitos, e cada valor lido por OCR mostra sua confiança. As grandezas são comparadas em SI, com pressão manométrica e absoluta separadas.",
        results=["Formatos: vaso de pressão (preenche o formulário oficial ASME U-DR-1), válvula de alívio (dados API 520/526), trocador casco-e-tubo (TEMA/API 660, lado do casco e dos tubos), tanque de armazenamento (API 650) e bomba centrífuga (API 610)",
                 "Um LLM local opcional (Ollama) lê valores escritos em frases e roda no seu próprio servidor, então os documentos nunca saem dele",
                 "Uma resposta do LLM só é mantida se o texto que ele cita realmente está no documento e contém o valor"],
        limit=None),
    en=dict(
        tagline="Datasheets and specifications become the filled form, with the source of every value.",
        problem="Ever spent a whole afternoon copying numbers from five datasheets into one form, only to have the vendor ask a question two weeks later because two of them disagreed?",
        how="Pick the document format, drop the datasheets and specifications, and get the form compiled. Every value carries its source: document, page and the exact text it was read from. Conflicts between documents are flagged (the document higher in your list wins; the others are shown) and missing required items are listed, so you know whom to ask before the vendor does. Scanned PDFs are read with OCR (grid lines erased first, so table borders aren't read as digits), and each OCR value shows its confidence. Quantities are compared in SI, with gauge and absolute pressure kept apart.",
        results=["Formats: pressure vessel (it fills the official ASME U-DR-1 form), relief valve (API 520/526 data), shell-and-tube exchanger (TEMA/API 660, shell and tube side), storage tank (API 650) and centrifugal pump (API 610)",
                 "An optional local LLM (Ollama) reads values written in plain sentences and runs on your own server, so documents never leave it",
                 "An LLM answer is kept only if the text it quotes really is in the document and contains the value"],
        limit=None),
)

BY_SLUG = {p["slug"]: p for p in P}
HOME_HIGHLIGHTS = ["aircraft-design-optimizer", "pcb-hotspot", "inverse-heat-lab", "mesh-quality", "heatsink-sizer", "engineering-data-health"]
