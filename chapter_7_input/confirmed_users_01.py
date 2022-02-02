untrusted_users = ['bob', 'jerry', 'alice', 'kodi']
trusted_users = []
print("\nThe next users will be move to trust group\n")
while untrusted_users:
    current_users = untrusted_users.pop()
    print("User " + current_users.title() + " will be move to trust group")
    trusted_users.append(current_users)
print("\nThe next users moved to trusted group\n")
for trusted_user in trusted_users:
    print("User " + trusted_user.title() + " moved to trust group")


    