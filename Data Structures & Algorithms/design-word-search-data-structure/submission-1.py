class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    return any(dfs(i+1, child) for child in cur.children.values())
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            
            return cur.end_of_word
        
        return dfs(0, self.root)
