import random
level = input("state the difficulty 1/2/3")
lives = 0
#because i use the same technique in all the levels of difficulty
#i will only comment the first level  
if level == "1":
    lives = 3
    print("easy mode")
    print("Using a number from 1-7")
    print("you will have 3 lives")
    compnumber = random.randint(1, 7)
    #here i am setting up a while loop to check when rhe lives have running out 
    while lives != 0:
        guess = input("guess my number")
        if int(guess) == compnumber: # here i use an if statement to check if guess is the the 						#same as the computers number 
            print("congratulations my number was: " + guess)
            break;
	#if so then the loop breaks
	#otherwise
        else:
            lives = lives - 1
            print("incorrect you now have "+ str(lives) + " lives remaining")
            #here i am check to see if the lives is not 0
            if lives != 0:
                if int(guess) > compnumber:
                    print("too high")
                else:
                    print("too low")
            elif lives == 0:
	    #elif lives is zero then i break the loop and thank the user for playing  
                print("thank you for playing")
                break;

#then i coppy and paste this ^ code 2 more times changing the range of the randint and the number of lives.

elif level == "2":
    lives = 5
    print("medium mode")
    print("Using a number from 1-15")
    print("you will have 5 lives")
    compnumber = random.randint(1, 15)
    while lives != 0:
        guess = input("guess my number")
        if int(guess) == compnumber:
            print("congratulations my number was: " + guess)
            break;
        else:
            lives = lives - 1
            print("incorrect you now have "+ str(lives) + " lives remaining")
            if lives != 0:
                if int(guess) > compnumber:
                    print("too high")
                else:
                    print("too low")
            elif lives == 0:
                print("thank you for playing")
                break;
if level == "3":
    lives = 7
    print("Beast mode")
    print("Using a number from 1-20")
    print("you will have 7 lives")
    compnumber = random.randint(1, 7)
    while lives != 0:
        guess = input("guess my number")
        if int(guess) == compnumber:
            print("congratulations my number was: " + guess)
            break;
        else:
            lives = lives - 1
            print("incorrect you now have "+ str(lives) + " lives remaining")
            if lives != 0:
                if int(guess) > compnumber:
                    print("too high")
                else:
                    print("too low")
            elif lives == 0:
                print("thank you for playing")
                break;
