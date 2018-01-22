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
        tmp = ''
        for i in string.split():
                tmp += (i + ' ')

        for i in tmp:
            if i.isalpha() or i == ' ':
                sanitizedString += i

        tmp = ''
        for i in sanitizedString.split():
            tmp += (i + ' ')

        sanitizedString = tmp
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


def special_char_count(string)->int:
    counter = 0
    for i in string:
        if not i.isalnum():
            counter += 1
    return counter


def vowel_count(string:str)->int:
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


def reverse_string(string:str)->str:
    '''
    Reverses a string.
    :param string: string to be reversed.
    :return: reversed string.
    '''
    return string[::-1]


def remove_vowels(string:str)->str:
    vowels = ['a', 'i', 'e', 'o', 'u', 'y']
    removed = ''
    for i in string:
        if i.lower() not in vowels:
            removed += i
    return removed


def FUNCTION_TESTS(string:str):
    '''Ensures that functions are working.'''
    x = string
    print('Initial string: ', end='')
    print(x)
    print('String sanitized w/ spaces: ', end='')
    print(sanitize(x))
    print('String sanitized w/o spaces: ', end='')
    print(sanitize(x, False))
    print('String Letter Count: ', end='')
    print(letter_count(x))
    print('String Special Char Count: ', end='')
    print(special_char_count(x))
    print('Vowel Count: ', end='')
    print(vowel_count(x))
    print('Random case: ', end='')
    print(random_case(x))
    print('String to simple leet: ', end='')
    print(to_number_leet(x))
    print('Reversed string: ', end='')
    print(reverse_string(x))
    print('String with no vowels: ', end='')
    print(remove_vowels(x))


FUNCTION_TESTS('My dumb, && long string that I love to use. **!')
