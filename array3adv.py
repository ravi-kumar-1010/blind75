#%%
def reversal(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
#%%
def ok(nums,k):
    k = k % len(nums)
    if k > 0:
        nums.reverse()
        reversal(nums,0,k-1)
        reversal(nums,k,len(nums)-1)
        print(nums)
#%%
ok([1,2],3)
# %%
