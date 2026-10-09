
import csv
import json

# Read data from CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Convert data into JSON format
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print("CSV data converted to JSON successfully!")