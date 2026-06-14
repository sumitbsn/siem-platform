import json
from pathlib import Path

from ai.ollama_client import ask_llm

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "alerts" / "enriched_incidents.json"
OUTPUT_FILE = PROJECT_ROOT / "alerts" / "executive_report.json"


def generate_report():

    if not INPUT_FILE.exists():
        print("enriched_incidents.json not found")
        return

    incidents = json.loads(INPUT_FILE.read_text())

    if len(incidents) == 0:
        print("No incidents found")
        return

    prompt = f"""
You are a Senior SOC Analyst.

Analyze the incidents below.

Provide:

1. Executive Summary
2. Highest Risk Incidents
3. MITRE ATT&CK Analysis
4. Recommended Actions
5. Investigation Priorities

Incidents:

{json.dumps(incidents[:20], indent=2)}
"""

    print("Sending incidents to Ollama...")

    report = ask_llm(prompt)

    OUTPUT_FILE.write_text(
        json.dumps(
            {
                "executive_report": report
            },
            indent=2
        )
    )

    print("Executive report generated")


if __name__ == "__main__":
    generate_report()