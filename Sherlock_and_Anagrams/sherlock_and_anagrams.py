
def sherlockAndAnagrams(s):

    res = 0

    # create dict of words
    # words are created from overlapping substrings
    # characters in the words are sorted before making it key
    # words are keys and their counts in the string are values

    anagramS = getOverlappingSubstrings(s)
    #print(anagramS)
    for k in anagramS.keys():
        # pairs =  half of (wordcount - 1 * wordcount)
        res += ((anagramS[k] - 1) * anagramS[k]) // 2

    return res




def getOverlappingSubstrings(s):

    dictx = {}

    for ssLen in range(len(s)):
        for ssStart in range(len(s) - ssLen):
            sub_string = s[ssStart:ssStart + ssLen + 1]
            anagramS = ''.join(sorted(sub_string))

            # if anagramS present then +1 else 0
            dictx[anagramS] = dictx.get(anagramS, 0) + 1
            #print(anagramS, ':', dictx[anagramS])


    return dictx


#s = 'abba'         # 4
#s = 'ifailuhkqq'   # 3
#s = 'abcd'         # 0
#s = 'cdcd'          # 5
s = 'kkkk' # 10

print(sherlockAndAnagrams(s))
