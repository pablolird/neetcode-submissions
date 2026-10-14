class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for str in strs:
            map_str = [0]*26
            for c in str:
                key = ord(c)-97
                map_str[key] = map_str[key]+1

            if tuple(map_str) not in map:
                map[tuple(map_str)] = [str]
            else:
                map[tuple(map_str)].append(str)

        return list(map.values())