# сложность O(N^2)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def averageOfLevels(root):                        # на вход подаю корень
        queue = [root]                             # создаю очередь, в ней пока что только корень
        result = []                                 # список результата пока пустой
        while queue:                                # пока очередь не пустая
            result.append(sum([node.val for node in queue] )/ len(queue))    # в результат добавляю сумму узлов из очереди (на этом шаге в очереди всегда будут узлы с одной глубины)

            new_queue = []             # создаю новую пустую очередь
            for node in queue:         # в нее добавляю детей всех узлов, что были в изначальной очереди, то есть все узлы на уровень глубже
                if node.left: new_queue.append(node.left)
                if node.right: new_queue.append(node.right)
            queue = new_queue       # теперь работаю с новой очередью и так далее пока совсем не останется узлов и не достигнется None во всех детях
        return result

# сейчас создам такое дерево
"""
            20
        34       0
               2  6
        Ответ должен быть 20, 17, 4
"""
def main():
    five = TreeNode(6, None, None)
    four = TreeNode(2, None, None)
    three = TreeNode(0, four, five)
    two = TreeNode(34, None, None)
    one = TreeNode(20, two, three)
    print(TreeNode.averageOfLevels(one))

main()