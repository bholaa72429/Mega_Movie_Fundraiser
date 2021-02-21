# function goes here

#checks for an integer more than 0
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


# main routine goes here
age = int_check("Age: ",12, 130)