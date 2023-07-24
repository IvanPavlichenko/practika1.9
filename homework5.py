def check_digits(first):
    first_str = str(first)
    if len(first_str) == 4:
        return True
    else:
        return False

def three_same_dig(number):
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10
    return thousands == hundreds == tens or thousands == hundreds == units or thousands == tens == units or hundreds == tens == units

while True:
    first_year = int(input("Введите первый год: "))
    if check_digits(first_year):
        second_year = int(input("Введите второй год: "))
        if check_digits(second_year):
            for i in range(first_year, second_year + 1):
                three_same_dig(i)
                if three_same_dig(i):
                    print(i)
            break
        else:
            print("Число должно быть четырехзначное.\nПовторите ввод.")
    else:
        print("Число должно быть четырехзначное.\nПовторите ввод.")

