person_0 = {
    'id': 25315628123,
    'first_name': 'rami',
    'last_name': 'malek',
    'bir_day': 25,
    'age': 35,
    'national': 'mauricanets',
    'location': "usa",
    'city': "boston",
        
}
person_1 = {
    'id': 48317528456,
    'first_name': 'denial',
    'last_name': 'kalevski',
    'bir_day': 10,
    'age': 22,
    'national': 'poland',
    'location': "rumunia",
    'city': "melsiv",
}

person_2 = {
    'id': 96354854212,
    'first_name': 'morgan',
    'last_name': 'spencer',
    'bir_day': 19,
    'age': 32,
    'national': 'american',
    'location': "singapur",
    'city': "choytawn",
}

person_3 = {
    'id': 10002153002,
    'first_name': 'terry',
    'last_name': 'fitcher',
    'bir_day': 14,
    'age': 45,
    'national': 'american',
    'location': "indonesia",
    'city': "portland",
}
full_name_0 = person_0['first_name'] + " " + person_0['last_name']
full_name_1 = person_1['first_name'] + " " + person_1['last_name']
full_name_2 = person_2['first_name'] + " " + person_2['last_name']
full_name_3 = person_3['first_name'] + " " + person_3['last_name']

for key, value in person_0.items():
    print(full_name_0.title())
    print("\tID: " + str(person_0['id']) + "\n\tAge: " + str(person_0['age']) + "\n\tNational: " + person_0['national'] + "\n\tLocation: " + person_0['location'])
#for key, value in person_1.items():
#    print(full_name_1.title())
#    print("\tID: " + str(person_1['id']) + "\tAge: " + str(person_1['age']) + "\tNational: " + person_1['national'] + "\tLocation: " + person_1['location'])
#for key, value in person_2.items():
#    print(full_name_2.title())
#    print("\tID: " + str(person_2['id']) + "\tAge: " + str(person_2['age']) + "\tNational: " + person_2['national'] + "\tLocation: " + person_2['location'])
#for key, value in person_3.items():
#    print(full_name_3.title())
#    print("\tID: " + str(person_3['id']) + "\tAge: " + str(person_3['age']) + "\tNational: " + person_3['national'] + "\tLocation: " + person_3['location'])     



#full_name = [full_name_0, full_name_1, full_name_2, full_name_3]
#print(full_name)

#print("\nFirst person: " + full_name_0.title() + "\nSecond person: " + full_name_1.title() + "\nThird person: " + full_name_2.title() + "\nForth person: " + full_name_3.title()) 
#print
#print("\nFirst person: " + full_name_0.title() + "\n\tID: " + str(person_0['id']) + "\n\tAge: " + str(person_0['age']) + "\n\tNational: " + person_0['national'].title() + "\n\tLocation: " + person_0['location'].upper())
#print("\nSecond person: " + full_name_1.title() + "\n\tID: " + str(person_1['id']) + "\n\tAge: " + str(person_1['age']) + "\n\tNational: " + person_1['national'].title() + "\n\tLocation: " + person_1['location'].title())
#print("\nThird person: " + full_name_2.title() + "\n\tID: " + str(person_2['id']) + "\n\tAge: " + str(person_2['age']) + "\n\tNational: " + person_2['national'].title() + "\n\tLocation: " + person_2['location'].title())
#print("\nForth person: " + full_name_3.title() + "\n\tID: " + str(person_3['id']) + "\n\tAge: " + str(person_3['age']) + "\n\tNational: " + person_3['national'].title() + "\n\tLocation: " + person_3['location'].title())