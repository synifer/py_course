prompt = "\nPlease type your age and I will calculate your ticket cost:  "
message = ""
while True:
    message = input(prompt)
    if message == 'quit':
        print("You enter " + message + ". Completed. Thank you!")
        break
    else:
        print("Your age is: " + message)
        if int(message) <= 3:
            print("Your ticket cost is free. Have a nice watching! ")
            break
        elif int(message) <= 12:
            print("Your ticket cost is 5$. Have a nice watching!")
            break
        elif int(message) <= 18:
            print("Your ticket cost is 10$. Have a nice watching!")
            break
        else:
            print("Your ticket cost is 15$. Have a nice watching!")
            break
