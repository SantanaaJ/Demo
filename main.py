
def login_credentials():
    username= input("Enter a username: ")
    age= int(input("Enter your age: "))
    limiter= 21

    if age >= limiter:
        print("Hello " + username,  "You are now logged in! ")
    elif limiter > age:
        print("Sorry " + username, "Access denied! scrub ")

    return limiter

login_credentials()

