languages_pulling = {
    'tomas': 'c++',
    'hary': 'ruby',
    'alice': 'python',
    'kodi': 'go',
    'frenk': 'C#',
    'mcgregor': "java",
    'luice': 'javascript', 
}

for name, language in languages_pulling.items():
    print(name.title() + ", you take the poll. Your favorite language is " + language.title())
    if 'guzzi' not in languages_pulling:
        print("Guzzi, Please take the poll")
        