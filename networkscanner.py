from scapy.all import ARP, Ether, srp, conf
import sys

def scan_network(target_ip, interface=None):
    try:
        # Set interface if provided
        if interface:
            conf.iface = interface

        # Create ARP packet
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        # Send the packet and receive responses
        result = srp(packet, timeout=3, verbose=0)[0]

        clients = []

        for sent, received in result:
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})

        # Print the result
        print("Available devices in the network:")
        print("IP" + " " * 18 + "MAC")
        for client in clients:
            print("{:16}    {}".format(client['ip'], client['mac']))

        if not clients:
            print("\nNo devices found. Make sure target IP/subnet is reachable.")

    except PermissionError:
        print("Error: Run this script as administrator/root (use sudo).")
    except Exception as e:
        print(f"An error occurred: {e}")

# Change this to your subnet (e.g., "192.168.29.0/24")
target_ip_range = "enter ip range"

# Optional: Set this if you have multiple interfaces (e.g., "eth0", "wlan0")
network_interface = "enter type of network interface"

scan_network(target_ip_range, network_interface)
