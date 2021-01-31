def solution(genres, plays):
    list_a = list(map(list,zip(genres, plays)))
    
    #1. dic1 만들기
    dic1 = {index:value for index,value in enumerate(list_a)} 
    
    dic2 = {}
    #2. dic2 생성 (key=곡의장르, value=총 수)
    for key in dic1.keys():
        if dic1[key][0] not in dic2:
            dic2[dic1[key][0]] = dic1[key][1]
        else:
            dic2[dic1[key][0]] += dic1[key][1]
            
    #3. dic2 count 기준 정렬 후 리스트를 뽑아내자 
    dic2 = dict(sorted(dic2.items(), key=lambda item : -item[1]))
    
    #순서 
    genres_rank = list(dic2.keys())
    
    # 장르 : 장르 순서순으로 새로운 dic3 ex) 'classic' : 0 ....
    dic3 = {value:index for index,value in enumerate(genres_rank)}
    
    
    #장르1의 장르를 dic1대로 변경하자 
    for word in dic3.keys():
        for key in dic1.keys():
            if(dic1[key][0] == word):
                dic1[key][0] = dic3[dic1[key][0]]
        
    #dic 1 sorted 
    #1-곡이름 오름차순, 2-곡숫자 내림차순 -> 3-index(key) 오름차순
    dic1 = dict(sorted(dic1.items(), key=lambda item : (item[1][0], -item[1][1], item[0])))
    
    #상위 두곡만 추출 
    dic4 = {code:g[0] for code, g in dic1.items()}

    result =[]
    for i in range(len(dic3)):
        result += [[]]

    for item in dic4.items():
        result[item[1]] += [item[0]]

    final = []
    for i in result :
        final += i[:2]
        
    return final
