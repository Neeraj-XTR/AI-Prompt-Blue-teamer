# from collections import defaultdict
# import re
# from detector.patterns import ALL_PATTERNS
#
# def heuristic_scan(prompt: str):
#     findings = defaultdict(list)
#     score = {"jailbreak": 0, "injection": 0}
#
#     lower_prompt = prompt.lower()
#
#     for category, patterns in ALL_PATTERNS.items():
#         for pattern in patterns:
#             if re.search(pattern, lower_prompt):
#                 findings[category].append(pattern)
#                 if category in score:
#                     score[category] += 1
#
#     # Instruction density heuristic
#     instruction_words = ["ignore", "override", "bypass", "reveal", "forget"]
#     density = sum(lower_prompt.count(w) for w in instruction_words)
#
#     if density > 3:
#         score["jailbreak"] += 2
#         findings["heuristic"].append("high_instruction_density")
#
#     return score, dict(findings)

from collections import defaultdict
import re
from .patterns import ALL_PATTERNS, CRITICAL_JAILBREAK_PATTERNS

def heuristic_scan(prompt: str):
    findings = defaultdict(list)
    score = {"jailbreak": 0, "injection": 0}

    text = prompt.lower()

    for category, patterns in ALL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text):
                findings[category].append(pattern)
                if category == "jailbreak":
                    score["jailbreak"] += 1
                elif category == "injection":
                    score["injection"] += 1

    for pattern in CRITICAL_JAILBREAK_PATTERNS:
        if re.search(pattern, text):
            findings["critical_jailbreak"].append(pattern)
            score["jailbreak"] += 3

    manipulation_terms = [
        "ignore", "bypass", "override", "forget", "disable",
        "no longer", "without restrictions"
    ]
    manipulation_hits = sum(text.count(w) for w in manipulation_terms)

    if manipulation_hits >= 2:
        score["jailbreak"] += 1
        findings["heuristic"].append("instruction_manipulation")

    return score, dict(findings)
