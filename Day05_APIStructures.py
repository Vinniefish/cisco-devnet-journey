""" You receive a simulated API response from a network device as a plain string:

Write a Python script that:

Splits the API response into key-value pairs.

Stores the pairs in a dictionary.

Prints the dictionary nicely formatted, one key-value per line, like""" 
 
 
api_response = "hostname:router1;ip:192.168.1.1;status:active;location:San Diego"

# Step 1: Split the API response into key-value pairs

api_response = "hostname:router1;ip:192.168.1.1;status:active;location:San Diego"

# Split the string into pairs using ';' as the delimiter
pairs = api_response.split(';')
print(pairs)

# Create an empty dictionary to store the key-value pairs
device_info = {}

# Loop through each pair and split it into key and value
for pair in pairs:
    key, value = pair.split(':')
    device_info[key] = value
    # Add the key-value pair to the dictionary  

# Print the dictionary nicely formatted
print(device_info)

# Pretty print the dictionary
for key, value in device_info.items():
    print(f"{key}: {value}")