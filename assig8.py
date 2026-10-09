

# Read data from input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Count the number of lines
print("Total number of lines:", len(lines))

# Extract the first two lines
first_two = lines[:2]

# Write the first two lines into a new file
with open("output.txt", "w") as file:
    file.writelines(first_two)

print("First two lines written to output.txt successfully!")