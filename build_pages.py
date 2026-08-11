# -*- coding: utf-8 -*-
"""Generate static pages matching erdogant.github.io layout for Nana Safo Duker."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

NAV = [
    ("Home", "/"),
    ("Curriculum Vitae", "/cv/"),
    ("Research Projects", "/publications/"),
    ("Blogs", "/blogs/"),
    ("Certifications", "/certifications/"),
    ("Workshops & Conferences", "/workshops/"),
    ("Contact", "/contact/"),
]

BIO = "Founder &amp; CEO of GeneHus<br>Computational Researcher"
EMAIL = "safoduker@genehus.bio"
SITE = "https://genehus.bio"
GITHUB = "https://github.com/Nana-Safo-Duker"
LINKEDIN = "https://www.linkedin.com/in/nana-safo-duker-0aa25227a/"
MEDIUM = "https://medium.com/@freshsafoduker300"
ORCID = "0009-0002-2472-8103"
ORCID_URL = f"https://orcid.org/{ORCID}"
NAME = "Nana Safo Duker"


def depth_prefix(rel_path: str) -> str:
    # rel_path like "index.html" or "cv/index.html"
    depth = rel_path.count("/")
    return "../" * depth if depth else "./"


def page(rel_path: str, title: str, heading: str, body: str, description: str = "", page_class: str = "") -> None:
    prefix = depth_prefix(rel_path)
    desc = description or f"{heading} | {NAME}"
    nav_items = []
    for label, url in NAV:
        href = prefix.rstrip("/") + url if url != "/" else (prefix if prefix != "./" else "./")
        if url == "/":
            href = f"{prefix}index.html" if prefix != "./" else "index.html"
        else:
            href = f"{prefix}{url.strip('/')}/index.html"
        nav_items.append(f'				    <li><a href="{href}">{label}</a></li>')

    home_href = f"{prefix}index.html" if prefix != "./" else "index.html"
    photo = f"{prefix}images/bio-photo.png"
    logo = f"{prefix}images/genehus-mark.png?v=20260811d"
    logo_full = f"{prefix}images/genehus-logo.png?v=20260811d"
    css = f"{prefix}css/site.css?v=20260811d"
    js = f"{prefix}js/nav.js?v=20260811d"
    article_class = f"page {page_class}".strip() if page_class else "page"

    html = f"""<!doctype html>
<html class="no-js" lang="en">
<head>
<meta charset="utf-8">
<title>{title} &#8211; {NAME}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{NAME}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="dark">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{css}">
</head>
<body class="js">
<header class="site-header">
  <div class="navigation-wrapper">
	<div class="site-name">
		<a href="{home_href}">{NAME}</a>
	</div>
	<div class="top-navigation">
		<nav role="navigation" id="site-nav" class="nav">
		    <button type="button" class="navtoggle navicon-lines-button x" aria-label="Menu">
		      <span class="navicon-lines"></span>
		    </button>
		    <ul>
{chr(10).join(nav_items)}
		    </ul>
		</nav>
	</div>
  </div>
  <div class="nav-accent" aria-hidden="true">
    <span class="nav-accent__orange"></span>
    <span class="nav-accent__gray"></span>
  </div>
</header>

<div id="main" role="main">
  <div class="article-author-side">
    <div itemscope itemtype="https://schema.org/Person">
      <img src="{photo}?v=20260811d" class="bio-photo" alt="{NAME} bio photo" width="150" height="150">
      <h3 itemprop="name">{NAME}</h3>
      <p>{BIO}</p>
      <a href="mailto:{EMAIL}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-envelope-square"></i> Email</a>
      <a href="{SITE}" class="author-social author-social--genehus" target="_blank" rel="noopener"><img src="{logo}" alt="GeneHus" class="genehus-logo-icon"> GeneHus</a>
      <a href="{ORCID_URL}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-certificate"></i> Orcid</a>
      <a href="{LINKEDIN}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-linkedin-square"></i> LinkedIn</a>
      <a href="{GITHUB}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-github"></i> Github</a>
      <a href="{MEDIUM}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-medium"></i> Medium</a>
    </div>
  </div>

  <div class="article-author-bottom">
    <div itemscope itemtype="https://schema.org/Person">
      <img src="{photo}?v=20260811d" class="bio-photo" alt="{NAME} bio photo" width="150" height="150">
      <h3 itemprop="name">{NAME}</h3>
      <p>{BIO}</p>
      <a href="mailto:{EMAIL}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-envelope-square"></i> Email</a>
      <a href="{SITE}" class="author-social author-social--genehus" target="_blank" rel="noopener"><img src="{logo}" alt="GeneHus" class="genehus-logo-icon"> GeneHus</a>
      <a href="{ORCID_URL}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-certificate"></i> Orcid</a>
      <a href="{LINKEDIN}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-linkedin-square"></i> LinkedIn</a>
      <a href="{GITHUB}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-github"></i> Github</a>
      <a href="{MEDIUM}" class="author-social" target="_blank" rel="noopener"><i class="fa fa-fw fa-medium"></i> Medium</a>
    </div>
  </div>

  <article class="{article_class}">
    <h1>{heading}</h1>
    <div class="article-wrap">
{body}
    </div>
  </article>
