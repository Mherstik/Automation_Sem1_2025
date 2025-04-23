#!
# Author: Marcus Herstik
# Date: 20250423
# Oi idiot... read this!!
import os			# interacting with operating system
import sys			# for getting system information
import time			# used for timing
import requests  	# used to download a file


# print(os.path.dirname(sys.executable))
# print(sys.executable)

## What is a speedtest??
## How to get download speed??
# Start a stopwatch = get the current time
start = time.time()

# Download a file
# time.sleep(2)
url = "https://github.com/Mherstik/Automation_Sem1_2025/blob/main/20MB.zip"
filename = "filename.zip"
### SAVING
# with open("filename.zip", mode="wb") as file:
#     for chunk in response.iter_content(chunk_size=10 * 1024):
#         file.write(chunk)
try:
    response = requests.get(url) #  , stream=True)
    response.raise_for_status()
    with open(filename, mode="w") as file:
        file.write(response.content.decode('utf - 8'))
except requests.exceptions.RequestException as e:
    print(f'Error occurred: {e}')
    
# Stop the stopwatch
end = time.time()

# How long did it take = finish time - start time.
dltime = end - start

# Calculate download speed = time vs file size.
# Filesize = 20MB * 8 = 160Mb
dlspeed = 160 / dltime
#print(int(dlspeed))
round_dlspeed = round(dlspeed,1)
print("Download speed = ", round_dlspeed, "Mbps")


