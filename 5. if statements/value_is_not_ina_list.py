banned_users = ["andrew", "carolina", "david"]
user = input("plese give me your product:")
if user in banned_users:
    print(f"{user.title()}, whisch is belong to the list")
else:
    print(f"{user.title()}, which id not belong to the list")
