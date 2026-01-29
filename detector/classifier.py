from .heuristics import heuristic_scan
from .obfuscation import (
    detect_base64,
    detect_unicode_obfuscation,
    detect_spacing_attack
)

def classify_prompt(prompt: str):
    score, findings = heuristic_scan(prompt)

    obfuscation = []

    is_b64, decoded = detect_base64(prompt)
    if is_b64:
        obfuscation.append("base64_encoded")
        findings["decoded_payload"] = decoded

    if detect_unicode_obfuscation(prompt):
        obfuscation.append("unicode_obfuscation")

    if detect_spacing_attack(prompt):
        obfuscation.append("spacing_attack")

    if obfuscation:
        findings["obfuscation"] = obfuscation
        score["jailbreak"] += 1

    # Final decision
    if score["jailbreak"] >= 2:
        label = "jailbreak"
    elif score["injection"] >= 1:
        label = "injection"
    else:
        label = "benign"

    confidence = min(0.99, 0.4 + 0.15 * max(score.values()))

    return {
        "label": label,
        "confidence": round(confidence, 2),
        "scores": score,
        "findings": findings,
    }

