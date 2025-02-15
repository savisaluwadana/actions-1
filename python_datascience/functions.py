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

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)
# Function to generate a frequency table
def freq_table(data_list):
    freq_dict = {}  # Create an empty dictionary
    for item in data_list:
        if item in freq_dict:
            freq_dict[item] += 1  # Increase count if item already exists
        else:
            freq_dict[item] = 1  # Add new item with count 1
    return freq_dict

# Generate frequency table for the prime_genre column
genres_ft = freq_table(genres)

# Print the frequency table
print(genres_ft)

# CODE FROM THE PREVIOUS SCREEN
# Open and read the file
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# Function to generate a frequency table for any column
def freq_table(column_index):
    freq_dict = {}  # Create an empty dictionary
    for row in apps_data[1:]:  # Exclude the header row
        value = row[column_index]  # Extract the value at the given index
        if value in freq_dict:
            freq_dict[value] += 1  # Increase count if value already exists
        else:
            freq_dict[value] = 1  # Add new value with count 1
    return freq_dict

# Generate frequency table for the user_rating column (index 7)
ratings_ft = freq_table(7)

# Print the frequency table
print(ratings_ft)

# Open and read the file
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

# Updated function to generate a frequency table for any dataset and column
def freq_table(dataset, column_index):
    freq_dict = {}  # Create an empty dictionary
    for row in dataset[1:]:  # Exclude the header row
        value = row[column_index]  # Extract the value at the given index
        if value in freq_dict:
            freq_dict[value] += 1  # Increase count if value already exists
        else:
            freq_dict[value] = 1  # Add new value with count 1
    return freq_dict

# Generate frequency table for the user_rating column (index 7)
ratings_ft = freq_table(apps_data, 7)

# Print the frequency table
print(ratings_ft)
