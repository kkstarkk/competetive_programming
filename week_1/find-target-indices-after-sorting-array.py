class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        tar=[]
        for i in range(len(nums)):
            if nums[i] == target:
                tar.append(i)
        return tar
        
