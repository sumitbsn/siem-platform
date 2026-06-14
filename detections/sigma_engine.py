import yaml
from pathlib import Path

SIGMA_DIRS = [
    Path("detections/sigma_rules"),
    Path("detections/custom")
]


def load_rules():

    rules = []

    for directory in SIGMA_DIRS:

        if not directory.exists():
            continue

        for file in directory.glob("*.yml"):

            with open(file) as f:

                try:
                    rules.append(
                        yaml.safe_load(f)
                    )

                except Exception as e:

                    print(
                        f"Failed loading {file}: {e}"
                    )

    return rules


RULES = load_rules()


def run_sigma(event):

    alerts = []

    for rule in RULES:

        detection = rule.get(
            "detection",
            {}
        )

        keywords = detection.get(
            "keywords",
            []
        )

        event_text = str(event).lower()

        if any(
            keyword.lower() in event_text
            for keyword in keywords
        ):

            alerts.append({

                "alert":
                    rule.get(
                        "title",
                        "Sigma Match"
                    ),

                "rule_id":
                    rule.get(
                        "id",
                        "unknown"
                    ),

                "severity":
                    rule.get(
                        "level",
                        "medium"
                    ),

                "event":
                    event

            })

    return alerts