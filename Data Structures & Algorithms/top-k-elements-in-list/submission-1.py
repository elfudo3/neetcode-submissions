class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        top_k_elements = freq_dict.most_common(k)
        result = []
        #this is how we loop through the dictionary and append to the returnable list
        for num, count in top_k_elements:
            result.append(num)
        
        return result
        