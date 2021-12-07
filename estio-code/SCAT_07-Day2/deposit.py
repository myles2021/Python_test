real_password = "password"

session_password = input("Please enter your password: \n")
deposit = input("How much do you want to make a deposit: \n")

if real_password == session_password and int(deposit) >= 50:
    print("Thank you for your deposit")
else:
    print("Failed to make deposit")
