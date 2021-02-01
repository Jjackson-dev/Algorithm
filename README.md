# Algorithm

## Context

 - [Hash table](#hash-table)
 - [Array](#array)

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
   - [베스트앨범 코드(best_album.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/best_album.py)
   - 피드백 
    1. 조금 더 간편한게 할 수 있는 방법은 없는지 알아보기 
    2. dictionary를 2개씩 slicing하는 것에서 오류가 많이 발생했음 -> 로직을 너무 생각없이 짜지 말자 
    3. sorted 함수를 잘 활용하면 코드를 획기적으로 줄일 수 있다. 


## Array
### [배열] Leetcode : 121. Best Time to Buy and Sell Stock (Easy)
  - _You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock_.
    _Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0._
  - 해결방법 : 리스트, 하나의 포인트, minmax
               min과 max를 sys.maxsize를 이용해 정의하고 배열을 순회하며 min과 max를 업데이트한다.(min이 우선순위이고 min과 max를 동시에 바꾸진 않는다.)  
               각 과정마다 max-min으로 profit을 계산해 profit_list라는 배열에 append
               min이 바뀌게 되면 더 이상  max는 쓰이지 않으므로 다시 초기의 -sys.maxsize로 초기화해준다.
               이후, profit_list에서 가장 큰 값을 return 해준다. 
  - 시도횟수 4회 
    1. 몇몇 케이스들에 대해 분석이 부족했다. 
    2. 딱히 할만한 거래가 존재하지 않는다면 profit을 0으로 반환한다는 조건을 제대로 반영하지 않았다. 
      - profit list를 [0]으로 초기화해서 해결 
    3. min이 바뀌게 되면 더 이상 max가 쓰일 수 없다는 사실을 간과했다.
  - _Runtime: __896 ms, faster than 25.08%__ of Python online submissions for Best Time to Buy and Sell Stock._
    _Memory Usage: __22.4 MB, less than 34.63%__ of Python online submissions for Best Time to Buy and Sell Stock._
  - [Sell Stock 코드(Sell_Stock.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/Sell_Stock.py)
