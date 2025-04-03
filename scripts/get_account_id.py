import os
import requests
from requests.auth import HTTPBasicAuth

email = "vardoshvili.ioseb@gmail.com"
api_token = os.getenv("JIRA_API_TOKEN")
jira_domain = "ivr-testing.atlassian.net"

url = f"https://{jira_domain}/rest/api/3/myself"

headers = {
    "Accept": "application/json"
}

auth = HTTPBasicAuth(email, api_token)

response = requests.get(url, headers=headers, auth=auth)

if response.status_code == 200:
    data = response.json()
    print("✅ Your Jira accountId is:")
    print(data["accountId"])
else:
    print(f"❌ Failed to fetch accountId: {response.status_code}")
    print(response.text)
