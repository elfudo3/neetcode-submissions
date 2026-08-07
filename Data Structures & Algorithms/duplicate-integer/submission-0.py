class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #initialize the hashset

        for n in nums: #for all numbers in nums
            if n in hashset: #if n is in the hashset
                return True #return true 
            hashset.add(n) #if not add it to the hashset
        return False #return false otherwise

        