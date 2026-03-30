jws-diag

CLI tool to diagnose misconfigurations in Tomcat/JBoss server.xml.

This focuses on common real-world issues like broken TLS setup, incorrect connectors, and reverse proxy misconfiguration. The goal is to surface these problems early instead of debugging them at runtime.

Usage

python main.py analyze server.xml

Checks include

- TLS configuration (protocols, keystore)
- Connector setup (ports, duplicates, security flags)
- Reverse proxy settings
- HTTP to HTTPS redirect
- Logging components

Project structure

jws_diag/
  parser   - XML parsing
  model    - internal representation
  rules    - diagnostics
  output   - CLI/JSON formatting

Status

Work in progress....