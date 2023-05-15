from linkedlist import LinkedList
import re
def get_file_lines(filename='/usr/share/dict/words'):
    with open(filename) as file:
        lines = [line.strip().upper() for line in file]
    return lines

def hash_words(words_list):
    # create a hash of all the words with the length being the key and the word as the value
    words = [None]*45
    for word in words_list:
        # longest word in the oxford dictionary is 45, just in case use modulus
        index = len(word) % 45
        if words[index] is None:
            words[index] = LinkedList()
        # add word to linked list
        words[index].append(word)

    return words

    return words[start:finish]
    
def solve_word_jumble(letters, circles, word_hash):
    possibilities = word_hash[len(letters)].items()
    answers = []
    sorted_letters = sorted(letters)
    for word in possibilities:
        if sorted(word) == sorted_letters:
            answers.append(word)

    letters = []
    for word in answers:
        for i in circles:
            letters.append(word[i])

    return (answers, letters)

def solve_final_jumble(circled_letters, num_letters, word_hash):
    if circled_letters != num_letters:
        return ''
    
    possibilities = word_hash[num_letters].items()
    answers = []
    letters = ''
    for letter in circled_letters:
        letters += letter

    sorted_letters = sorted(letters)

    for word in possibilities:
        if sorted(word) == sorted_letters:
            answers.append(word)
    
    return answers



def test_solve_word_jumble():
    words = get_file_lines()
    words = hash_words(words)

    circled_letters = []

    ans1 = solve_word_jumble('TEFON', [2,4], words)
    circled_letters.append(ans1[1])
    print(ans1)

    ans2 = solve_word_jumble('SOKIK', [0, 1, 3], words)
    circled_letters.append(ans2[1])
    print(ans2)

    ans3 = solve_word_jumble("NIUMEM", [4], words)
    circled_letters.append(ans3[1])
    print(ans3)

    ans4 = solve_word_jumble("SICONU", [4, 5], words)
    circled_letters.append(ans4[1])
    print(ans4)
    
    print(solve_final_jumble(circled_letters, 8, words))


if __name__ == '__main__':
    # word_list = get_file_lines()
    # words = hash_words(words_list)
    test_solve_word_jumble()

