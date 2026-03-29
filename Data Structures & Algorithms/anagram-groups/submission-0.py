class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in range(0,len(strs)):
            CURRENT_STRING = strs[i].lower()
            CURRENT_KEY = "".join(sorted(CURRENT_STRING))
            if CURRENT_KEY in anagram_dict:
                anagram_dict[CURRENT_KEY].append(strs[i])
            else:
                anagram_dict[CURRENT_KEY] = [strs[i]]
        
        final_list = []
        for key, val in anagram_dict.items():
            final_list.append(val)
        return final_list
