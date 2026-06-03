from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list)
        
        for s in strs:
            hashtable[tuple(sorted(s))].append(s)

        return list(hashtable.values())
        