favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edware': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#values
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
#set
for language in set(favorite_languages.values()):
    print(language.title())