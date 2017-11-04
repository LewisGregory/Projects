import random
level = input("state the difficulty 1/2/3")
lives = 0
if level == "1":
    lives = 3
    print("easy mode")
    print("Using a number from 1-7")
    print("you will have 3 lives")
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
