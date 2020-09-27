numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',

    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',

    100: 'hundred',
    1000: 'thousand',
    1000000: 'million',
    1000000000: 'billion',
    1000000000000: 'trillion',
}


def _number2word_tens(num):
    remainder = num % 100

    if remainder < 20:
        return numbers[remainder]

    if remainder % 10 == 0:
        return numbers[remainder]
    else:
        return numbers[remainder // 10 * 10] + '-' + numbers[remainder % 10]


def _number2word_hundreds(num):
    quotient = num // 100
    remainder = num % 100

    return (numbers[quotient] + ' ' + numbers[100] if quotient != 0 else '') + ' ' + _number2word_tens(remainder)


def _number2word_thousands(num):
    quotient = num // 1000
    remainder = num % 1000

    return (_number2word_hundreds(quotient) + ' ' + numbers[1000] if quotient != 0 else '') + ' ' + _number2word_hundreds(remainder)


def _number2word_millions(num):
    quotient = num // 1000000
    remainder = num % 1000000

    return (_number2word_hundreds(quotient) + ' ' + numbers[1000000] if quotient != 0 else '') + ' ' + _number2word_thousands(remainder)


def _number2word_billions(num):
    quotient = num // 1000000000
    remainder = num % 1000000000

    return (_number2word_hundreds(quotient) + ' ' + numbers[1000000000] if quotient != 0 else '') + ' ' + _number2word_millions(remainder)


def _number2word_digits(num, word_base):
    if word_base == 0:
        return ''

    quotient = num // word_base
    remainder = num % word_base

    if quotient == 0:
        return ' ' + _number2word_digits(remainder, word_base // 1000)
    
    if word_base >= 1000:
        return _number2word_hundreds(quotient) + ' ' + numbers[word_base] + ' ' + _number2word_digits(remainder, word_base // 1000)
    else:
        return _number2word_hundreds(quotient)


def number2word(num):
    if num < 0:
        raise ValueError('number should be greater than 0.')

    if num > 1000000000000000:
        raise ValueError('number should be less than one quadrillion.')

    return _number2word_digits(num, 1000000000000)


hi = number2word(139193457)
print(hi)
