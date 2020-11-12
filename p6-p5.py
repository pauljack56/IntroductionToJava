userPassword = "password123"
programmeRunning = True
numWrongGuesses = 0

while programmeRunning:
    passwordAttempt = input("Please input your password \n> ")
    if passwordAttempt != userPassword:
        print("Sorry the password is wrong. You will now be asked to enter the correct password three times as a "
              "security measure to ensure you are not trying to gain unuauthorised access to this machine")
        for i in range(0,3):
            errorPasswordAttempt = passwordAttempt = input(f"{i+1}: Please input your password \n> ")
            if(errorPasswordAttempt != userPassword):
                print("You have been denied access")
                exit(0)
        print("You have successfully logged in")
        programmeRunning = False

    else:
        print("You have successfully logged in")
        programmeRunning = False
