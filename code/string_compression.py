from collections import Counter
def solution(s):
    list_len = []
    if len(s) ==1:
        return 1
    for n in range(1, len(s)):
        list_s = []
        st= 0
        end= n
        while True:
            if len(s[st:end]) == 0:
                break
            list_s.append(s[st:end])
            st += n
            end += n
        stack = []
        l = 0
        for ls in list_s:
            if not stack:
                stack.append(ls)
                continue
            if stack[-1] == ls:
                stack.append(ls)
            else:
                if len(stack) > 1:
                    l += len(str(len(stack)))
                l += len(stack[-1])
                stack = []
                stack.append(ls)

        if stack:
            if len(stack) > 1:
                l += len(str(len(stack)))
            l += len(stack[-1])
        list_len.append(l)

    return min(list_len)
