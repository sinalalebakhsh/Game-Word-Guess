import os
os.system('cls')

list_word = ['sina', 'mahsa', 'lale', 'gilan', 'kimia', 'gandom', 'ommid', 'mina', 'lina', 'dina']

def dividing_line():
    print('-'*20)

def get_input():
    while True:
        user_input = input('Enter word: ')
        if user_input.isalpha():
            return user_input
        print('-'*20)
        print('Wrong word. Try again.')

def print_game_intro():
    dividing_line()
    print('Wellcome')
    print('word for guess:', list_word)
    dividing_line()

def run_game(number_rounds):
    print_game_intro()
    print(f'number of guess = {number_rounds}')
    correct_word = list_word[1]
    for s in range(number_rounds):
        user_input = get_input()
        if user_input.lower() == correct_word:
            dividing_line()
            print('YOU WON.')
            dividing_line()
            return
        else:
            print('Guessed wrong')
            print(f'Rounds left: {number_rounds-1-s}')
    dividing_line()
    print('You Lost')
    dividing_line()

run_game(3)


