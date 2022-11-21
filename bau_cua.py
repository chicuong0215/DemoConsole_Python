import random


def run():
    score = 1000
    while True:
        if score > 0:
            select_arr = {'nai': 0, 'bau': 0, 'ga': 0, 'ca': 0, 'cua': 0, 'tom': 0}
            print('Điểm hiện tại: ' + str(score))
            print('Lựa chọn: ')
            for i in select_arr:
                print('\t' + i + ' - điểm đặt cược: ')
                select_arr[i] = int(input())
                score -= select_arr[i]

            item1 = random.choice(['nai', 'bau', 'ga', 'ca', 'cua', 'tom'])
            item2 = random.choice(['nai', 'bau', 'ga', 'ca', 'cua', 'tom'])
            item3 = random.choice(['nai', 'bau', 'ga', 'ca', 'cua', 'tom'])

            print('Kết quả:')
            for i in select_arr:
                if i == item1:
                    print('\t' + item1 + ": +" + str(2 * select_arr[i]))
                    score += 2 * select_arr[i]
                if i == item2:
                    print('\t' + item2 + ": +" + str(2 * select_arr[i]))
                    score += 2 * select_arr[i]
                if i == item3:
                    print('\t' + item3 + ": +" + str(2 * select_arr[i]))
                    score += 2 * select_arr[i]

            print('Điểm hiện tại: ' + str(score))
        else:
            print('Bạn đã phá sản!')

        print('Bạn có muốn tiếp tục? (y/n): ')
        if str.lower(input()) == 'n': break
