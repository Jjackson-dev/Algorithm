def solution(arr):
    if sum(arr)==0:
        return 0
    
    lag = 0
    for idx, val in enumerate(sorted(arr, reverse=True)):
        if idx+1 > val:
            return idx
        else:
            lag = val
            
    return idx+1
