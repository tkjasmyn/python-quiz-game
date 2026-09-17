import random
from utils import game, get_input

questions = [
    {
        "question": "Which animal is known for changing its color?",
        "options": ["Elephant", "Chameleon", "Dolphin", "Penguin"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "George Orwell"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "Which gas do humans need to breathe to survive?",
        "options": ["Carbon dioxide", "Oxygen", "Hydrogen", "Helium"],
        "answer": "B"
    },
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "C"
    }
]

while True:
    print('\n==== QUIZ ====')
    print('Start (y/n)?')
    user_input = get_input('> ').strip().lower()
    if user_input == 'y' or not user_input:
        random.shuffle(questions)
        game(questions)
        print('\nDo you want to replay? (y/n)')
        replay = get_input('> ').strip().lower()
        if replay == 'y' or not replay:
            continue
        elif replay == 'n':
            print('\nGoodbye!')
            exit()
    elif user_input == 'n':
        print('\nGoodbye!')
        exit()
    else:
        print('\nUnrecognized Input')