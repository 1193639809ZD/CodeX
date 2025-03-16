#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#


# @lc code=start
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        target = 24
        epsilon = 1e-6
        add, multiply, subtract, divide = 0, 1, 2, 3

        def backtrack(cards: List[float]) -> bool:
            if not cards:
                return False
            if len(cards) == 1:
                return abs(cards[0] - target) < epsilon
            for i, x in enumerate(cards):
                for j, y in enumerate(cards):
                    if i != j:
                        newCards = list()
                        for k, z in enumerate(cards):
                            if k != i and k != j:
                                newCards.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == add:
                                newCards.append(x + y)
                            elif k == multiply:
                                newCards.append(x * y)
                            elif k == subtract:
                                newCards.append(x - y)
                            elif k == divide:
                                if abs(y) < epsilon:
                                    continue
                                newCards.append(x / y)
                            # 如果返回结果是bool类型，这种写法可以减少判断代码
                            if backtrack(newCards):
                                return True
                            newCards.pop()
            return False

        return backtrack(cards)


# @lc code=end
