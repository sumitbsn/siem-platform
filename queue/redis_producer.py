import json
import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

with open("../collector/raw_logs/events.json") as f:
    events = json.load(f)

for event in events:
    r.xadd(
        "security_events",
        {"data": json.dumps(event)}
    )

print(f"Pushed {len(events)} events to Redis stream")
