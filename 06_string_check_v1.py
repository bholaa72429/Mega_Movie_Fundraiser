# string checking functions, takes in
# question and list of valid responses
def string_checker(question, to_checker):

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()

        if response in to_checker:
            return response
        else:
            for item in to_checker:
                # checks if response is the first letter of
                # an item in the left
                if response == item[0]:
                    # note: returns the entire response
                    # rather than just the first letter
                    return item
        print("Sorry that is not is not a valid response")

# Main routines starts here
for item in range (0, 6):
    want_snacks = string_checker("Do you want "
                                 "snacks? ", ["yes", "no"])
    print("Answer OK, you said:", want_snacks)
    print()
