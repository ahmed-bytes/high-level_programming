# Get The users Username
username = input("Enter your Username: ")
# Get The Users Password
password = input("Enter your Password: ")

print(f'Dear {username},\nYour Password: {len(password) * "*"} is {len(password)} characters long')
