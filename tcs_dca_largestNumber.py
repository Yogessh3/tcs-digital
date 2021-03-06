def dominantIndex(nums):
    maxi=max(nums)
    for i in range(len(nums)):
        if(nums[i]!=maxi):
            if(2*nums[i]<=maxi):
                continue
            else:
                return -1
    return nums.index(maxi)