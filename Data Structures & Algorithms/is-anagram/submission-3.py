class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hash_table_s = {}
        hash_table_t = {}
        
        for char_s, char_t in zip(s, t):
            hash_table_s[char_s] = hash_table_s.get(char_s, 0) + 1
            hash_table_t[char_t] = hash_table_t.get(char_t, 0) + 1
            
        return hash_table_s == hash_table_t
