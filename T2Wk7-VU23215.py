
#### How the range function/type works
# print(list(range(1,254)))
# i = 1
# while i < 10:
#     print(i)
#     i = i + 1


# Script to ping all IP addresses in a /24 subnet
# Only return active hosts

import os
import subprocess
## check what operating system I'm using
import platform

# print(platform.platform())
# print(platform.machine())
# print(platform.processor())
print(platform.system())
# print(platform.release())
# print(platform.version())
#### print(platform.system_alias()) ## DEAD!!
pingType = ''


def getOS():
    global pingType
    osType = platform.system()
    if osType == 'Windows':
        pingType = '-n'
    else:
        pingType = '-c'
    return pingType

## Now lets ping
network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
print(f" Pinging {network}.0/24")

# getOS()

def ping_host(ip_address):
    ping_param = getOS()
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


# Iterate over all usable IPs in this subnet
active_hosts = []

for host in range (200, 215 + 1):  # changed from 254 + 1
    # print("Pinging " + network + "." + str(host))
# Windows error here!! Fixed with checking OS
# Now swapped to a subprocess
    #  os.system(f"ping -{pingType} 2 " + network + "." + str(host)) # swapped to 
    host_address = network + "." + str(host)
    if ping_host(host_address):
        active_hosts.append(host_address)
    # print(f"finished pinging {host_address}\n") # print to finish
        print(f"✓ {host_address}")
print(f"Summary: {len(active_hosts)} active")
print(f" All hosts list is {active_hosts}")