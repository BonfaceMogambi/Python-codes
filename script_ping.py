import os
response = os.system("ping -c 1 8.8.8.8")
if response == 0:
    print("Network is up")
else:
    print("Network is down")