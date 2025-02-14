def square(a_number):
    return a_number ** 2

squared_6 = square(6)
squared_11 = square(11)

#Extract Values from Any Column

# Open the file and read data
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# Function to extract a column
def extract(column_index):
    column_values = []  # Create an empty list
    for row in apps_data[1:]:  # Exclude the header
        column_values.append(row[column_index])  # Append the value at the given index
    return column_values

# Extract prime_genre column (index 11)
genres = extract(11)

# Print first few values to verify
print(genres[:5])
