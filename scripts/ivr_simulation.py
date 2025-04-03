import json
import datetime

# Load the call flow configuration from the JSON file
with open('call_flows/sample_call_flow.json', 'r') as file:
    call_flow = json.load(file)

# Display the IVR greeting message
print(call_flow["greeting"])

# Prompt user for input (simulating DTMF input)
user_input = input("Your selection: ").strip()

# Get the current timestamp for logging
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Prepare the initial log entry with timestamp and selection
log_entry = f"[{timestamp}] User selected: {user_input} - "

# Check if the input matches a valid IVR option
if user_input in call_flow["options"]:
    response = call_flow["options"][user_input]           # Fetch the corresponding action
    print(response["message"])                            # Show the system response to the user
    log_entry += f"{response['action']}\n"                # Append action to the log
else:
    print(call_flow["invalid_option"])                    # Handle invalid input
    log_entry += "invalid_selection\n"                    # Log as invalid selection

# Save the interaction to the log file for UAT/QA audit trail
with open('logs/interaction_log.txt', 'a') as log_file:
    log_file.write(log_entry)
