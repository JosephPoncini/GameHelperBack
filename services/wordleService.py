from utils.utils import code_to_data, get_new_word_bank, get_possible_codes
import json
import os

def get_wordle_data (word, code, word_bank):
    
    # print(word)
    # print(code)
    # print(word_bank)

    g_d = []
    y_d = []
    b_d = []
    for ii in range(5):
        if code[ii] == 'g':
            g_d.append(word[ii])
        else:
            g_d.append(0)

        if code[ii] == 'y':
            y_d.append(word[ii])
        else:
            y_d.append(0)

        if code[ii] == 'b':
            b_d.append(word[ii])
        else:
            b_d.append(0)

    code_data = [g_d, y_d, b_d]
    print(g_d)
    print(y_d)
    print(b_d)

    word_bank = get_new_word_bank(g_d, y_d, b_d, word_bank)
    print(word_bank)

    possible_codes = get_possible_codes()

    best_word = ''
    best_score = len(word_bank)

    for word in word_bank:
        print("The word is: " + word)
        score = 0
        for code in possible_codes:
            data = code_to_data(word, code)
            wordbank = word_bank.copy()
            wordbank = get_new_word_bank(data[0], data[1], data[2], wordbank)
            temp_score = len(wordbank)
            if temp_score > score:
                score = temp_score
                # bwb = wordbank.copy()
        if score < best_score:
            best_score = score
            best_word = word
            # wwb = bwb.copy()
    
    bs = best_score

    wordle_data = {
        "best_word": best_word,
        "best_score": best_score,
        "possible_words": word_bank,
    }

    print("This is the best word: " + best_word)

    return wordle_data