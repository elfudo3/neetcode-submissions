class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq_dict = Counter(nums)
       return [num for num, count in freq_dict.most_common(k)]
       
        
        
        
