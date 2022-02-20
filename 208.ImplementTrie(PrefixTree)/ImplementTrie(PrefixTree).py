from typing import Optional
from typing import List

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        # 逐个字符向下查找
        for ch in word:
            ch = ord(ch) - ord("a")
            # 如果找不到，成为新的结点
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        # 词结束时，标记node状态为「结束」
        node.isEnd = True

    def search_prefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            # 查找不到返回None
            if not node.children[ch]:
                return None
            # 找的到的话 -> node 变成 子node
            node = node.children[ch]
        # 返回查找到的最后一个node
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        # 如果能检测到，并且该单词已经个结束
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None

if __name__ == '__main__':
    # 初始化数组
    trie = Trie()
    trie.insert('apple')
    trie.search('apple')
    trie.search('app')
    trie.startsWith('app')
    trie.insert('app')
    trie.search('app')