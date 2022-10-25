def numberOfSteps(num):
    result = 0 # обьявляем переменную, в которой будем считать количество шагов
    while num > 0: # пока число не дошло до 0
        if num % 2: # если при делении на 2 есть остаток, то вычитаем один
            num -= 1
        else:
            num /= 2 # и потом мы  делим на 2
        result += 1 # считаем количество шагов
    return result


print(numberOfSteps(8))