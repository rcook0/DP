def minimize_largest_sum(arr, k):
    def feasible(cap):
        parts=1; s=0
        for x in arr:
            if x>cap: return k+1
            if s+x<=cap: s+=x
            else:
                parts+=1; s=x
        return parts
    lo,hi=max(arr), sum(arr)
    while lo<hi:
        mid=(lo+hi)//2
        if feasible(mid)<=k: hi=mid
        else: lo=mid+1
    return lo
