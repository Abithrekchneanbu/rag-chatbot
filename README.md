<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>RAG Chatbot — README</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/tabler-icons.min.css"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet"/>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#07090f;--surface:#0d1117;--surface2:#131820;
  --border:rgba(99,179,237,0.12);--accent:#63b3ed;--accent2:#9f7aea;--accent3:#68d391;
  --text:#e2e8f0;--muted:#718096;--glow:rgba(99,179,237,0.18);
  --b-blue-bg:#e6f1fb;--b-blue-bd:#378add;--b-blue-tx:#0c447c;
  --b-purple-bg:#eeedfe;--b-purple-bd:#7f77dd;--b-purple-tx:#3c3489;
  --b-green-bg:#eaf3de;--b-green-bd:#639922;--b-green-tx:#27500a;
  --b-amber-bg:#faeeda;--b-amber-bd:#ba7517;--b-amber-tx:#633806;
  --b-teal-bg:#e1f5ee;--b-teal-bd:#1d9e75;--b-teal-tx:#085041;
}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;line-height:1.7;min-height:100vh;overflow-x:hidden}
#stars{position:fixed;inset:0;z-index:0;pointer-events:none}
.wrap{position:relative;z-index:1;max-width:860px;margin:0 auto;padding:0 28px 80px}

/* HERO */
.hero{text-align:center;padding:80px 0 56px;position:relative}
.hero-particles{position:absolute;inset:0;pointer-events:none;z-index:0}
.hero-content{position:relative;z-index:1}
.hero-icon{width:80px;height:80px;margin:0 auto 24px;border-radius:22px;background:linear-gradient(135deg,#1a2a4a,#0d1a30);border:1.5px solid var(--accent);display:flex;align-items:center;justify-content:center;font-size:38px;animation:bob 3.5s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.hero-eye{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:3px;text-transform:uppercase;color:var(--accent);margin-bottom:14px;opacity:0;animation:fadein .6s .2s forwards}
.hero-title{font-size:clamp(36px,7vw,62px);font-weight:600;letter-spacing:-2px;line-height:1.05;background:linear-gradient(135deg,#fff 0%,var(--accent) 55%,var(--accent2) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;opacity:0;animation:fadein .6s .4s forwards}
.hero-sub{font-size:16px;color:var(--muted);max-width:480px;margin:16px auto 0;opacity:0;animation:fadein .6s .6s forwards}
.badge-row{display:flex;flex-wrap:wrap;gap:7px;justify-content:center;margin-top:26px;opacity:0;animation:fadein .6s .8s forwards}
.badge{font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:700;letter-spacing:1.2px;padding:4px 11px;border-radius:100px;border:1px solid}
.b-blue{background:var(--b-blue-bg);border-color:var(--b-blue-bd);color:var(--b-blue-tx)}
.b-purple{background:var(--b-purple-bg);border-color:var(--b-purple-bd);color:var(--b-purple-tx)}
.b-green{background:var(--b-green-bg);border-color:var(--b-green-bd);color:var(--b-green-tx)}
.b-amber{background:var(--b-amber-bg);border-color:var(--b-amber-bd);color:var(--b-amber-tx)}
.b-teal{background:var(--b-teal-bg);border-color:var(--b-teal-bd);color:var(--b-teal-tx)}
.cta-row{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:32px;opacity:0;animation:fadein .6s 1s forwards}
.btn{display:inline-flex;align-items:center;gap:8px;padding:11px 24px;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;transition:all .22s;text-decoration:none;border:none}
.btn-primary{background:var(--accent);color:#07090f;box-shadow:0 0 28px rgba(99,179,237,.25)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 0 44px rgba(99,179,237,.45)}
.btn-ghost{background:transparent;color:var(--text);border:1px solid rgba(99,179,237,.2)}
.btn-ghost:hover{border-color:var(--accent);color:var(--accent);transform:translateY(-2px)}

/* STATS */
.stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:2rem}
.stat{background:var(--surface2);border:1px solid var(--border);border-radius:14px;padding:20px;text-align:center;transition:border-color .2s}
.stat:hover{border-color:rgba(99,179,237,.35)}
.stat-num{font-size:28px;font-weight:600;color:#fff}
.stat-lbl{font-size:12px;color:var(--muted);margin-top:4px}
.pulse{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--accent3);margin-right:6px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.65)}}

/* DIVIDER */
.divider{height:1px;background:linear-gradient(90deg,transparent,var(--accent),var(--accent2),transparent);margin:56px 0;opacity:.25}

/* SECTION */
.section-eye{font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:3px;text-transform:uppercase;color:var(--accent);margin-bottom:8px}
.section-h{font-size:24px;font-weight:600;letter-spacing:-.5px;margin-bottom:20px}

/* FLOW */
.flow-scroll{overflow-x:auto;padding-bottom:8px}
.flow{display:flex;align-items:center;min-width:600px}
.fstep{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:14px;padding:18px 8px 14px;text-align:center;cursor:pointer;transition:border-color .2s,transform .2s,background .2s;position:relative}
.fstep:hover,.fstep.active{border-color:var(--accent);transform:translateY(-4px);background:#0d1a2e}
.fstep-ico{font-size:24px;margin-bottom:8px}
.fstep-num{font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:2px;color:var(--muted);margin-bottom:3px}
.fstep-name{font-size:12px;font-weight:600;color:#fff}
.fstep-tech{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--muted);margin-top:3px}
.farr{color:var(--accent);font-size:16px;padding:0 6px;flex-shrink:0;opacity:.5}
.step-detail{background:var(--surface2);border:1px solid rgba(99,179,237,.25);border-radius:12px;padding:14px 18px;margin-top:14px;font-size:13px;color:var(--muted);line-height:1.7;display:none}
.step-detail.show{display:block;animation:fadein .25s}
.step-detail strong{color:var(--accent)}
.step-detail code{font-family:'JetBrains Mono',monospace;font-size:12px;background:rgba(99,179,237,.08);padding:1px 6px;border-radius:4px;color:var(--accent)}

/* FEATURES */
.feat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
.fcard{background:var(--surface2);border:1px solid var(--border);border-radius:14px;padding:20px;transition:border-color .2s,transform .2s}
.fcard:hover{border-color:rgba(99,179,237,.35);transform:translateY(-3px)}
.fcard-ico{font-size:22px;margin-bottom:10px}
.fcard-title{font-size:14px;font-weight:600;color:#fff;margin-bottom:6px}
.fcard-desc{font-size:13px;color:var(--muted);line-height:1.6}

/* TABS + CODE */
.tab-row{display:flex;gap:6px;margin-bottom:14px;flex-wrap:wrap}
.tab{font-size:12px;font-weight:600;padding:6px 16px;border-radius:8px;border:1px solid var(--border);background:var(--surface2);cursor:pointer;color:var(--muted);transition:all .18s;font-family:'Inter',sans-serif}
.tab.active,.tab:hover{border-color:var(--accent);background:rgba(99,179,237,.08);color:var(--accent)}
.code-wrap{background:#060a10;border:1px solid var(--border);border-radius:14px;overflow:hidden}
.code-bar{display:flex;align-items:center;gap:6px;padding:10px 16px;background:var(--surface2);border-bottom:1px solid var(--border)}
.tb-dot{width:10px;height:10px;border-radius:50%}
.code-lbl{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--muted);margin-left:8px}
.copy-btn{margin-left:auto;background:transparent;border:1px solid var(--border);border-radius:6px;padding:3px 12px;font-size:11px;color:var(--muted);cursor:pointer;transition:all .18s;font-family:'Inter',sans-serif}
.copy-btn:hover{border-color:var(--accent);color:var(--accent)}
.code-body{padding:20px 24px;font-family:'JetBrains Mono',monospace;font-size:12.5px;line-height:2;overflow-x:auto;white-space:pre;tab-size:2}
.cm{color:#4a5568}.kw{color:var(--accent2)}.str{color:var(--accent3)}.cmd{color:var(--accent)}.hi{color:#fff}

/* FILE TREE */
.tree{background:var(--surface2);border:1px solid var(--border);border-radius:14px;padding:20px 24px;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:2.2;overflow-x:auto;white-space:pre}
.tree-tag{display:inline-block;font-size:9px;padding:1px 8px;border-radius:100px;border:1px solid;margin-left:10px;vertical-align:middle;font-weight:700;letter-spacing:.5px}
.tt-b{background:var(--b-blue-bg);border-color:var(--b-blue-bd);color:var(--b-blue-tx)}
.tt-p{background:var(--b-purple-bg);border-color:var(--b-purple-bd);color:var(--b-purple-tx)}
.tt-g{background:var(--b-green-bg);border-color:var(--b-green-bd);color:var(--b-green-tx)}
.tt-m{border-color:var(--border);color:var(--muted)}

/* CONTRIB */
.contrib-list{display:flex;flex-direction:column;gap:10px}
.cstep{display:flex;align-items:flex-start;gap:16px;background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:16px 20px;transition:border-color .2s}
.cstep:hover{border-color:rgba(99,179,237,.35)}
.csnum{width:28px;height:28px;flex-shrink:0;border-radius:8px;background:rgba(99,179,237,.1);border:1px solid rgba(99,179,237,.3);display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:700;color:var(--accent)}
.cs-title{font-size:14px;font-weight:600;color:#fff}
.cs-code{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--muted);margin-top:3px}

/* FOOTER */
.footer{text-align:center;padding-top:40px;font-size:13px;color:var(--muted)}
.footer a{color:var(--accent);text-decoration:none}
.footer a:hover{text-decoration:underline}

/* REVEAL */
.reveal{opacity:0;transform:translateY(24px);transition:opacity .6s,transform .6s}
.reveal.visible{opacity:1;transform:none}

@keyframes fadein{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@media(max-width:600px){.farr{display:none}.stat-row{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>

<canvas id="stars"></canvas>

<div class="wrap">

  <!-- HERO -->
  <div class="hero">
    <canvas class="hero-particles" id="hero-canvas"></canvas>
    <div class="hero-content">
      <div class="hero-icon">🤖</div>
      <div class="hero-eye">Open Source · Python · Local LLM</div>
      <h1 class="hero-title">RAG Chatbot</h1>
      <p class="hero-sub">Ask questions about your documents. Powered by local LLMs, ChromaDB, and LangChain — no API key needed.</p>
      <div class="badge-row">
        <span class="badge b-blue">PYTHON 3.10+</span>
        <span class="badge b-purple">LANGCHAIN</span>
        <span class="badge b-teal">CHROMADB</span>
        <span class="badge b-amber">LLAMA 3.2</span>
        <span class="badge b-green">STREAMLIT</span>
      </div>
      <div class="cta-row">
        <a href="https://github.com/Abithrekchneanbu/rag-chatbot" class="btn btn-primary" target="_blank">⭐ View on GitHub</a>
        <a href="#quickstart" class="btn btn-ghost">🚀 Quick Start</a>
      </div>
    </div>
  </div>

  <!-- STATS -->
  <div class="stat-row reveal">
    <div class="stat"><div class="stat-num" id="cnt-files">0</div><div class="stat-lbl">source files</div></div>
    <div class="stat"><div class="stat-num" id="cnt-steps">0</div><div class="stat-lbl">pipeline steps</div></div>
    <div class="stat"><div class="stat-num"><span class="pulse"></span>local</div><div class="stat-lbl">LLM mode</div></div>
  </div>

  <div class="divider"></div>

  <!-- ARCHITECTURE -->
  <div class="reveal">
    <div class="section-eye">Architecture</div>
    <h2 class="section-h">How it works <span style="font-size:14px;font-weight:400;color:var(--muted)">— click any step</span></h2>
    <div class="flow-scroll">
      <div class="flow" id="flow">
        <div class="fstep active" onclick="selectStep(0)">
          <div class="fstep-ico">📄</div>
          <div class="fstep-num">STEP 01</div>
          <div class="fstep-name">Load</div>
          <div class="fstep-tech">loaders.py</div>
        </div>
        <div class="farr">›</div>
        <div class="fstep" onclick="selectStep(1)">
          <div class="fstep-ico">✂️</div>
          <div class="fstep-num">STEP 02</div>
          <div class="fstep-name">Chunk</div>
          <div class="fstep-tech">LangChain</div>
        </div>
        <div class="farr">›</div>
        <div class="fstep" onclick="selectStep(2)">
          <div class="fstep-ico">🗄️</div>
          <div class="fstep-num">STEP 03</div>
          <div class="fstep-name">Store</div>
          <div class="fstep-tech">ChromaDB</div>
        </div>
        <div class="farr">›</div>
        <div class="fstep" onclick="selectStep(3)">
          <div class="fstep-ico">🔍</div>
          <div class="fstep-num">STEP 04</div>
          <div class="fstep-name">Retrieve</div>
          <div class="fstep-tech">retriever.py</div>
        </div>
        <div class="farr">›</div>
        <div class="fstep" onclick="selectStep(4)">
          <div class="fstep-ico">🦙</div>
          <div class="fstep-num">STEP 05</div>
          <div class="fstep-name">Generate</div>
          <div class="fstep-tech">Llama 3.2</div>
        </div>
        <div class="farr">›</div>
        <div class="fstep" onclick="selectStep(5)">
          <div class="fstep-ico">💬</div>
          <div class="fstep-num">STEP 06</div>
          <div class="fstep-name">Answer</div>
          <div class="fstep-tech">streamlit_app.py</div>
        </div>
      </div>
    </div>
    <div class="step-detail show" id="step-detail"></div>
  </div>

  <div class="divider"></div>

  <!-- FEATURES -->
  <div class="reveal">
    <div class="section-eye">Capabilities</div>
    <h2 class="section-h">Features</h2>
    <div class="feat-grid">
      <div class="fcard"><div class="fcard-ico">🏠</div><div class="fcard-title">Fully local</div><div class="fcard-desc">Zero external API calls. Your documents never leave the machine.</div></div>
      <div class="fcard"><div class="fcard-ico">📚</div><div class="fcard-title">PDF ingestion</div><div class="fcard-desc">Upload any PDFs — auto-chunked, embedded, and stored in ChromaDB.</div></div>
      <div class="fcard"><div class="fcard-ico">🔎</div><div class="fcard-title">Semantic search</div><div class="fcard-desc">Vector similarity search fetches the most relevant chunks per query.</div></div>
      <div class="fcard"><div class="fcard-ico">🛡️</div><div class="fcard-title">Grounded answers</div><div class="fcard-desc">LLM is instructed to use only the retrieved context — no hallucinations.</div></div>
      <div class="fcard"><div class="fcard-ico">🎛️</div><div class="fcard-title">Streamlit UI</div><div class="fcard-desc">Clean browser-based chat interface — no frontend skills required.</div></div>
      <div class="fcard"><div class="fcard-ico">🔌</div><div class="fcard-title">Modular design</div><div class="fcard-desc">Swap models, loaders, or retriever logic independently.</div></div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- QUICK START -->
  <div class="reveal" id="quickstart">
    <div class="section-eye">Setup</div>
    <h2 class="section-h">Quick start</h2>
    <div class="tab-row">
      <button class="tab active" onclick="setTab('install')">Install</button>
      <button class="tab" onclick="setTab('run')">Run</button>
      <button class="tab" onclick="setTab('usage')">Usage</button>
    </div>
    <div class="code-wrap">
      <div class="code-bar">
        <div class="tb-dot" style="background:#fc8181"></div>
        <div class="tb-dot" style="background:#f6e05e"></div>
        <div class="tb-dot" style="background:#68d391"></div>
        <span class="code-lbl" id="code-lbl">terminal — install</span>
        <button class="copy-btn" onclick="copyCode()">copy</button>
      </div>
      <div class="code-body" id="code-body"><span class="cm"># Clone the repository</span>
<span class="cmd">git</span> clone https://github.com/Abithrekchneanbu/rag-chatbot
<span class="cmd">cd</span> rag-chatbot

<span class="cm"># Install dependencies</span>
<span class="cmd">pip</span> install langchain langchain-ollama chromadb streamlit

<span class="cm"># Pull the local LLM via Ollama</span>
<span class="cmd">ollama</span> pull <span class="str">llama3.2:3b</span></div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- FILE TREE -->
  <div class="reveal">
    <div class="section-eye">Repository</div>
    <h2 class="section-h">Project structure</h2>
    <div class="tree"><span style="color:var(--muted)">📁 rag-chatbot/</span>
├── 🐍 <span style="color:var(--text)">chatbot.py</span><span class="tree-tag tt-b">core logic</span>
├── 🐍 <span style="color:var(--text)">loaders.py</span><span class="tree-tag tt-p">pdf ingestion</span>
├── 🐍 <span style="color:var(--text)">retriever.py</span><span class="tree-tag tt-g">vector search</span>
├── 🐍 <span style="color:var(--text)">streamlit_app.py</span><span class="tree-tag tt-b">web ui</span>
├── 📁 <span style="color:var(--muted)">chroma_db/</span><span class="tree-tag tt-m">auto-generated</span>
├── 📄 <span style="color:var(--muted)">UNIT -5 -FDS.pdf</span><span class="tree-tag tt-m">sample doc</span>
└── 📄 <span style="color:var(--muted)">Visualizing errors... .pdf</span><span class="tree-tag tt-m">sample doc</span></div>
  </div>

  <div class="divider"></div>

  <!-- CONTRIBUTING -->
  <div class="reveal">
    <div class="section-eye">Contributing</div>
    <h2 class="section-h">Get involved</h2>
    <div class="contrib-list">
      <div class="cstep"><div class="csnum">01</div><div><div class="cs-title">Fork the repository</div><div class="cs-code">gh repo fork Abithrekchneanbu/rag-chatbot --clone</div></div></div>
      <div class="cstep"><div class="csnum">02</div><div><div class="cs-title">Create a feature branch</div><div class="cs-code">git checkout -b feat/your-feature</div></div></div>
      <div class="cstep"><div class="csnum">03</div><div><div class="cs-title">Commit your changes</div><div class="cs-code">git commit -m "feat: describe your change"</div></div></div>
      <div class="cstep"><div class="csnum">04</div><div><div class="cs-title">Open a pull request</div><div class="cs-code">gh pr create --title "Your feature name"</div></div></div>
    </div>
  </div>

  <div class="divider"></div>

  <div class="footer reveal">
    <p>Built by <a href="https://github.com/Abithrekchneanbu" target="_blank">Abithrekchneanbu</a> · Python 100% · MIT License</p>
    <p style="margin-top:8px;font-size:12px;opacity:.5">RAG Chatbot — Retrieval-Augmented Generation over local documents</p>
  </div>

</div>

<script>
/* ── STAR FIELD ── */
const sc=document.getElementById('stars'),sctx=sc.getContext('2d');
let stars=[];
function resizeSc(){sc.width=window.innerWidth;sc.height=document.body.scrollHeight;initStars()}
function initStars(){stars=Array.from({length:200},()=>({x:Math.random()*sc.width,y:Math.random()*sc.height,r:Math.random()*1.3+.2,a:Math.random(),da:(Math.random()-.5)*.004}))}
function drawStars(){sctx.clearRect(0,0,sc.width,sc.height);stars.forEach(s=>{s.a=Math.max(.05,Math.min(.85,s.a+s.da));if(s.a<=.05||s.a>=.85)s.da*=-1;sctx.beginPath();sctx.arc(s.x,s.y,s.r,0,Math.PI*2);sctx.fillStyle=`rgba(99,179,237,${s.a})`;sctx.fill()});requestAnimationFrame(drawStars)}
resizeSc();drawStars();window.addEventListener('resize',resizeSc);

/* ── HERO PARTICLES ── */
const hc=document.getElementById('hero-canvas'),hctx=hc.getContext('2d');
let hpts=[];
function resizeHc(){hc.width=hc.offsetWidth;hc.height=hc.offsetHeight;hpts=Array.from({length:50},()=>({x:Math.random()*hc.width,y:Math.random()*hc.height,vx:(Math.random()-.5)*.4,vy:(Math.random()-.5)*.4,r:Math.random()*1.8+.4,a:Math.random()*.4+.1}))}
function drawHero(){hctx.clearRect(0,0,hc.width,hc.height);hpts.forEach(p=>{p.x+=p.vx;p.y+=p.vy;if(p.x<0||p.x>hc.width)p.vx*=-1;if(p.y<0||p.y>hc.height)p.vy*=-1;hctx.beginPath();hctx.arc(p.x,p.y,p.r,0,Math.PI*2);hctx.fillStyle=`rgba(99,179,237,${p.a})`;hctx.fill()});requestAnimationFrame(drawHero)}
hc.style.cssText='position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:0';
setTimeout(()=>{resizeHc();drawHero()},100);

/* ── COUNT UP ── */
function countUp(el,target,dur){let s=null;function step(ts){if(!s)s=ts;const p=Math.min((ts-s)/dur,1);el.textContent=Math.round(p*target);if(p<1)requestAnimationFrame(step)}requestAnimationFrame(step)}
countUp(document.getElementById('cnt-files'),4,900);
countUp(document.getElementById('cnt-steps'),6,900);

/* ── PIPELINE ── */
const stepData=[
  {t:'Load PDFs',d:'<code>loaders.py</code> reads PDF documents using LangChain\'s document loaders and splits the raw text into overlapping chunks ready for embedding.'},
  {t:'Chunk & embed',d:'LangChain splits text into configurable chunks with overlap, then computes dense vector embeddings for each one.'},
  {t:'Store vectors',d:'Embeddings are persisted to a local <code>chroma_db/</code> directory via ChromaDB — no external database or cloud required.'},
  {t:'Retrieve context',d:'<code>retriever.py</code> runs a semantic similarity search to fetch the top-k most relevant chunks for the user\'s question.'},
  {t:'Generate answer',d:'<code>chatbot.py</code> builds a prompt with the retrieved context and question, then calls <strong>Llama 3.2 (3B)</strong> via Ollama to produce a grounded answer.'},
  {t:'Display in UI',d:'<code>streamlit_app.py</code> renders the chat interface in the browser, shows the response, and displays the source context used.'},
];
function selectStep(idx){
  document.querySelectorAll('.fstep').forEach((el,i)=>el.classList.toggle('active',i===idx));
  const d=document.getElementById('step-detail');
  d.innerHTML=`<strong>${stepData[idx].t}</strong> — ${stepData[idx].d}`;
  d.classList.add('show');
}
selectStep(0);

/* ── CODE TABS ── */
const tabs={
  install:{lbl:'terminal — install',body:`<span class="cm"># Clone the repository</span>\n<span class="cmd">git</span> clone https://github.com/Abithrekchneanbu/rag-chatbot\n<span class="cmd">cd</span> rag-chatbot\n\n<span class="cm"># Install dependencies</span>\n<span class="cmd">pip</span> install langchain langchain-ollama chromadb streamlit\n\n<span class="cm"># Pull the local LLM via Ollama</span>\n<span class="cmd">ollama</span> pull <span class="str">llama3.2:3b</span>`},
  run:{lbl:'terminal — run',body:`<span class="cm"># Streamlit web UI (recommended)</span>\n<span class="cmd">streamlit</span> run <span class="hi">streamlit_app.py</span>\n\n<span class="cm"># Or use the terminal chatbot</span>\n<span class="cmd">python</span> <span class="hi">chatbot.py</span>`},
  usage:{lbl:'python — chatbot.py',body:`<span class="kw">from</span> retriever <span class="kw">import</span> get_retriever\n<span class="kw">from</span> langchain_ollama <span class="kw">import</span> OllamaLLM\n\n<span class="kw">def</span> <span class="str">ask_question</span>(question):\n    retriever = get_retriever()\n    docs = retriever.invoke(question)\n    context = <span class="str">"\n\n"</span>.join([d.page_content <span class="kw">for</span> d <span class="kw">in</span> docs])\n    llm = OllamaLLM(model=<span class="str">"llama3.2:3b"</span>)\n    <span class="kw">return</span> llm.invoke(prompt).strip()`},
};
function setTab(name){
  document.querySelectorAll('.tab').forEach((el,i)=>el.classList.toggle('active',['install','run','usage'][i]===name));
  document.getElementById('code-lbl').textContent=tabs[name].lbl;
  document.getElementById('code-body').innerHTML=tabs[name].body;
}
function copyCode(){
  navigator.clipboard.writeText(document.getElementById('code-body').innerText).then(()=>{
    const b=document.querySelector('.copy-btn');b.textContent='copied!';setTimeout(()=>b.textContent='copy',1800);
  });
}

/* ── SCROLL REVEAL ── */
const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target)}}),{threshold:.1});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
</script>
</body>
</html>
