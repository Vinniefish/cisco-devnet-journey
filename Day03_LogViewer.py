import json
import os

# Load missions
json_file = "missions.json"

if not os.path.exists(json_file):
    print("No missions found yet. Please create and save a mission first!")
    exit()

with open(json_file, "r") as f:
    missions_list = json.load(f)

# Display missions
print("\n=== Mission Log ===\n")

for mission in missions_list:
    print(f"Mission ID: {mission['mission_id']}")
    print(f"Timestamp: {mission['timestamp']}")
    print(f"Commander: {mission['commander']}")
    print(f"Mission Name: {mission['mission_name']}")
    print(f"Ship Name: {mission['ship_name']}")
    print("-" * 40)

print("\nTotal missions recorded:", len(missions_list))