</div>

<div class="footer-wrap">
  <footer>
    <div class="site-footer">
      <span class="site-footer__links"><a href="{SITE}">GeneHus</a> &middot; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
      <hr class="site-footer__bar" />
      <span class="site-footer__copy">&copy; 2026 {NAME}.</span>
    </div>
  </footer>
</div>
<script src="{js}"></script>
</body>
</html>
"""
    out = ROOT / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", rel_path)


HOME = """
      <p>
        I’m a computational researcher in AI/ML and data science, building data-driven models for cancer genomics, precision medicine, infectious disease dynamics, digital health systems, and climate-health analytics.
      </p>
      <p>
        My work integrates machine learning, statistical modeling, and cloud technologies to support biomarker discovery, scalable analytics, and deployable health innovations.
      </p>
      <p>
        My interests lie in integrating biomedical and environmental data to support more proactive, resilient, and equitable healthcare systems.
      </p>
      <p>
        I’m committed to the ethical and responsible use of AI to drive equitable, transparent, and impactful solutions in global health.
      </p>
      <p class="founder-statement">
        <span class="founder-statement__role">Founder | CEO</span>
        <span class="founder-statement__brand">
          <a href="https://genehus.bio" target="_blank" rel="noopener" class="founder-statement__brand-link">
            <img src="./images/genehus-logo.png?v=20260811d" alt="GeneHus" class="genehus-logo-full">
          </a>
        </span>
        <a class="founder-statement__email" href="mailto:safoduker@genehus.bio">safoduker@genehus.bio</a>
      </p>
"""

CV = """
      <p class="cv-subtitle">AI/ML | Data Science | Bioinformatics | Infectious Disease Modeling | Climate &amp; Energy Analytics | AI Law</p>
      <hr />
      <h2>About Me</h2>
      <p>I am a Computational researcher developing AI-driven predictive and analytical systems across bioinformatics, precision medicine, infectious disease modeling, climate and energy analytics, and responsible AI.</p>
      <hr />
      <h2>Skills</h2>
      <ul class="cv-skills">
        <li>Artificial Intelligence</li>
        <li>Machine Learning</li>
        <li>Data Science</li>
        <li>R Programming</li>
        <li>Python</li>
        <li>Climate Health</li>
        <li>Energy Analytics</li>
        <li>Cancer Genomics</li>
        <li>Infectious Disease Modeling</li>
        <li>Version Control</li>
        <li>Statistical Modeling</li>
        <li>Bioinformatics</li>
        <li>Cloud Computing</li>
        <li>Digital Health</li>
        <li>AI Governance</li>
      </ul>
      <hr />
      <h2>Research Interests</h2>
      <ul class="cv-interests">
        <li>Bioinformatics &amp; Precision Medicine</li>
        <li>Artificial Intelligence &amp; Machine Learning</li>
        <li>Infectious Disease Modeling &amp; Epidemiology</li>
        <li>Clinical Health Data Analytics</li>
        <li>Climate &amp; Energy Analytics</li>
        <li>Responsible AI &amp; Digital Governance</li>
        <li>Predictive Analytics &amp; Decision Intelligence</li>
        <li>Cloud Computing &amp; Data Engineering</li>
      </ul>
      <hr />
      <h2>Current Focus</h2>
      <p class="cv-focus-title"><i class="fa fa-flask" aria-hidden="true"></i> <strong>AI-Powered Genomic Diagnostics for Prostate Cancer</strong></p>
      <p>Developing machine learning systems for genomic interpretation, biomarker discovery, mutation impact prediction, and precision oncology applications.</p>
