
def sherlockAndAnagrams(s):

    res = 0

    # create dict of words
    # words are created from overlapping substrings
    # characters in the words are sorted before making it key
    # words are keys and their counts in the string are values

    anagramS = getOverlappingSubstrings(s)
    print(anagramS)
    for k in anagramS.keys():
        if anagramS[k] > 1:
            #print(k, anagramS[k])
            if len(k) == 1 and anagramS[k] == 2:
                res = res + 1
            else:
                res += anagramS[k]
    return res




def getOverlappingSubstrings(s):

    dictx = {}

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j+1]
            anagramS = ''.join(sorted(sub_string))
            #print(i, sub_string, '==>' ,anagramS)
            if anagramS in dictx.keys():
                dictx[anagramS] = dictx[anagramS] + 1
            else:
                dictx[anagramS] = 1

            #print(anagramS, ':', dictx[anagramS])


    return dictx





#s = 'abba'         # 4
#s = 'ifailuhkqq'   # 3
#s = 'abcd'         # 0
#s = 'cdcd'          # 5
s = 'kkkk' # 10

print(sherlockAndAnagrams(s))
