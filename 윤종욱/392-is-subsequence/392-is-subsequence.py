class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        idx = 0
        if len(s) == 0:
            return True
        for v in t:
            if s[idx] == v:
                idx += 1
                if idx != 0 and idx == len(s):
                    return True
            
        
        return False
        
        