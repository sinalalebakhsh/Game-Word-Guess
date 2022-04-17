import os
os.system('cls')

def dividing_line():
    print('-'*20)

def get_input():
    while True:
        user_input = input('Enter word: ')
        if user_input.isalpha():
            return user_input
        dividing_line()
        print('Wrong word. Try again.')

def select_in_list(user_input, words):
    while user_input.lower() not in words:
        dividing_line()
        print('Wrong word. Try again in list')
        user_input = get_input()

def print_game_intro():
    dividing_line()
    print('Wellcome')
    print('word for guess:', list_word)
    dividing_line()

def run_game(number_rounds, words):
    print_game_intro()
    print(f'number of guess = {number_rounds}')
    correct_word = words[1]
    for s in range(number_rounds):
        user_input = get_input()
        select_in_list(user_input, words)
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

list_word = ['sina', 'mahsa', 'lale', 'gilan', 'kimia', 'gandom', 'ommid', 'mina', 'lina', 'dina']
run_game(3, list_word)


