def solution(s):
    #input to list
    stack = []
    s = s[1:-1].split('}')
    stack = [num[2:] for num in s[1:]][:-1]
    stack.append(s[0][1:])
    
    #Counting
    for nums in stack:
        list_num = nums.split(',')
        for num in list_num:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
    #Sorting
    dict_key = sorted(counter.items(),
           key=lambda item:item[1],
           reverse=True)
   
    answer = [int(num[0]) for num in dict_key]
    
    return answer