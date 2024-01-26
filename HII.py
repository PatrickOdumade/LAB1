import statistics as st  # Importing the statistics module and aliasing it as 'st'


#Part 2 Q 1
import statistics as st

# Prints a message indicating the start of the program
print("My first Python program")

# Assigns values to variables
int1 = 0
int2 = 10
int3 = int1 + int2
print(int3)

# Creat3w a list
my_list = [2, 4, 6, 8, 10, 12, 16]
print(my_list)  # Prints the list

# Calculating the mean, median, and mode of the list
mean = st.mean(my_list)  # Calculates the mean using the mean() function from the statistics module
median = st.median(my_list)  # Calculates the median using the median() function from the statistics module
mode = st.mode(my_list)  # Calculates the mode using the mode() function from the statistics module

# Prints the calculated mean, median, and mode
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)



#Q2 D
from statistics import mean, median, mode, stdev

data_set = [2.99, 3.99, 5.99, 6.99, 8.99, 1.99, 2.99, 3.99, 1.99, 2.99, 5.99, 1.99, 2.99, 8.99, 0.99, 2.99, 1.99, 6.99, 2.99, 1.99, 6.99, 4.99, 1.99, 1.99, 2.99, 3.99, 5.99, 2.99]


mean_value = mean(data_set)


median_value = median(data_set)

mode_value = mode(data_set)

std_deviation = stdev(data_set)

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Standard Deviation:", std_deviation)


#q3d

from statistics import mean, stdev

# Constants
AVERAGE_RESTING_HEART_RATE = 70

# Define the data for each person
data = {
    "Person 1": [80, 120, 77],
    "Person 2": [55, 152, 0],
    "Person 3": [147, 60, 55],
    "Person 4": [0, 120, 85]
}

# Function to replace zero rates with the average resting heart rate
def replace_zeros(person_data):
    return [AVERAGE_RESTING_HEART_RATE if rate == 0 else rate for rate in person_data]

# Calculate statistics for each person's data
for person, heart_rates in data.items():
    heart_rates = replace_zeros(heart_rates)
    mean_rate = mean(heart_rates)
    max_rate = max(heart_rates)
    min_rate = min(heart_rates)
    std_dev = stdev(heart_rates)
    
    print(f"{person}:")
    print("Mean:", mean_rate)
    print("Max:", max_rate)
    print("Min:", min_rate)
    print("Standard Deviation:", std_dev)
    print()

# Calculate the mean heart rate for each person and its standard deviation
mean_heart_rates = [mean(heart_rates) for heart_rates in data.values()]
mean_heart_rates_std_dev = stdev(mean_heart_rates)
print("Mean Heart Rates:", mean_heart_rates)
print("Standard Deviation of Mean Heart Rates:", mean_heart_rates_std_dev)
