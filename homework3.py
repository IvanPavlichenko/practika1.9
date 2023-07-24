def smallest_divisor(num):
    if num < 2:
        return None

    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            return divisor
        divisor += 1
    return None


number = int(input("Введите число: "))
result = smallest_divisor(number)

if result is not None:
    print("Наименьший делитель отличный от единицы:", result)
else:
    print("Наименьший делитель, отличный от единицы:", number)
