#%%
## Solution works fine but is not efficient
nums = [1,2,3,4,5,6,7]
k = 3
for j in range(k):
    temp = nums[-1]
    print("#",temp)
    for i in range(len(nums)-1,0,-1):
        nums[i] = nums[i-1]
        print(nums)
    nums[0] = temp
# %%
print(nums)
# %%
