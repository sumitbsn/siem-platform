import json
from pathlib import Path

from parser.ocsf_mapper import map_to_ocsf

from detections.stateless import (
    detect_high_risk,
    detect_foreign_login
)

from detections.stateful import (
    detect_bruteforce,
    detect_port_scan
)

from findings.writer import write_finding

RAW_DIR = Path("collector/raw_logs")

for file in RAW_DIR.glob("*.json"):

    print(f"Processing {file}")

    with open(file) as f:
        events = json.load(f)

    for event in events:

        normalized = map_to_ocsf(event)

        alerts = [
            detect_high_risk(event),
            detect_foreign_login(event),
            detect_bruteforce(event),
            detect_port_scan(event)
        ]

        for alert in alerts:
            if alert:
                write_finding(alert)

print("Pipeline completed")
