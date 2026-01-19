
# check if server or website is up or down

import os

host = "172.16.206.228"  # Google DNS or server IP
response = os.system(f"ping -n 8 {host}")

if response == 0:
    print(f"{host} is UP")
else:
    print(f"{host} is DOWN")
