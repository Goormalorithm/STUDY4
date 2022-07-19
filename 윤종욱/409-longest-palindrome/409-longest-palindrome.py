class Solution:
    def longestPalindrome(self, s: str) -> int:
        # dict_s = {}
        # for c in s:
        #     if c in dict_s.keys():
        #         dict_s[c] = dict_s[c] + 1
        #     else:
        #         dict_s[c] = 1
         
        dict_s = collections.Counter(s)
        length = 0
        for v in dict_s:
            length += dict_s[v] // 2 * 2
            if length % 2 == 0 and dict_s[v] % 2 == 1:
                length += 1
                
        
        return length
                