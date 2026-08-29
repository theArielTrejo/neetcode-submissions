from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        # Defauldict is different from regular dict aka if i were to do anagrams = {}
        # If I wanted to store a key in a regular DICT, i have to check if it exist first
        # In a DEFAULTDICT, it autocreates, no need to check if it exist first 
        for word in strs:
            key = ''.join(sorted(word)) # Creates a key if doesnt not exist, as mentioned above
            # then if another word has the same key, it adds the word from the list to the pair
            anagrams[key].append(word)
        
        # Return grouped anagrams as a list of lists
        return list(anagrams.values())