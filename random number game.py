import random


number = random.randint(1,50)
guess_count= ''
tries= 10
limit= ''
clue1='too low'
clue2='too high'
guess=''
guess_name = input("enter name here: ")

print(guess_name)
print(' Hello',guess_name,'I am thinking of a number between 1 - 50')
print('you have',tries,'to guess the number. Good luck :)')

while limit < '10':
    guess = int(input('enter your guess here:'))

    if guess < number:
        print(clue1)
        guess_count += guess_count
    elif guess > number:
        print(clue2)
        guess_count += guess_count
    elif guess == number:
        print('congrats the number is:',number)
        break

if limit == 11:
    print('out of tries the answer is:',number)
    
