jws-diag

CLI tool to analyze Apache Tomcat server.xml and detect common misconfigurations.

Covers:
- TLS issues (SSL enabled but not secure)
- Duplicate ports
- Basic reverse proxy misconfig

Usage:

python main.py analyze test.xml

Example:

[ERROR] Connector on port 8443 has SSL enabled but not marked secure  
Fix: Set secure="true"

[ERROR] Duplicate port detected: 8080  
Fix: Ensure each connector uses a unique port

[WARNING] Connector on port 8443 may be missing proxy configuration  
Fix: Set proxyName and proxyPort