def kadane1d(arr):
    max_current = max_global = arr[0]
    for i in range(1,len(arr)-1):
        max_current = max(arr[i], arr[i]+max_current)
        if max_current > max_global:
            max_global = max_current
    return max_global 
        
print(kadane1d([1,-3,2,1,-1])) 
