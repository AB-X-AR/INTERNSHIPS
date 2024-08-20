**Overview**


This program captures and analyzes network packets, displaying key details such as source IP, destination IP, protocol, and payload data. It saves the captured packet information to a file for later review.

**How It Works**


- Packet Capture: The program uses the scapy library to capture network packets in real-time.
- Packet Processing: Each packet is analyzed to extract:
- Source IP address
- Destination IP address
- Protocol used
- Payload data (if available)
- Logging: The captured packet information is saved to captured_packets.txt for later review.
- User Input: The program runs indefinitely, capturing packets until interrupted by the user with Ctrl + Z or Ctrl + C .


**Usage Example**


1. Install the necessary library with the command: pip install scapy.
2. Run the program.
3. The program will start capturing network packets and display the packet details in the terminal.
4. It will also save the packet details to captured_packets.txt.
5. Press Ctrl + Z or Ctrl + C to stop the packet capture process.