"""

PUBLICATIONS = """
      <div class="projects-grid">
        <article class="project-card">
          <h3>AI/ML Bioinformatics &amp; Precision Medicine - Integrated, Multi-Omics Project Portfolio</h3>
          <p>
            A curated multi-project lab of reproducible AI/ML and statistical genomics workflows. Each project is a complete pipeline focused on a specific precision medicine problem—from variant pathogenicity prediction and transcription-factor binding modeling to gene expression inference and biomarker discovery.
          </p>
          <p>This portfolio integrates:</p>
          <ul>
            <li>Deep learning architectures (CNNs, RNNs, Transformers) for genomic sequence analysis</li>
            <li>Statistical genetics and biostatistical modeling for population-level insights</li>
            <li>Explainable machine learning to interpret biological mechanisms</li>
            <li>Cloud-ready, scalable bioinformatics pipelines</li>
            <li>Clinical data science methodologies aligned with real-world healthcare applications</li>
          </ul>
          <p>
            Together, these projects demonstrate an end-to-end approach to next-generation precision medicine—combining data-driven insight, biological interpretability, and clinical relevance.
          </p>
          <a href="https://github.com/Nana-Safo-Duker/AI-ML-Bioinformatics_Precision-Medicine" target="_blank" rel="noopener" class="btn">View Portfolio →</a>
        </article>

        <article class="project-card">
          <h3>Data Science &amp; Predictive Analytics - Multi-Domain Project Portfolio</h3>
          <p>
            A collection of end-to-end analytics projects spanning real-world domains including marketing analytics, customer intelligence, cybersecurity, NLP, HR insights, fraud detection, energy analysis, ML education, compensation science, and startup analytics.
          </p>
          <p>Each project is built using a consistent, reproducible workflow:</p>
          <ol>
            <li>Data Cleaning &amp; Feature Engineering</li>
            <li>Exploratory Data Analysis (EDA)</li>
            <li>Predictive Modeling (ML, statistical modeling, or NLP)</li>
            <li>Insight Generation &amp; Communication</li>
          </ol>
          <p>
            The structure makes it easy to open any folder, understand the problem, run the notebook/script, and reproduce the full workflow. It’s both a practical learning resource and a demonstration of applied data science across diverse, high-impact domains.
          </p>
          <a href="https://github.com/Nana-Safo-Duker/Data-Science-Predictive-Analytics" target="_blank" rel="noopener" class="btn">View Portfolio →</a>
        </article>

        <article class="project-card">
          <h3>Clinical Data Science &amp; Health Analytics - Translational AI in Public Health Portfolio</h3>
          <p>
            A curated set of clinical data science and health analytics projects demonstrating real-world applications of machine learning, statistical modeling, and evidence-based analysis across healthcare. Projects span disease prediction and risk stratification, treatment adherence modeling, patient behavior analysis, and population-level health insights.
          </p>
          <p>The portfolio includes:</p>
          <ul>
            <li>End-to-end predictive modeling pipelines for chronic disease, metabolic conditions, and clinical outcomes</li>
            <li>Risk scoring systems and stratification frameworks inspired by real-world clinical decision support tools</li>
            <li>Behavioral and lifestyle analytics that surface patient-level patterns influencing disease progression</li>
            <li>Treatment initiation and adherence modeling, plus data cleaning, feature engineering, and statistical validation for replicable, interpretable insights</li>
          </ul>
          <p>
            Each project is organized for reuse and reproducibility, with clear structure, well-documented analysis steps, and modular code aligned with best practices in clinical AI and health informatics.
          </p>
          <a href="https://github.com/Nana-Safo-Duker/Clinical-Data-Science-Health-Analytics" target="_blank" rel="noopener" class="btn">View Portfolio →</a>
        </article>

        <article class="project-card">
          <h3>Infectious Disease Modelling &amp; Epidemiology - Computational Transmission &amp; Intervention Analytics Portfolio</h3>
          <p>
            A focused infectious disease modelling portfolio that turns transmission questions into reproducible code—pairing compartmental and stochastic perspectives with intervention-style analyses so dynamics can be explored before real-world deployment.
          </p>
          <p>Key capabilities:</p>
          <ul>
            <li>Python, R, shell, and Jupyter-friendly workflows sized for transparent assumptions and iterative experimentation</li>
            <li>Transmission modelling motifs suited to vector-borne contexts such as malaria and related scenario exploration</li>
            <li>Modular repository layout so methods can extend to additional pathogens or geographical settings</li>
            <li>Open, version-controlled artifacts aligned with reproducibility expectations in computational epidemiology</li>
          </ul>
          <p>
            The portfolio bridges mechanistic intuition with simulation discipline—stress-testing hypotheses with documented pipelines rather than one-off scripts.
          </p>
          <a href="https://github.com/Nana-Safo-Duker/Infectious-Disease-Modelling_Epidemiology-Portfolio" target="_blank" rel="noopener" class="btn">View Portfolio →</a>
        </article>

        <article class="project-card">
          <h3>Computational Biomedical Research - Integrated Imaging, Sequence &amp; Oncology AI Portfolio</h3>
          <p>
            A multi-project computational biomedical laboratory spanning neurological signal analytics from eye-movement data, retinal-image cardiovascular risk stratification, DNA sequence–based gene expression modeling, oncology genomics and radiomics, ultrasound-informed hepatology analytics, microscopy cell phenotyping, and AI-guided drug and cancer-target discovery.
          </p>
          <p>Key capabilities:</p>
          <ul>
            <li>Deep learning and classical ML stacks with diagnostics oriented toward interpretability and clinical relevance</li>
            <li>Imaging and sequence pipelines—from CNN-style fundus workflows to radiomics, ultrasound tasks, and sequence encoders</li>
            <li>Robust feature engineering, statistical validation, and artifact exports that keep experiments auditable</li>
            <li>Standalone project folders with notebooks and scripts that preserve reproducible structure end-to-end</li>
          </ul>
          <p>
            Together these workflows show how modern ML can stay disciplined for biomedical rigor—from discovery through transparent evaluation and reporting.
          </p>
          <a href="https://github.com/Nana-Safo-Duker/Computational_Biomedical_Research-Portfolio" target="_blank" rel="noopener" class="btn">View Portfolio →</a>
        </article>

        <article class="project-card">
          <h3>Climate, Energy &amp; Green Microbiology - Forecasting, Renewables &amp; Sustainable Systems Portfolio</h3>
          <p>
            A climate and energy intelligence portfolio spanning AI-assisted global weather forecasting, renewable optimization under climate variability, electricity pricing strategies, load and demand forecasting, extreme-event risk modeling, reinforcement learning for energy systems control, and sustainable transition scenarios—including datasets and narratives aligned with green biotechnology contexts where climate intersects microbiology.
          </p>
          <p>Key capabilities:</p>
          <ul>
            <li>Time-series and probabilistic forecasting layered with deep learning and graph-inspired atmospheric models</li>
            <li>Climate-informed renewable yield and planning analytics grounded in realistic variability assumptions</li>
            <li>Electricity market–aware modeling for price, dispatch, and volatility-aware decision support</li>
            <li>Scenario-centric tooling for decarbonization pathways and resilient infrastructure planning</li>
          </ul>
          <p>
            The collection frames sustainability challenges as forecasting and operations problems—pairing disciplined data governance with models stakeholders can inspect and extend.
          </p>
          <a href="https://github.com/Nana-Safo-Duker/Climate_Energy_GreenMicrobiology-Portfolio" target="_blank" rel="noopener" class="btn">View Portfolio →</a>
        </article>
      </div>
