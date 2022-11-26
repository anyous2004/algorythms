"""Сложность алгоритма == O(n)^2"""

def uniquePathsWithObstacles(obstacleGrid):
    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]   # Создаем матрицу
    dp[0][0] = 1# Первый элемент равен 1
    for i in range(len(obstacleGrid)): # Проходим по списку
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[i][j] == 1: # Если камень нашелся
                dp[i][j] = 0 # Отметим камень
            elif i > 0 or j > 0: # Если индекс > 0
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]# прибавляем количество путей в матрицу
    return dp[-1][-1] # Выводим последний элемент матрицы


print(uniquePathsWithObstacles ([[0,0,0],[0,1,0],[0,0,0]]))