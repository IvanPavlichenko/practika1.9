def sum_digits(number, sum):
    for i in str(number):
        sum += int(i)
    return sum

def count_digits(number, count):
    while number > 0:
        number //= 10
        count += 1
    return count


while True:
    number = int(input("Введите число: "))
    if number > 0:
        break
    else:
        print("Вы ввели некоретное число, попробуйте снова")

sum_dig = 0
count_dig = 0

print("\nСумма чисел:", sum_digits(number, sum_dig))
print("\nКоличество цифр в числе:", count_digits(number, count_dig))
print("\nРазность суммы и количества цифр:", sum_digits(number, sum_dig) - count_digits(number, count_dig))

