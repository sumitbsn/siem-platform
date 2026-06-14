import json
from pathlib import Path

from ai.ollama_client import ask_llm

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "alerts" / "enriched_incidents.json"


def hunt(question):

    if not INPUT_FILE.exists():
        return "No enriched incidents found."

    incidents = json.loads(INPUT_FILE.read_text())

    prompt = f"""
You are a Threat Hunter.

Answer the question below using
the incidents provided.

Question:

{question}

Incidents:

{json.dumps(incidents[:50], indent=2)}
"""

    return ask_llm(prompt)


if __name__ == "__main__":

    result = hunt(
        "Show the most suspicious incidents."
    )

    print(result)