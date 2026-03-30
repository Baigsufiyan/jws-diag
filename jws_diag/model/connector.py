class Connector:
    def __init__(self, port, protocol, secure=False, ssl_enabled=False):
        self.port = int(port)
        self.protocol = protocol
        self.secure = secure
        self.ssl_enabled = ssl_enabled

    def __repr__(self):
        return (
            f"Connector(port={self.port}, protocol='{self.protocol}', "
            f"secure={self.secure}, ssl_enabled={self.ssl_enabled})"
        )