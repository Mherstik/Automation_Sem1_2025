import socket
import ssl
from ftplib import FTP
import paramiko
import requests
from urllib.parse import urlparse

class PortScanner:
    def __init__(self):
        self.protocols = {
            'ftp': {'port': 21, 'protocol': 'TCP', 'method': self.scan_ftp},
            'telnet': {'port': 23, 'protocol': 'TCP', 'method': self.scan_telnet},
            'ssh': {'port': 22, 'protocol': 'TCP', 'method': self.scan_ssh},
            'http': {'port': 80, 'protocol': 'TCP', 'method': self.scan_http}
        }
    
    def scan_ftp(self, host):
        """Scan FTP port and retrieve welcome message"""
        try:
            with FTP(host) as ftp:
                welcome = ftp.getwelcome()
                return f"FTP Server Response:\n{welcome}"
        except Exception as e:
            return f"FTP scan failed: {str(e)}"
    
    def scan_telnet(self, host):
        """Scan Telnet port and retrieve banner"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((host, 23))
                banner = s.recv(1024).decode('utf-8', errors='ignore')
                return f"Telnet Banner:\n{banner}"
        except Exception as e:
            return f"Telnet scan failed: {str(e)}"
    
    def scan_ssh(self, host):
        """Scan SSH port and retrieve server information"""
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port=22, username='kali', password='', 
                       look_for_keys=False, allow_agent=False)
            transport = ssh.get_transport()
            return f"SSH Server Info:\n{transport.get_remote_server_key()}"
        except Exception as e:
            return f"SSH scan failed: {str(e)}"
    
    def scan_http(self, host):
        """Scan HTTP port and retrieve server information"""
        try:
            url = f"http://{host}"
            response = requests.get(url, timeout=5)
            return f"HTTP Server Response:\nStatus: {response.status_code}\n" \
                   f"Headers: {dict(response.headers)}"
        except Exception as e:
            return f"HTTP scan failed: {str(e)}"
    
    def scan_host(self, host):
        """Scan all supported protocols on a host"""
        results = {}
        for protocol, info in self.protocols.items():
            results[protocol] = info['method'](host)
        return results

def main():
    scanner = PortScanner()
    host = input("Enter the host IP or hostname to scan: ")
    results = scanner.scan_host(host)
    
    print("\nScan Results:")
    print("-" * 50)
    for protocol, result in results.items():
        print(f"\n{protocol.upper()} ({scanner.protocols[protocol]['port']}):")
        print(result)
        print("-" * 50)

if __name__ == "__main__":
    main()