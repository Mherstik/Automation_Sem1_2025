import psutil

def net_statistics():
    print("TCP Connections")
    portStat = []
    # get giant list of all ports that are open/available
    connStat = psutil.net_connections(kind='tcp')
    print(connStat)
    input()  # pause for user
    
    # go over the connection information
    for connStat in psutil.net_connections():
        # for each connection find the ones that
        # do NOT have the status of LISTEN
        if connStat.status != 'LISTEN':
            # print just the connection status
            # and the IP address and the port
            print(connStat.status,
                  connStat.laddr.ip,
                  connStat.laddr.port)
    input()  # pause for user
            # portStat.append()
    return portStat, connStat
    
connections = net_statistics()
print(connections)
print(type(connections))

shortList = []
# for each in connections:
#     if status != 'LISTEN':
#         shortList.append()
print()