'''
The CSU Global Bookstore has a book club that awards points to its students based on the number
of books purchased each month. The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month and
then display the number of points awarded.
'''

# Function to validate that inuted value is integer
def get_integer_input(prompt):
    while True:
        try:
            # Attempt to convert the input to an integer
            value = int(input(prompt))
            return value
        except ValueError:
            # If an exception occurs, prompt the user to enter a valid integer
            print("Invalid input. Please enter a valid integer.")

# Asking user to enter number of books purchased the month
num_books = get_integer_input("Enter the number of books you have purchased this month: ")

# Determining the points awarded based on the number of books
if num_books == 0:
    points = 0
elif 1 <= num_books <= 1:
    points = 0
elif 2 <= num_books <= 3:
    points = 5
elif 4 <= num_books <= 5:
    points = 15
elif 6 <= num_books <= 7:
    points = 30
elif num_books >= 8:
    points = 60

# Displaying awarded points
print(f"Congratulations! You have earned {points} points for purchasing {num_books} books this month.")
