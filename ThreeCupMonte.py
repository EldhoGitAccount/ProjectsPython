from random import shuffle

def shuffle_cups(mylist):
    shuffle(mylist)
    return mylist

def player_guess():

    guess=''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0,1 or 2")
    
    return int(guess)

def check_guess(mylist, myguess):
    if mylist[myguess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess")
        print(mylist)

#initial cup list
mylist = [' ', 'O', ' ']

#shuffle the cup list
shuffled_cup_list = shuffle_cups(mylist)

# user guess
guess = player_guess()

#check guess
check_guess(shuffled_cup_list, guess)