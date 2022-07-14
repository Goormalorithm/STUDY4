class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        pair_st = {}
        pair_ts = {}
        
        for s_v, t_v in zip(s,t):
            if (s_v not in pair_st) and (t_v not in pair_ts):
                pair_st[s_v] = t_v
                pair_ts[t_v] = s_v   
                   
            elif pair_st.get(s_v) != t_v or pair_ts.get(t_v) != s_v:
                return False
        
        return True
                
        