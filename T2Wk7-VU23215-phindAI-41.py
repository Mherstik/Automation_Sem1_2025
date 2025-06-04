import platform
import subprocess

def ping_host(ip_address):
    """Ping a host and return True if it's active"""
    os_type = platform.system()
    ping_param = '-n' if os_type == 'Windows' else '-c'
    
    try:
        result = subprocess.run(['ping', ping_param, '2', ip_address],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True,
                              timeout=2)
        
        return result.returncode == 0
    
    except subprocess.TimeoutExpired:
        return False
    except Exception as e:
        print(f"Error pinging {ip_address}: {str(e)}")
        return False

def scan_network():
    """Scan a network range for active hosts"""
    network = input("Enter first 3 numbers of IP network (e.g., 192.168.1): ")
    active_hosts = []

    print(f"\nScanning network {network}.0/24...")
    print("Active hosts:")
    print("-" * 20)

    for host in range(200, 216):  # Changed from 254+1 to match original range
        current_ip = f"{network}.{host}"
        if ping_host(current_ip):
            active_hosts.append(current_ip)
            print(f"✓ {current_ip}")

    print("\nSummary:")
    print(f"Total active hosts found: {len(active_hosts)}")

if __name__ == "__main__":
    scan_network()