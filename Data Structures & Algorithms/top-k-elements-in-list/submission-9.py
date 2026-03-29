from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums ==[]:
            return []
        else:
            counter_arr = Counter(nums)
            print(counter_arr)
            scr =dict(sorted(counter_arr.items(), key =lambda x:x[1], reverse=True))
            print("sorted:", scr)
            k_most_frequent=[] 
            i=0

            for key,val in scr.items():
                k_most_frequent.append(key)
                i=i+1
                if i<k:
                    continue
                else:
                    break
            return k_most_frequent