"""

BLOGS = """
      <div class="blogs-grid">
        <article class="blog-card">
          <h3>🩺 Predicting Cancer Outcomes with Radiomics and AI in Radiology</h3>
          <p>
            Quantitative imaging biomarkers and machine learning for precision oncology: how radiomics and AI extract prognostic signals from medical images
            to help tailor treatment, identify high-risk patients, and support personalized cancer care.
          </p>
          <a href="https://medium.com/@freshsafoduker300/predicting-cancer-outcomes-with-radiomics-and-ai-in-radiology-87651eedf701" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>🛰️ From Satellites to Predictions: Machine Learning for Malaria Outbreak Forecasting</h3>
          <p>
            A spatio-temporal AI framework for translating climate data into actionable disease surveillance—linking rainfall, temperature, humidity, and vegetation
            to mosquito-driven malaria transmission and outbreak timing.
          </p>
          <a href="https://medium.com/@freshsafoduker300/from-satellites-to-predictions-machine-learning-for-malaria-outbreak-forecasting-266e0f1c3cab" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>⚠️ Every AI Tool Is Also a Potential Weapon</h3>
          <p>
            How the first major study on malicious AI use foresaw today’s dual-use reality—and why generative models turned a known risk into a mass-access problem
            that benefits alone cannot explain away.
          </p>
          <a href="https://medium.com/@freshsafoduker300/every-ai-tool-is-also-a-potential-weapon-730b3dfc7f1d" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>📊 Making Sense of Health Signals: A Machine Learning Approach to Digital Epidemiology</h3>
          <p>
            Statistical learning for noisy time-series analysis, hypothesis testing, and early disease signal detection in digital epidemiology.
            Explores how machine learning can extract actionable surveillance signals from imperfect health data—supporting proactive public health
            response before outbreaks fully materialize.
          </p>
          <a href="https://medium.com/@freshsafoduker300/making-sense-of-health-signals-a-machine-learning-approach-to-digital-epidemiology-f41e6cd3b3bb" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>🧬 Genomic Data to Clinical Insight: Deep Learning Models for Cancer Type Prediction</h3>
          <p>
            A computational pipeline linking high-dimensional gene expression to diagnostic classification: normalization, variance-based feature selection,
            neural network modeling, and statistically grounded evaluation. Demonstrates how deep learning transforms raw genomic measurements into
            clinically relevant cancer type predictions—with links to reproducible portfolio work in computational oncology.
          </p>
          <a href="https://medium.com/@freshsafoduker300/genomic-data-to-clinical-insight-deep-learning-models-for-cancer-type-prediction-9252ce4253d5" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>⚖️ The Politics of Climate Change: Why Justice Can't Be Optional</h3>
          <p>
            A just transition is not only about cutting emissions—it requires fairness, dignity, and equity for people and planet. Synthesizes climate,
            energy, and environmental justice within SDG and Paris Agreement contexts, arguing that equity must be embedded in policy design rather than
            appended after technical decarbonization plans.
          </p>
          <a href="https://medium.com/@freshsafoduker300/the-politics-of-climate-change-why-justice-cant-be-optional-479940b00a2b" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>🌍 Why Smarter Algorithms Can Still Fail the Climate</h3>
          <p>
            A governance-focused essay on climate machine learning: why benchmark accuracy and innovation narratives are not enough when models sit inside electricity markets, supply chains, and institutions with misaligned incentives. Draws on high-impact ML-for-climate surveys and argues for auditable standards, independent evaluation, and outcome-based accountability—not just better predictions.
          </p>
          <a href="https://medium.com/@freshsafoduker300/why-smarter-algorithms-can-still-fail-the-climate-67977fd5b46f" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>🛰️ Graph Neural Networks for Weather Forecasting: A Critical Analysis of GraphCast</h3>
          <p>
            A structured review of graph neural networks for medium-range global weather prediction, centered on the GraphCast paradigm: graph formulation, training on reanalysis data, skill versus NWP baselines, and open questions around uncertainty, extremes, and robustness under climate shift—with links to reproducible portfolio work on AI-based global forecasting.
          </p>
          <a href="https://medium.com/@freshsafoduker300/graph-neural-networks-for-weather-forecasting-a-critical-analysis-of-graphcast-576eba6af296" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>🔮 A Bayesian Machine Learning Framework for Modeling Infectious Disease Outbreaks</h3>
          <p>
            Describes a Bayesian ML pipeline for epidemic time series: feature construction, probabilistic count models, posterior inference, and posterior predictive forecasts that expose uncertainty—contrasted with deterministic single-point predictions—plus discussion of strengths, limits, and links to an open implementation for outbreak prediction.
          </p>
          <a href="https://medium.com/@freshsafoduker300/a-bayesian-machine-learning-framework-for-modeling-infectious-disease-outbreaks-12fc4c05ac86" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>🏛️ AI Is Moving Faster Than Governments Can Respond</h3>
          <p>
            An AI governance essay distinguishing technical safety from institutional governance: anticipatory regulation, capacity gaps, voluntary “responsible AI” versus enforceable accountability, and concrete mechanisms—risk-tiered rules, audit infrastructure, and international coordination—grounded in leading policy and FAccT-era literature.
          </p>
          <a href="https://medium.com/@freshsafoduker300/ai-is-moving-faster-than-governments-can-respond-4fd7c0785d88" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>♻️ Can AI Fight Climate Change Without Worsening It?</h3>
          <p>
            Explores the tension between AI as climate infrastructure (grids, disasters, land use) and the hidden environmental cost of compute, hardware, and rebound effects; argues for lifecycle disclosure, impact assessment, equity in deployment, and governance that rewards verified emissions outcomes rather than green narratives alone.
          </p>
          <a href="https://medium.com/@freshsafoduker300/can-ai-fight-climate-change-without-worsening-it-617762bc9261" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>👁️ Wearable Sensors for Brain Disorder Detection Through Eye Movements: A Comprehensive Research Review</h3>
          <p>
            How eye-tracking wearables are transforming neurological diagnostics from Parkinson's to Alzheimer's.
            This research review examines innovative wearable, high resolution eye movement sensors capable of detecting
            neurological disorders in real time, potentially reshaping how clinicians screen for conditions like Parkinson's disease,
            Alzheimer's disease, concussion, and traumatic brain injury.
          </p>
          <a href="https://medium.com/@freshsafoduker300/wearable-sensors-for-brain-disorder-detection-through-eye-movements-a-comprehensive-research-86071018ef6c" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>🦟 Simulating and Fitting Malaria Transmission Model in Madagascar: Impact of Insecticide-Treated Nets</h3>
          <p>
            An applied research post on modeling disease transmission and evaluating ITN interventions using R.
            This study investigates the epidemiological impact of ITNs under varying resistance scenarios using a modified
            Susceptible, Infected, Recovered (SIR) model with integrated vector dynamics, simulating malaria transmission
            in Madagascar and comparing outcomes across different intervention scenarios.
          </p>
          <a href="https://medium.com/@freshsafoduker300/simulating-and-fitting-malaria-transmission-model-in-madagascar-impact-of-insecticide-treated-nets-fd9c10d4cda4" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>🧬 Predicting Gene Expression from DNA Sequence Using Deep Learning Models</h3>
          <p>
            A breakthrough in computational biology exploring how advanced neural network architectures can learn the complex
            regulatory grammar embedded in DNA. This research demonstrates how artificial intelligence can decipher how genes
            are turned on or off a feat with profound implications for precision medicine, functional genomics, and therapeutic innovation.
          </p>
          <a href="https://medium.com/@freshsafoduker300/predicting-gene-expression-from-dna-sequence-using-deep-learning-models-1b612908bb9c" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
        <article class="blog-card">
          <h3>📘 From Retina to Risk: Predicting Cardiovascular Health Through Deep Learning</h3>
          <p>
            A comprehensive analysis of <em>Nature Biomedical Engineering (2018)</em>, exploring how retinal imaging and deep learning
            can predict systemic cardiovascular health. Highlights AI's role in early disease detection and precision health,
            demonstrating that deep learning models can predict key cardiovascular risk factors directly from retinal fundus photographs.
          </p>
          <a href="https://medium.com/@freshsafoduker300/from-retina-to-risk-predicting-cardiovascular-health-through-deep-learning-c24f6ac58646" target="_blank" rel="noopener" class="btn">Read Article →</a>
        </article>
      </div>
