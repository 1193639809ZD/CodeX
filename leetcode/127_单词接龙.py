#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 边界条件：如果 endWord 不在字典中，直接返回 0
        if endWord not in wordList:
            return 0
        # 边界条件：起点和终点相同，无需转换
        if beginWord == endWord:
            return 1

        L = len(beginWord)  # 所有单词的长度相同
        # 预处理：构建模式 -> 单词列表的映射
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # 将第i个字符替换为通配符"*"，生成模式
                pattern = word[:i] + "*" + word[i + 1 :]
                all_combo_dict[pattern].append(word)  # 记录该模式对应的原始单词

        # BFS初始化：起点为 beginWord，层级为1
        queue = deque([(beginWord, 1)])
        visited = set()  # 记录已访问的单词，避免环路
        visited.add(beginWord)  # 初始标记

        # BFS主循环
        while queue:
            current_word, level = queue.popleft()  # 取出当前层级的单词
            # 遍历单词的每个字符位置
            for i in range(L):
                # 生成当前单词的通配符模式
                pattern = current_word[:i] + "*" + current_word[i + 1 :]
                # 查找所有与该模式匹配的单词
                for adjacent_word in all_combo_dict.get(pattern, []):
                    # 找到终点，返回当前层级+1
                    if adjacent_word == endWord:
                        return level + 1
                    # 如果相邻单词未被访问过
                    if adjacent_word not in visited:
                        visited.add(adjacent_word)  # 标记为已访问
                        queue.append((adjacent_word, level + 1))  # 加入队列，层级+1

        # 如果遍历完所有可能仍未找到终点，返回0
        return 0


# @lc code=end
