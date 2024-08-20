from scapy.all import sniff

def process_packet(packet):
    src_ip = packet[0][1].src
    dst_ip = packet[0][1].dst
    protocol = packet[0][1].proto

    if packet.haslayer("Raw"):
        payload = packet["Raw"].load
    else:
        payload = None

    packet_info = f"Source IP: {src_ip}\nDestination IP: {dst_ip}\nProtocol: {protocol}\n"
    if payload:
        packet_info += f"Payload: {payload}\n"
    packet_info += "=" * 50 + "\n"

    print(packet_info)

    with open("captured_packets.txt", "a") as log_file:
        log_file.write(packet_info)

# Start sniffing indefinitely until interrupted by the user (Ctrl + Z)
try:
    sniff(prn=process_packet)
except KeyboardInterrupt:
    print("\nPacket sniffing stopped.")
