import csv
import json

students = [
    ["Roll No", "Name", "Branch", "Python", "DBMS", "Maths"],
    ["1", "Amit", "CSE", 85, 60, 78],
    ["2", "Sneha", "AI", 75, 60, 70],
    ["3", "Rahul", "CSE", 40, 45, 50]
]

# Write data into CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)


# Read the CSV file
processed_students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:

        python = int(student["Python"])
        dbms = int(student["DBMS"])
        maths = int(student["Maths"])

        total = python + dbms + maths
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        processed_students.append({
            "Roll No": student["Roll No"],
            "Name": student["Name"],
            "Branch": student["Branch"],
            "Total": total,
            "Percentage": round(percentage, 2),
            "Grade": grade
        })


# Write processed data into JSON
with open("students.json", "w") as file:
    json.dump(processed_students, file, indent=4)

print("Data processed and stored successfully!")