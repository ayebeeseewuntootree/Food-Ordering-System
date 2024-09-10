# Ask user for their information (name, address, number)
many_words = ""
# Functions to do so

def has_numbers(customer_info):
    return any(char.isdigit() for char in customer_info)
 

def name():
    # Creating variables to store customer information

    customer_name = input("Please enter your first and last name: ")
    many_words = ""

    # Make sure the name has two words and no numbers

    if has_numbers(customer_name):
        print("Your name cannot include numbers. Please try again.")
        print()
        name()

    
    else:   

        if " " in customer_name:
            many_words = "True"

        else:
            many_words = "False"

        if many_words == "True":
            print("Hello {}".format(customer_name))

        else:
          print()
          name()


name()

