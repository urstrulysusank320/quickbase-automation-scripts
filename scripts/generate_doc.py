import os, requests, json

realm = os.environ["QB_REALM"]
token = os.environ["QB_USER_TOKEN"]

headers = {
    "QB-Realm-Hostname": realm,
    "Authorization": f"QB-USER-TOKEN {token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

url = "https://api.quickbase.com/v1/docTemplates/3/generate"
body = { "tableId": "bu8bfunx7", "recordId": 1, "filename": "xyz", "format": "html" }

r = requests.post(url, headers=headers, json=body)
print(r.json())
