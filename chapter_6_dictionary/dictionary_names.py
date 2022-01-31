from turtle import title


user_1 = {'first_name': "Alan", "last_name": "Morgan", "age": '22', "city": "Bermingem"}
print(user_1["first_name"])
# users_pool = {"user_1": ['first_name': "Alan", "last_name": "Morgan", "age": '22', "city": "Bermingem"], 
#             "user_2": ['first_name': "Terry", "last_name": "Logan", "age": '56', "city": "Vermont"]}
print("Hello, " + user_1["first_name"] + " " + user_1["last_name"] + ". Your age is " + user_1["age"] + ". You live in " + user_1["city"].title() + ". Welcome to python world!")