import yaml

def load_sigma_rule(rule_file):

    with open(rule_file) as f:
        return yaml.safe_load(f)


def match_sigma(event, rule):

    keywords = rule["detection"]["keywords"]

    for keyword in keywords:

        if keyword in event["event_type"]:

            return True

    return False
