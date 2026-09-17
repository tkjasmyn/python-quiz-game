def game(questions):
    score = 0
    for q in questions:
        while True:
            print(f'''
Question: {q['question']}
Options: (A) {q['options'][0]} (B) {q['options'][1]} (C) {q['options'][2]} (D) {q['options'][3]}
''')
            user_answer = get_input('Your answer (press enter to skip): ').strip()
            if not user_answer:
                print(f"Skipped\nThe answer is {q['answer'].lower()}")
                break
            elif user_answer.upper() not in ('A', 'B', 'C', 'D'):
                print('Invalid Option')
                continue
            elif user_answer.upper() == q['answer']:
                print('\nCorrect ✅')
                score += 1
                break
            else:
                print(f"\nWrong ❌. The correct answer is {q['answer'].lower()}")
                break

    if score == len(questions):
        print(f'\nYou scored {score}/{len(questions)} 🎉')
    else:
        print(f'\nYou scored {score}/{len(questions)}')

def get_input(prompt):
    answer = input(prompt)

    if answer.lower() == 'exit':
        print('\nGoodbye!')
        exit()

    return answer