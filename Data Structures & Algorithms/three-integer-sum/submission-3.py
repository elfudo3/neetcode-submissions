class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output_list = []
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            m = i + 1
            r = len(nums) - 1


            while m < r:
                if nums[i] + nums[m] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[m] + nums[r] < 0:
                    m += 1
                else:
                    
                    output_list.append([nums[i], nums[m], nums[r]])
                    m += 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1
                        
            
        return output_list
                
                


            

            


