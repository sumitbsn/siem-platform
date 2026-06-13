from collections import defaultdict

failed_logins = defaultdict(int)

ports_hit = defaultdict(set)


def detect_bruteforce(event):

    if event["event_type"] == "login_failed":

        ip = event["source_ip"]

        failed_logins[ip] += 1

        if failed_logins[ip] >= 5:

            return {
                "alert": "Possible Brute Force Attack",
                "source_ip": ip,
                "count": failed_logins[ip]
            }


def detect_port_scan(event):

    if event["event_type"] == "port_scan":

        ip = event["source_ip"]

        target = event["destination_ip"]

        ports_hit[ip].add(target)

        if len(ports_hit[ip]) >= 10:

            return {
                "alert": "Possible Port Scan",
                "source_ip": ip
            }
