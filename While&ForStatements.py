import random

gameflag = True
while(gameflag):
    print("Welcome to the While and For statement game\nPlease choose a topic\n")
    print("1. Counting up to a specific number\n2. Printing anything to console with an exit word\n3. Guessing a number between 1 and 100\n")
    choice = int(input("Input number here: "))
    
    if(choice == 1):
        countnum = int(input("Please input a number to count up to: "))
        for i in range(countnum + 1):
            print(i)
    elif(choice == 2):
        print("Please choose any String to write to console, with the exit word being 'banana'\n")
        word = ""
        while(word != "banana"):
            word = input("Enter any word: ")
            print(word)
            
        print("You have exited the word input option")
    
    elif(choice == 3):
        print("You will guess a number between 1 and 100, you have 10 attempts")
        attempts = 10
        robonum = random.randint(1, 100)
        while(attempts != 0):
            choicenum = int(input("Enter your guessed number: "))
            if(choicenum == robonum):
                print("You correctly guessed the number, Congrats!\n")
                break
            else:
                attempts = attempts - 1
                print("Wrong number try again\nYour have ",
                      attempts, " attempts left")

        if(attempts == 0):
            print("You lost")
    
    repeatgame = (input("Would you like to play again?\nYes to play again, anything else to leave: "))
    if(repeatgame.lower() == "yes"):
        gameflag = True
    else:
        gameflag = False
        
    

print("Thanks for playing")
