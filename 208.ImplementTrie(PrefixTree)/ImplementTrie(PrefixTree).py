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
            # 如果找不到，返回None
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search_prefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            # 查找不到返回None
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None

if __name__ == '__main__':
    # 初始化数组
    trie = Trie()
    trie.insert("apple")
    trie.search('apple')
    trie.search('app')
    trie.startsWith('app')
    trie.insert("app")
    trie.search('app')