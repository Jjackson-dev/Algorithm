def solution(clothes):
    dic = {}
    for _ , cate in clothes:
        if not cate in dic:
            dic[cate] = 1
        else:
            dic[cate] += 1
    result = 1
    for i in dic.keys():
        result *= dic[i] + 1
    return result - 1
