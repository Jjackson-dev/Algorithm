# Algorithm

## Context

 - [Hash table](#hash-table)

## Hash table
- [해시] 프로그래머스 1번 문제 : 위장
  - ('옷이름','카테고리')의 문자열 n개를 받아서 카테고리가 겹치지 않는 모든 경우의 수를 구하는 문제 
  - 첫번째 시도 : 모든 조합을 구하는 Power_set을 구한 뒤 카테고리가 겹치면 지우는 방식 --> 제한시간 초과 
  - 두번째 시도 : 하나의 새로운 카테고리가 들어올때마다 몇개의 경우의 수가 증가하는지를 파악한 뒤 문자열이 아닌 숫자계산으로만 해결 (해결완료) 
``` python
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
````
  - 피드백 
    1. 문자열 문제라고 무조건 문자로만 사용하지 않기 -> 간편화 가능성을 항상 염두 
    2. python다운 코드를 작성하기 -> 두개의 정보를 가진 문자열을 굳이 분리할 필요가 없음 
           
