def detect_high_risk(event):

    if event["risk_score"] > 80:

        return {
            "alert": "High Risk Activity",
            "event": event
        }


def detect_foreign_login(event):

    suspicious = ["Germany", "Brazil"]

    if (
        event["event_type"] == "vpn_login"
        and event["country"] in suspicious
    ):

        return {
            "alert": "Suspicious Foreign VPN Login",
            "country": event["country"],
            "event": event
        }
