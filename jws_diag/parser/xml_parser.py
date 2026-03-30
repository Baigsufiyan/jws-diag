from lxml import etree
from jws_diag.model.connector import Connector


def parse_connectors(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()

    connectors = []

    for conn in root.findall(".//Connector"):
        port = conn.attrib.get("port")
        protocol = conn.attrib.get("protocol", "HTTP/1.1")
        secure = conn.attrib.get("secure", "false").lower() == "true"
        ssl_enabled = conn.attrib.get("SSLEnabled", "false").lower() == "true"

        connector_obj = Connector(
            port=port,
            protocol=protocol,
            secure=secure,
            ssl_enabled=ssl_enabled
        )

        connectors.append(connector_obj)

    return connectors