"""

CERTIFICATIONS = """
      <p class="cred-intro">Selected professional certifications in genomics, precision medicine, bioinformatics, data science, and AI law.</p>
      <ul class="cred-list">
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Big Data, Genes, and Medicine</h3>
            <p class="cred-meta">Coursera · The State University of New York · May 2024</p>
          </div>
          <a class="cred-link" href="files/big-data-genes-and-medicine.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Precision Medicine</h3>
            <p class="cred-meta">Coursera · University of Geneva · May 2024</p>
          </div>
          <a class="cred-link" href="files/precision-medicine.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Data Science in Stratified Healthcare and Precision Medicine</h3>
            <p class="cred-meta">Coursera · The University of Edinburgh · May 2024</p>
          </div>
          <a class="cred-link" href="files/data-science-stratified-healthcare-precision-medicine.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>The Data Science of Healthcare, Medicine and Public Health</h3>
            <p class="cred-meta">LinkedIn Learning · Apr 2024</p>
          </div>
          <a class="cred-link" href="files/data-science-healthcare-medicine-public-health.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Python for Health Sciences and Healthcare</h3>
            <p class="cred-meta">LinkedIn Learning · Apr 2024</p>
          </div>
          <a class="cred-link" href="files/python-for-health-sciences-healthcare.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Access Bioinformatics Databases with Biopython</h3>
            <p class="cred-meta">Coursera Project Network · May 2024</p>
          </div>
          <a class="cred-link" href="files/access-bioinformatics-databases-biopython.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Computing for Cancer Informatics</h3>
            <p class="cred-meta">Coursera · Johns Hopkins University · May 2024</p>
          </div>
          <a class="cred-link" href="files/computing-for-cancer-informatics.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Introduction to Genomic Technologies</h3>
            <p class="cred-meta">Coursera · Johns Hopkins University · May 2024</p>
          </div>
          <a class="cred-link" href="files/introduction-to-genomic-technologies.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Introduction to the Biology of Cancer</h3>
            <p class="cred-meta">Coursera · Johns Hopkins University · May 2024 · With Honors</p>
          </div>
          <a class="cred-link" href="files/introduction-to-biology-of-cancer.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Understanding Cancer Metastasis</h3>
            <p class="cred-meta">Coursera · Johns Hopkins University · May 2024</p>
          </div>
          <a class="cred-link" href="files/understanding-cancer-metastasis.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Understanding Prostate Cancer</h3>
            <p class="cred-meta">Coursera · Johns Hopkins University · Apr 2024</p>
          </div>
          <a class="cred-link" href="files/understanding-prostate-cancer.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>AI &amp; Law</h3>
            <p class="cred-meta">Coursera · Lund University · Apr 2024</p>
          </div>
          <a class="cred-link" href="files/ai-and-law.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Genomics for Law</h3>
            <p class="cred-meta">Coursera · University of Illinois at Urbana-Champaign · Apr 2024</p>
          </div>
          <a class="cred-link" href="files/genomics-for-law.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Legal Tech and the Digital Transformation of Law</h3>
            <p class="cred-meta">Coursera · Universidad Austral · Apr 2024</p>
          </div>
          <a class="cred-link" href="files/legal-tech-digital-transformation-of-law.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>International Webinar Series for Life Scientists</h3>
            <p class="cred-meta">Genomac Institute Inc. · Genomics, Bioinformatics &amp; Data Science · Jan 2025</p>
          </div>
          <a class="cred-link" href="files/international-webinar-series-life-scientists.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
      </ul>
