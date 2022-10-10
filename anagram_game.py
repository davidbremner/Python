import random
import sys

answer_list = ['russia', 'germany', 'england', 'france', 'italy',
               'spain', 'bolivia', 'portugal', 'netherlands', 'sweden']

list_count = len(answer_list)
country_count = 0
lives = 3

while True:
    anagram = random.choice(answer_list)
    choice_list = list(anagram)
    random.shuffle(choice_list)
    combined = ''.join(choice_list)
    print(combined)
    answer = input('What is the anagram? Answer: ').lower().strip()

    if answer == anagram:
        print('That is correct!')
        country_count += 1
        answer_list.remove(anagram)
    else:
        lives -= 1
        print(f'Unfortunately, that is incorrect. Lives left {lives}.')
    if country_count == list_count:
        break
    if lives == 0:
        sys.exit(f'Sorry you now have 0 lives and scored {country_count}, go study the globe.')

print(f'Well done you matched them all with a grand score of {country_count}!')
