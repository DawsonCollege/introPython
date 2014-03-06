# now I want to get data into the variable from outside my program
# so I ask for user input!

# instead of putting a string into my variable, I call a function raw_input
# raw_input() displays the string I give it on the screen and expects
# someone to type in something.  Whatever they type in is put into userName

# NOTE: If you are using python 3 then use input() instead of raw_input()

userName = raw_input("Give me your first name ")
print("this is what you said your name is ")
print(userName)

lastName = raw_input("What is your last name ")
print("Your last name is")
print(lastName)


# I can put strings an variables that contain strings together in my 
# printed output
print("Your first name is "+ userName + " last name  " + lastName)
