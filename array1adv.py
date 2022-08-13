#%%
def removeDuplicates(nums):
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    unique = 0
    for pointer in range(1,len(nums)):
        if nums[pointer] != nums[unique]:
            nums[unique+1],nums[pointer] = nums[pointer],nums[unique+1]
            unique += 1
    return unique+1
#%% 
removeDuplicates([1,1])
# %%
