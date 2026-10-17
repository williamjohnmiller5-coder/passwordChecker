import time
query = "no"
file = open("password.txt", "r")
password = file.read()
print(password)
file.close()
changeTries = 1







tries = 0
while True:

    question = input("what is the password?")
    if question == password:
        print("password is correct")
        query = "yes"
        break
    else:
        print("password is not correct")
        tries = tries + 1
        #after 3 tries it will make the user wait for 1 minute
        if tries == 3:
            print("please try again later")
            print("Waiting starts now...")
            time.sleep(6)
            print("60 seconds have passed you may now try again ")
        #after 5 tries it will make the user wait for 5 minutes
        if tries == 5:
            print("password incorrect multiple times please try again in 5 minutes")
            time.sleep(3)
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
        changeToANewPassword = "yes"
        break
    elif change == "n":
        print("okay system abort")
        changeToANewPassword = "no"
        break


    else:
       print("please enter y(yes) or n(no)")

if changeToANewPassword == "yes":
    while True:
        oldPassword = input("please enter your old password")
        file = open("password.txt", "r")
        Passwordcheck = file.read()
        file.close()
        if oldPassword == Passwordcheck:

            file = open("password.txt", "w")
            changePassword = input("please enter your new password")
            checkNewPassword = changePassword
            secondCheck = input("please enter your new password again")
            if checkNewPassword == secondCheck:
                file.write(changePassword)
                file.close()
                break
            else:
                secondCheck = input("please enter your new password again")
                if checkNewPassword == secondCheck:
                    file.write(changePassword)
                    file.close()
                    break
                else:
                    changeTries = changeTries + 1
                    if changeTries <= 2:
                        break
