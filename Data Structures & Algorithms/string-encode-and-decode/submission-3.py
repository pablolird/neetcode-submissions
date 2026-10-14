class Solution:
    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i]))+"$"+strs[i]
        
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        list_of_strings = []

        index = 0
        last = 0
        while index<=(len(s)-1):
            if (s[index]=="$"):
                x = int(s[last:index])
                list_of_strings.append(s[index+1:index+x+1])
                last = index+x+1
                index = index+x
            
            index = index + 1
        
        return list_of_strings


            
