class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq, window = {}, {}
        res = ""

        for c in t:
            t_freq[c] = 1 + t_freq.get(c, 0)
        
        have, need = 0, len(t_freq)

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_freq and window[c] == t_freq[c]:
                have += 1
            
            while have == need:
                if len(res) == 0 or len(res) > r - l:
                    res = s[l:r+1]
                
                c = s[l]
                window[c] = -1 + window.get(c, 0)

                if c in t_freq and window[c] < t_freq[c]:
                    have -= 1

                l += 1
            
        return res
