# Algorithm

## Context

 - [Hash table](#hash-table)

## Hash table
### [해시] 프로그래머스 : 위장 (Level 2) 
  - ('옷이름','카테고리')의 문자열 n개를 받아서 카테고리가 겹치지 않는 모든 경우의 수를 구하는 문제 
  - 첫번째 시도 : 모든 조합을 구하는 Power_set을 구한 뒤 카테고리가 겹치면 지우는 방식 --> 제한시간 초과 
  - 두번째 시도 : 하나의 새로운 카테고리가 들어올때마다 몇개의 경우의 수가 증가하는지를 파악한 뒤 문자열이 아닌 숫자계산으로만 해결 (해결완료) 
  - [위장 코드 (camouflage.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/camouflage.py)
  
  - 피드백 
    1. 문자열 문제라고 무조건 문자로만 사용하지 않기 -> 간편화 가능성을 항상 염두 
    2. python다운 코드를 작성하기 -> 두개의 정보를 가진 문자열을 굳이 분리할 필요가 없음 
           
           
  ### [해시] 프로그래머스 : 베스트앨범 (Level 3) 
   - 장르 리스트와 재생횟수 리스트를 받아 베스트 앨범을 출력하는 함수 
   - 세가지 조건에 따라 정렬되어야함 ( 1. 플레이수가 많은 장르  / 2. 플레이수가 많은 곡 / 3. 낮은 고유번호) 
   - 첫번째 시도 : 딕셔너리를 이용해 풀기 (해결완료) 
``` python
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
```
- 피드백 
 1. 조금 더 간편한게 할 수 있는 방법은 없는지 알아보기 
 2. dictionary를 2개씩 slicing하는 것에서 오류가 많이 발생했음 -> 로직을 너무 생각없이 짜지 말자 
 3. sorted 함수를 잘 활용하면 코드를 획기적으로 줄일 수 있다. 
 
