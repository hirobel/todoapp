def add_10(num):
    try:
        add_num = num + 10
        print('add_num is {}'.format(add_num))
        return add_num
    except:
        print('Error!')

add_10('a')