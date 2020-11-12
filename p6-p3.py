userResponse = input("What is your name?\n> ")
illegalName = userResponse.lower() == "mickey mouse" or userResponse.lower() == "spongebob"
if illegalName:
    print("I don't think that is your name")
else:
    print('Nice name!')