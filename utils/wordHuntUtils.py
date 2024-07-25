import os

def get_words(board):

    dictionary = []
    letters = []

    file_path = os.path.join(os.path.dirname(__file__), '../data/Collins Scrabble Words (2019).txt')
    
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for word in lines:
        word = word[0:-1].upper()
        dictionary.append(word)   

    for seq in board:
        for l in seq:
            letters.append(l)

    dictionary = shorten_dictionary(dictionary,letters, board)

    switch_board = []

    def check_word(w, i, loc):
        switches = switch_board[:]
        grape = False
        for x in range(4):
            for y in range(4):
                if check_if_letter(x, y, w, i, board) and check_not_taken(x, y, switches) and check_if_next_to(x, y, loc):
                    if check_if_last_letter(w, i):
                        grape = True
                    else:
                        i += 1
                        switch_board[x][y] = 1
                        loc = [x, y]
                        grape = check_word(w, i, loc)
        return grape

    words = []
    for w in dictionary:
        i = 0
        loc = []
        switch_board = [[0 for _ in range(4)] for _ in range(4)]
        if check_word(w, i, loc):
            words.append(w)
    return words

def check_if_letter(x, y, w, i, board):
    if board[x][y] == w[i]:
        return True
    else:
        return False

def check_if_next_to(x, y, loc):
    if loc == []:
        return True
    elif (abs(x - loc[0]) <= 1) and (abs(y - loc[1]) <= 1):
        return True
    else:
        return False

def check_not_taken(x, y, switches):
    if switches[x][y] == 0:
        return True
    else:
        return False

def check_if_last_letter(w, i):
    if len(w)-1 == i:
        return True
    else:
        return False

def get_squ_lvl_2(board):
    adds = [0, 1, -1]
    squ_lvl_2 = []

    for x in range(4):
        for y in range(4):
            for h in adds:
                if (x+h >= 0) and (x+h <= 3):
                    for k in adds:
                        if (y+k >= 0) and (y+k <= 3):
                            if (h != 0) or (k != 0):
                                seq = board[x][y] + board[x+h][y+k]
                                squ_lvl_2.append(seq)

    return squ_lvl_2

def shorten_dictionary(dict, letters,board):

    squ_lvl_2 = get_squ_lvl_2(board)


    lst = []
    for xx in squ_lvl_2:
        if xx not in lst:
            lst.append(xx)

    new_dict = []
    for seq in lst:
        for word in dict:
            if seq in word:
                new_dict.append(word)

    new_dict2 = []

    i = 0
    for w in new_dict:
        good = True
        for l in w:
            if l not in letters:
                good = False
        if good:
            new_dict2.append(w)

    return new_dict2

