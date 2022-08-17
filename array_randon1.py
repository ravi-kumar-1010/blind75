def ok(nums,k):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    res = []
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}
    res = list(freq.keys())[:k]
    return res
ok([0,1,1,1,2,2,3],2)