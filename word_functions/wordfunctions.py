'''
Just your everyday functions. Maybe extend out strings.
'''
import random
def sanitize(string:str, keepSpaces=True )->str:
    '''
    Cleans a string down to letters.
    :param string: A string.
    :param keepSpaces: Do we want to keep spaces or not?
    :return: Cleaned string.
    '''
    if keepSpaces == True:
        sanitizedString = ''
        l = string.split()
        tmp = ''
        for i in l:
                tmp += (i + ' ')
        for i in tmp:
            if i.isalpha() or i == ' ':
                sanitizedString += i
        return sanitizedString
    else:
        l = ''.join(string.split())
        sanitizedString = ''
        for i in l:
            if i.isalpha():
                sanitizedString += i
        return sanitizedString


def letter_count(string:str)->int:
    '''
    Send in a string, get only letters back.
    :param string: Any string.
    :return: Number of chars
    '''
    count = sanitize(string, False)
    return len(count)

def total_vowel_count(string:str)->int:
    '''
    Run in a string, this will count up vowels.
    :param string: Some string.
    :return: a count of vowels
    '''
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    s = string.lower()
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count

def to_number_leet(string:str)->str:
    '''
    Converts a string to number leet speak.
    :param string: string to convert.
    :return: converted string
    '''
    leetDict = {'o':'0', 'l':'1', 'z':'2', 'e':'3', 'a':'4',
                's':'5', 'g':'6', 't':'7', 'b':'8', 'p':'9'}
    leetString = ''
    for c in string:
        lower = c.lower()
        if lower in leetDict:
            leetString += leetDict[lower]
        else:
            leetString += c
    return leetString

def random_case(string)->str:
    '''
    randomize string case
    :param string: string in.
    :return: randomized case
    '''
    finishedString = ''
    for i in string:
        ranInt = random.randint(0,2)
        if i.isalpha:
            if ranInt == 0:
                finishedString += i
            elif ranInt == 1:
                finishedString += i.lower()
            else:
                finishedString += i.upper()
        else:
            finishedString += i
    return finishedString


x = 'my string is... really long&&.    x'
x = sanitize(x)
x = random_case(x)
x = to_number_leet(x)
print('x is:',x)