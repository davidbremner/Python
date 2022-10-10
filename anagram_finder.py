with open('/Users/david.bremner/Documents/Engineering/Klarna Python Course/2of4brif.txt') as in_file:
    word_list = in_file.read().strip().split('\n')
    word_list = [x.lower() for x in word_list]


while True:

    lookup_word = input('Give me a word: ').strip().lower()
    clean_word = sorted(lookup_word)

    anagram_list = []

    for word in word_list:
        if lookup_word == word:
            pass
        elif sorted(word) == clean_word:
            anagram_list.append(word)

    number_of_anagrams = len(anagram_list)

    if number_of_anagrams >= 1:
        print(f"Congratulations you have {number_of_anagrams} from the word '{lookup_word}'! "
              f"{lookup_word.title()}'s anagrams are: {', '.join(anagram_list)}.")
    else:
        print('Sorry not an anagram from our list...')
