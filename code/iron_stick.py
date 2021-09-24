def solution(arrangement):
    n=0
    answer=0
    list_n = []
    for i in arrangement:
        if i == "(":
            if n == 0:
                list_n += [0]
                n+=1         
            else : 
                if list_n[n-1]==0:
                    list_n[n-1]+=1
                    list_n += [0]
                    n+=1
                else:
                    list_n += [0]
                    n+=1
        else:
            if list_n[n-1] == 0:
                #레이저
                del list_n[n-1]
                n-=1
                list_n = [x+1 for x in list_n]
            else : 
                answer += list_n.pop(n-1)
                n-=1
    return answer
