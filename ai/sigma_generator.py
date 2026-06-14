import json
from pathlib import Path

from ai.ollama_client import ask_llm

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "alerts" / "incidents.json"

OUTPUT_DIR = (
    PROJECT_ROOT
    / "detections"
    / "generated"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

OUTPUT_FILE = (
    OUTPUT_DIR
    / "generated_sigma_rules.yml"
)


def generate_sigma_rule(incident):

    prompt = f"""
You are a Detection Engineer.

Generate a Sigma detection rule for the incident below.

Incident:

{json.dumps(incident, indent=2)}

Requirements:

1. Valid Sigma YAML
2. Add title
3. Add logsource
4. Add detection block
5. Add condition
6. Add MITRE tag if possible

Return ONLY YAML.
"""

    return ask_llm(prompt)


def run():

    if not INPUT_FILE.exists():

        print("incidents.json not found")

        return

    incidents = json.loads(
        INPUT_FILE.read_text()
    )

    if len(incidents) == 0:

        print("No incidents found")

        return

    generated_rules = []

    print(
        f"Generating Sigma rules for "
        f"{len(incidents)} incidents"
    )

    for incident in incidents:

        incident_type = incident.get(
            "incident_type",
            "Unknown Incident"
        )

        print(
            f"Generating Sigma rule for: "
            f"{incident_type}"
        )

        try:

            sigma_rule = generate_sigma_rule(
                incident
            )

            generated_rules.append(
                sigma_rule
            )

        except Exception as e:

            print(
                f"Failed for "
                f"{incident_type}: {e}"
            )

    if not generated_rules:

        print("No Sigma rules generated")

        return

    OUTPUT_FILE.write_text(

        "\n\n---\n\n".join(
            generated_rules
        )

    )

    print(
        f"\nGenerated "
        f"{len(generated_rules)} Sigma rules"
    )

    print(
        f"Saved to:\n{OUTPUT_FILE}"
    )


if __name__ == "__main__":
    run()