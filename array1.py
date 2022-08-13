def removeDuplicates(nums):
    i = 0
    j = 1
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    if max(nums) == min(nums):
        return 1
    while(nums[i] <= nums[j]):
        # print("#", i, j,"##",nums[i],nums[j])
        if nums[i] == nums[j]:
            # print("Inside first if")
            x = nums[j]
            # print("x",x)
            # print(j,len(nums)-1)
            if min(nums[j:len(nums)]) == max(nums[j:len(nums)]):
                return j
            for k in range(j,len(nums)-1):
                # print("Inside for loop",k)
                nums[k] = nums[k+1]
            nums[len(nums)-1] = x
        elif nums[i] < nums[j]:
            i+=1
            j+=1
            if j == len(nums):
                return j
        # print(nums)
    return i+1
removeDuplicates([0,0,1,1,1,2,2,3,3,4])