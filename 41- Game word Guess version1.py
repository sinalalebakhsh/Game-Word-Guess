import os
os.system('cls')

def get_input():
    while True:
        user_input = input('Enter word: ')
        if user_input.isalpha():
            return user_input
        print('-'*20)
        print('Wrong word. Try again.')
        user_input = input('Enter word: ')

print(get_input())


