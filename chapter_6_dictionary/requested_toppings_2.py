available_toppings = ['mushrooms', 'olives', 'green papers', 'paperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
    else:
        print("Sorry, we don't have " + requested_topping + ".")


    