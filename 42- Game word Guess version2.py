import os
os.system('cls')

list_word = ['sina', 'mahsa', 'lale', 'gilan', 'kimia', 'gandom', 'ommid', 'mina', 'lina', 'dina']

def get_input():
    while True:
        user_input = input('Enter word: ')
        if user_input.isalpha():
            return user_input
        print('-'*20)
        print('Wrong word. Try again.')

def print_game_intro():
    print('-'*20)
    print('Wellcome')
    print('word for guess:', list_word)
    print('-'*20)

def run_game():
    print_game_intro()
    print('number of guess = 5')
    correct_word = list_word[1]
    for s in range(5):
        user_input = get_input()
        if user_input == correct_word:
            print('YOU WON.')
            break
        else:
            print('Guessed wrong')
            print(f'Rounds left: {4-s}')

run_game()


