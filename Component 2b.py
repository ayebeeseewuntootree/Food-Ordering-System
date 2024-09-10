# This sub component is to ask for a phone number and make sure it has no letters
def has_only_numbers(customer_info):
    return all(char.isdigit() for char in customer_info)

def phone_number():
    
    valid = False
    while not valid:
        error = "Please enter numbers only"

        try:
            phone_number = input("Please enter your phone number: ")

            if has_only_numbers(phone_number):
                print("Your number is valid")
                valid = True
            
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            

phone_number()
