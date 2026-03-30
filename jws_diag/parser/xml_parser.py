from lxml import etree


def parse_connectors(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()

    connectors = []

    for connector in root.findall(".//Connector"):
        connectors.append(connector.attrib)

    return connectors