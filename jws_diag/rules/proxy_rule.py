class ProxyMisconfigRule:
    def check(self, connectors):
        issues = []

        for c in connectors:
            # Only check HTTPS connectors
            if c.ssl_enabled:
                # We didn't parse proxyName/Port yet → so simulate for now
                # Future: extend model

                issues.append({
                    "type": "PROXY",
                    "severity": "WARNING",
                    "message": f"Connector on port {c.port} may be missing proxy configuration",
                    "fix": "Set proxyName and proxyPort when using reverse proxy"
                })

        return issues