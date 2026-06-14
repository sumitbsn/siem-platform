import json
from pathlib import Path

from parser.ocsf_mapper import map_to_ocsf

from detections.sigma_engine import run_sigma

from detections.stateless import (
    detect_high_risk,
    detect_foreign_login
)

from detections.stateful import (
    detect_bruteforce,
    detect_port_scan
)

from findings.writer import write_finding

# AI Pipeline
from ai.incident_builder import build_incidents
from ai.mitre_mapper import map_mitre
from ai.ai_incident_analyzer import generate_report
from ai.sigma_generator import run as generate_sigma_rules


RAW_DIR = Path("collector/raw_logs")
FINDINGS_FILE = Path("alerts/findings.json")


def clear_previous_findings():

    if FINDINGS_FILE.exists():

        FINDINGS_FILE.unlink()

        print("Removed old findings.json")


def run_detection_pipeline():

    total_events = 0
    total_alerts = 0

    for file in RAW_DIR.glob("*.json"):

        print(f"\nProcessing {file}")

        with open(file) as f:
            events = json.load(f)

        print(f"Loaded {len(events)} events")

        for event in events:

            total_events += 1

            normalized = map_to_ocsf(event)

            alerts = []

            # Sigma Rules
            sigma_alerts = run_sigma(normalized)

            alerts.extend(sigma_alerts)

            # Stateless + Stateful
            alerts.extend([

                detect_high_risk(event),

                detect_foreign_login(event),

                detect_bruteforce(event),

                detect_port_scan(event)

            ])

            for alert in alerts:

                if alert:

                    write_finding(alert)

                    total_alerts += 1

    print("\nDetection Pipeline Complete")
    print(f"Total Events Processed : {total_events}")
    print(f"Total Alerts Generated : {total_alerts}")


def run_ai_pipeline():

    print("\n" + "=" * 60)
    print("Starting AI Pipeline")
    print("=" * 60)

    print("\nStep 1: Building Incidents")
    build_incidents()

    print("\nStep 2: Mapping MITRE Techniques")
    map_mitre()

    print("\nStep 3: Generating Executive Report")
    generate_report()

    print("\nStep 4: Generating Sigma Rules")
    generate_sigma_rules()

    print("\nAI Pipeline Complete")


def main():

    print("=" * 60)
    print("SIEM Platform Starting")
    print("=" * 60)

    clear_previous_findings()

    run_detection_pipeline()

    try:

        run_ai_pipeline()

    except Exception as e:

        print("\nAI Pipeline Failed")

        print(str(e))

        print(
            "\nDetection pipeline completed successfully."
            "\nCheck Ollama configuration if AI stages failed."
        )

    print("\n" + "=" * 60)
    print("SIEM Platform Completed")
    print("=" * 60)


if __name__ == "__main__":
    main()