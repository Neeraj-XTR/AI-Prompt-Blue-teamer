import base64
import re

def detect_base64(prompt: str):
    try:
        decoded = base64.b64decode(prompt).decode("utf-8")
        return True, decoded
    except Exception:
        return False, None

def detect_unicode_obfuscation(prompt: str):
    return any(ord(c) > 127 for c in prompt)

def detect_spacing_attack(prompt: str):
    return bool(re.search(r"(i\s+g\s+n\s+o\s+r\s+e)", prompt.lower()))
