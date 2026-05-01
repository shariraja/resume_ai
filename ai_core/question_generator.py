# ai_core/question_generator.py

from groq import Groq
import os
from dotenv import load_dotenv
from config import PRIMARY_MODEL

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# ── Topic pool — resume-relevant rotating topics ──────────────
TOPIC_POOL = [
    "LangChain pipeline architecture and agent design",
    "RAG chunking strategy and retrieval tuning",
    "FAISS vs ChromaDB vector store trade-offs",
    "SMOTE and imbalanced dataset handling techniques",
    "Fine-tuning LoRA/QLoRA trade-offs and memory optimization",
    "LangGraph state management and multi-agent coordination",
    "MobileNetV2 CNN architecture and transfer learning decisions",
    "Groq LLaMA vs GPT-4o model selection strategy",
    "Streamlit deployment scaling and production limitations",
    "XGBoost hyperparameter tuning and feature importance",
    "Prompt engineering strategies for production LLM apps",
    "Docker containerization and Kubernetes orchestration",
    "HuggingFace model hub and pipeline optimization",
    "System design for high-concurrency ML inference",
    "Embedding models selection and vector search optimization",
]


def _build_prompt(
    resume_text:      str,
    difficulty:       int,
    difficulty_label: str,
    mode_label:       str,
    mode_description: str,
    weakness_target:  str,
    topic_focus:      str,
) -> str:
    return f"""
You are a FAANG-level Senior Technical Interviewer at difficulty level {difficulty}: {difficulty_label}.

Hiring mode: {mode_label} — {mode_description}

Generate EXACTLY 1 deeply technical scenario-based interview question.

=== RULES ===
- The question MUST be specifically about: {topic_focus}
- Reference SPECIFIC projects, tools, or roles from this resume
- Do NOT generate generic questions like "Tell me about yourself"
- Difficulty must match level {difficulty}
- Target this known weakness if present: {weakness_target}
- Question must be different from system design / house price every time
- Focus on the EXACT topic: {topic_focus} — do not drift to other topics

=== OUTPUT ===
- Output ONLY the question
- No numbering, no bullets, no intro text
- Must end with ?

Resume:
{resume_text}
"""


def generate_single_question(
    resume_text:      str,
    difficulty:       int,
    difficulty_label: str,
    mode_label:       str,
    mode_description: str,
    weakness_target:  str = "none",
    topic_focus:      str = "general",
) -> str:
    prompt = _build_prompt(
        resume_text, difficulty, difficulty_label,
        mode_label, mode_description, weakness_target, topic_focus
    )
    res = client.chat.completions.create(
        model=PRIMARY_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.45,
    )
    q = res.choices[0].message.content.strip()
    if q and not q.endswith("?"):
        q += "?"
    return q


def generate_questions_batch(
    resume_text:    str,
    n:              int,
    adaptive_engine,
    knowledge_graph,
) -> list:
    """
    Generate n questions with guaranteed topic diversity.
    Each question targets a different area from TOPIC_POOL.
    """
    questions    = []
    mode_cfg     = adaptive_engine.get_mode_config()

    # Shuffle topic pool so every interview feels fresh
    import random
    topics = random.sample(TOPIC_POOL, min(n, len(TOPIC_POOL)))
    # If n > pool size, cycle through
    while len(topics) < n:
        topics.append(random.choice(TOPIC_POOL))

    for i in range(n):
        weak_topics = knowledge_graph.weakest_topics(n=1)
        weakness    = weak_topics[0] if weak_topics else "none"
        topic       = topics[i]

        q = generate_single_question(
            resume_text=resume_text,
            difficulty=adaptive_engine.difficulty,
            difficulty_label=adaptive_engine.get_difficulty_label(),
            mode_label=mode_cfg["label"],
            mode_description=mode_cfg["description"],
            weakness_target=weakness,
            topic_focus=topic,
        )
        questions.append(q)

    return questions