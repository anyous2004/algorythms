# сложность   O(n)

def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)): # проходимся по ценам
        if prices[i] > prices[i - 1]: # если цена элемента, где мы сейчас больше, чем цена предыдущего, то
            max_profit += prices[i] - prices[i - 1] # к прибыли прибавляем их разницу
    return max_profit # возвращаем максимальную прибыль


print(maxProfit([7, 1, 5, 3, 6, 4]))