class TreeNode:
    def __init__(self, v: str):
        self.val: str = v
        self.children: dict = {}
        self.endhere: bool = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root: TreeNode = TreeNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        wordLength: int = len(word)
        for i in range(wordLength):
            char: str = word[i]
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i == wordLength - 1:
                parent.endhere = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.endhere

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True
