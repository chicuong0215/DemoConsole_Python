import random


def run():
    is_continue = True
    while is_continue:
        print('Lựa chọn của bạn (keo, bua, bao): ')
        user_selection = str.lower(input())
        machine_selection = random.choice(['keo', 'bua', 'bao'])

        print('Bạn chọn: ' + user_selection)
        print('Máy chọn: ' + machine_selection)

        if user_selection == 'keo':
            if machine_selection == 'keo':
                print('Hòa nhau!')
            elif machine_selection == 'bua':
                print('Bạn thua!')
            elif machine_selection == 'bao':
                print('Bạn thắng!')
        elif user_selection == 'bua':
            if machine_selection == 'bua':
                print('Hòa nhau!')
            elif machine_selection == 'bao':
                print('Bạn thua!')
            elif machine_selection == 'keo':
                print('Bạn thắng!')
        elif user_selection == 'bao':
            if machine_selection == 'bao':
                print('Hòa nhau!')
            elif machine_selection == 'keo':
                print('Bạn thua!')
            elif machine_selection == 'bua':
                print('Bạn thắng!')

        print('Bạn có muốn tiếp tục? (y/n): ')
        is_continue = input()
        if str.lower(is_continue) == 'n': break
