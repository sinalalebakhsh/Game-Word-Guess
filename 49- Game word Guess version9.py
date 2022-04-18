import os, random
os.system('cls')

user_input = 0

list_word = [] 


def input_for_list_words():
    input_user = 'sina'
    while input_user != 'finish':
        list_word.append(input_user)
        input_user = input('Enter one word: ')
    return list_word
    
def number_rounds():  
    user_input = int(input('How many rounds do you play? '))
    return user_input

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
    return user_input.lower()

def print_game_intro():
    dividing_line()
    print('Wellcome')
    print('word for guess:', list_word)
    dividing_line()

def run_game(number_rounds, words):
    print_game_intro()
    print(f'number of guess = {number_rounds}')
    correct_word = random.choice(words)
    for s in range(number_rounds):
        user_input = get_input()
        select_in_list(user_input, words)
        if user_input == correct_word:
            dividing_line()
            print('YOU WON.')
            dividing_line()
            return
        else:
            print('Guessed wrong')
            print(f'Rounds left: {number_rounds-1-s}')
    dividing_line()
    print('You Lost')
    print(f'the correct answer: {correct_word}')
    dividing_line()


input_for_list_words()

run_game(number_rounds(), list_word)


