import json
from pathlib import Path

ALERT_FILE = Path("alerts/findings.json")

ALERT_FILE.parent.mkdir(exist_ok=True)

if not ALERT_FILE.exists():
    ALERT_FILE.write_text("[]")


def write_finding(alert):

    with open(ALERT_FILE) as f:
        findings = json.load(f)

    findings.append(alert)

    with open(ALERT_FILE, "w") as f:
        json.dump(findings, f, indent=2)
