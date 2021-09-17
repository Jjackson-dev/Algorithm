def solution(numbers, hand):
    answer = ''
    left_f = [3,0]
    right_f = [3,2]
    dict_nums = {
        1:[0,0], 2:[0,1],3:[0,2],4:[1,0],5:[1,1],
        6:[1,2],7:[2,0],8:[2,1],9:[2,2],0:[3,1]}
    def calc_dist(value, start):
        goal = dict_nums[value]
        return abs(goal[0]-start[0]) + abs(goal[1]-start[1])    


    for num in numbers:
        if num in [1,4,7]:
            left_f = dict_nums[num]
            answer+="L"
        elif num in [3,6,9]:
            right_f = dict_nums[num]
            answer+="R"
        else:
            left_dist = calc_dist(num, left_f)
            right_dist = calc_dist(num, right_f)
            if left_dist < right_dist:
                left_f = dict_nums[num]
                answer+="L"
            elif right_dist < left_dist:
                right_f = dict_nums[num]
                answer+="R"
            else:
                if hand == "left":
                    left_f = dict_nums[num]
                    answer+="L"
                else: 
                    right_f = dict_nums[num]
                    answer+="R"
    return answer
