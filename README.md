# IVR UAT Simulation 🎧📞

This project simulates a real-world **User Acceptance Testing (UAT)** process for an IVR (Interactive Voice Response) system, integrating **Python automation** with **Jira Cloud** for issue tracking.

---

## 🚀 Features

- 📞 Simulates an IVR call flow in Python (Sales, Support, Operator, Invalid Input)
- 🐛 Bulk issue creation in Jira for UAT testing
- ✅ Assigns issues automatically to the tester
- 🧪 Includes unit tests with logging
- 🔐 API tokens handled securely with environment variables
- 📂 Structured folders for scripts, logs, screenshots

---

## 📁 Project Structure

```plaintext
ivr-uat-simulation/
├── scripts/
│   ├── ivr_simulation.py         # Core IVR menu logic
│   ├── test_ivr_simulation.py    # Unit tests for simulation
│   ├── create_jira_issue.py      # Creates a single Jira issue
│   ├── bulk_create_issues.py     # Bulk-creates predefined issues in Jira
│   └── get_account_id.py         # (Optional) Fetches Jira account ID
├── call_flows/
│   └── sample_call_flow.json     # Sample IVR options in JSON format
├── logs/
│   └── interaction_log.txt       # Records user selections
├── assets/
│   └── screenshots/              # Stores evidence/screenshots
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🛠 Tech Stack

- **Python 3**
- **Jira Cloud API (v3)**
- `requests`, `json`, `os`
- Secure token handling via environment variables

---

## ⚙️ Core Functionalities

- 🎛 **Simulated Call Flow Execution**  
  Load test scenarios from `call_flows/*.json` and simulate IVR interactions.

- 🐞 **Automated Jira Ticket Creation**  
  Generate tickets for UAT issues like routing errors and prompt mismatches.

- 🔐 **Secure Token Management**  
  Keep your Jira token safe using shell environment variables (`JIRA_API_TOKEN`).

- 🧪 **Scripted Testing**  
  Validate logic with `test_ivr_simulation.py` and log user inputs for QA review.

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone git@github.com:ios79/ivr-uat-simulation.git
cd ivr-uat-simulation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Your Environment Variable

```bash
# Windows CMD
set JIRA_API_TOKEN=your-new-valid-token

# Or Bash
export JIRA_API_TOKEN=your-new-valid-token
```

### 4. Run Scripts

```bash
python scripts/create_jira_issue.py
python scripts/bulk_create_issues.py
```

---

## 🧪 Sample Issue Types

- ✅ DTMF input mismatch
- ✅ Wrong audio prompt
- ✅ Missing confirmation on call exit
- ✅ Invalid input handling
- ✅ Routing to live agent

---

## 📸 Sample Screenshots

![IVR Simulation Jira Board](https://github.com/ios79/ivr-uat-simulation/raw/main/assets/screenshots/Screenshot%202025-04-03%20002803.png)

---

## 👤 Author

**Ioseb Vardoshvili**  
📧 vardoshvili.ioseb@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ioseb-vardoshvili-34171017a/)

---

## 📌 Project Status

✅ **Currently Active** – Jira automation and GitHub integration complete.  
📈 Next Up – Expanding test coverage, adding mock voice recordings, and dashboard integration.
