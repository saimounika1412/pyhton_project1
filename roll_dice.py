import random
while True:
    ans=input('Want to roll dice? :(y/n)')
    if ans=='y' or ans=='Y':
        x=random.randint(1,6)
        y=random.randint(1,6)
        print(f'({x},{y})')
    elif ans=='n' or ans=='N':
        print('Thanks for playing!')
        break
    else:
        print('Please enter a valid input.')
