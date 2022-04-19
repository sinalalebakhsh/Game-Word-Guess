
import os, random
# from telnetlib import DO
os.system('cls')

def number_rounds():
    flag = 0
    list_org = []
    input_user = input('Enter rounds 1 to 999: ')
    while flag == 0:
        if len(input_user) == 0:
            input_user = input('Empty!!! Enter rounds 1 to 999 ')
        elif len(input_user) == 1 and flag == 0:
            if input_user in ['1','2','3','4','5','6','7','8','9']:
                list_org.append(int(input_user))
                flag = 1
            else:
                input_user = input('One number!!! not One character!!! Enter rounds 1 to 999 number: ')
        elif len(input_user) == 2 and flag == 0:
            if input_user[0] in ['1','2','3','4','5','6','7','8','9'] and input_user[1] in ['1','2','3','4','5','6','7','8','9','0']:
                list_org.append(int(input_user[0]))
                list_org.append(int(input_user[1]))
                flag = 1
            else:
                input_user = input('two number!!! not two character!!! Enter rounds 1 to 999 number:')
        elif len(input_user) == 3 and flag == 0:
            if input_user[0] in ['1','2','3','4','5','6','7','8','9'] and input_user[1] in ['1','2','3','4','5','6','7','8','9','0'] and input_user[2] in ['1','2','3','4','5','6','7','8','9','0']:
                list_org.append(int(input_user[0]))
                list_org.append(int(input_user[1]))
                list_org.append(int(input_user[2]))
                flag = 1
            else:
                input_user = input('three number!!! not three character!!! Enter rounds 1 to 999 number:')
        else:
            input_user = input('Do not enter more than 3! Enter rounds 1 to 999 ')

    strings = [str(integer) for integer in list_org]
    a_string = "". join(strings)
    an_integer = int(a_string)
    return an_integer    

user_input = 0
list_word = [] 

def input_for_list_words():
    input_user = '_'
    while input_user != 'finish':
        list_word.append(input_user)
        input_user = input('Enter one word: ')
    return list_word

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
