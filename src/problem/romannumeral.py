def romanToInt(number):
    value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    previous_character = 0
    answer = 0

    for i in range(len(number)-1, -1, -1):
        if value[number[i]] >= previous_character:
            answer += value[number[i]]
        else:
            answer -= value[number[i]]

        previous_character = value[number[i]]

    print(answer)


print(romanToInt('III'))
