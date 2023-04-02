from random import randint
def main():
    number = randint(0,100)
    def guess():
        looper = True
        while looper == True:
            try:
                inpguess = int(input("input your guess "))
                looper = False
            except:
                print("please input a number")
        if inpguess > 100 or inpguess < 0:
            print("please enter a number between 0 and 100")
            guess()
        elif inpguess > number:
            print("lower")
            guess()
        elif inpguess < number:
            print("higher")
            guess()
        else:
            print("YOU WON! :)")
            inp = ""
            while inp != "yes":
                inp = input("do you wish to restart? ").lower()
                if inp == "yes":
                    print("resarting...")
                    main()
                elif inp == "no":
                    print("finished")
                    quit()
                else:
                    print("please input yes or no")
    guess()
main()
