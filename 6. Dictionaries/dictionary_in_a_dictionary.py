users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurite': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    print(f"\tFullName: {userinfo['first'].title()} {userinfo['last'].title()}")
    print(f"\tLocation: {userinfo['location'].title()}")