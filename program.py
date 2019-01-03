#import random
import random

print('--------------------------------------------')
print('              HELLO WORLD')
print('--------------------------------------------')
print()

the_number = random.randint(0, 100)
name = input ('What is your name?')
#print (the_number, type(the_number))
#print (guess, type(guess))
#print (guess_text, type(guess_text))

guess = 101

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('{0} is too low, sucka. I mean {1}.'.format(guess, name))
    elif guess > the_number:
        print('{0}. Too damn high. {1}.'.format(guess, name))
    elif guess == the_number:
        print('Yay {0]. You win goodbye.'.format(name))
    else:
        'WTF kinda guess is that?'

print ('done.')

exit()
