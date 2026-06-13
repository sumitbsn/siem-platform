def map_to_ocsf(event):

    return {
        "class_uid": 1001,
        "category_name": "Security",
        "activity_name": event["event_type"],

        "src_endpoint": {
            "ip": event["source_ip"]
        },

        "dst_endpoint": {
            "ip": event["destination_ip"]
        },

        "user": {
            "name": event["user"]
        },

        "severity_id": event["risk_score"]
    }
