"""
This program will accept float number as input, and take it as an amount to
represent given amount in words. The output will be printing words that
representing amount that was given as user's input.
"""

# Level 1: Procedural Abstraction
def write_check_amount(amount):
    """
    Writes the given numeric dollar amount in words.
    """
    # Convert the amount to a string and split it into dollars and cents
    amount_str = str(amount)
    dollars, cents = amount_str.split('.')

    # Write the dollar amount in words
    dollar_words = write_dollars(int(dollars))

    # Write the cent amount in words
    cent_words = write_cents(int(cents))

    # Combine the dollar and cent words
    amount_words = dollar_words + ' and ' + cent_words + ' cents'

    return amount_words

# Level 2: Procedural Abstraction
def write_dollars(dollars):
    """
    Writes the given dollar amount in words.
    """
    # Define a dictionary to map digit values to their corresponding words
    digit_words = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    # Define a list to store the words for the dollar amount
    dollar_words = []

    # Process the dollar amount digit by digit
    for i, digit in enumerate(str(dollars)[::-1]):
        digit_value = int(digit)
        if digit_value != 0:
            digit_word = digit_words[digit_value]
            if i == 0:
                dollar_words.append(digit_word)
            elif i == 1:
                dollar_words.append(digit_word + ' ten')
            elif i == 2:
                dollar_words.append(digit_word + ' hundred')
            elif i == 3:
                dollar_words.append(digit_word + ' thousand')
            # Add more cases for higher denominations if needed

    # Reverse the list and join the words
    dollar_words.reverse()
    dollar_amount = ' '.join(dollar_words)

    return dollar_amount

# Level 3: Procedural Abstraction
def write_cents(cents):
    """
    Writes the given cent amount in words.
    """
    # Define a dictionary to map digit values to their corresponding words
    digit_words = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }

    # Handle the case where cents are zero
    if cents == 0:
        return 'zero'

    # Process the cent amount digit by digit
    cent_words = []
    for digit in str(cents):
        digit_value = int(digit)
        cent_words.append(digit_words[digit_value])

    # Join the words for the cent amount
    cent_amount = ' '.join(cent_words)

    return cent_amount

# Usage
amount = float(input("Enter a dollar amount: "))
amount_words = write_check_amount(amount)
print(f"The amount {amount} in words is: {amount_words}")