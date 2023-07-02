for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('taktik')
    elif i % 3 == 0:
        print('tak')
    elif i % 5 == 0:
        print('tik')
    else:
        print(i)