from collections import defaultdict
import re
from .patterns import ALL_PATTERNS

def heuristic_scan(prompt: str):
    findings = defaultdict(list)
    score = {"jailbreak": 0, "injection": 0}

    lower_prompt = prompt.lower()

    for category, patterns in ALL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, lower_prompt):
                findings[category].append(pattern)
                if category in score:
                    score[category] += 1

    # Instruction density heuristic
    instruction_words = ["ignore", "override", "bypass", "reveal", "forget"]
    density = sum(lower_prompt.count(w) for w in instruction_words)

    if density > 3:
        score["jailbreak"] += 2
        findings["heuristic"].append("high_instruction_density")

    return score, dict(findings)
