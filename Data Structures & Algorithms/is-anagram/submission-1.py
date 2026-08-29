class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def count(strings):
            ana_set = {}
            for letters in strings:
                if letters in ana_set:
                    ana_set[letters] += 1
                else: 
                    ana_set[letters] = 1
            return ana_set
        s_set = count(s)
        t_set = count(t)
        if s_set == t_set:
            return True
        else:
            return False

