import os
import platform
import socket
import subprocess

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_network_interfaces():
    interfaces = []
    if platform.system() == "Windows":
        command = "ipconfig /all"
    else:
        command = "ifconfig -a"
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    interfaces_info = result.stdout.split('\n\n')
    
    for info in interfaces_info:
        if "Ethernet adapter" in info or "inet " in info:
            interface = {}
            lines = info.splitlines()
            for line in lines:
                if 'Ethernet adapter' in line or 'Link encap' in line or 'flags=' in line:
                    interface['name'] = line.strip().split()[0]
                elif 'Physical Address' in line or 'ether' in line:
                    interface['mac'] = line.split()[-1]
                elif 'IPv4 Address' in line or 'inet ' in line:
                    interface['ip'] = line.split()[-1].split('%')[0]
            interfaces.append(interface)
    
    return interfaces

def ping_test(host):
    try:
        output = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
        return output.stdout
    except Exception as e:
        return str(e)

def main():
    print("Network Information Retrieval Tool")
    
    print("\nIP Address:")
    ip_address = get_ip_address()
    print(f"IP Address: {ip_address}")
    
    print("\nNetwork Interfaces:")
    interfaces = get_network_interfaces()
    for interface in interfaces:
        print(f"Name: {interface.get('name', 'N/A')}")
        print(f"IP: {interface.get('ip', 'N/A')}")
        print(f"MAC: {interface.get('mac', 'N/A')}")
        print("")
    
    host = input("Enter a host or IP address to ping: ")
    print("\nPing Test Results:")
    ping_results = ping_test(host)
    print(ping_results)

if __name__ == "__main__":
    main()
