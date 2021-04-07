# import statements
import re
import pandas

# function go here


# checks that ticket name is not blank
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

# checks number of ticket left and warns user
# if maximum is bring approached
def check_tickets(tickets_sold, ticket_limit):
    # tell user that only one seat is left!
    if tickets_sold < ticket_limit - 1:
        print()
        print("You have {} seats "
              "left".format(ticket_limit - tickets_sold))
    # Warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

    return ""

# Gets ticket price based on age
def get_ticket_cost():
    def string_check(choice, options):

        is_valid = "yes"
        chosen = ""
        for var_list in options:

            # if the snack  is in one of the lists, return the full
            if choice in var_list:

                # Get full name of snacks abd put it
                # in title case so it looks nice when outputted
                chosen = var_list[0].title()
                is_valid = "yes"
                break
            # if the chosen option is not valid, set is_valid to no
            else:
                is_valid = "no"

        # if the snack is not OK - ask question again.
        if is_valid == "yes":
            return chosen
        else:
            return "invalid choice"

    # Get list of snacks
    def get_snack():
        # regular expression to find if item starts with a number
        number_regex = "^[1-9]"

        # valid snacks holds list all snacks
        # Each item in valid snacks is a list with
        # valid options for each snacks <full name, letter code (a -e)
        # , and possible abbreviations etc>
        valid_snacks = [
            ["popcorn", "p", "pop", "corn", "a"],
            ["M&M's", "m&m's", "mms", "m", "b"],  # first item is M&M
            ["pita chips", "chips", "pc", "pita", "c"],
            ["water", "w", "d"],
            ["orange juice", "oj", "o", "juice", "e"],
        ]

        # holds snack order for a single user.
        snack_order = []

        desired_snack = ""
        while desired_snack != "xxx":

            snack_row = []

            # ask user for desired snack and put it in lowercase
            desired_snack = input("Snack: ").lower()

            if desired_snack == "xxx":
                return snack_order

            # if item has a number, separate it into two (number / item)
            if re.match(number_regex, desired_snack):
                amount = int(desired_snack[0])
                desired_snack = desired_snack[1:]
            else:
                amount = 1
                desired_snack = desired_snack

            # remove white space around snacks
            desired_snack = desired_snack.strip()

            # check if snack is valid
            snack_choice = string_check(desired_snack, valid_snacks)

            if snack_choice == "invalid choice":
                print("Please enter a valid option ")

            # check snack amount is valid (less than 5)
            if amount >= 5:
                print("Sorry - we have a four snack maximum")
                snack_choice = "invalid choice"

            # add snack AND amount to list...

            snack_row.append(amount)
            snack_row.append(snack_choice)

            # check that snack is not the exit code before adding
            if snack_choice != "xxx" and snack_choice != "invalid choice":
                snack_order.append(snack_row)

    # Get age (between 12 and 130)
    age = int_check("Age: ")

    # check that age is valid...
    if age < 12:
        print("Sorry you are too young for the movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_cost = 7.50
    elif age < 65:
        ticket_cost = 10.50
    else:
        ticket_cost = 6.5

    return ticket_cost

# string checker
def string_check(choice, options):

    is_valid = "yes"
    chosen = ""
    for var_list in options:

        # if the snack  is in one of the lists, return the full
        if choice in var_list:

            # Get full name of snacks abd put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# Get list of snacks
def get_snack():
    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list all snacks
    # Each item in valid snacks is a list with
    # valid options for each snacks <full name, letter code (a -e)
    # , and possible abbreviations etc>
    valid_snacks = [
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"],    # first item is M&M
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice","oj","o","juice", "e"],
]

    # holds snack order for a single user.
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, separate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snacks
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        if snack_choice == "invalid choice":
            print("Please enter a valid option ")

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack AND amount to list...

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)

# ******** Main Routine *******

# lists for valid options for yes / no response
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
# lists for valid response for payment method
pay_method = [
    ["cash", "ca"],
    ["credit","cr"]
]

# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_name = []
all_tickets = []
# snack lists
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn,mms, pita_chips, water, orange_juice]

# store surcharge multiplier
surcharge_multi_list = []

# Lists to store summary data...
summary_heading = ["Popcorn", "M&M's", "Pita Chips", "Water", "Orange Juice", "Sanck Profit", "Ticket Profit", "Total Profit"]
summary_data = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_name,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_multi_list
}

# Summary Dictionary
summary_data_dict = {
    'Item': summary_heading,
    'Amount': summary_data
}


# Cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

# Ask user if they have used the program before & show instruction

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

        # check number of tickets limit has not been exceeded
        check_tickets(ticket_count, MAX_TICKETS)

       # Get details ...

          # ----- Get name (can't be blank) -----
        name = not_blank("Name: ", "Sorry - this can't be blank, please enter your name")

        # end the loop if the exit code is entered
        if name == "xxx":
            break

        # Get ticket price based on age
        ticket_cost = get_ticket_cost()
        # If age is invalid, restart loop (and get name again)
        if ticket_cost == "invalid ticket price":
            continue

        ticket_count += 1
        ticket_sales += ticket_cost

        # add name and ticket price to lists
        all_name.append(name)
        all_tickets.append(ticket_cost)
# ---- End of tickets loop ----


# ----- Loop to ask for snacks -----
        # ask user if they want a snack
        check_snack = "invalid choice"
        while check_snack == "invalid choice":
            want_snack = input("Do you want to order snacks ? ").lower()

            check_snack = string_check(want_snack, yes_no)

            if check_snack == "invalid choice":
                print("Please enter yes / no ")

        # If they say yes, ask what snacks they want (and add to our snacks)
        if check_snack == "Yes":
            snack_order = get_snack()

        else:
            snack_order = []

        # Assume no snacks have been bought
        for item in snack_lists:
            item.append(0)

        for item in snack_order:
            if len(item) > 0:
                to_find = (item[1])
                amount = (item[0])
                add_list = movie_data_dict[to_find]
                add_list[-1] = amount


        # Ask for payment method
        how_pay = "invalid choice"
        while how_pay == "invalid choice":
            how_pay = input("Please pick a payment method (cash \ credit) ").lower()
            how_pay = string_check(how_pay, pay_method)

        if how_pay == "Credit":
            surcharge_multiplier = 0.05
        else:
            surcharge_multiplier = 0

        surcharge_multi_list.append(surcharge_multiplier)


# Print details...
# create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snack and ticket

movie_frame["Snack"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame["Snack"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# shorten column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ', 'Pita Chips': 'Chips', 'Surcharge_Multiplier': 'SM'})

# Set up summary dataframe
# populate snack items...
for items in snack_lists:
    # sum itms in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# Get Ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

# work out total profit and add to list
total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# Set up columns to be printed...
pandas.set_option('display.max_columns', None)

# Display number to 2 dp
pandas.set_option('precision', 2)

print_all = input("Print all columns ?? (y) for yes")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total','Surcharge', 'Total']])

print()


# Tell user if they have unsold tickets ...
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets  \n "
            "There is {} places still available"
            .format(ticket_count, MAX_TICKETS - ticket_count))




    # calculate snack price

    # ask for payment method (and apply surchange if necesary)

# calculate total sales and profit

