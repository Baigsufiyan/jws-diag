class RuleEngine:
    def __init__(self, rules):
        self.rules = rules

    def run(self, connectors):
        issues = []

        for rule in self.rules:
            issues.extend(rule.check(connectors))

        return issues