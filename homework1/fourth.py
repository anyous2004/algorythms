def sumBase(n, k):
    result = 0             # результат = нулю
    while n != 0:           # пока число не равно нулю
        result += n % k    # к счетчику прибавим остаток от деления нацело( 0 + 1)
        n = n // k          # n равно целой части от n:k ( 4, 0)
    return result          # возвращаю результат


print(sumBase(16, 4))