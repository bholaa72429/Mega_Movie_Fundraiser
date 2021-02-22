profit = 0

name = ""
while name != "xxx":

    name = input("Name: ")  # replace with function call

    # If name is exit code, break out of loop
    if name == "xxx":
        break

    age = int(input("Age: "))  # replace with function

    if age < 16:
       ticket_cost = 7.50
    elif age < 65:
        ticket_cost = 10.50
    else:
        ticket_cost = 6.5

    profit_made = ticket_cost - 5
    profit += profit_made

    print("{} : ${:.2f}".format(name, ticket_cost))

print("Profit from Tickets: ${:.2f}".format(profit))