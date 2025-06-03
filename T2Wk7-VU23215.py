
# print(list(range(1,254)))
# i = 1
# while i < 10:
#     print(i)
#     i = i + 1


# Script to ping all IP addresses in a /24 subnet
import os

network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
print(network)

# Iterate over all usable IPs in this subnet
for host in range (1, 254 + 1):
    print("Pinging " + network + "." + str(host))
    os.system("ping -c 2 " + network + "." + str(host))

