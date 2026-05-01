# ai_core/followup_engine.py

import re
from groq import Groq
import os
from dotenv import load_dotenv
from config import PRIMARY_MODEL

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("prompts/followup_prompt.txt", "r") as f:
    FU_PROMPT_TEMPLATE = f.read()


def generate_followup(
    original_question: str,
    user_answer:       str,
    followup_type:     str,
    weakness_vector:   dict
) -> str:
    """
    Generate one adaptive follow-up probe.
    followup_type: deep_dive | edge_case | scaling | failure
    """
    weakness_summary = ", ".join(
        f"{k}: {v:.0%}" for k, v in
        sorted(weakness_vector.items(), key=lambda x: x[1])[:3]
    ) if weakness_vector else "none"

    prompt = FU_PROMPT_TEMPLATE.format(
        followup_type=followup_type,
        weakness_vector=weakness_summary,
        original_question=original_question,
        user_answer=user_answer
    )

    res = client.chat.completions.create(
        model=PRIMARY_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    fu = res.choices[0].message.content.strip()
    fu = re.sub(r"^[\d\.\-\*\s]+", "", fu).strip()
    if fu and not fu.endswith("?"):
        fu += "?"
    return fu