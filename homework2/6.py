# сложность O(n)

def rob(nums): # код с лекции
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(dp)):
        dp[i] = max(dp[i-1], dp[i - 2] + nums[i])
    return dp[-1]


list_ = [1,2,3]
print(max(rob(list_[1:]), rob(list_[:len(list_) - 1]))) # ответ - это макс элемент от функции rob, вызванной сначала для всех домов, кроме 0-го, а потом для функции от всех домов, кроме последнего