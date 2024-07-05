
def code_to_data(word, code):

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

    data = [g_d, y_d, b_d]
    return data

def get_new_word_bank(gd, yd, bd, wordbank):
    #green check
    i = 0
    while i < len(wordbank):
        w = wordbank[i]
        trigger = True
        for j, g in enumerate(gd):
            if g != 0 and g != w[j] and trigger:
                wordbank.remove(w)
                i -= 1
                trigger = False
        i += 1



    # black check
    i = 0
    while i < len(wordbank):
        w = wordbank[i]
        w_cpy = str(w) + ' '
        trigger = True
        for b in bd:
            if b not in yd:
                gd_cpy = gd.copy()
                index = []
                while b in gd_cpy:
                    index.append(gd_cpy.index(b))
                    gd_cpy[index[-1]] = '#'
                jj = 0
                for ii in index:
                    w_cpy = w_cpy[0:(ii-jj)] + w_cpy[(ii+1-jj)::]
                    jj += 1
                if b != 0:
                    if b in w_cpy and trigger:
                        wordbank.remove(w)
                        i -= 1
                        trigger = False
        i += 1

    # yellow check
    i = 0
    while i < len(wordbank):
        w = wordbank[i]
        trigger = True
        for ii, y in enumerate(yd):
            if y == w[ii] and trigger:
                wordbank.remove(w)
                i -= 1
                trigger = False
            elif y != 0 and str(y) not in w and trigger:
                wordbank.remove(w)
                i -= 1
                trigger = False
        i += 1

    return wordbank

def get_possible_codes():
    colors = ['g', 'y', 'b']

    combos = []

    for x1 in colors:
        for x2 in colors:
            for x3 in colors:
                for x4 in colors:
                    for x5 in colors:
                        combos.append(x1+x2+x3+x4+x5)

    return combos

