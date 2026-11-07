from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # print(s.split(''))
        return Counter(list(s)) == Counter(list(t))
        # print(s_l)
        # t_l = Counter(list(t))
        # print(t_l)
        # print(s_l ==t_l)
        # print(t.split(''))

        # return False