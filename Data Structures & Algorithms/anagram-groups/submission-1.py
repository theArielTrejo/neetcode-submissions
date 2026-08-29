from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      thegroups = defaultdict(list)
      for word in strs:
        key = "".join(sorted(word))
        thegroups[key].append(word)
      return list(thegroups.values())  