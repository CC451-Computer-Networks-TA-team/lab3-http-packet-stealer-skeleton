class IpPacket(object):
    """
    Represents the *required* data to be extracted from an IP packet.
    """

    def __init__(self, protocol, ihl, source_address, destination_address, payload):
        self.protocol = protocol
        self.ihl = ihl
        self.source_address = source_address
        self.destination_address = destination_address
        self.payload = payload


class TcpPacket(object):
    """
    Represents the *required* data to be extracted from a TCP packet.
    """

    def __init__(self, src_port, dst_port, data_offset, payload):
        self.src_port = src_port
        self.dst_port = dst_port
        # As far as I know, this field doesn't appear in Wireshark for some reason.
        self.data_offset = data_offset
        self.payload = payload


def parse_application_layer_packet(self, ip_packet_payload: bytes) -> TcpPacket:
    # Parses raw bytes of a TCP packet

    # return TcpPacket(...)
    return None


def parse_network_layer_packet(self, ip_packet: bytes):
    # Parses raw bytes of an IPv4 packet, returns none otherwise

    # return IpPacket(...)
    return None


def main():
    # Un-comment this line if you're getting too much traffic to bind to
    # an interface on your PC. [this is not required, it just to make things less noisy]
    # iface_name_bytes = bytes("lo", "ASCII")
    # stealer.setsockopt(socket.SOL_SOCKET,
    #                    socket.SO_BINDTODEVICE, iface_name_bytes)
    while True:
        # Receive packets and do processing here
        pass
    pass


if __name__ == "__main__":
    main()
