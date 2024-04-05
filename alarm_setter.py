"""
Part 2. Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
Write a Python program to solve the general version of the above problem.
Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
Your program should output what the time will be on a 24-hour clock when the alarm goes off.
"""

# Function to calculate the alarm time on a 24-hour clock
def calculate_alarm_time():
    # Input: current time (in hours) and hours to wait for the alarm
    current_time = int(input("Enter the current time (in hours, 0-23): "))
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

    # Calculate the alarm time
    alarm_time = (current_time + hours_to_wait) % 24

    # Display the alarm time
    print("The alarm will go off at", alarm_time, "hours on a 24-hour clock.")

# Call the function
calculate_alarm_time()