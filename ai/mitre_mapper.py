import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "alerts" / "incidents.json"
OUTPUT_FILE = PROJECT_ROOT / "alerts" / "enriched_incidents.json"


MITRE_MAP = {
    "Brute Force": ["T1110"],
    "Port Scan": ["T1046"],
    "Suspicious VPN Login": ["T1078"],
    "High Risk Activity": ["T1078"],
    "Credential Stuffing": ["T1110.004"],
    "Privilege Escalation": ["T1068"]
}


def map_mitre():

    if not INPUT_FILE.exists():
        print("incidents.json not found")
        return

    incidents = json.loads(INPUT_FILE.read_text())

    for incident in incidents:

        incident["mitre_techniques"] = MITRE_MAP.get(
            incident.get("incident_type"),
            ["Unknown"]
        )

    OUTPUT_FILE.write_text(
        json.dumps(incidents, indent=2)
    )

    print(
        f"Mapped MITRE techniques for "
        f"{len(incidents)} incidents"
    )


if __name__ == "__main__":
    map_mitre()