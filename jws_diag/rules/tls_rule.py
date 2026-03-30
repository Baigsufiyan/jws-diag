class TLSMisconfigRule:
    def check(self, connectors):
        issues = []

        for c in connectors:
            if c.ssl_enabled and not c.secure:
                issues.append({
                    "type": "TLS",
                    "severity": "ERROR",
                    "message": f"Connector on port {c.port} has SSL enabled but not marked secure",
                    "fix": "Set secure='true' for HTTPS connectors"
                })

        return issues