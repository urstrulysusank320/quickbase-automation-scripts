import os
import requests
import json

# ---- Environment variables ----
realm = os.environ.get("QB_REALM")
token = os.environ.get("QB_USER_TOKEN")

# ---- Table and record info ----
tableId = "bu8bfunx7"
recordId = 1  # can be dynamic
fields_to_update = {
    6: "Document Generated"  # fieldId : newValue (replace with your field IDs)
}

# ---- Headers ----
headers = {
    "QB-Realm-Hostname": realm,
    "Authorization": f"QB-USER-TOKEN {token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# ---- API URL ----
url = f"https://api.quickbase.com/v1/records"

# ---- Body for PATCH request ----
body = {
    "to": tableId,
    "data": [
        {
            "3": {"value": recordId},  # 3 = Record ID field (adjust if needed)
            **{str(k): {"value": v} for k, v in fields_to_update.items()}
        }
    ]
}

# ---- Make PATCH request ----
response = requests.patch(url, headers=headers, json=body)

try:
    response.raise_for_status()
    print("Record updated successfully:")
    print(json.dumps(response.json(), indent=4))
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Error: {e}")
