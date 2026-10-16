class PrefixTree:
    def __init__(self):
        self.rootMap = {}

    def insert(self, word: str) -> None:
        self.addNode(word, 0, self.rootMap)

    def addNode(self, word, index, map):
        if index==len(word):
            map["TERMINATION"] = True
            return
        
        if word[index] not in map:
            map[word[index]] = {}
        
        if "TERMINATION" not in map:
            map["TERMINATION"] = False
        
        self.addNode(word, index+1, map[word[index]])
            

    def search(self, word: str) -> bool:
        return self.checkNode(word, 0, self.rootMap)

    def checkNode(self, word, index, map):
        if (index==len(word)):
            return map["TERMINATION"]

        if word[index] not in map:
            return False
        
        return self.checkNode(word, index+1, map[word[index]])
        

    def startsWith(self, prefix: str) -> bool:
        return self.checkPrefix(prefix, 0, self.rootMap)

    def checkPrefix(self, prefix, index, map):
        if (index==len(prefix)):
            if map:
                return True
            else:
                return False
        
        if prefix[index] not in map:
            return False
        
        return self.checkPrefix(prefix, index+1, map[prefix[index]])
        