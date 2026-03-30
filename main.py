import argparse

def main():
    parser = argparse.ArgumentParser(
        description="jws-diag: Diagnose Tomcat/JBoss server.xml configurations"
    )

    subparsers = parser.add_subparsers(dest="command")

    analyze_parser = subparsers.add_parser(
        "analyze", help="Analyze a server.xml file"
    )
    analyze_parser.add_argument(
        "file", help="Path to server.xml"
    )

    args = parser.parse_args()

    if args.command == "analyze":
        from jws_diag.parser.xml_parser import parse_connectors
        from jws_diag.rules.tls_rule import TLSMisconfigRule
        from jws_diag.rules.port_rule import DuplicatePortRule
        from jws_diag.rules.engine import RuleEngine

        connectors = parse_connectors(args.file)

        print("Connectors found:")
        for c in connectors:
            print(c)

        # Rule engine
        rules = [
            TLSMisconfigRule(),
            DuplicatePortRule(),
        ]

        engine = RuleEngine(rules)
        issues = engine.run(connectors)

        if issues:
            print("\nIssues found:")
            for issue in issues:
                print(f"[{issue['severity']}] {issue['message']}")
                print(f"Fix: {issue['fix']}")
        else:
            print("\nNo issues found.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()