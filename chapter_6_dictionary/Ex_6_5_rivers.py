rivers = {
    'dnipro': 'ukraine',
    'amazonka': 'amerika',
    'dunai': 'russian',
    'nile': 'egypt',
}

for river, country in rivers.items():
    print("The river " + river.title() + " flows in " + country.title())
for river in sorted(rivers.keys()):
    print(river.title())
for country in rivers.values():
    print(country.title())
    