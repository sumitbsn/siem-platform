import json
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "alerts" / "findings.json"
OUTPUT_FILE = PROJECT_ROOT / "alerts" / "incidents.json"


def build_incidents():

    if not INPUT_FILE.exists():
        print("findings.json not found")
        return

    findings = json.loads(INPUT_FILE.read_text())

    groups = defaultdict(list)

    for finding in findings:

        key = (
            finding.get("alert", "unknown"),
            finding.get("source_ip", "unknown")
        )

        groups[key].append(finding)

    incidents = []

    for (alert, source_ip), alerts in groups.items():

        incident = {
            "incident_type": alert,
            "source_ip": source_ip,
            "alert_count": len(alerts),
            "sample_alerts": alerts[:10]
        }

        incidents.append(incident)

    OUTPUT_FILE.write_text(
        json.dumps(incidents, indent=2)
    )

    print(f"Created {len(incidents)} incidents")


if __name__ == "__main__":
    build_incidents()