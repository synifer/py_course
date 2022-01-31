fav_num = {
    'alan': 3,
    'billi': 25,
    'tommy': 11,
    'ashly': 23,
    'linkoln': 15,
}

fav_languages = {
    'alan': 'python',
    'billi': 'c++',
    'tommy': 'go',
    'ashly': 'java',
    'linkoln': 'pyskal',
}

# Favorite number my friends
print("Favorite number my friends\n")
# Looping throught all key-value pair in dictionary
for friend, number in fav_num.items():
    print(friend.title() + "'s favorite number is " + str(number) + ".\n")
print("Favorit programming language my friends\n")
for friend, langusge in fav_languages.items():
    if langusge == 'python':
        print(friend.title() + ", it's best choise for quick start your perfect carer.\n")
    elif langusge == 'pyskal':
        print(friend.title() + ", it's not good choise to start carer, but better than anythink.\n")
    else:
        print(friend.title() + "'s favorite language is " + langusge.title() + "\n")
# Looping throught all keys in dictionary 
for name in sorted(fav_languages.keys()):
    print("\n" + name.title() + ", thank you for taking the poll.")
if 'nikolas' not in fav_languages.keys():
    print("\nNikola, please take out poll!")