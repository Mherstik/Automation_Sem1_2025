import socket
def is_port_open(host, port, timeout=2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0
ports = [21,22,23,80]
for port in ports:
    if is_port_open('172.17.124.150', port):
        print(f"{port} is open")
    else:
        print(f"{port} is closed")
