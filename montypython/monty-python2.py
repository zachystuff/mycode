#!/usr/bin/env python3

def montypython():

    rounds = 0
    while True:
        rounds += 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess \n --> ")

        if answer == 'Brian':
            print('Correct')
            break
        elif rounds == 3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Sorry! Try again!")


montypython()



