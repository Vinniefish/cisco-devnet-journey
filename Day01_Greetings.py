import datetime
import json
import os




# Load the last mission ID
mission_id_file = "mission_id.txt"
if os.path.exists(mission_id_file):
    with open(mission_id_file, "r") as f:
        mission_id = int(f.read().strip())
else:
    mission_id = 1  # Start from 1 if no file

# Default values
default_name = "Vincent"
default_mission = "Operation HeadyStorm"
default_ship = "USS InfraMaster"

# Get user input
user_name = input("Please enter your name, Commander (press Enter for default): ") or default_name

while True:
    mission_name = input("Please enter the mission name (cannot be blank): ") or default_mission
    if mission_name.strip():
        break
    print("Mission name cannot be empty. Please try again.")

ship_name = input("Please enter the ship name (press Enter for default): ") or default_ship

# Get the current timestamp
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Build the Mission Briefing
mission_briefing = (
    f"Mission ID: {mission_id}\n"
    f"Time: {current_time}\n"
    f"Commander {user_name}, welcome to Mission '{mission_name}' aboard the ship '{ship_name}'.\n"
    "Good luck. The fate of the fleet is in your hands.\n"
)

# Build mission dictionary
mission_data = {
    "mission_id": mission_id,
    "timestamp": current_time,
    "commander": user_name,
    "mission_name": mission_name,
    "ship_name": ship_name
}

# Print to console
print()
print(mission_briefing)

# Ask user to confirm saving the mission
save_confirmation = input("Do you want to save this mission to the log? (Y/N): ").strip().lower()

if save_confirmation == "y":
    # Save to mission_log.txt
    with open("mission_log.txt", "a") as file:
        file.write(mission_briefing)
        file.write("\n" + "-"*40 + "\n")
    print("Mission successfully saved to mission_log.txt.")

    # Save to missions.json
    json_file = "missions.json"

    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            missions_list = json.load(f)
    else:
        missions_list = []

    missions_list.append(mission_data)

    with open(json_file, "w") as f:
        json.dump(missions_list, f, indent=4)

    print("Mission successfully saved to missions.json.")

    # After saving, increment mission_id
    mission_id += 1
    with open(mission_id_file, "w") as f:
        f.write(str(mission_id))
else:
    print("Mission was NOT saved.")


log_file = os.path.join(os.path.dirname(__file__), "Day03_MissionLog.txt")
with open(log_file, "a") as file:
    file.write(mission_briefing)