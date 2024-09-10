
def has_only_numbers(customer_info):
    return all(char.isdigit() for char in customer_info)

def has_numbers(customer_info):
    return any(char.isdigit() for char in customer_info)

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


address()

 