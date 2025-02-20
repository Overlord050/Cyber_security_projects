


## this shit needs work, not working correctly as intended

from scapy.all import sniff, IP, TCP, UDP

# Packet processing function
def process_packet(packet):
    try:
        if packet.haslayer(IP):  # Check if it's an IP packet
            ip_src = packet[IP].src  # Source IP
            ip_dst = packet[IP].dst  # Destination IP
            
            if packet.haslayer(TCP):  # If it's a TCP packet
                protocol = "TCP"
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport
            elif packet.haslayer(UDP):  # If it's a UDP packet
                protocol = "UDP"
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport
            else:
                protocol = "Other"
                src_port = dst_port = "N/A"

            log_entry = f"[+] {ip_src}:{src_port} → {ip_dst}:{dst_port} ({protocol})\n"
            print(log_entry.strip())  # Print packet info

            # Save packet data to a log file
            with open("packets.log", "a") as log:
                log.write(log_entry)

    except Exception as e:
        print(f"Error processing packet: {e}")

# Start sniffing packets
print("Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=False)  # Sniff packets and send them to process_packet()
