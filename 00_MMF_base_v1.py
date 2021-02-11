# import statement

# function go here
# check that ticket name is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        # if name is not blank, program continues
        if response != "":
            return response
        # if name is blank, show error message
        else:
            print(error_message)

# ********** Main Routine **********

# Set up dictionaries / lists needed to hold data

# Ask the user if they have used the program before & show instruction if necessary

# Loop to get ticket details

    # Get name (can't be blank)
name = not_blank("Name:", "Sorry - this can't be blank, please enter your name")
    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surchange if necesary)

# calculate total sales and profit