def checkMagazine(magazine, note):

    # stores and their counts
    dict_mag =  get_dict_of_counts(magazine)
    dict_note = get_dict_of_counts(note)

    # If any word is absent then set it to False
    res = True

    for words_in_note in dict_note.keys():
        if words_in_note not in dict_mag.keys():
            res = False
            break

        elif dict_note[words_in_note] > dict_mag[words_in_note]:
            res = False
            break

    print('Yes' if res else 'No')


def get_dict_of_counts(words):
    dictx = {}
    for w in words:
        if w not in dictx.keys():
            dictx[w] = 1
            continue
        dictx[w] += dictx[w]+ 1

    return dictx


m = ['ive','got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
n = ['ive', 'got', 'some', 'coconuts']

checkMagazine(m, n)