import os
import requests
import json

# ---- Environment variables (set in GitHub Secrets or locally) ----
realm = os.environ.get("QB_REALM")
token = os.environ.get("QB_USER_TOKEN")

# ---- Template and record info ----
templateId = 3
tableId = "bu8bfunx7"
recordId = 1  # can make dynamic if needed
filename = "xyz"
format_type = "html"
unit = "in"
pageSize = "A4"
orientation = "portrait"
margin = "1 1 1 1"

# ---- Headers for Quickbase API ----
headers = {
    "QB-Realm-Hostname": realm,
    "Authorization": f"QB-USER-TOKEN {token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# ---- Body for POST request ----
body = {
    "tableId": tableId,
    "recordId": recordId,
    "filename": filename,
    "format": format_type,
    "unit": unit,
    "pageSize": pageSize,
    "orientation": orientation,
    "margin": margin
}

# ---- API URL ----
url = f"https://api.quickbase.com/v1/docTemplates/{templateId}/generate"

# ---- Make POST request ----
response = requests.post(url, headers=headers, json=body)

try:
    response.raise_for_status()
    print("Document generated successfully:")
    print(json.dumps(response.json(), indent=4))
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Error: {e}")
