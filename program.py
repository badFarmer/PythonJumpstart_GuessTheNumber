#import random
import random

print('--------------------------------------------')
print('              HELLO WORLD')
print('--------------------------------------------')
print()

the_number = random.randint(0,100)

#print (the_number, type(the_number))
#print (guess, type(guess))
#print (guess_text, type(guess_text))

guess = 101

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('too low, sucka.')
    elif guess > the_number:
        print('too damn high.')
    elif guess == the_number:
        print('Yay. You win goodbye.')
    else:
        'WTF kinda guess is that?'

print ('done.')

exit()
