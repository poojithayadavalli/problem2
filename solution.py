def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    res = []
    if( len(nums1) < len(nums2) ):
        for i in nums1:
            if(i in nums2):
                res.append(i)
    else:
        for i in nums2:
            if(i in nums1):
                res.append(i)
    return res
    
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
print(intersection(nums1, nums2))
