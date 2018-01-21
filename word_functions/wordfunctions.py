'''
These functions get statistics on strings.
'''
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


def letterCount(string:str)->int:
    '''
    Send in a string, get only letters back.
    :param string: Any string.
    :return: Number of chars
    '''
    count = sanitize(string, False)
    return len(count)

def vowelCount(string:str)->dict:
    '''
    Run in a string, this will count up vowels.
    :param string: Some string.
    :return: A dictionary with vowel count.
    '''
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
    s = string.lower()
    for i in s:
        if i in vowels:
            vowels[i] += 1
    return vowels

x = 'my strIng is... really long&&.    x'
x = sanitize(x)
print('x is:', vowelCount(x))