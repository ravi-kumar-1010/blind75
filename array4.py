def ok(nums=[1,2,3,1]):
    x = set()
    for i in nums:
        if i in x:
            return True
        else:
            x.add(i)
    return False
ok()