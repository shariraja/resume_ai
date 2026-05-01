# app.py

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

st.set_page_config(
    page_title="S.S_AI — Resume Coach & Interview Simulator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    box-sizing: border-box;
}

/* ── BACKGROUND ── */
.stApp {
    background: #f0f2f8;
    min-height: 100vh;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ── TOP NAVBAR ── */
.ss-navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: #ffffff;
    border-bottom: 1.5px solid #e2e8f0;
    padding: 0 3rem;
    height: 68px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.ss-nav-left {
    display: flex;
    align-items: center;
    gap: 14px;
}
.ss-logo-box {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 800;
    font-size: 15px;
    color: #fff;
    letter-spacing: -0.5px;
    animation: logoPulse 3s ease-in-out infinite;
    flex-shrink: 0;
}
@keyframes logoPulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(79,70,229,0.4); }
    50%       { box-shadow: 0 0 0 8px rgba(79,70,229,0); }
}
.ss-brand-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #1e1b4b;
    letter-spacing: -0.5px;
}
.ss-brand-name span { color: #4f46e5; }
.ss-nav-tagline {
    font-size: 13px;
    color: #64748b;
    font-weight: 400;
    margin-left: 6px;
    padding-left: 16px;
    border-left: 1.5px solid #e2e8f0;
}
.ss-nav-badge {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    font-size: 12px;
    font-weight: 600;
    padding: 5px 14px;
    border-radius: 99px;
    letter-spacing: 0.3px;
}

/* ── HERO SECTION ── */
.ss-hero {
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 40%, #4338ca 100%);
    padding: 4rem 4rem 3.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.ss-hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 300px; height: 300px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
}
.ss-hero::after {
    content: '';
    position: absolute;
    bottom: -80px; left: -40px;
    width: 250px; height: 250px;
    background: rgba(255,255,255,0.03);
    border-radius: 50%;
}
.ss-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.2);
    color: #c7d2fe;
    font-size: 13px;
    font-weight: 600;
    padding: 6px 18px;
    border-radius: 99px;
    margin-bottom: 1.5rem;
    letter-spacing: 0.5px;
}
.ss-hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 48px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.15;
    margin-bottom: 1rem;
    letter-spacing: -1px;
}
.ss-hero-title span {
    background: linear-gradient(90deg, #a5b4fc, #c4b5fd, #93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.ss-hero-sub {
    font-size: 18px;
    color: #c7d2fe;
    font-weight: 400;
    max-width: 600px;
    margin: 0 auto 2rem;
    line-height: 1.6;
}
.ss-hero-stats {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2.5rem;
    margin-top: 2rem;
}
.ss-stat-item {
    text-align: center;
}
.ss-stat-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #fff;
}
.ss-stat-label {
    font-size: 13px;
    color: #a5b4fc;
    font-weight: 400;
    margin-top: 2px;
}
.ss-stat-div {
    width: 1px;
    height: 40px;
    background: rgba(255,255,255,0.15);
}

/* ── MAIN CONTENT AREA ── */
.ss-main {
    max-width: 1100px;
    margin: 0 auto;
    padding: 2.5rem 2rem 4rem;
}

/* ── SECTION LABEL ── */
.ss-section-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #4f46e5;
    margin-bottom: 8px;
}
.ss-section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #1e1b4b;
    margin-bottom: 6px;
}
.ss-section-sub {
    font-size: 15px;
    color: #64748b;
    margin-bottom: 1.5rem;
    line-height: 1.5;
}

