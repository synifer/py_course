# Start with users need to be verified,
# and en empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users
print("New users will be verifyng\n")
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying users: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed: \n")
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) 