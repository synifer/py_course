fav_languages = {
    'alan': 'python',
    'billi': 'c++',
    'tommy': 'go',
    'ashly': 'java',
    'linkoln': 'pyskal',
}
friends = ['ashly', 'linkoln']

for name in fav_languages:
    print("\n" + name.title())
    if name in friends:
        print("\tHi " + name.title() + ", I see your favotite language is " + fav_languages[name].title() + "!")