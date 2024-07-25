from utils.wordHuntUtils import get_words


def get_word_hunt_data (board):
    words = get_words(board)

    new_lst = []
    for w in words:
        if w not in new_lst:
            new_lst.append(w)

    new_lst.sort(key=len, reverse=True)

    return new_lst
