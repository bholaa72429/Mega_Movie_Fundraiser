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

# checks for an integer more than 0
def int_check(question):

    error = "Please enter a whole number that is more than 0 "

    valid = False
    while not valid:

        # ask user for a number and check its valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response
        # If integer is not entered, show error
        except ValueError:
         print(error)


# ********** Main Routine **********

# Set up dictionaries / lists needed to hold data

# Ask the user if they have used the program before & show instruction if necessary

# Loop to get ticket details
 # start of loop


# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0


while name != "xxx" and ticket_count < MAX_TICKETS:

        # tell user that only one seat is left!
        if ticket_count < MAX_TICKETS - 1:
            print("You have {} seats "
                  "left".format(MAX_TICKETS - ticket_count))
        # Warns user that only one seat is left!
        else:
            print("*** There is ONE seat left!! ***")

        # Get details ...

        # Get name (can't be blank)
        name = not_blank("Name:", "Sorry - this can't be blank, please enter your name")

        # end the loop if the exit code is entered
        if name == "xxx":
            break

        # Get age (between 12 and 130)
        age = int_check("Age: ")


        # check that age is valid...
        if age < 12:
            print("Sorry you are too young for the movie")
            continue
        elif age > 130:
            print("That is very old - it looks like a mistake")
            continue

        if age < 16:
            ticket_cost = 7.50
        elif age < 65:
            ticket_cost = 10.50
        else:
            ticket_cost = 6.5

        ticket_count += 1
        ticket_sales += ticket_cost

# End of tickets loop

# calculate ticket profit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets ...
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets  \n "
            "There is {} places still available"
            .format(ticket_count, MAX_TICKETS - ticket_count))



    # Calculate ticket price

    # Loop to ask for snacks

    # calculate snack price

    # ask for payment method (and apply surchange if necesary)

# calculate total sales and profit
