class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            grouped[sortedWord].append(word)
        return list(grouped.values())