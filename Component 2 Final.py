# Everything together

# Ask user for their information (name, address, number)
many_words = ""

# Functions to do so

def has_numbers(customer_info):
    return any(char.isdigit() for char in customer_info)
    return any("" for char in customer_info)

def has_only_numbers(customer_info):
    return all(char.isdigit() for char in customer_info)
 

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
            

def street_num():
        valid = False

        while valid == False:
            street_number = input("Please enter your street number: ")

            if has_only_numbers(street_number):
                valid = True
                return(street_number)
            
            elif street_number == "":
                 street_num()

            else:
                print()
                street_num()
                print()

def strt_name():
        valid = False

        while valid == False:
            street_name = input("Please enter your street name: ")
            
            if has_numbers(street_name):
                print()
                print("Please enter your street name only")
                print()
                strt_name()

            elif street_name == "":
                 strt_name()

            else:
                valid = True
                return(street_name)

def suburb():
        valid = False

        while valid == False:
            suburb = input("Please enter your suburb name: ")
            if has_numbers(suburb):
                print()
                print("Please enter your suburb name only")
                print()
                suburb()
            else:
                valid = True
                return(suburb)

def city():
        valid = False

        while valid == False:
            city = input("Please enter your city name: ")
            if has_numbers(city):
                print()
                print("Please enter your city name only")
                print()
                city()
            else:
                valid = True
                return(city)

def post_code():
        valid = False

        while valid == False:
            post_code = input("Please enter your post code: ")
            if has_only_numbers(post_code):
                valid = True
                return(post_code)
            else:
                print()
                print("Please enter numbers only")
                print()

def address():

    st_number = street_num()
    st_name = strt_name()
    suburb_name = suburb()
    city_name = city()
    post_code_num = post_code()

    print ("{} {} {} {} {}".format(st_number, st_name, suburb_name, city_name, post_code_num))

def information_details():
     
    name()
    phone_number()
    address()

information_details()
