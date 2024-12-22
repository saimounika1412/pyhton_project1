import random
start_range,end_range=1,50
random_number=random.randint(start_range,end_range)
chances=5
no_of_guess=0
while no_of_guess<chances:
    no_of_guess+=1
    user_guess=int(input())
    if user_guess==random_number:
        print('Congrats !! Your guess is correct.')
        break
    elif user_guess>random_number:
        
        print('Your guess is higher.')
        continue
    elif user_guess<random_number:
        print('Your guess is lower.')
        continue
    else:
        print('Your guess is invalid.')
        continue
else:
    print('Oops,Better Luck Next Time!')
