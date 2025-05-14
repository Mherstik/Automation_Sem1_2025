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

print(os.getcwd())   # Get the current working directory

## Filename
filename = 't2wk4.csv'

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
    with open(filename, "x") as f:
        print(f"{filename} created")
        f.write("Name,Age\n")
        print("Headers added")

## Generate data
name = input("Please give me your name: ")
age = int(input("How old are you: "))
## Check if the data already exists
## If DATA exists, warn user.
## Else add DATA to file
# print(f"{name},{age}")
with open(filename, "a") as f:
    f.write(f"{name},{age}\n")
## Exit the application (save file)



