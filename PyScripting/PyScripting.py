import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def dif_select():
    difficulty = int(input("Select a difficulty: \n\n[1]> EASY (50 lifes)\n[2]> MEDIUM (20 lifes)\n[3]> HARD (5 lifes)\n\n$- "))
    if ((difficulty <= 0) or (difficulty >= 4)):
        input("\nWARNING: INPUT must be greater than 0 and smaller than 4, try again.")
        clear()
        alg()
    else:
        if difficulty == 1:
            return 50
        if difficulty == 2:
            return 20
        if difficulty == 3:
            return 5

def alg():
    lifes = dif_select()

    init = int(input("\nSet a initial range: "))
    end = int(input("Set a final range: "))
    
    if end < init:
        input("\nWARNING: INIT needs to be greater than END, try again.\n")
        clear()
        alg()
    
    hidden = random.randint(init, end)
    
    while 1:
        tried = 0
        limit = 20
        range_limit = end - init
        if range_limit < limit:
            input("\nWARNING: \nEND - INIT = {}\nEND - INIT must be greater than {}, try again.\n".format(range_limit ,limit))
            clear()
            alg()
        else:
            while 1:
                guess = int(input("\nTry a number between [{}] and [{}]: ".format(init,end)))
                if guess < init:
                    print("\nWARNING: [{}] is smaller than INIT, please use a value between [{}] and [{}]".format(guess, init, end))
                    tried += 1
                if guess > end:
                    print("\nWARNING: [{}] is larger than END, please use a value between [{}] and [{}]".format(guess, init, end))
                    tried += 1
                else:
                    if lifes == 0:
                        print("Game over, run out of lifes! Good luck next time...")
                        break
                    else:
                        if (guess == hidden) & (guess > init) & (guess < end):
                            clear()
                            tried += 1
                            input("YOU WIN!!!\n\nYou found the hidden value! It is [{}]!\nYou tried [{}] numbers.\n".format(hidden, tried))
                            exit(0)
                            break
                        if (guess > hidden) & (guess >= init) & (guess <= end):
                            tried += 1
                            lifes -= 1
                            print("\n[{}] is greater than the hidden value, try again!\n[{}] lifes remaining".format(guess, lifes))
                        if (guess < hidden) & (guess >= init) & (guess <= end):
                            tried += 1
                            lifes -= 1
                            print("\n[{}] is smaller than the hidden value, try again!\n[{}] lifes remaning".format(guess, lifes))

alg()