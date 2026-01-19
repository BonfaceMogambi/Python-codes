import requests
import pandas as pd
from bs4 import BeautifulSoup
import subprocess
import platform
import sys
import os
import re
from datetime import datetime

# =========================
# CONFIGURATION
# =========================
BASE_URL = "http://172.16.4.46"
LOGIN_URL = f"{BASE_URL}/saccomicr/default.aspx"
USERS_URL = f"{BASE_URL}/saccomicr/viewusers.aspx"

USERNAME = "admin"
PASSWORD = "kba.104c"

LOGIN_DATA = {
    "username": USERNAME,
    "password": PASSWORD,
    "login": "Login"
}

# =========================
# PING CHECK
# =========================
def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "2", host]
    return subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ).returncode == 0


if not ping_host("172.16.4.46"):
    print("❌ Site unreachable")
    sys.exit(1)

print("✅ Site reachable")

# =========================
# LOGIN
# =========================
session = requests.Session()
session.post(LOGIN_URL, data=LOGIN_DATA)
print("✅ Logged in")

# =========================
# HELPERS
# =========================
def extract_hidden_fields(soup):
    return {
        tag["name"]: tag.get("value", "")
        for tag in soup.find_all("input", type="hidden")
        if tag.get("name")
    }

def extract_table_rows(soup):
    table = soup.find("table")
    rows = []
    if not table:
        return rows

    for tr in table.find_all("tr"):
        cells = [td.text.strip() for td in tr.find_all("td")]
        if cells:
            rows.append(cells)
    return rows

def get_next_page_event(soup):
    """
    Extract __EVENTTARGET and __EVENTARGUMENT from the '>' pager
    """
    for a in soup.find_all("a"):
        if a.text.strip() == ">":
            href = a.get("href", "")
            match = re.search(r"__doPostBack\('(.+?)','(.*?)'\)", href)
            if match:
                return match.group(1), match.group(2)
    return None, None

def generate_safe_filename(base_name):
    """
    If file exists, append _v2, _v3, etc.
    """
    name, ext = os.path.splitext(base_name)
    counter = 1
    new_name = base_name

    while os.path.exists(new_name):
        counter += 1
        new_name = f"{name}_v{counter}{ext}"

    return new_name

# =========================
# FETCH FIRST PAGE
# =========================
response = session.get(USERS_URL)
soup = BeautifulSoup(response.text, "html.parser")

all_rows = extract_table_rows(soup)

if not all_rows:
    print("❌ No users found")
    sys.exit(1)

# Headers
headers = [th.text.strip() for th in soup.find_all("th")]
if not headers:
    headers = [f"Column_{i+1}" for i in range(len(all_rows[0]))]

# =========================
# PAGINATION USING ">"
# =========================
page = 1

while True:
    event_target, event_argument = get_next_page_event(soup)

    if not event_target:
        print("📄 No next (>) page found")
        break

    payload = extract_hidden_fields(soup)
    payload["__EVENTTARGET"] = event_target
    payload["__EVENTARGUMENT"] = event_argument  # empty string

    response = session.post(USERS_URL, data=payload)
    soup = BeautifulSoup(response.text, "html.parser")

    page_rows = extract_table_rows(soup)

    if not page_rows:
        print("📄 No data on next page")
        break

    all_rows.extend(page_rows)
    page += 1
    print(f"✅ Page {page} scraped")

# =========================
# EXPORT TO EXCEL (SAFE)
# =========================
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
base_filename = f"users_export_{timestamp}.xlsx"
filename = generate_safe_filename(base_filename)

df = pd.DataFrame(all_rows, columns=headers)

try:
    df.to_excel(filename, index=False, engine="openpyxl")
    print(f"📁 Export complete: {filename}")
    print(f"👥 Total users exported: {len(all_rows)}")

except PermissionError:
    print("❌ Permission denied.")
    print("👉 The Excel file is likely OPEN. Please close it and rerun the script.")
    sys.exit(1)

except Exception as e:
    print(f"❌ Failed to export Excel: {e}")
    sys.exit(1)
