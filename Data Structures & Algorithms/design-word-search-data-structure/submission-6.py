class TrieNode:
    def __init__(self):
        self.next = {}
        self.ends = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.next:
                ptr.next[c] = TrieNode()
            ptr = ptr.next[c]
        ptr.ends = True
        
    def search(self, word: str) -> bool:
        return self.searchPattern(word, 0, self.root)

    def searchPattern(self, pattern, index, node):
        if (index==len(pattern)):
            return node.ends

        if pattern[index]==".":
            for letter in node.next:
                if self.searchPattern(pattern, index+1, node.next[letter]):
                    return True
            return False
        else:
            if pattern[index] not in node.next:
                return False
            return self.searchPattern(pattern, index+1, node.next[pattern[index]])
        
