def numJewelsInStones(jewels, stones):
    count = 0                 # счетчик = 0
    for i in stones:            # прохожусь по своим камням
        for j in jewels:        # прохожу по каждому драгоценному камню
            if i == j:          # если есть совпадение
                count += 1    # счетчик +1
    return count              # счетчик возвращается


print(numJewelsInStones('укЯ', 'ууКяЯкерт'))