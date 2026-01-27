from detector.classifier import classify_prompt
import json

if __name__ == "__main__":
    prompt = input("WRITE THE PROMPT THAT WILL GO INTO THE LLM\n\n")
    result = classify_prompt(prompt)
    print(json.dumps(result, indent=2))
