number =int(input('Enter a number'))
if number%3==0 and number%5==0:
    print('Hi -- Bye')
elif number%5==0:
    print('Bye')
elif number%3==0:
    print('Hi')
else:
    print('Good luck')