import json
import csv
from datetime import datetime

# Function to parse JSON Lines file
def parse_jsonl(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

# Function to calculate duration between two timestamps
def calculate_duration(start_time, end_time):
    start = datetime.fromisoformat(start_time)
    end = datetime.fromisoformat(end_time)
    return (end - start).total_seconds()

# Read and parse references_log.jsonl
references_log = list(parse_jsonl('references_log.jsonl'))

# Read and parse user_actions.jsonl
user_actions = list(parse_jsonl('user_actions.jsonl'))

# Create a dictionary to store user actions by user_id
user_actions_dict = {}
for action in user_actions:
    user_id = action['user_id']
    if user_id not in user_actions_dict:
        user_actions_dict[user_id] = []
    user_actions_dict[user_id].append(action)

# Create a list to store the output data
output_data = []
# Process each reference log entry
for ref_log in references_log:
    # Safely get values with error checking
    reference_id = ref_log.get('id', '')
    study = ref_log.get('study', {})
    accession_number = ref_log.get('accession_number', '')
    doi = ref_log.get('doi', '')
    is_qa = False  # Assuming is_qa is always False based on the example

    if not study:
        continue

    study_id = study.get('id', '')
    if not study_id:
        continue

    # Get the list of users assigned to this study safely
    users = []
    extraction_tasks = study.get('extraction_task', [])
    for task in extraction_tasks:
        if task and isinstance(task, dict):
            team_member = task.get('team_member', {})
            if team_member and isinstance(team_member, dict):
                user_id = team_member.get('user_id')
                if user_id:
                    users.append(user_id)

    # Process each user
    for user_id in users:

        # Get the save operations for this user and reference
        save_ops = [log for log in ref_log['logs'] if log['user_id'] == user_id]

        # Sort save operations by timestamp
        save_ops.sort(key=lambda x: x['created_at'])

        # For each save operation, find the previous user action to determine the start time
        for save_op in save_ops:
            save_time = save_op['created_at']
            user_actions_for_user = user_actions_dict.get(user_id, [])

            # Find the previous action before the save operation
            previous_action = None
            for action in user_actions_for_user:
                if action['server_timestamp'] < save_time:
                    previous_action = action
                else:
                    break

            if previous_action:
                start_time = previous_action['server_timestamp']
                duration = calculate_duration(start_time, save_time)
                output_data.append([
                    user_id, study_id, reference_id, accession_number, doi, is_qa,
                    duration, start_time, save_time
                ])

# Write the output data to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'user_id', 'study_id', 'reference_id', 'accession_number', 'doi', 'is_qa',
        'duration in seconds', 'start_timestamp', 'last_timestamp'
    ])
    writer.writerows(output_data)

print("CSV file 'output.csv' has been generated.")


