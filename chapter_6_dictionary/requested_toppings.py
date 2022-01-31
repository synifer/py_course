requested_toppings = ['mushrooms', 'green papers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green papers':
        print("Sorry, we are out of green papers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
