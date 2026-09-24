class Solution:
    def encode(self, strs: List[str]) -> str:
        results = ""
        for word in strs:
            results += str(len(word)) + '#' + word
        return results


    def decode(self, s: str) -> List[str]:
      results = []
      i = 0

      while i < len(s):
          j = i
          while s[j] != '#':
              j += 1
          length = int(s[i:j])
          i = j + 1
          j = i + length
          results.append(s[i:j])
          i = j
      return results  
