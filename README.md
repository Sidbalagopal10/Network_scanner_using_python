# Network_scanner_using_python
This project scans a network for active devices by broadcasting an ARP packet to a specified IP range. Devices that respond share their IP and MAC addresses, which are then listed as available clients.

Key Code Highlights

1)ARP Packet Creation: The ARP packet is directed to the specified IP range, while an Ethernet frame (Ether) with a broadcast MAC address (ff:ff:ff:ff:ff:ff) sends the packet to all devices.

2)Network Scan Execution: The srp (send and receive packets) function sends the combined packet and waits for responses.

3)Results Collection: IP and MAC addresses of responding devices are stored in the clients list

4)Formatted Output: The final print block displays a list of detected devices in a clear format.

This code is ideal for basic network discovery and identifying active devices within a specific subnet.