"""

WORKSHOPS = """
      <p class="cred-intro">Selected workshops, faculty development programmes, and conference participation in AI/ML, computational biology, data science, and research methods.</p>
      <ul class="cred-list">
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>High Performance Computing and AI for Computational Biology</h3>
            <p class="cred-meta">Workshop · IIT Kharagpur &amp; Tezpur University · National Supercomputing Mission · Oct 2021</p>
          </div>
          <a class="cred-link" href="files/hpc-ai-computational-biology-iit-kharagpur.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Workshop on Python Programming</h3>
            <p class="cred-meta">Workshop · Dr. M.G.R. Educational and Research Institute · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/workshop-python-programming.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Practical Debugging for Data Science</h3>
            <p class="cred-meta">Webinar · Government Engineering College, Rajkot · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/practical-debugging-for-data-science.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Research Perspective on Artificial Intelligence and Machine Learning</h3>
            <p class="cred-meta">Webinar · Centre for Distance and Online Education · Apr 2022</p>
          </div>
          <a class="cred-link" href="files/research-perspective-ai-ml.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>The Role of Linear Algebra in Machine Learning, AI &amp; Data Science</h3>
            <p class="cred-meta">International FDP · Mahatma Gandhi Institute of Technology · Nov–Dec 2021</p>
          </div>
          <a class="cred-link" href="files/linear-algebra-ml-ai-data-science-fdp.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Research Issues in Machine Learning and Artificial Intelligence</h3>
            <p class="cred-meta">FDP · Pollachi College of Arts and Science · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/research-issues-ml-ai-fdp.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Cloud Computing for Industry 4.0</h3>
            <p class="cred-meta">National Level Online FDP · Institute of Aeronautical Engineering · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/cloud-computing-industry-4-fdp.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Biomaterials and Tissue Engineering</h3>
            <p class="cred-meta">BPI Mini-Symposium · IIT Madras · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/biomaterials-tissue-engineering-iit-madras.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>A Systematic Navigation from Research to Research Proposals 2.0</h3>
            <p class="cred-meta">National Level Online FDP · MVSR Engineering College · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/research-to-research-proposals-fdp.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Research Methodology</h3>
            <p class="cred-meta">National Level Workshop · D.G. Vaishnav College · 2021</p>
          </div>
          <a class="cred-link" href="files/research-methodology-workshop.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>New Gen Cyber Crimes</h3>
            <p class="cred-meta">Webinar · C-DAC Hyderabad · Apr 2022</p>
          </div>
          <a class="cred-link" href="files/new-gen-cyber-crimes-cdac.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Innovation in Cyber Security using Image Steganography</h3>
            <p class="cred-meta">International Webinar · Maharishi Markandeshwar University · Apr 2022</p>
          </div>
          <a class="cred-link" href="files/cyber-security-image-steganography.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>Cybercrime and Information Technology Act</h3>
            <p class="cred-meta">National Level Webinar · St. Joseph’s College of Arts &amp; Science · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/cybercrime-and-it-act.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>International Webinar on Applied Research</h3>
            <p class="cred-meta">Webinar · Bharata Mata College / M.G. University · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/international-webinar-applied-research.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>The Role of Fourier Analysis in Signal Processing</h3>
            <p class="cred-meta">International Seminar · Mangayarkarasi College of Arts and Science · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/fourier-analysis-signal-processing.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
        <li class="cred-item">
          <div class="cred-item__body">
            <h3>International Conference on Numerical and Analytical Techniques in Differential Equations (ICNATDE-2021)</h3>
            <p class="cred-meta">Conference · Pondicherry University · Nov 2021</p>
          </div>
          <a class="cred-link" href="files/icnatde-2021-differential-equations.pdf" target="_blank" rel="noopener">View Certificate</a>
        </li>
      </ul>
