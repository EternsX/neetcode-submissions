class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        S1 = [0] * 26
        S2 = [0] * 26

        for i in range(len(s1)):
            S1[ord(s1[i]) - ord('a')] += 1
            S2[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(26):
            match += 1 if S1[i] == S2[i] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True
            c = s2[r]
            i = ord(c) - ord('a')
            S2[i] += 1
            if S2[i] == S1[i]:
                match += 1
            elif S2[i] - 1 == S1[i]:
                match -= 1
            

            c = s2[l]
            i = ord(c) - ord('a')
            S2[i] -= 1
            if S2[i] == S1[i]:
                match += 1
            elif S2[i] + 1 == S1[i]:
                match -= 1
            l += 1
        return match == 26




