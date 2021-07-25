
def sherlockAndAnagrams(s):

    res = 0

    # create dict of words
    # words are created from overlapping substrings
    # characters in the words are sorted before making it key
    # words are keys and their counts in the string are values

    anagramS = getOverlappingSubstrings(s)

    for k in anagramS.keys():
        if anagramS[k] > 1:
            res += 1

    return res




def getOverlappingSubstrings(s):

    dictx = {}

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j+1]
            anagramS = ''.join(sorted(sub_string))

            if anagramS in dictx.keys():
                dictx[anagramS] += dictx[anagramS]

            else:
                dictx[anagramS] = 1


    return dictx





s = 'abba'
#s = 'abcd'
print(sherlockAndAnagrams(s))
