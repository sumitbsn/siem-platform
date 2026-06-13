import json
import uuid
import random
from datetime import datetime, timedelta

events = []

base_time = datetime.utcnow()

event_types = [
    "login_success",
    "login_failed",
    "process_start",
    "port_scan",
    "vpn_login",
    "firewall_allow",
    "firewall_deny"
]

for i in range(10000):

    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": (
            base_time + timedelta(seconds=i)
        ).isoformat(),

        "event_type": random.choice(event_types),

        "user": random.choice([
            "admin",
            "john",
            "alice",
            "svc_backup"
        ]),

        "source_ip":
            f"10.{random.randint(0,255)}."
            f"{random.randint(0,255)}."
            f"{random.randint(1,254)}",

        "destination_ip":
            f"172.16.{random.randint(0,255)}."
            f"{random.randint(1,254)}",

        "risk_score":
            random.randint(0,100),

        "country":
            random.choice([
                "India",
                "Germany",
                "Brazil",
                "USA"
            ])
    }

    events.append(event)

with open("events.json", "w") as f:
    json.dump(events, f, indent=2)

print("Generated 10000 events")
