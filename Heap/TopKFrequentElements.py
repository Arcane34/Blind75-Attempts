#https://leetcode.com/problems/top-k-frequent-elements/
#FINISHED

def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d={}

    for i in nums:
        if i in d:
            d.update( { i: d[i]+1} )
        else:
            d.update( {i: 0})

    """
    keys = d.keys()
    vals = d.values()
    topk= sorted(vals,reverse= True)
    
    out = []
    for i in range(k):
        indi = vals.index(topk[i])
        out.append(keys[indi])
    
    return out


    """

    dictB = sorted(d, key=d.get, reverse=True)
    return(dictB[0:k])        