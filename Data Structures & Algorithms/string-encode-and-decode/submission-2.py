class Solution:
    jointext = "XxX$$$$===$$$$XxX"

    def encode(self, strs: List[str]) -> str:
        strs.append(str(len(strs)))
        return (self.jointext.join(strs))

    def decode(self, s: str) -> List[str]:
        l = s.split(self.jointext)

        if ((s==self.jointext) and l[-1]=="0"):
            return []
        
        l.pop()
        return l