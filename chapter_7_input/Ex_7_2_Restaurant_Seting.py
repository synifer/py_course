dinner_group = input("How many people are in the dinner group? ")
dinner_group = int(dinner_group)

if dinner_group >= 8:
    print("Your group must wait for a free table.")
else:
    print("The table for your group is ready.")