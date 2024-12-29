import random
print('Welcome to this game "Rock , Paper and Scissors"...')

choices=('r','p','s')
type={'r':'ROCK','p':'PAPER','s':'SCISSORS'}
while True:
    user_choice=input('Rock,paper or scissors (r/p/s): ').lower()
    if user_choice not in choices:
        print('Please enter a valid choice.')

    computer= random.choice(choices)

    print(f'You chose {type[user_choice]}')
    print(f'Computer chose {type[computer]}')

    if user_choice==computer:
        print('Draw')
    elif (user_choice=='p' and computer=='r') or (user_choice=='r' and computer=='s') or (user_choice=='s' and computer=='p'):
        print('You Won!')
    else:
        print('You Lose')

    play_again=input('Wanna play again? (y/n): ').lower()
    if play_again=='n':
        print('Thanks for playing,come again!')
        break




