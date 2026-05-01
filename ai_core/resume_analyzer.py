# ai_core/resume_analyzer.py

from groq import Groq
import os
from dotenv import load_dotenv
from config import PRIMARY_MODEL

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_resume(text: str) -> str:
    prompt = f"""
You are a strict Senior Technical Recruiter at a FAANG company evaluating a resume.
Do a DEEP and HONEST analysis. Follow every rule strictly.

=== SKILLS RULES ===
- Extract ONLY real technical tools, frameworks, languages mentioned
- No soft skills

=== STRENGTHS RULES ===
- Only list strengths CLEARLY VISIBLE in the resume
- Must be specific, not generic

=== WEAKNESS DETECTION RULES ===
Check ALL of these:
1. No quantified metrics? → weakness
2. Thin education section? → weakness
3. No GitHub/portfolio URL? → weakness
4. Vague project descriptions? → weakness
5. No team/leadership mention? → weakness
6. No certifications? → weakness
7. Generic professional summary? → weakness
8. Missing soft skills? → weakness
9. Very short work experience? → weakness
10. Technologies listed with no project proof? → weakness

Return at least 2-4 real weaknesses. Do NOT say "Not Mentioned" — name the actual gap.

=== SCORE RULES ===
- Score out of 10
- Deduct for each weakness
- 4+ weaknesses → max score 6

Return ONLY valid raw JSON. No markdown, no backticks, no extra text.

{{
  "skills": [],
  "strengths": [],
  "weaknesses": [],
  "suggestions": [],
  "score": 0
}}

Resume:
{text}
"""
    response = client.chat.completions.create(
        model=PRIMARY_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return response.choices[0].message.content


def is_valid_cv(text: str) -> bool:
    keywords = [
        "education", "experience", "skills", "projects",
        "university", "degree", "resume", "cv",
        "email", "phone", "github", "linkedin"
    ]
    score = sum(1 for w in keywords if w in text.lower())
    return score >= 3