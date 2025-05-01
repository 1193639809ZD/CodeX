#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#


# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # 如果没有变化，返回0
        if startGene == endGene:
            return 0
        # 将band变为hash表，加速查询
        bank = set(bank)
        # 如果end不在bank中，不合法，直接返回-1
        if endGene not in bank:
            return -1
        # 进行BFS
        queue = deque([(startGene, 0)])
        while queue:
            # cur是当前节点，step是当前节点的步数
            cur, step = queue.popleft()
            for i, x in enumerate(cur):
                for y in "ACGT":
                    if y != x:
                        comb = cur[:i] + y + cur[i + 1 :]
                        if comb in bank:
                            # 因为是最短路径，找到直接进行返回
                            if comb == endGene:
                                return step + 1
                            bank.remove(comb)
                            queue.append((comb, step + 1))
        return -1


# @lc code=end
