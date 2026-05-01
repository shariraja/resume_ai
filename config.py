# config.py

# =========================
# 🔧 MODEL CONFIG
# =========================
PRIMARY_MODEL = "llama-3.1-8b-instant"
JUDGE_MODEL   = "llama-3.1-8b-instant"

MAX_QUESTIONS = 5

# =========================
# 🏢 HIRING MODES
# =========================
HIRING_MODES = {
    "meta": {
        "label": "🏢 Meta Mode",
        "strictness": 0.9,
        "follow_up_aggression": "high",
        "depth_weight": 0.45,
        "description": "Brutal system design + production thinking focus"
    },
    "google": {
        "label": "🔍 Google Mode",
        "strictness": 0.85,
        "follow_up_aggression": "high",
        "depth_weight": 0.40,
        "description": "Algorithms + scalability + clarity"
    },
    "startup": {
        "label": "⚡ Startup Mode",
        "strictness": 0.6,
        "follow_up_aggression": "medium",
        "depth_weight": 0.30,
        "description": "Speed + product thinking + pragmatism"
    }
}

# =========================
# 📊 DIFFICULTY LEVELS
# =========================
DIFFICULTY_LEVELS = {
    1: "Basic ML / API concepts",
    2: "System design medium",
    3: "FAANG LLD",
    4: "Meta/Google production system",
    5: "Unknown scenario / research level"
}

# =========================
# ⚖️ MULTI-AGENT WEIGHTS
# =========================
AGENT_WEIGHTS = {
    "technical": 0.40,
    "depth":     0.40,
    "bar_raiser": 0.20
}

# =========================
# 📈 FINAL SCORE FORMULA WEIGHTS
# =========================
FINAL_SCORE_WEIGHTS = {
    "interview":        0.50,
    "followup_depth":   0.20,
    "consistency":      0.15,
    "improvement_slope": 0.15
}

# =========================
# 🎯 RUBRIC MAX POINTS
# =========================
RUBRIC = {
    "correctness":     4,
    "depth":           3,
    "edge_cases":      2,
    "system_thinking": 2,
    "communication":   2
}
RUBRIC_TOTAL = sum(RUBRIC.values())  # 13 → normalized to /10