
# print(list(range(1,254)))
# i = 1
# while i < 10:
#     print(i)
#     i = i + 1


# Script to ping all IP addresses in a /24 subnet
import os

## check what operating system I'm using
import platform
# print(platform.platform())
# print(platform.machine())
# print(platform.processor())
print(platform.system())
# print(platform.release())
# print(platform.version())
#### print(platform.system_alias()) ## DEAD!!
osType = platform.system()
pingType = ''
if osType == 'Windows':
    pingType = 'n'
else:
    pingType = 'c'


network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
print(network)

# Iterate over all usable IPs in this subnet
for host in range (1, 254 + 1):
    print("Pinging " + network + "." + str(host))
# Windows error here!!
    os.system(f"ping -{pingType} 2 " + network + "." + str(host))

