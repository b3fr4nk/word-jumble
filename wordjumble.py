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
    # gets all words with same number of letters
    possibilities = word_hash[len(letters)].items()
    answers = []
    # finds all words matching the letters
    sorted_letters = sorted(letters)
    for word in possibilities:
        if sorted(word) == sorted_letters:
            answers.append(word)

    # gets the circled letters currently for last word only
    letters = []
    for word in answers:
        for i in circles:
            letters.append(word[i])

    return (answers, letters)

def solve_final_jumble(circled_letters, num_letters, word_hash):
    """very similar to solve jumble but uses circled letters in a list instead of a string and does not return any circled letters"""
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

    ans1 = solve_word_jumble('ITNGA', [1, 4], words)
    circled_letters.append(ans1[1])
    print(ans1)

    ans2 = solve_word_jumble('KAOEW', [2, 3, 4], words)
    circled_letters.append(ans2[1])
    print(ans2)

    ans3 = solve_word_jumble("NUCPHA", [3, 5], words)
    circled_letters.append(ans3[1])
    print(ans3)

    ans4 = solve_word_jumble("OTLBET", [2, 3, 5], words)
    circled_letters.append(ans4[1])
    print(ans4)
    
    print(solve_final_jumble(circled_letters, 10, words))


if __name__ == '__main__':
    # word_list = get_file_lines()
    # words = hash_words(words_list)
    test_solve_word_jumble()

