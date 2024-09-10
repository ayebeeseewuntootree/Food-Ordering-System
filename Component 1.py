# Ask user whether they want to order for pickup or delivery and sotore it in a variable

# Function to do so
def order_type():

     # Variables/list needed for order options and loop
    order_types = ["pickup", "p", "delivery", "d"]
    valid = True

    # Loop question until valid
    while valid == True:

        # Ask user whether they want pickup or delivery
        pickup_or_delivery = input("Would you like to order for pickup or delivery?\nPlease write either 'p' or 'd': ").lower()
        print()

        # Makes sure user's option is valid else asks again
        if pickup_or_delivery in order_types:
           
            if pickup_or_delivery == "d":
                choice = "Delivery"
           
            elif pickup_or_delivery == "p":
                choice = "Pickup"


            elif pickup_or_delivery == "delivery":
                choice = "Delivery"
           
            elif pickup_or_delivery == "pickup":
                choice = "Pickup"

            # Prints user's choice if valid
            print("You have chosen: {}".format(choice))
            valid = False

        # Lets user know their information was invalid before asking the question agian
        elif pickup_or_delivery not in order_types:
            print("Invalid input")


# Calling function to determine order type
order_type()