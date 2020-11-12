userPassword = "password123"
programmeRunning = True
numWrongGuesses = 0

while programmeRunning:
    passwordAttempt = input("Please input your password \n> ")
    if passwordAttempt != userPassword:
        numWrongGuesses = numWrongGuesses + 1
        if numWrongGuesses == 3:
            print("You have been denied access")
            programmeRunning = False
        else:
            print("password incorrect. Try again\n")
            continue
    else:
        print("You have successfully logged in")
        programmeRunning = False
