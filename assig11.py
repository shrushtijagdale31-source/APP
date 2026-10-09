import pandas as pd

# Create a Series containing 10 numbers
numbers = pd.Series([12, 25, 18, 30, 45, 20, 35, 15, 40, 28])

print("Series:")
print(numbers)

# Indexing
print("Element at index 3:", numbers[3])

# Filtering
print("Numbers greater than 25:")
print(numbers[numbers > 25])

# Statistical operations
print("Mean:", numbers.mean())
print("Median:", numbers.median())
print("Minimum:", numbers.min())
print("Maximum:", numbers.max())