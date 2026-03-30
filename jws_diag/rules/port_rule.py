class DuplicatePortRule:
    def check(self, connectors):
        issues = []
        seen_ports = set()

        for c in connectors:
            if c.port in seen_ports:
                issues.append({
                    "type": "PORT",
                    "severity": "ERROR",
                    "message": f"Duplicate port detected: {c.port}",
                    "fix": "Ensure each connector uses a unique port"
                })
            else:
                seen_ports.add(c.port)

        return issues