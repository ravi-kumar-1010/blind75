def ok(nums1,nums2):
    freq1 = {}
    freq2 = {}
    for i in nums1:
        if i in freq1:
            freq1[i] +=1
        else:
            freq1[i] = 1
    for i in nums2:
        if i in freq2:
            freq2[i] +=1
        else:
            freq2[i] = 1
    resd = {key: min(freq1[key],freq2[key]) for key in freq2 if key in freq1}
    res = []
    for i in resd.keys():
        res.extend(resd[i]*[i])
    return res
ok([4,9,5],[9,4,9,8,4,5])
