ticketPrice = 10
service = 2
ticketRemain = 100

def calculate(ticketSale):
    return (ticketPrice * ticketSale) + service

while ticketRemain >= 1: 

    print("There are {} tickets remaining.".format(ticketRemain))

    name = input("Enter name ")
    print(" Welcome {}!".format(name))

    ticketSale = input("How many tickets would you like {}? ".format(name))
    try:
        ticketSale = int(ticketSale)
        if ticketSale > ticketRemain:
            raise ValueError("there are only {}".format(ticketRemain))
    except ValueError as err:
        print("o no, please try again. {}.".format(err))
    else:
        total = calculate(ticketSale)
        print("Total due is ${}".format(total))

        confirm = input("Confirm you want to purchase {}.  yes/no  ".format(ticketSale))
        if confirm.lower() == "yes":
            ticketRemain -= ticketSale
            print("sold!")
        else:
            print("Thank you {}.".format(name))
print("sorry")
