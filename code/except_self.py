def solutions(nums: list) -> list:
    # calculate left_list
    left = [1]
    for i in range(len(nums)-1):
        # left_list == 1 , a, a*b, a*b*c == list[0], list[0]*num[0], list[1]*num[1], list[2]*num[2]
        left.append(nums[i] * left[i])

    # calculate right_list:
    right = [1]
    j = 0
    for i in range(len(nums)-1, 0, -1):
        right.append(nums[i] * right[j])
        j += 1
    right = right[::-1]
    
    return [left[i] * right[i] for i in range(len(left))]