"""

CONTACT = """
      <p class="contact-links">
        <a href="mailto:safoduker@genehus.bio"><i class="fa fa-envelope"></i> safoduker@genehus.bio</a>
        <a href="https://genehus.bio" target="_blank" rel="noopener" class="author-social--genehus"><img src="../images/genehus-mark.png?v=20260811d" alt="GeneHus" class="genehus-logo-icon"> GeneHus</a>
        <a href="https://orcid.org/0009-0002-2472-8103" target="_blank" rel="noopener"><i class="fa fa-certificate"></i> Orcid</a>
        <a href="https://github.com/Nana-Safo-Duker" target="_blank" rel="noopener"><i class="fa fa-github"></i> GitHub</a>
        <a href="https://www.linkedin.com/in/nana-safo-duker-0aa25227a/" target="_blank" rel="noopener"><i class="fa fa-linkedin"></i> LinkedIn</a>
        <a href="https://medium.com/@freshsafoduker300" target="_blank" rel="noopener"><i class="fa fa-medium"></i> Medium</a>
      </p>
      <p>For collaboration, research inquiries, or questions about <a href="https://genehus.bio" target="_blank" rel="noopener">GeneHus</a>, email <a href="mailto:safoduker@genehus.bio">safoduker@genehus.bio</a>.</p>
"""


def main():
    page("index.html", NAME, NAME, HOME, "AI/ML & Bioinformatics Research Portfolio")
    page("cv/index.html", "Curriculum Vitae", "Nana Safo Duker", CV, page_class="cv-page")
    page("publications/index.html", "Research Projects Portfolio", "Research Projects Portfolio", PUBLICATIONS, page_class="projects-page")
    page("blogs/index.html", "Articles & Blogs", "Articles & Blogs", BLOGS, page_class="blogs-page")
    page("certifications/index.html", "Certifications", "Certifications", CERTIFICATIONS, page_class="creds-page")
    page("workshops/index.html", "Workshops & Conferences", "Workshops & Conferences", WORKSHOPS, page_class="creds-page")
    page("contact/index.html", "Contact", "Contact", CONTACT)


if __name__ == "__main__":
    main()
