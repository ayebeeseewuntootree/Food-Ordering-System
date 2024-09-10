# Create and display menu for user to pick with prices

menu = {1: ["buorgor" , 7.99],
        2: ["other borgoer -", 8.99],
        3: ["more borger -", 7.68],
        4: ["cool bourgor -", 9.64],
        5: ["not cool bourgor -", 8.53]}

items_picked = []

def has_only_numbers(customer_info):
    return all(char.isdigit() for char in customer_info)

def menu_order():
    amount_in_order = 0

    for key, value in menu.items():
        print("{}: {}".format(key, value))

    while amount_in_order < 6:

        print()
        user_choice = int(input("Please select the number  of the item that you would like to order: "))
        
        if user_choice in range (-1, len(menu)+1):
        
            amount_in_order += 1
            print(menu[user_choice][0])
            items_picked.append(menu[user_choice])
        
        elif user_choice == "":
            user_choice = int(input("Please select the number  of the item that you would like to order: "))
        
        else:
            print()
            print("Please enter a number that is in the menu")
            user_choice = int(input("Please select the number  of the item that you would like to order: "))

    print("Your order is {}".format(items_picked))

menu_order()