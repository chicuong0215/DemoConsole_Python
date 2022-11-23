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


def run():
    while True:
        print("Chức năng")
        print("\t1. Morse encode")
        print("\t2. Morse decode")
        print("Lựa chọn: ", end='')
        selection = int(input())
        if selection == 1:
            print("Nhập text: ", end='')
            encode(input())
        if selection == 2:
            print("Nhập text: ", end='')
            decode((input()))

        print('\nBạn có muốn tiếp tục? (y/n): ')
        if str.lower(input()) == 'n': break


# test
run()
