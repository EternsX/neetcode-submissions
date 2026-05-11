class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S = [0] * 26
        T = [0] * 26

        for i in range(len(s)):

            S[ord(s[i]) - ord('a')] += 1
            T[ord(t[i]) - ord('a')] += 1
        
        return T == S
            