/* ── CARDS ── */
.ss-card {
    background: #ffffff;
    border-radius: 18px;
    border: 1.5px solid #e2e8f0;
    padding: 2rem 2.25rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    animation: cardIn 0.5s ease both;
}
@keyframes cardIn {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}
.ss-card-header {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #1e1b4b;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.ss-card-icon {
    width: 34px; height: 34px;
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
}
.icon-purple { background: #ede9fe; }
.icon-green  { background: #dcfce7; }
.icon-red    { background: #fee2e2; }
.icon-blue   { background: #dbeafe; }
.icon-amber  { background: #fef3c7; }

/* ── SCORE RING CARD ── */
.ss-score-card {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    text-align: center;
    color: #fff;
    position: relative;
    overflow: hidden;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 32px rgba(79,70,229,0.35);
}
.ss-score-ring {
    width: 140px; height: 140px;
    border-radius: 50%;
    border: 8px solid rgba(255,255,255,0.2);
    display: flex; align-items: center; justify-content: center;
    flex-direction: column;
    margin: 0 auto 1rem;
    background: rgba(255,255,255,0.08);
    animation: ringPulse 2.5s ease-in-out infinite;
}
@keyframes ringPulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(255,255,255,0.2); }
    50%       { box-shadow: 0 0 0 12px rgba(255,255,255,0); }
}
.ss-ring-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 48px;
    font-weight: 800;
    line-height: 1;
    color: #fff;
}
.ss-ring-denom {
    font-size: 16px;
    color: rgba(255,255,255,0.6);
    font-weight: 400;
}
.ss-score-label-text {
    font-size: 16px;
    font-weight: 600;
    color: rgba(255,255,255,0.9);
    letter-spacing: 0.2px;
}

/* ── SKILL TAGS ── */
.ss-tag {
    display: inline-block;
    background: #ede9fe;
    color: #5b21b6;
    font-size: 13px;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 99px;
    margin: 4px;
    border: 1px solid #ddd6fe;
    transition: all 0.2s;
}
.ss-tag:hover {
    background: #4f46e5;
    color: #fff;
    border-color: #4f46e5;
}

/* ── LIST ITEMS ── */
.ss-list-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 14px 0;
    border-bottom: 1px solid #f1f5f9;
    font-size: 15px;
    line-height: 1.6;
}
.ss-list-item:last-child { border-bottom: none; }
.ss-bullet-green {
    width: 26px; height: 26px; border-radius: 50%;
    background: #dcfce7; color: #16a34a;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 700; flex-shrink: 0; margin-top: 1px;
}
.ss-bullet-red {
    width: 26px; height: 26px; border-radius: 50%;
    background: #fee2e2; color: #dc2626;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 700; flex-shrink: 0; margin-top: 1px;
}
.ss-bullet-blue {
    width: 26px; height: 26px; border-radius: 50%;
    background: #dbeafe; color: #2563eb;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 700; flex-shrink: 0; margin-top: 1px;
}
.ss-item-text-green { color: #14532d; font-weight: 500; }
.ss-item-text-red   { color: #7f1d1d; font-weight: 500; }
.ss-item-text-blue  { color: #1e3a5f; font-weight: 500; }

/* ── PROGRESS BAR ── */
.ss-progress-wrap { margin: 8px 0; }
.ss-progress-top {
    display: flex; justify-content: space-between;
    font-size: 14px; font-weight: 600; color: #374151; margin-bottom: 6px;
}
.ss-progress-bg {
    width: 100%; height: 10px;
    background: #e5e7eb; border-radius: 99px; overflow: hidden;
}
.ss-progress-fill {
    height: 100%; border-radius: 99px;
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    transition: width 1s ease;
}

/* ── MODE SELECTOR CARDS ── */
.ss-mode-card {
    border: 2px solid #e2e8f0;
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    cursor: pointer;
    transition: all 0.2s;
    background: #fff;
    margin-bottom: 0.75rem;
}
.ss-mode-card:hover {
    border-color: #4f46e5;
    box-shadow: 0 4px 16px rgba(79,70,229,0.12);
}
.ss-mode-active {
    border-color: #4f46e5 !important;
    background: #f5f3ff !important;
    box-shadow: 0 4px 16px rgba(79,70,229,0.15) !important;
}

/* ── QUESTION BOX ── */
.ss-qbox {
    background: #f8faff;
    border: 1.5px solid #c7d2fe;
    border-left: 5px solid #4f46e5;
    border-radius: 14px;
    padding: 1.75rem 2rem;
    margin-bottom: 1.5rem;
    animation: cardIn 0.4s ease both;
}
.ss-qlabel {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #4f46e5;
    margin-bottom: 10px;
}
.ss-qtext {
    font-size: 17px;
    color: #1e1b4b;
    line-height: 1.75;
    font-weight: 500;
}

/* ── FOLLOW-UP BOX ── */
.ss-fubox {
    background: #fffbeb;
    border: 1.5px solid #fcd34d;
    border-left: 5px solid #f59e0b;
    border-radius: 14px;
    padding: 1.75rem 2rem;
    margin-bottom: 1.5rem;
    animation: cardIn 0.4s ease both;
}
.ss-fulabel {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #b45309;
    margin-bottom: 10px;
}
.ss-futext {
    font-size: 17px;
    color: #451a03;
    line-height: 1.75;
    font-weight: 500;
}

/* ── DIFFICULTY BADGE ── */
.ss-diff-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: #ede9fe; border: 1.5px solid #c4b5fd;
    color: #5b21b6; font-size: 13px; font-weight: 700;
    padding: 6px 16px; border-radius: 99px; margin-bottom: 1.25rem;
    letter-spacing: 0.3px;
}

/* ── AGENT SCORE BOXES ── */
.ss-agent-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin: 1.25rem 0;
}
.ss-agent-box {
    background: #f8faff;
    border: 1.5px solid #e0e7ff;
    border-radius: 14px;
    padding: 1.25rem;
    text-align: center;
}
.ss-agent-score {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #4f46e5;
    line-height: 1;
    margin-bottom: 4px;
}
.ss-agent-label {
    font-size: 13px;
    font-weight: 600;
    color: #64748b;
    margin-bottom: 6px;
}
.ss-agent-weight {
    font-size: 12px;
    color: #94a3b8;
    font-weight: 400;
}

/* ── FINAL SCORE BANNER ── */
.ss-final-banner {
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
    border-radius: 20px;
    padding: 3rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 12px 40px rgba(67,56,202,0.35);
    animation: cardIn 0.6s ease both;
}
.ss-final-label {
    font-size: 12px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 2px;
    color: #a5b4fc; margin-bottom: 10px;
}
.ss-final-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 80px; font-weight: 800; color: #fff; line-height: 1;
}
.ss-final-denom {
    font-size: 28px; color: rgba(255,255,255,0.4); font-weight: 400;
}
.ss-final-verdict {
    margin-top: 14px; font-size: 17px; font-weight: 600;
}

/* ── KG ROW ── */
.ss-kg-row {
    display: flex; align-items: center; gap: 12px;
    margin: 10px 0;
}
.ss-kg-label {
    font-size: 14px; color: #374151; font-weight: 500;
    min-width: 200px; white-space: nowrap;
    overflow: hidden; text-overflow: ellipsis;
}
.ss-kg-bar-bg {
    flex: 1; background: #e5e7eb;
    border-radius: 99px; height: 8px;
}
.ss-kg-bar-fill {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    border-radius: 99px; height: 8px;
}
.ss-kg-pct {
    font-size: 14px; font-weight: 700;
    color: #4f46e5; min-width: 40px; text-align: right;
}

/* ── REVIEW ITEM ── */
.ss-review-q {
    background: #f5f3ff; border-left: 4px solid #4f46e5;
    border-radius: 10px; padding: 14px 18px; margin-bottom: 10px;
}
.ss-review-q-label {
    font-size: 11px; font-weight: 700; color: #4f46e5;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px;
}
.ss-review-q-text { font-size: 15px; color: #1e1b4b; font-weight: 500; line-height: 1.6; }
.ss-review-a {
    background: #f8fafc; border-radius: 10px;
    padding: 14px 18px; margin-bottom: 10px;
}
.ss-review-a-label {
    font-size: 11px; font-weight: 700; color: #64748b;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px;
}
.ss-review-a-text { font-size: 15px; color: #374151; line-height: 1.65; }
.ss-score-pill {
    display: inline-block;
    font-size: 14px; font-weight: 700;
    padding: 5px 18px; border-radius: 99px;
}
.ss-pill-green { background: #dcfce7; color: #15803d; }
.ss-pill-amber { background: #fef3c7; color: #b45309; }
.ss-pill-red   { background: #fee2e2; color: #dc2626; }
.ss-review-fu {
    background: #fffbeb; border-left: 4px solid #f59e0b;
    border-radius: 10px; padding: 14px 18px; margin-bottom: 10px;
}
.ss-review-fu-label {
    font-size: 11px; font-weight: 700; color: #b45309;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px;
}

/* ── STREAMLIT OVERRIDES ── */
.stSelectbox > div > div {
    background: #fff !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 12px !important;
    font-size: 15px !important;
    color: #1e1b4b !important;
}
.stButton > button {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    color: #fff !important; border: none !important;
    border-radius: 12px !important; font-weight: 700 !important;
    font-size: 16px !important; padding: 0.75rem 2rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 18px rgba(79,70,229,0.35) !important;
    letter-spacing: 0.2px !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(79,70,229,0.45) !important;
}
.stTextArea > div > div > textarea {
    background: #fff !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 14px !important;
    color: #1e1b4b !important;
    font-size: 15px !important;
    line-height: 1.7 !important;
    transition: border-color 0.2s !important;
}
.stTextArea > div > div > textarea:focus {
    border-color: #4f46e5 !important;
    box-shadow: 0 0 0 3px rgba(79,70,229,0.1) !important;
}
.stFileUploader > div {
    background: #fafbff !important;
    border: 2px dashed #c7d2fe !important;
    border-radius: 16px !important;
    transition: all 0.2s !important;
}
.stFileUploader > div:hover {
    border-color: #4f46e5 !important;
    background: #f0f0ff !important;
}
.stProgress > div > div {
    background: linear-gradient(90deg, #4f46e5, #7c3aed) !important;
    border-radius: 99px !important;
}
.stProgress > div {
    background: #e0e7ff !important;
    border-radius: 99px !important;
}
[data-testid="metric-container"] {
    background: #fff !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 14px !important;
    padding: 1.25rem !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
}
[data-testid="metric-container"] label {
    color: #64748b !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.6px !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #4f46e5 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 26px !important;
    font-weight: 800 !important;
}
.streamlit-expanderHeader {
    background: #f8faff !important;
    border: 1.5px solid #e0e7ff !important;
    border-radius: 12px !important;
    color: #1e1b4b !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    padding: 0.85rem 1.25rem !important;
}
.streamlit-expanderContent {
    background: #fff !important;
    border: 1.5px solid #e0e7ff !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
    padding: 1.25rem !important;
}
hr { border-color: #e2e8f0 !important; margin: 2rem 0 !important; }
#MainMenu, footer, header { visibility: hidden; }
.stAlert { border-radius: 12px !important; font-size: 15px !important; }
</style>
""", unsafe_allow_html=True)

# ── Imports ────────────────────────────────────────────────────
from utils.pdf_reader                import extract_text
from utils.structured_output_cleaner import clean_json_output
from utils.helpers                   import display_score_breakdown
from ai_core.resume_analyzer         import analyze_resume, is_valid_cv
from ai_core.question_generator      import generate_questions_batch
from ai_core.followup_engine         import generate_followup
from evaluators.answer_evaluator     import evaluate_answer
from interview.interview_state       import init_state, reset_state
from interview.knowledge_graph       import KnowledgeGraph
from config                          import MAX_QUESTIONS, HIRING_MODES, FINAL_SCORE_WEIGHTS
from evaluators.score_rubric         import compute_final_interview_score

TECH_KEYWORDS = [
    "LangChain","LangGraph","RAG","FAISS","ChromaDB","Pinecone",
    "SMOTE","XGBoost","LightGBM","LoRA","QLoRA","Fine-tuning",
    "MobileNetV2","TensorFlow","PyTorch","Keras","Groq","LLaMA",
    "GPT-4o","Claude","HuggingFace","Streamlit","Docker","Kubernetes",
    "FastAPI","Prompt Engineering","System Design","Vector Store",
    "Embedding","Inference","Microservices","Kafka","Redis",
]

def extract_topic(question: str) -> str:
    q_lower = question.lower()
    for kw in TECH_KEYWORDS:
        if kw.lower() in q_lower:
            return kw
    words = [w for w in question.split() if len(w) > 3]
    return " ".join(words[:4]) if words else "General"

def score_pill(score):
    if score >= 7:
        return f'<span class="ss-score-pill ss-pill-green">Score: {score}/10</span>'
    elif score >= 5:
        return f'<span class="ss-score-pill ss-pill-amber">Score: {score}/10</span>'
    else:
        return f'<span class="ss-score-pill ss-pill-red">Score: {score}/10</span>'

def render_kg(kg):
    items = sorted(kg.mastery.items(), key=lambda x: x[1])
    html  = ""
    for topic, score in items:
        label = (topic[:30] + "…") if len(topic) > 30 else topic
        pct   = int(score * 100)
        html += f"""<div class="ss-kg-row">
            <span class="ss-kg-label">{label}</span>
            <div class="ss-kg-bar-bg">
                <div class="ss-kg-bar-fill" style="width:{pct}%"></div>
            </div>
            <span class="ss-kg-pct">{pct}%</span>
        </div>"""
    return html

def display_eval(eval_result):
    if not eval_result:
        st.warning("No evaluation data.")
        return
    if not eval_result.get("pass", True):
        reason = eval_result.get("verification", {}).get("reason", "Invalid answer.")
        st.error(f"**Answer Rejected:** {reason}")
        return

    weighted    = eval_result.get("weighted", {})
    final_score = eval_result.get("final_score", 0)
    agents      = eval_result.get("agents", {})

    if final_score >= 8:
        color, label = "#16a34a", "Excellent"
    elif final_score >= 6:
        color, label = "#4f46e5", "Good"
    elif final_score >= 4:
        color, label = "#d97706", "Needs Improvement"
    else:
        color, label = "#dc2626", "Poor"

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,{'#4f46e5' if final_score>=6 else '#d97706' if final_score>=4 else '#dc2626'},{'#7c3aed' if final_score>=6 else '#f59e0b' if final_score>=4 else '#ef4444'});
        border-radius:16px;padding:1.5rem 2rem;margin-bottom:1.25rem;
        display:flex;align-items:center;justify-content:space-between;">
        <div>
            <div style="font-size:13px;font-weight:700;text-transform:uppercase;
                letter-spacing:1px;color:rgba(255,255,255,0.7);margin-bottom:4px;">Final Score</div>
            <div style="font-family:'Space Grotesk',sans-serif;font-size:44px;
                font-weight:800;color:#fff;line-height:1;">{final_score}
                <span style="font-size:20px;opacity:0.6">/10</span>
            </div>
        </div>
        <div style="text-align:right;">
            <div style="background:rgba(255,255,255,0.2);border-radius:10px;
                padding:8px 18px;font-size:15px;font-weight:700;color:#fff;">{label}</div>
        </div>
    </div>
    <div class="ss-agent-grid">
        <div class="ss-agent-box">
            <div class="ss-agent-score">{weighted.get('technical_score',0)}</div>
            <div class="ss-agent-label">Technical Judge</div>
            <div class="ss-agent-weight">Weight: 40%</div>
        </div>
        <div class="ss-agent-box">
            <div class="ss-agent-score">{weighted.get('depth_score',0)}</div>
            <div class="ss-agent-label">Depth Judge</div>
            <div class="ss-agent-weight">Weight: 40%</div>
        </div>
        <div class="ss-agent-box">
            <div class="ss-agent-score">{weighted.get('bar_raiser_score',0)}</div>
            <div class="ss-agent-label">Bar Raiser</div>
            <div class="ss-agent-weight">Weight: 20%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    import re
    for agent_key, label in [("technical","Technical Judge"),("depth","Depth Judge"),("bar_raiser","Bar Raiser")]:
        agent_data = agents.get(agent_key, {})
        if not agent_data:
            continue
        scores   = agent_data.get("scores", {})
        raw_text = agent_data.get("raw_text", "")
        with st.expander(f"{label} — Detailed Breakdown"):
            c1,c2,c3,c4,c5 = st.columns(5)
            c1.metric("Correctness",    f"{scores.get('correctness',0)}/4")
            c2.metric("Depth",          f"{scores.get('depth',0)}/3")
            c3.metric("Edge Cases",     f"{scores.get('edge_cases',0)}/2")
            c4.metric("Sys. Thinking",  f"{scores.get('system_thinking',0)}/2")
            c5.metric("Communication",  f"{scores.get('communication',0)}/2")
            fb = re.search(r"Feedback:\s*(.+?)(?=Gaps:|$)", raw_text, re.DOTALL)
            if fb:
                st.info(f"**Feedback:** {fb.group(1).strip()}")
            gaps = re.search(r"Gaps:\s*(.+?)$", raw_text, re.DOTALL)
            if gaps:
                numbered = re.findall(r"\(\d+\)\s*(.+?)(?=\(\d+\)|$)", gaps.group(1).strip(), re.DOTALL)
                if numbered:
                    st.warning("**To score higher, you were missing:**")
                    for g in numbered:
                        st.warning(f"→ {g.strip()}")

# ── Init ───────────────────────────────────────────────────────
init_state()

# ═══════════════════════════════════════════════════════════════
# TOP NAVBAR
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ss-navbar">
    <div class="ss-nav-left">
        <div class="ss-logo-box">S.S</div>
        <span class="ss-brand-name">S.S<span>_AI</span></span>
        <span class="ss-nav-tagline">AI Resume Coach & Interview Simulator</span>
    </div>
    <div class="ss-nav-badge">Meta · Google · FAANG Level</div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="ss-hero">
    <div class="ss-hero-badge">Powered by Multi-Agent AI Evaluation</div>
    <div class="ss-hero-title">
        Analyze Your Resume.<br>
        <span>Ace Your FAANG Interview.</span>
    </div>
    <div class="ss-hero-sub">
        Get a deep AI-powered resume analysis and practice with an adaptive interview simulator
        that uses 3 specialized AI judges — just like real FAANG hiring panels.
    </div>
    <div class="ss-hero-stats">
        <div class="ss-stat-item">
            <div class="ss-stat-num">3</div>
            <div class="ss-stat-label">AI Judge Agents</div>
        </div>
        <div class="ss-stat-div"></div>
        <div class="ss-stat-item">
            <div class="ss-stat-num">L1–L5</div>
            <div class="ss-stat-label">Adaptive Difficulty</div>
        </div>
        <div class="ss-stat-div"></div>
        <div class="ss-stat-item">
            <div class="ss-stat-num">100%</div>
            <div class="ss-stat-label">Resume Tailored</div>
        </div>
        <div class="ss-stat-div"></div>
        <div class="ss-stat-item">
            <div class="ss-stat-num">Real</div>
            <div class="ss-stat-label">FAANG Standards</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# MAIN CONTENT
# ═══════════════════════════════════════════════════════════════
st.markdown('<div class="ss-main">', unsafe_allow_html=True)

# ── Step 1: Mode + Upload ──────────────────────────────────────
col_left, col_right = st.columns([1, 1.6], gap="large")

with col_left:
    st.markdown("""
    <div class="ss-section-label">Step 1</div>
    <div class="ss-section-title">Select Interview Mode</div>
    <div class="ss-section-sub">Choose the company style that matches your target role.</div>
    """, unsafe_allow_html=True)

    mode_labels   = {k: v["label"] for k, v in HIRING_MODES.items()}
    selected_mode = st.selectbox(
        "", options=list(mode_labels.keys()),
        format_func=lambda k: f"{HIRING_MODES[k]['label']}",
        index=1, label_visibility="collapsed"
    )
    if selected_mode != st.session_state.hiring_mode:
        st.session_state.hiring_mode = selected_mode
        if st.session_state.adaptive_engine:
            st.session_state.adaptive_engine.mode = selected_mode

    mode_info = HIRING_MODES[selected_mode]
    st.markdown(f"""
    <div class="ss-card" style="margin-top:1rem;border-left:4px solid #4f46e5;padding:1.25rem 1.5rem;">
        <div style="font-size:18px;font-weight:700;color:#1e1b4b;margin-bottom:4px;">{mode_info['label']}</div>
        <div style="font-size:14px;color:#64748b;line-height:1.5;">{mode_info['description']}</div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class="ss-section-label">Step 2</div>
    <div class="ss-section-title">Upload Your Resume</div>
    <div class="ss-section-sub">Upload your CV in PDF format to get a complete AI-powered analysis and generate tailored interview questions.</div>
    """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["pdf"], label_visibility="collapsed")

st.divider()

if uploaded_file:
    text = extract_text(uploaded_file)
    if not is_valid_cv(text):
        st.error("❌ Invalid CV detected. Please upload a proper resume in PDF format.")
        st.stop()

    with st.spinner("Running deep AI analysis on your resume..."):
        result = analyze_resume(text)
        try:
            data = clean_json_output(result)
        except Exception:
            st.error("❌ Parsing failed. Please try again.")
            st.stop()

    st.success("✅ Resume analysis complete — scroll down to see your results")
    st.divider()

    # ── ANALYSIS RESULTS ──────────────────────────────────────
    st.markdown("""
    <div class="ss-section-label">Resume Analysis</div>
    <div class="ss-section-title">Your Complete Resume Report</div>
    <div class="ss-section-sub">Deep AI analysis covering skills, strengths, weaknesses, and actionable suggestions.</div>
    """, unsafe_allow_html=True)

    score_val = data.get("score", 0)
    score_pct = score_val * 10

    res_col1, res_col2 = st.columns([1, 2], gap="large")

    with res_col1:
        st.markdown(f"""
        <div class="ss-score-card">
            <div style="font-size:13px;font-weight:700;text-transform:uppercase;
                letter-spacing:1.5px;color:rgba(255,255,255,0.6);margin-bottom:1rem;">
                Resume Score
            </div>
            <div class="ss-score-ring">
                <div class="ss-ring-num">{score_val}</div>
                <div class="ss-ring-denom">/10</div>
            </div>
            <div class="ss-score-label-text">
                {"Excellent Resume" if score_val>=8 else "Good Resume" if score_val>=6 else "Needs Improvement" if score_val>=4 else "Major Revisions Needed"}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="ss-card" style="padding:1.5rem;">
            <div class="ss-card-header">
                <div class="ss-card-icon icon-purple">📊</div>
                Score Breakdown
            </div>
        """, unsafe_allow_html=True)

        dims = [
            ("Resume Content",   min(score_pct + 5, 100)),
            ("Technical Skills", min(score_pct + 8, 100)),
            ("Presentation",     max(score_pct - 10, 0)),
            ("Completeness",     max(score_pct - 5, 0)),
        ]
        for dim_label, dim_val in dims:
            st.markdown(f"""
            <div class="ss-progress-wrap">
                <div class="ss-progress-top">
                    <span>{dim_label}</span>
                    <span>{dim_val}%</span>
                </div>
                <div class="ss-progress-bg">
                    <div class="ss-progress-fill" style="width:{dim_val}%"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with res_col2:
        # Skills
        st.markdown("""
        <div class="ss-card">
            <div class="ss-card-header">
                <div class="ss-card-icon icon-purple">🔧</div>
                Technical Skills Detected
            </div>
        """, unsafe_allow_html=True)
        skills_html = "".join(f'<span class="ss-tag">{s}</span>' for s in data.get("skills", []))
        st.markdown(f'{skills_html}</div>', unsafe_allow_html=True)

        # Strengths
        st.markdown("""
        <div class="ss-card">
            <div class="ss-card-header">
                <div class="ss-card-icon icon-green">✅</div>
                Strengths
            </div>
        """, unsafe_allow_html=True)
        for s in data.get("strengths", []):
            st.markdown(f"""
            <div class="ss-list-item">
                <div class="ss-bullet-green">✓</div>
                <span class="ss-item-text-green">{s}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Weaknesses
        st.markdown("""
        <div class="ss-card">
            <div class="ss-card-header">
                <div class="ss-card-icon icon-red">⚠️</div>
                Areas for Improvement
            </div>
        """, unsafe_allow_html=True)
        for w in data.get("weaknesses", []):
            st.markdown(f"""
            <div class="ss-list-item">
                <div class="ss-bullet-red">✗</div>
                <span class="ss-item-text-red">{w}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Suggestions
        st.markdown("""
        <div class="ss-card">
            <div class="ss-card-header">
                <div class="ss-card-icon icon-blue">💡</div>
                Actionable Suggestions
            </div>
        """, unsafe_allow_html=True)
        for sug in data.get("suggestions", []):
            st.markdown(f"""
            <div class="ss-list-item">
                <div class="ss-bullet-blue">→</div>
                <span class="ss-item-text-blue">{sug}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # ═══════════════════════════════════════════════════════════
    # INTERVIEW SECTION
    # ═══════════════════════════════════════════════════════════
    st.markdown(f"""
    <div class="ss-section-label">Step 3</div>
    <div class="ss-section-title">Adaptive Interview Simulator</div>
    <div class="ss-section-sub">
        5 resume-tailored questions with adaptive difficulty (L1–L5).
        Scored by 3 specialized AI judges — Technical, Depth, and Bar Raiser.
        Strong answers unlock deeper follow-up probes.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀  Start Interview Now", use_container_width=True):
        reset_state()
        st.session_state.hiring_mode          = selected_mode
        st.session_state.adaptive_engine.mode = selected_mode
        kg = st.session_state.knowledge_graph
        ae = st.session_state.adaptive_engine
        for w in data.get("weaknesses", []):
            kg.update(w[:40], score_10=3.0)
        with st.spinner("Generating adaptive questions tailored to your resume..."):
            st.session_state.questions = generate_questions_batch(
                resume_text=text, n=MAX_QUESTIONS,
                adaptive_engine=ae, knowledge_graph=kg,
            )
        st.session_state.interview_started = True
        st.rerun()

    # ── Interview Flow ─────────────────────────────────────────
    if st.session_state.interview_started:

        if not st.session_state.questions:
            st.error("❌ Failed to generate questions. Please restart.")
            if st.button("🔄 Restart"):
                reset_state(); st.rerun()
            st.stop()

        idx   = st.session_state.index
        phase = st.session_state.interview_phase
        ae    = st.session_state.adaptive_engine
        kg    = st.session_state.knowledge_graph

        if idx < len(st.session_state.questions):
            question = st.session_state.questions[idx]

            # ── MAIN QUESTION ──────────────────────────────────
            if phase == "main":
                st.divider()
                total_q = len(st.session_state.questions)
                st.progress(idx / total_q)
                st.caption(f"Question {idx+1} of {total_q}")

                st.markdown(f"""
                <div class="ss-diff-badge">
                    Level {ae.difficulty} &nbsp;·&nbsp; {ae.get_difficulty_label()}
                    &nbsp;·&nbsp; {mode_info['label']}
                </div>
                <div class="ss-qbox">
                    <div class="ss-qlabel">Interview Question {idx+1}</div>
                    <div class="ss-qtext">{question}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("**Your Answer**", unsafe_allow_html=False)
                answer = st.text_area(
                    "", key=f"ans_{idx}", height=220,
                    placeholder="Write a detailed technical answer. Mention WHY you chose your approach, trade-offs, edge cases, and real-world implications...",
                    label_visibility="collapsed"
                )

                if st.button("Submit Answer  →", key=f"btn_{idx}", use_container_width=True):
                    with st.spinner("Running 3-agent AI evaluation..."):
                        eval_result = evaluate_answer(question, answer)
                    score = eval_result["final_score"]
                    st.session_state.scores.append(score)
                    st.session_state.answers.append(answer)
                    st.session_state.eval_results.append(eval_result)
                    st.session_state.last_eval = eval_result
                    kg.update(extract_topic(question), score_10=score)
                    ae.update_difficulty(score)

                    if score >= 4 and eval_result["pass"]:
                        fu_type = ae.select_followup_type(score, kg.weakness_vector())
                        with st.spinner(f"Generating {fu_type.replace('_',' ')} follow-up probe..."):
                            fu_q = generate_followup(question, answer, fu_type, kg.weakness_vector())
                        if fu_q and len(fu_q.strip()) > 10:
                            st.session_state.follow_up_question = fu_q
                            st.session_state.follow_up_questions_list.append(fu_q)
                            st.session_state.interview_phase = "followup"
                        else:
                            st.session_state.follow_up_questions_list.append("")
                            st.session_state.follow_up_answers.append("")
                            st.session_state.follow_up_scores.append(0)
                            st.session_state.follow_up_evals.append(None)
                            st.session_state.interview_phase = "show_main_feedback"
                    else:
                        st.session_state.follow_up_questions_list.append("")
                        st.session_state.follow_up_answers.append("")
                        st.session_state.follow_up_scores.append(0)
                        st.session_state.follow_up_evals.append(None)
                        st.session_state.interview_phase = "show_main_feedback"
                    st.rerun()

            # ── MAIN FEEDBACK ──────────────────────────────────
            elif phase == "show_main_feedback":
                st.divider()
                st.markdown('<div class="ss-section-label">Evaluation Result</div>', unsafe_allow_html=True)
                display_eval(st.session_state.last_eval)
                with st.expander("🧠 Knowledge Graph — Your Topic Mastery", expanded=False):
                    st.markdown(render_kg(kg), unsafe_allow_html=True)
                st.divider()
                if st.button("Next Question  →", key=f"next_main_{idx}", use_container_width=True):
                    st.session_state.interview_phase = "main"
                    st.session_state.index += 1
                    st.rerun()

            # ── FOLLOW-UP ──────────────────────────────────────
            elif phase == "followup":
                st.divider()
                st.markdown('<div class="ss-section-label">Main Answer — Evaluation</div>', unsafe_allow_html=True)
                display_eval(st.session_state.last_eval)
                st.divider()

                st.markdown(f"""
                <div class="ss-fubox">
                    <div class="ss-fulabel">Follow-up Probe — Go Deeper</div>
                    <div class="ss-futext">{st.session_state.follow_up_question}</div>
                </div>
                """, unsafe_allow_html=True)
                st.caption("Explain WHY, HOW, edge cases, failure modes, and production/scale implications.")

                st.markdown("**Your Follow-up Answer**")
                fu_answer = st.text_area(
                    "", key=f"fu_ans_{idx}", height=220,
                    placeholder="Dig deeper — explain your reasoning, trade-offs, edge cases, and real-world production implications...",
                    label_visibility="collapsed"
                )
                if st.button("Submit Follow-up Answer  →", key=f"fu_btn_{idx}", use_container_width=True):
                    with st.spinner("Evaluating follow-up with 3-agent system..."):
                        fu_eval = evaluate_answer(
                            st.session_state.follow_up_question, fu_answer,
                            is_follow_up=True,
                            original_qa={"question": question,
                                         "answer": st.session_state.answers[idx] if idx < len(st.session_state.answers) else ""},
                        )
                    st.session_state.follow_up_answers.append(fu_answer)
                    st.session_state.follow_up_scores.append(fu_eval["final_score"])
                    st.session_state.follow_up_evals.append(fu_eval)
                    st.session_state.last_eval = fu_eval
                    st.session_state.interview_phase = "show_followup_feedback"
                    st.rerun()

            # ── FOLLOW-UP FEEDBACK ─────────────────────────────
            elif phase == "show_followup_feedback":
                st.divider()
                st.markdown('<div class="ss-section-label">Follow-up — Evaluation</div>', unsafe_allow_html=True)
                display_eval(st.session_state.last_eval)
                st.divider()
                if st.button("Next Question  →", key=f"next_fu_{idx}", use_container_width=True):
                    st.session_state.interview_phase = "main"
                    st.session_state.index += 1
                    st.rerun()

        # ── INTERVIEW COMPLETE ─────────────────────────────────
        else:
            st.balloons()
            st.divider()

            fu_scores_valid = [s for s in st.session_state.follow_up_scores if s > 0]
            final_result    = compute_final_interview_score(
                main_scores=st.session_state.scores,
                followup_scores=fu_scores_valid,
                weights=FINAL_SCORE_WEIGHTS,
            )
            bd    = final_result["breakdown"]
            final = final_result["final"]

            if final >= 8:
                verdict_color, verdict_text = "#10b981", "🏆 FAANG-Ready Performance — Outstanding!"
            elif final >= 6:
                verdict_color, verdict_text = "#4f46e5", "📈 Strong Performance — Minor gaps to address"
            elif final >= 4:
                verdict_color, verdict_text = "#d97706", "⚠️ Average — Work on trade-offs and edge cases"
            else:
                verdict_color, verdict_text = "#dc2626", "❌ Needs Significant Improvement"

            st.markdown(f"""
            <div class="ss-final-banner">
                <div class="ss-final-label">Interview Complete — Final Score</div>
                <div class="ss-final-num">{final}
                    <span class="ss-final-denom">/10</span>
                </div>
                <div class="ss-final-verdict" style="color:{verdict_color};">{verdict_text}</div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Interview Score",  f"{bd['avg_main']}/10")
            c2.metric("Follow-up Depth",  f"{bd['avg_followup']}/10")
            c3.metric("Consistency",      f"{bd['consistency']:.1f}/10")
            c4.metric("Improvement",      f"{bd['slope_score']:.1f}/10")

            st.divider()

            st.markdown('<div class="ss-section-label">Knowledge Graph</div>', unsafe_allow_html=True)
            st.markdown('<div class="ss-section-title">Topic Mastery Overview</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="ss-card">
                {render_kg(kg)}
            </div>
            """, unsafe_allow_html=True)

            st.divider()

            st.markdown('<div class="ss-section-label">Full Review</div>', unsafe_allow_html=True)
            st.markdown('<div class="ss-section-title">Complete Interview Transcript</div>', unsafe_allow_html=True)

            for i in range(len(st.session_state.answers)):
                q          = st.session_state.questions[i] if i < len(st.session_state.questions) else "N/A"
                ans        = st.session_state.answers[i]
                ms         = st.session_state.scores[i] if i < len(st.session_state.scores) else 0
                fu_q       = st.session_state.follow_up_questions_list[i] if i < len(st.session_state.follow_up_questions_list) else ""
                fu_ans     = st.session_state.follow_up_answers[i] if i < len(st.session_state.follow_up_answers) else ""
                fu_s       = st.session_state.follow_up_scores[i] if i < len(st.session_state.follow_up_scores) else 0

                pill = score_pill(ms)
                with st.expander(f"Question {i+1}  —  Score: {ms}/10" + ("  ·  Follow-up included" if fu_q else "")):
                    st.markdown(f"""
                    <div class="ss-review-q">
                        <div class="ss-review-q-label">Question {i+1}</div>
                        <div class="ss-review-q-text">{q}</div>
                    </div>
                    <div class="ss-review-a">
                        <div class="ss-review-a-label">Your Answer</div>
                        <div class="ss-review-a-text">{ans if ans else '<em style="color:#94a3b8">No answer provided</em>'}</div>
                    </div>
                    {pill}
                    """, unsafe_allow_html=True)

                    if fu_q:
                        fu_pill = score_pill(fu_s)
                        st.markdown(f"""
                        <div class="ss-review-fu" style="margin-top:14px;">
                            <div class="ss-review-fu-label">Follow-up Probe</div>
                            <div class="ss-review-q-text">{fu_q}</div>
                        </div>
                        <div class="ss-review-a">
                            <div class="ss-review-a-label">Your Follow-up Answer</div>
                            <div class="ss-review-a-text">{fu_ans if fu_ans else '<em style="color:#94a3b8">Skipped</em>'}</div>
                        </div>
                        {fu_pill}
                        """, unsafe_allow_html=True)

            st.divider()
            if st.button("🔄  Start New Interview", use_container_width=True):
                reset_state(); st.rerun()

st.markdown('</div>', unsafe_allow_html=True)