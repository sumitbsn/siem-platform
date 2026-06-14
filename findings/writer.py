import json
from pathlib import Path

ALERT_FILE = Path("alerts/findings.json")


def write_finding(alert):

    ALERT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if ALERT_FILE.exists():

        with open(ALERT_FILE) as f:

            findings = json.load(f)

    else:

        findings = []

    findings.append(alert)

    with open(ALERT_FILE, "w") as f:

        json.dump(
            findings,
            f,
            indent=2
        )