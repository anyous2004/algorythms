# сложность O(n)

def getDescentPeriods(prices):
    n = len(prices)
    dp = [0] * n # создаем массив
    dp[0] = 1  # нулевой элемент равен 1

    for i in range(1, n): # проходимся по массиву
        dp[i] = 1 # элемент равен 1
        if prices[i] == prices[i - 1] - 1: # если цена элемента, где мы сейчас > цены единицы предыдущего на 1, то
            dp[i] += dp[i - 1] # в элемент добавляем предыдущий

    return sum(dp) # возвращаем сумму с массива


print(getDescentPeriods([3, 2, 4]))