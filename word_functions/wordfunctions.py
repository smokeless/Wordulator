'''
Just your everyday functions. Maybe extend out strings.
'''
import random
import emoji


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
        if not i.isalnum() and i != ' ':
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


def most_common_vowel(string:str)->tuple:
    '''
    String in, out most common vowel. Includes y.
    :param string:
    :return: tuple, most common vowel/number.
    '''
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
    working = sanitize(string, False)
    working = working.lower()
    for i in working:
        if i in vowels:
            vowels[i] += 1
    occ    = 0
    letter = ''

    for k in vowels:
        if vowels[k] > occ:
            occ = vowels[k]
            letter = k
    return (letter, occ)


def least_common_vowel(string:str)->tuple:
    '''
    Get the least common vowel and a count.
    :param string:
    :return: (vowel, count)
    '''
    working = sanitize(string, keepSpaces=False)
    working = working.lower()
    vowels  = {'a':0, 'i':0, 'e':0, 'o':0, 'y':0}

    for i in working:
        if i in vowels:
            vowels[i] += 1
    char  = ''
    count = 0
    for k in vowels: #get a non-zero vowel to compare against.
        if vowels[k] != 0:
            char  = k
            count = vowels[k]

    for k,v in vowels.items():
        if v < count and v != 0:
            count  = v
            char = k

    if not char: #todo decide how to handle no vowels.
        try:
            raise ValueError('No vowels with > 0 count.', char, count)
        except ValueError as e:
            print(e.args)

    return char, count


def to_morse_code(string:str)->str:
    '''
    convert string to morse code.
    :param string: string
    :return: morse code.
    '''
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ".": ".-.-.-",
        ",": "--..--"
    }
    working   = string.upper()
    working   = working.split()
    morseList = []
    for i in working:
        word = ''
        for c in i:
            if c in morse:
                word += (morse[c] + ' ')
        morseList.append(word)
    converted = ' '.join(morseList)
    return converted

def to_emoji(string:str)->str:
    '''
    Using emoji module.
    :param string: string to convert.
    :return: converted string.
    '''


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
    print('Most common vowel:', end='')
    print(most_common_vowel(x))
    print('Least common vowel: ', end='')
    print(least_common_vowel(x))
    print('To morse code: ', end='')
    print(to_morse_code(x))

FUNCTION_TESTS('This is some messy string that no 1 chars** about!')
