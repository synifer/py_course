guests = ['Tom', 'Charly', 'Jerry', 'Monika']
print("Today we celebrate a new day and I invited " + guests[0] + ", " + guests[1] + " and " + guests[2] + '.')
print(guests[2] + " called me in morning. Hi will be with " + guests[-1] + "." )

guests.append('Fernando')
print(guests)
print("Also i invited my college " + guests[-1] + ". Hi will be without a girlfriend.")

popped_guests = guests.pop()
print(guests)
print(popped_guests + " called a few minute ago. Hi don't know or get to come.")
guests.insert(2, 'Krew')
print(guests)
