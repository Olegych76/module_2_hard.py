dict_ = {3: ['1 и 2'],
         4: ['1 и 3'],
         5: ['1 и 4,', '2 и 3'],
         6: ['1 и 2,', '1 и 5,', '2 и 4'],
         7: ['1 и 6,', '2 и 5,', '3 и 4'],
         8: ['1 и 3,', '1 и 7,', '2 и 6,', '3 и 5'],
         9: ['1 и 2,', '1 и 8,', '2 и 7,', '3 и 6,', '4 и 5'],
         10: ['1 и 4,', '1 и 9,', '2 и 3,', '2 и 8,', '3 и 7,', '4 и 6'],
         11: ['1 и 10,', '2 и 9,', '3 и 8,', '4 и 7,', '5 и 6'],
         12: ['1 и 2,', '1 и 3,', '1 и 5,', '1 и 11,', '2 и 4,', '2 и 10,', '3 и 9,', '4 и 8,', '5 и 7'],
         13: ['1 и 12,', '2 и 11,', '3 и 10,', '4 и 9,', '5 и 8,', '6 и 7'],
         14: ['1 и 6,', '1 и 13,', '2 и 5,', '2 и 12,', '3 и 4,', '3 и 11,', '4 и 10,', '5 и 9,', '6 и 8'],
         15: ['1 и 2,', '1 и 4,', '1 и 14,', '2 и 3,', '2 и 13,', '3 и 12,', '4 и 11,', '5 и 10,', '6 и 9,', '7 и 8'],
         16: ['1 и 3,', '1 и 7,', '1 и 15,', '2 и 6,', '2 и 14,', '3 и 5,', '3 и 13,', '4 и 12,', '5 и 11,', '6 и 10,',
              '7 и 9'],
         17: ['1 и 16,', '2 и 15,', '3 и 14,', '4 и 13,', '5 и 12,', '6 и 11,', '7 и 10,', '8 и 9'],
         18: ['1 и 2,', '1 и 5,', '1 и 8,', '1 и 17,', '2 и 4,', '2 и 7,', '2 и 16,', '3 и 6,', '3 и 15,', '4 и 5,',
              '4 и 14',
              '5 и 13,', '6 и 12,', '7 и 11,', '8 и 10'],
         19: ['1 и 18,', '2 и 17,', '3 и 16,', '4 и 15,', '5 и 14,', '6 и 13,', '7 и 12,', '8 и 11,', '9 и 10'],
         20: ['1 и 3,', '1 и 4,', '1 и 9,', '1 и 19,', '2 и 3,', '2 и 8', '2 и 18,', '3 и 7,', '3 и 17,', '4 и 6,',
              '4 и 16',
              '5 и 15,', '6 и 14,', '7 и 13,', '8 и 12,', '9 и 11']}

while 1:
    str = input("Введите целое число от 3 до 20: ")
    if str.isdigit():
        num = int(str)
    else:
        break
    if 2 < num < 21:
        print('Пароли для введённого числа:')
        print(*dict_[num])
    else:
        break
