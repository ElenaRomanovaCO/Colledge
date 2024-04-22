'''
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
The program should first ask for the number of years. The outer loop will iterate once for each year.
The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask
the user for the inches of rainfall for that month. After all iterations, the program should display the
number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
'''

# List of months
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

# Asking user to enter number of years that he desire to calculate rainfall data
num_years = int(input("Enter the number of years for calculating average rainfall data: "))

# Initializing variables to store total rainfall and total months
total_rainfall = 0
total_months = 0

# Creating outer loop to iterate via each year in given number of years
for year in range(1, num_years + 1):
    print(f"{year=}:")

    # Creating inner loop to iterate via each month
    for month in range(1, 13):
        month_name = month_names[month - 1]
        # Asking user for rainfall data for each month
        rainfall = float(input(f"Enter number of inches of rainfall for month {month_name}: "))
        total_rainfall += rainfall
        total_months += 1

# Calculating the average rainfall per month
average_rainfall = total_rainfall / total_months

# Display the results
print(f"Results is calculated for {num_years} consequtive years:")
print(f"Total inches of rainfall for given period was: {total_rainfall:.2f}")
print(f"Total number of months in given period was: {total_months}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
