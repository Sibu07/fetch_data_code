import requests

url = "https://raw.githubusercontent.com/Sibu07/my_json/main/updated-calls.json"
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    if isinstance(json_data, list):
        # If json_data is a list, assume each item is a dictionary and print the values of the "time" and "call_duration" keys for each dictionary
        for item in json_data:
            print(item["time"])
            print(item["call_duration"])
    else:
        # If json_data is a dictionary, print the values of the "time" and "call_duration" keys
        print(json_data["time"])
        print(json_data["call_duration"])
else:
    print("Failed to fetch JSON data. Status code:", response.status_code)
