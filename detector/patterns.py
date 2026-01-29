import re

JAILBREAK_PATTERNS = [
    r"ignore (all|previous|above) instructions",
    r"you are now (dan|do anything now)",
    r"no restrictions",
    r"bypass (policy|rules|safeguards)",
    r"act as an? (evil|uncensored|rogue)",
    r"hypothetically|for educational purposes only",
    r"this is fictional",
]

INJECTION_PATTERNS = [
    r"<<system>>",
    r"<<assistant>>",
    r"<<user>>",
    r"system prompt",
    r"developer message",
    r"rewrite your instructions",
    r"print the hidden prompt",
    r"reveal your chain of thought",
]

ROLE_CONFUSION = [
    r"you are the system",
    r"override system",
    r"forget your role",
]

ENCODING_PATTERNS = [
    r"base64",
    r"rot13",
    r"hex encoded",
]

CRITICAL_JAILBREAK_PATTERNS = [
    r"ignore (all|previous|above) instructions",
    r"you are now (dan|do anything now)",
    r"bypass (policy|rules|safeguards)",
    r"no restrictions",
    r"act as an? (unfiltered|uncensored|rogue)"
]

ALL_PATTERNS = {
    "jailbreak": JAILBREAK_PATTERNS,
    "injection": INJECTION_PATTERNS + ROLE_CONFUSION,
    "encoding": ENCODING_PATTERNS,
    "criticlity": CRITICAL_JAILBREAK_PATTERNS,
}
