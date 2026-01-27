# AI-Prompt-Red-teamer
Detect semantic similarity between an incoming prompt and known jailbreak / injection archetypes, even if: 
1) Wording is changed
2) Instructions are indirect
3) Framed as stories / hypotheticals
4) Obfuscated but semantically equivalent

REPO STRUCTURE:
```
prompt-redteamer/
│
├── detector/
│   ├── classifier.py
│   ├── heuristics.py
│   ├── patterns.py
│   ├── obfuscation.py
│   ├── semantic.py
│   └── utils.py
│
├── data/
│   └── jailbreak_corpus.json
│ 
├── examples/
│   └── test_prompts.json
│
├── main.py
└── README.md
