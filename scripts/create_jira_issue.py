import os
import requests
from requests.auth import HTTPBasicAuth
import json

# Load Jira API token securely from environment variable
api_token = os.getenv("JIRA_API_TOKEN")
if not api_token:
    raise EnvironmentError("⚠️ Environment variable JIRA_API_TOKEN is not set.")

# Jira account details
email = "vardoshvili.ioseb@gmail.com"
jira_domain = "ivr-testing.atlassian.net"
project_key = "CPG"

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
        "project": {"key": project_key},
        "summary": summary,
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": description}]
                }
            ]
        },
        "issuetype": {"name": "Task"},
        "assignee": {
            "id": "712020:ee71cb31-3db9-4262-a4b9-98d3a760ab75"
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
