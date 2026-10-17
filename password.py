###############  welcome to my python project (credits to me) please use this for anything and feel free to add to it  ###############
print("this program was made by williamjohnmiller")
#this code itsnt mandatory, please just delete if if you want but it would help it you kept it somewhere













#this imports the time function for a timeout
import time
#this variable allows to see how many times the user has entered an input and got it wrong.
tries = 0
#this is the first check for the program allowing the user to continue after changing their password(do not change)
query = "no"
changeNewPassword = "no"
#this line of code opens the file "password.txt" and stores it in a variable for line 22 to check the password from the user
file = open("password.txt", "r")
password = file.read()
#this line of code (line 11) below is for testing, it will show the users password before the program starts,remove it when you use the program
print(password)
file.close()




while True:

    question = input("what is the password?")
    if question == password:
        print("password is correct")
        query = "yes"
        break
    else:
        print("password is not correct")
        #if the user gets the password wrong it will add one to the "tries" counter
        tries = tries + 1
        #after 3 tries it will make the user wait for 24 seconds
        if tries == 3:
            print("please try again later")
            print("Waiting starts now...")
            time.sleep(24)
            print("60 seconds have passed you may now try again ")
        #after 5 tries it will make the user wait for 2 minutes
        if tries == 5:
            print("password incorrect multiple times please try again in 5 minutes")
            time.sleep(120)
            print("5 minutes have passed you may now try again")
        #after ten tries it will eject the user from the password system
        if tries == 10:
            print("password incorrect multiple times system ejected")
            query = "no"
            break

#after the loop is broken it will ask the user if they want to change their password
while True:
    if query == "yes":
        change = input("would you like to change your password?(y/n)")
        if change == "y":
            changeToANewPassword = "yes"
            break
        elif change == "n":
            print("okay system abort")
            changeToANewPassword = "no"
            break


        else:
           print("please enter y(yes) or n(no)")
#if they say yes to changing their password, it will ask them for their old password
if changeToANewPassword == "yes":
    while True:
        oldPassword = input("please enter your old password")
        file = open("password.txt", "r")
        #passwordCheck will check if their input matches their old password
        Passwordcheck = file.read()
        file.close()
        if oldPassword == Passwordcheck:
            #if it matches, the program will allow the user to carry on with changing their password with the variable (changeNewPassword)
            #being set to "yes"
            changeNewPassword = "yes"
            break
#this checks if program lets the user continue
if changeNewPassword == "yes":
    while True:
        file = open("password.txt", "w")
        #the program will now ask the user to enter their new password
        changePassword = input("please enter your new password")
        #"checkNewPassword" will store their new password in a variable
        checkNewPassword = changePassword
        # "secondCheck" will ask the user to enter their password for a second time to make sure they know it
        secondCheck = input("please enter your new password again")
        if checkNewPassword == secondCheck:
            #it will then write it in the "password.txt" file
            file.write(changePassword)
            file.close()
            break
        else:
            #if the second password check didn't match, it will ask again for another two times before asking them to provide their
            #initial new password again
            secondCheck = input("please enter your new password again")
            if checkNewPassword == secondCheck:
                file.write(changePassword)
                file.close()
                break


