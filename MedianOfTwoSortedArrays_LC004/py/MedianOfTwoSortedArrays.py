def findMedian(ns1, ns2):
    MIN_V = -2e10
    MAX_V = 2e10
    len1 = len(ns1)
    len2 = len(ns2)
    size = len1+len2

    if len1 > len2:
        return findMedian(ns2, ns1)
    
    if len1 == 0:
        return (ns2[(len2-1)//2] + ns2[len2//2])/2
    

    cutL = 0
    cutR = len1
    cut1 = (cutL+cutR)//2
    cut2 = size//2 - cut1

    while cut1 < len1:
        cut1 = (cutL+cutR)//2
        cut2 = size//2 - cut1
        print('cutL = {}'.format(cutL))
        print('cutR = {}'.format(cutR))
        print('cut1 = {}'.format(cut1))
        print('cut2 = {}'.format(cut2))

        L1 = MIN_V if (cut1 == 0) else ns1[cut1-1]
        R1 = MAX_V if (cut1 == len1) else ns1[cut1]
        L2 = MIN_V if (cut2 == 0) else ns2[cut2-1]
        R2 = MAX_V if (cut2 == len2) else ns2[cut2]

        if L1 > R2:
            cutR = cut1-1
        elif L2 > R1:
            cutL = cut1+1
        else:
            if size%2 == 0:
                L1 = max(L1,L2)
                R1 = min(R1,R2)
                return (L1+R1)/2
            else:
                return min(R1,R2) 

ns2 = [1,2,3,4,6,7,12,15,18,30]
ns1 = [5,7,9,10,11,19,21,22,23,24]
ret = findMedian(ns2, ns1)
print(ret)
