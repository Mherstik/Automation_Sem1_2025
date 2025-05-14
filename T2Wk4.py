###
# Get hostname
import os
import platform
import socket as s

def get_hostname():
    # print(platform.node())
    return platform.node()
    
hostname1 = get_hostname()


def get_hostname2():
    # print(s.gethostname())
    return s.gethostname()

hostname2 = get_hostname2()

### List length check
basicList = [12, 14, 27, 90]
print(len(basicList))

###

#
# Name: Marcus Herstik
# Description: A script to check if a CSV file exists
# and write header and random data as CSV.
#
# Input: Random Data, filename
# Output:
### ComputerName, IP-address, MAC-address, ProcessorModel, OperatingSystem, SystemTime, Internet_connection_speed, Active ports

import os
import csv

## Filename
filename = 't2wk4.csv'

headerList = ['ComputerName',
              'IP-address',
              'MAC-address',
              'ProcessorModel',
              'OperatingSystem',
              'SystemTime',
              'Internet_connection_speed',
              'Active ports'
              ]

## Check if file exists
## If not, create file
## If file exists... delete it!
if os.path.exists(filename):
    print(f"The file {filename} exists.")
#     try:
#         os.remove(filename)
#         print(f"{filename} removed!")
#     except:
#         print("Something went wrong")
    
else:
    print(f"{filename} ain't here!")

## Create file + add header
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headerList)
        writer.writeheader()
    print("Created file and wrote header")
## Add Data
def addData():
    newRow = [hostname1,get_hostname2(), basicList]
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(newRow)
        print("Added row")

addData()
### Read Data
i = 0
with open(filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        i += 1
        print(row)
        print(i)


