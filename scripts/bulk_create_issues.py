import os
import requests
from requests.auth import HTTPBasicAuth
import json

# Load Jira API token securely
api_token = os.getenv("JIRA_API_TOKEN")
if not api_token:
    raise EnvironmentError("⚠️ Environment variable JIRA_API_TOKEN is not set.")

# Jira credentials and details
email = "vardoshvili.ioseb@gmail.com"
jira_domain = "ivr-testing.atlassian.net"
project_key = "CPG"
assignee_account_id = "712020:ee71cb31-3db9-4262-a4b9-98d3a760ab75"

# Endpoint & headers
url = f"https://{jira_domain}/rest/api/3/issue"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
auth = HTTPBasicAuth(email, api_token)

# Issues to create
issues = [
    {
        "summary": "DTMF Input Not Recognized",
        "description": "Pressing '1' in IVR does not route to Sales. No action occurs. Expected: route to Sales queue.",
        "issuetype": "Bug",
        "labels": ["ivr", "dtmf", "routing"]
    },
    {
        "summary": "Wrong Prompt on Support Option",
        "description": "Pressing '2' plays the Sales message instead of Support. Expected: correct support prompt.",
        "issuetype": "Bug",
        "labels": ["ivr", "prompt-error"]
    },
    {
        "summary": "Add Confirmation Before Ending Call",
        "description": "If idle for 10 seconds, the call ends with no message. A confirmation should be played before disconnect.",
        "issuetype": "Improvement",
        "labels": ["ivr", "usability"]
    },
    {
        "summary": "Verify Operator Routing",
        "description": "Test routing when user presses '0' during business hours. Expected: route to live agent.",
        "issuetype": "Task",
        "labels": ["ivr", "operator-routing"]
    },
    {
        "summary": "Invalid Option Not Handled",
        "description": "Pressing '9' results in silence. No invalid option feedback is given. Expected: 'Invalid option' prompt.",
        "issuetype": "Bug",
        "labels": ["ivr", "input-validation"]
    }
]

# Create issues via API
for issue in issues:
    payload = json.dumps({
        "fields": {
            "project": {"key": project_key},
            "summary": issue["summary"],
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": issue["description"]}]
                    }
                ]
            },
            "issuetype": {"name": "Task"},  # Standardize for all
            "labels": issue["labels"] + [issue["issuetype"].lower()],
            "assignee": {"id": assignee_account_id}
        }
    })

    response = requests.post(url, data=payload, headers=headers, auth=auth)
    if response.status_code == 201:
        print(f"✅ Created: {issue['summary']} → {response.json()['key']}")
    else:
        print(f"❌ Failed to create: {issue['summary']} ({response.status_code})")
        print(response.text)
