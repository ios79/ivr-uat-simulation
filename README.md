# IVR UAT Simulation 🎧📞

This project simulates a real-world **User Acceptance Testing (UAT)** process for an IVR (Interactive Voice Response) system, integrating **Python automation** with **Jira Cloud** for issue tracking.

---

## 🚀 Features

- 📌 Auto-creates Jira issues for IVR test cases
- ✅ Assigns issues automatically to the tester (you)
- 🔐 Uses secure environment variables for API tokens
- 📂 Organized folder structure (`scripts/`, `logs/`, `assets/screenshots/`)
- 🧠 Demonstrates real QA/UAT automation workflow

---

## 📁 Project Structure

```plaintext
ivr-uat-simulation/
├── scripts/
│   ├── create_jira_issue.py       # Creates one Jira issue
│   ├── bulk_create_issues.py      # Creates multiple issues at once
│   └── get_account_id.py          # Fetch your Jira account ID
├── logs/
│   └── interaction_log.txt        # (Optional) logging test activity
├── call_flows/
│   └── sample_call_flow.json      # (Optional) for voice test scripting
├── assets/screenshots/            # Visuals from Jira board
├── README.md
├── .gitignore
 
