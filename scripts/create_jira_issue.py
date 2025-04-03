import requests
from requests.auth import HTTPBasicAuth
import json

# Jira account details
email = "vardoshvili.ioseb@gmail.com"
api_token = "ATATT3xFfGF0_HTWaKiG7JjKil9XjgSPyHfq9QIh01MrqoWDJ0KFaF79QfdqEbhYLEI26SZv0sQ2WXPRPHB6k8RCHJb6rmmL13R5I8J7viac7NQEAyl60I4wpl36AmvIMxmTq_1z2TDgDp1cOfJ1XtYwwo1nS5iUPcRUk8IOiOpYW4XhycA7g68=98ED0ED5"
jira_domain = "ivr-testing.atlassian.net"
project_key = "CPG"  # Double-checked from your new project board

# Issue details
summary = "Test Issue from New Jira Site"
description = "This issue was created from Python using the new Jira site and API token."

# Jira API endpoint
url = f"https://{jira_domain}/rest/api/3/issue"

# Request headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Payload
payload = json.dumps({
    "fields": {
        "project": {
            "key": project_key
        },
        "summary": summary,
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": description
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Task"
        }
    }
})


# Authentication
auth = HTTPBasicAuth(email, api_token)

# Send the request
response = requests.post(url, data=payload, headers=headers, auth=auth)

# Result
if response.status_code == 201:
    print("✅ Issue created successfully!")
    print(response.json())
else:
    print(f"❌ Failed to create issue: {response.status_code}")
    print(response.text)
