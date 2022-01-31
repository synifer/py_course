fav_languages = {
    'alan': 'python',
    'billi': 'c++',
    'tommy': 'go',
    'ashly': 'java',
    'linkoln': 'pyskal',
}
print("The following languages have been mentioned:\n ")
for language in sorted(set(fav_languages.values())):
    print(language.title())