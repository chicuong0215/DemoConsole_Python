import random


def run():
    while True:
        print('Lựa chọn của bạn (tai, xiu): ')
        user_selection = str.lower(input())
        item1 = random.randint(1, 6)
        item2 = random.randint(1, 6)
        item3 = random.randint(1, 6)
        result = item1 + item2 + item3

        # xỉu
        if 4 <= result <= 10:
            print('Kết quả: xỉu')
            if user_selection == 'xiu':
                print('Bạn thắng!')
            else:
                print('Bạn thua!')
        # tài
        elif 11 <= result <= 17:
            print('Kết quả: tài')
            if user_selection == 'tai':
                print('Bạn thắng!')
            else:
                print('Bạn thua!')

        print('Bạn có muốn tiếp tục? (y/n): ')
        if str.lower(input()) == 'n': break
