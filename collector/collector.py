import requests
import json
from pathlib import Path

BASE_URL = "http://localhost:8000/events"

offset = 0
limit = 100

RAW_DIR = Path("raw_logs")
RAW_DIR.mkdir(exist_ok=True)

all_events = []

while True:

    try:
        response = requests.get(
            BASE_URL,
            params={
                "offset": offset,
                "limit": limit
            },
            timeout=10
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code != 200:
            print("API Error:")
            print(response.text)
            break

        data = response.json()

        # Debug output
        print("Response Keys:", list(data.keys()))

        events = data.get("events", [])

        if not events:
            print("No more events found.")
            break

        all_events.extend(events)

        offset += len(events)

        print(
            f"Collected {len(events)} events "
            f"(Total: {len(all_events)})"
        )

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        break

    except json.JSONDecodeError:
        print("Invalid JSON received:")
        print(response.text)
        break

with open(RAW_DIR / "events.json", "w") as f:
    json.dump(all_events, f, indent=2)

print(f"\nCollected {len(all_events)} total events")
print(f"Saved to {RAW_DIR / 'events.json'}")