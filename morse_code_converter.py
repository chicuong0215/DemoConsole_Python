morse_arr = {'a': '.-',
             'b': '-...',
             'c': '-.-.',
             'd': '-..',
             'e': '.',
             'f': '..-.',
             'g': '--.',
             'h': '....',
             'i': '..',
             'j': '.---',
             'k': '-.-',
             'l': '.-..',
             'm': '--',
             'n': '-.',
             'o': '---',
             'p': '.--.',
             'q': '--.-',
             'r': '.-.',
             's': '...',
             't': '-',
             'u': '..-',
             'v': '...-',
             'w': '.--',
             'x': '-..-',
             'y': '-.--',
             'z': '--..',
             '1': '.----',
             '2': '..---',
             '3': '...--',
             '4': '....-',
             '5': '.....',
             '6': '-....',
             '7': '--...',
             '8': '---..',
             '9': '----.',
             '0': '-----',
             ' ': ' '
             }


def encode(text):
    for i in text:
        print(morse_arr[i], end=' ')


def decode(text):
    # convert text to array
    data = ''
    data_arr = []

    for i in text:
        if i != ' ':
            data += i
        else:
            data_arr.append(data)
            data = ''
    data_arr.append(data)

    # morse decode
    for code in data_arr:
        for key in morse_arr:
            if code == morse_arr[key]:
                print(key, end='')


# test
text1 = 'nguyenchicuong'
encode(text1)
print()
text2 = '-. --. ..- -.-- . -. -.-. .... .. -.-. ..- --- -. --.'
decode(text2)
