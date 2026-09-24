class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
      updated_s = s
      index_s = 0
      index_t = 0
      count = 0
      while index_t < len(t):
        if updated_s[index_s] == t[index_t]:
            index_s += 1
            index_t += 1

        else:
            index_s += 1

        if index_s >= len(updated_s):
            count += 1
            updated_s = updated_s + t[index_t : len(t)]
                      
      return len(updated_s) - len(s)