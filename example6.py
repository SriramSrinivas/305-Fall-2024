import random
guess=random.randint(1,50)
print(guess)
number=int(input('Enter a number'))
if(guess==number):
    print('Lucky number!')
elif (number<guess):
    print('number is less')
else:
    print('number is greater')