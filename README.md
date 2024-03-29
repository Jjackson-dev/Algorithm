# Algorithm

알고리즘을 공부하며 문제 해결을 위한 핵심아이디어나 실패했던 삽질들을 저장해두기 위한 저장소입니다.

굳이 하나의 플렛폼을 이용하지 않고 여러 플랫폼이나 책 등의 예시문제를 풀면서 작성했습니다. 

[참고 목록](#참고목록)

[알고리즘종류](#알고리즘-종류)

## Context
 - [Implement](#implement)
 - [String](#string)
 - [Hash table](#hash-table)
 - [Array](#array)
 - [Linked List](#linked-list)
 - [Stack/Queue](#stack-queue)
 - [Sorting](#sorting)
 - [DFS(Depth-First-Search)](#dfs)
 - [BFS(Breath-First-Search)](#bfs)

 
 
---
## Implement
### [구현] 프로그래머스 : 멀쩡한 사각형(Level 2)
   1. 저 세개의 그래프를 다 그려보면 가운데 그은 직선이 점을 지날 때가 존재한다.
     마지막 점을 포함해보면 최대공약수의 값과 일치하는 것을 알 수 있다. w=8, h=12인 사각형을 4개의 점으로 나눠보면 w=2, h=3인 사각형이 4개 존재하는 것을 알 수 있다. 
     정리해보면, X∗gcd(W,H) 를 통해 접어진 사각형을 알 수있다.
   2. 최소한의 크기의 직사각형에서 선이 그려지는걸 하나하나 생각해보면.
w=2, h=3인 직사각형에서 w와 h를 하나씩 추가해가면서 선을 그려보면 맨 시작부분에서 한번 겹치고 w와 h가 하나씩 추가 될 때마다 접히는 사각형이 하나씩 추가된다. 수식으로는 직선이 지나는 갯수 w+h−1이 되며 이를 전체 크기의 사각형으로 생각해보면 W+H−gcd(W,H) 공식을 통해 최종적으로 구할 수 있다.
  - [멀쩡한 사각형 코드 (plain_square.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/plain_square.py)
  - [문제 링크 (멀쩡한 사각형)](https://programmers.co.kr/learn/courses/30/lessons/62048)
     
### [구현] 프로그래머스 : 키패드누르기 (Level 2) 
  - KAKAO 인턴 채용문제 
  - 특별한 알고리즘은 보이지 않고 구현을 물어보는 문제같다 
  - 최적화를 생각한다면 목표숫자와 두 손가락의 거리를 어떻게 계산할 것인가? 하는 문제
   - value의 거리와 x와 y의 차이가 몇인가이므로 이렇게 표현하면 간단하다. 
   ```python
   def calc_dist(value, start):
    return abs(value[0]-start[0]) + abs(value[1]-start[1])
   ```
  - [키패드누르기 코드 (push_keypad.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/push_keypad.py)
  - [문제 링크 (키패드 누르기)](https://programmers.co.kr/learn/courses/30/lessons/67256)
  
## String
### [문자열] 프로그래머스 : 문자열 압축 (Level 2)
  - KAKAO 2020 블라인드 채용문제 
  - 문자열을 압축하는 알고리즘
  - 해결방법 : 1 ~ s의 길이-1 까지 모든 경우의 수에 대해서 문자열을 n개씩 자른 뒤 stack에 넣으면서 연속되면 합쳐주고 아니면 길이에 추가
  - [문자열 압축 코드 (string_compression.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/string_compression.py)
  - 삽질 3가지 
    - abcabcde 이렇게 있을 때 abc abc de 앞부분만 세개씩 자르면 de는 남아도됨
    - 중간에 설명이 있지만 한개만 있는경우 1이 생략됨
    - "aaaaaaaaaaa...aaaaa" 처럼 100a 이렇게 나오면 길이가 4임 -> 길이의 자릿수를 고려할 것

## Hash table
### [해시] 프로그래머스 : 튜플 (Level 2)
  - [문제링크 (튜플)](https://programmers.co.kr/learn/courses/30/lessons/64065)
  - 2019 카카오 개발자 인턴쉽
  - 이 문제에서 헷갈렸던 부분은 예시
     튜플이 (2, 1, 3, 4)인 경우
     {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
     {{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
     {{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}
     마지막 {{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}} 부분에서 왜 순서가 바뀌었나 싶었는데 사실 그게 중요한게 아님
     이 문제의 핵심은 튜플 수가 하나 둘 셋 넷 이렇게 늘면서 가장 많이 중복된 순서대로 결과물이 나온다는 점
  - [튜플 링크(tuple.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/tuple.py)
     
### [해시] 프로그래머스 : 오픈채팅방 (Level 2)
  - 2019 KAKAO 블라인드 채용 문제 
  - 해시 사용해서 유저ID에 대응되는 닉네임을 저장 
  - for문을 다시 돌며 문구를 저장, 시간복잡도는 약 O(N) 추정?
  - [오픈채팅방 코드 (openchat.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/openchat.py)
  - [문제 링크 (프로그래머스 오픈채팅방)](https://programmers.co.kr/learn/courses/30/lessons/42888) 

### [해시] 프로그래머스 : 위장 (Level 2) 
  - ('옷이름','카테고리')의 문자열 n개를 받아서 카테고리가 겹치지 않는 모든 경우의 수를 구하는 문제 
  - 첫번째 시도 : 모든 조합을 구하는 Power_set을 구한 뒤 카테고리가 겹치면 지우는 방식 --> 제한시간 초과 
  - 두번째 시도 : 하나의 새로운 카테고리가 들어올때마다 몇개의 경우의 수가 증가하는지를 파악한 뒤 문자열이 아닌 숫자계산으로만 해결 (해결완료) 
  - [위장 코드 (camouflage.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/camouflage.py)
  - 피드백 
    1. 문자열 문제라고 무조건 문자로만 사용하지 않기 -> 간편화 가능성을 항상 염두 
    2. python다운 코드를 작성하기 -> 두개의 정보를 가진 문자열을 굳이 분리할 필요가 없음 
   
           
  ### [해시] 프로그래머스 : 베스트앨범 (Level 3) 
   - 장르 리스트와 재생횟수 리스트를 받아 베스트 앨범을 출력하는 함수 
   - 세가지 조건에 따라 정렬되어야함 ( 1. 플레이수가 많은 장르  / 2. 플레이수가 많은 곡 / 3. 낮은 고유번호) 
   - 첫번째 시도 : 딕셔너리를 이용해 풀기 (해결완료) 
   - [베스트앨범 코드(best_album.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/best_album.py)
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
  - _Runtime: __896 ms, faster than 25.08%__ of Python online submissions for Best Time to Buy and Sell Stock._<br/>
    _Memory Usage: __22.4 MB, less than 34.63%__ of Python online submissions for Best Time to Buy and Sell Stock._
  - [Sell Stock 코드(Sell_Stock.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/Sell_Stock.py)
  
  ## Linked List
  ### [연결리스트] Leetcode : 234. Palindrome Linked List (Easy)
   - Given a singly linked list, determine if it is a palindrome.
   - 입력이 연결 리스트 형태로 주어질 때 팬린드롬여부를 확인한다. 
   - singly-linked list의 형태
   ```python
   # Definition for singly-linked list.
   class ListNode(object):
       def __init__(self, val=0, next=None):
           self.val = val
           self.next = next
   ```
   - 해결방법 1 : listnode.next가 0이 될 때까지 순회하며 List형태로 추가 후 <br>
                 list.pop()과 list.pop(0)를 하나씩 비교 (pop(0)의 시간복잡도는 O(N))
                 
   - 해결방법 2 : list가 아닌 collections.deque()에 append로 추가해준 뒤 <br>
                 deque.pop()과 deque.popleft()를 비교 (popleft()의 시간복잡도는 O(1))
                 
   - 해결방법 3 : 런너를 이용한 방법 -> fast가 2칸씩 slow는 한칸씩이동하며 slow와 반대인 rev생성<br>
                 fast가 끝에 도달하면 slow는 중간지점이므로 rev와 하나씩 비교 
   - [연결리스트팬린드롬 코드(linked_list_palindrome.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/linked_list_palindrome.py)
   - [런너방식 설명](https://github.com/Jjackson-dev/Python_Study)
   - [런너방식 코드(linked_lisr_palindrome_runner.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/linked_list_palindrome_runner.py)

 ### [연결리스트] Leetcode : 21. Merge Two Sorted Lists (Easy)
 Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
   - Easy 난이도임에도 불구하고 해결하지 못한걸 보니 연결리스트 문제가 취약하다. 
   - 해결하지 못했다. -> 시도 : 연결리스트를 리스트로 바꾼 뒤 +와 sorted로 날먹하려던걸 실패 
   - 해결방법 : 재귀로 비교해가면서 넣기 
   - [MergeSortedList 코드 (merge_sorted_list.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/merge_sorted_list.py)
   사실 내가 해결하지 못했던 방법이 왜 안되는지 궁금해서 한시간 넘게 디버깅해봤는데도 일단 답이 안나왔다.
   - TodoList(finished) : 
      1. retry with recursion on 2021.02.12 ( O ) -> Couldn't solve again, but understood the Logic -> try to next week again
      2. 내가 원래 했던 방법을 다시 시도해보고 성공한다면 성능 분석/비교해보기 ( O )
           -> nearly, but recursion technique is immature
      4. final Solve with recursion 21.02.19  ( O )
         -> finally solved!! on 2021.02.20
         -> Since the center is l1, first check 'if l1 is None', then 'if l2 is None', or compare with l1.val and l2.val.
      
 ### [연결리스트] Leetcode : Reverse Linked List (Easy)
- Reverse a singly linked list.
- 반복은 한번에 풀 수 있었지만 재귀는 바로는 못 풀어서 책을 참고했다.
- [반복을 이용한 코드(Reverse_iteration.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/Reverse_iteration.py)
- 재귀의 방식은
  - node.next = prev에 맞추어 먼저 나온게 맨 뒤로 가도록한다. (prev의 기본값은 None)
  - 다음 node는 next로 지정해 재귀적으로 reverse(next, node)를 반복하면 node가 새로운 prev가 되어 뒤집어진다. 
  - 기저조건은 node가 빌 때까지 이다. (if not node)
- [재귀를 이용한코드(Reverse_recursion.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/Reverse_recursion.py)
- 코드는 재귀가 더 간편해 보이지만 시간복잡도 공간복잡도는 반복이 훨씬 좋은 효율을 보였다. 반복은 Leetcode기준 전부 90%보다 상위인 높은 효율이였지만
  재귀에서는 시간복잡도는 70% 정도 더 앞서있었고 공간복잡도는 5% 보다 앞서서 반복보다 안좋은 효율을 보였다.
    
    
  ## Stack Queue
  ### [스택] 프로그래머스 : 쇠막대기 (Level 2) 
  - 쌓여있는 쇠막대기를 레이저로 자르면 몇개까지 나오는지 맞추는 문제
  - 문제해결관점에서 보면 list_n이라는 스택에 "("가 올때 0을 넣어둔다. 그리고 다음 입력이 "("가 오면 레이저가 아니기 때문에 0으로 넣었던 값을 1로 바꿔주고 0을 하나 더 append한다.
  - 그러다가 스택에 0이 있는데 ")"가 들어오면 레이저라는 뜻이므로 0을 스택에서 pop하고 이전 스택에 쌓인 값들을 전부 1씩 더해준다. (컷팅되었기 때문) 앞이 1인데 ")"이 들어오면 레이저가아니라 스틱이 끝났다는 뜻이므로 마지막값을 pop해주면서 total에 더해준다. 마지막 스틱이 끝나면 stack은 비게되고 total에 모든 값이 계산되어 들어가게 되는 구조
  - 구현하기 위해 list_n = [x+1 for x in list_n] 이런식으로 해결했는데 모든 리스트 값에 1씩 더해주는 방법이 생각이 안나서 이런 코드를 썼다.
  ```python
  #list_n = [x+1 for x in list_n]
  answer += sum(list_n)
  ```
  한번씩 다 접근해서 1씩 더하지말고 그냥 그때의 list_n 전체값을 total에 더하기
  - [쇠막대기코드(iron_stick.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/iron_stick.py)
  
  ### [스택] 프로그래머스 : 다리를 지나는 트럭 (Level 2) 
  - Too difficult Problem about stack. In Python, Most function already implemented so, Problem Implement should be perfected 
  - trying about it over an hour, but couldn't solve it.
  - TodoList(Processing) :: retry on 2021-02-27(  )


  ### [스택] 프로그래머스 : 주식가격 (Level 2) 
  - fail, Must Think different for time complexity (O(N))
  - TodoList(Processing) :: retry on 2021-02-27(  )


  ## Sorting
  ### [정렬] Leetcode : 148. Sort List
  - 입력이 Linked-List로 오기 때문에 Sorted보다는 병합정렬로 처리한다. 
  - Linked List의 경우 index를 내 마음대로 설정하기 어렵기 때문에 Quick Sorting은 비효율적이다. 
  - 병합 정렬에서 partition을 위해 중간지점을 알아야하지만 Linked_list이므로 Runner 방식을 활용한다. 
  - 배열을 받으면 순서대로 Linked_list 입력값을 만드는 init_linked_list()함수도 포함
  - 코드 자체내에서 테스트를 해보고 있음 
  - [Sort list 코드(Sort_list.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/Sort_list.py)


  ### [정렬] 프로그래머스 : 가장 큰 수 (Level 2) 
  - 순열을 만드는 것 까진 쉽게 생각 할 수 있으나 숫자의 비교를 어떻게 할지에 따라 방법이 천차만별이였다. 
  - 처음 시도 (실패) 
  ```python
  import itertools

  def solution(numbers):
    return sorted(["".join(i) for i in itertools.permutations(map(str,numbers))])[-1]
  ```
  - 실패원인 : 시간초과 O(N^2)
              생각하기에 가장 기본적으로 생각나는 방법으로 풀었으나 시간초과의 문제가 있었다. 
              핵심은 ['221', '3', '41', '34', '30'] 이런 입렺이 주어졌을 때 
              가장 큰 값이 되기 위해서는 숫자 맨앞을 기준으로 내림차순 정렬 해주면 된다. 
              여기까진 쉽게 알 수 있는데 문제는 '3', '34', '30' 맨 앞 숫자는 어떻게 
              구분할 것인가? 라는 문제가 발생했다. 처음 시도에선 간단하게 int로 바꿔서
              경우의 수를 구분했지만 이런 방식은 시간복잡도가 최악이였다. 
  - [가장 큰 값 코드(biggest_val.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/biggest_val.py)
  - 해결방식 : 결국 다른 사람의 코드를 참고했는데 문제 풀이 방식이 충격적이다. 
              lambda x: x*3를 이용해 문자열에 3을 곱한 것 
              아까의 예제에 다시 시도해보면 '333', '343434', '303030'으로 
              python에서 문자열의 대소구분은 맨앞부터 아스키를 구분하게 되므로 
              결국 ['34', '3' '30'] 이렇게 정렬이 가능하다. 
              문자열 문제를 조금 풀어봤지만 문자열의 곱셈을 해 대소구분한건 진짜 신박했다.
              
              
  ### [정렬] 프로그래머스 : H-Index (Level 2) 
  - 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
  - 해결방법 : 문제를 이해하는게 핵심인문제 구현자체는 정말 간단하다.
              H-Index는 실제로 학자를 평가하기 위해 사용되고있는 지표로 문제설명보단 
              wikipedia나 다른 레퍼런스를 보면서 이해할 수 있었다. 
              핵심 알고리즘은 인용 수를 내림차순으로 정렬한 뒤 index를 붙힌다. 
              index가 인용수보다 높아지는 시점이 H-Index이다. 
 -[H-Index코드(H_index.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/H_index.py)
  
  ## DFS
  ### [깊이우선탐색] Leetcode : 200. Number of Islands (Level 2)
  - An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.
  - DFS의 기본같은 문제 시뮬레이션 + DFS로 재귀를 이용해 쉽게 풀 수 있다. 
  - 내부함수를 이용할 수 도 있지만 기본적으로 Leetcode는 class형태로 제출하므로 self.인자를 이용해 구현했다.
  - 첫번째 시도는 시간초과 때문에 실패했는데 로직은 다음과 같다. 
    1. 처음부터 끝까지 순회하며 (이미갔던 곳이면 continue, 해당 위치값이 '1'이면 dfs(위치)를 실행한다.
    2. dfs는 맵 밖을 벗어나면 return 방문했다는 위치를 추가하며 동,서,남,북으로 dfs 재귀실행
    실패한 이유 : 기존 dfs의 방문개념에 충실해 if 위치 in discovered 같은걸 추가했는데 이게 문제였던 것 같다.
    [실패한 섬세기 코드(fail_count_islands.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/fail_count_islands.py)
  - 최적화 : discovered 삭제 
    이미 input으로 grid가 주어졌기 때문에 따로 discovered리스트를 만들지 않고 방문한 곳은 해당 위치를 '0'으로 바꾼 뒤 
    "1"일때만 dfs를 시도하는 식으로 최적화했더니 성공하였다.
    [섬세기 코드(count_islands.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/count_islands.py)
  
  ## BFS
  ### [너비우선탐색] 동빈나님 유튜브 예제 : 미로탈출 최소 거리?
   - N x M 모양의 미로에서 시작은 (1,1) 탈출구는 (n,m)으로 시작부터 탈출구까지의 최단거리를 찾는 문제이다. 
   - 미로의 각 지역마다 1 혹은 0 숫자가 지정되어있는데 1이 지나갈 수 있는 위치 0은 지나갈 수 없는 위치이다. 
   - 중요조건: 정답은 항상 있으며 시작지점과 탈출지점은 항상 1이다. 
   - 해결방법: 이동에 비용이 전부 동일하기 때문에 최단경로를 찾기 위해 BFS가 적합했다. 
   - BFS를 전공 책에서만 볼때는 Node들이 각자 어떻게 이어져있는지 나와있는 2차원배열이 보통이였는데 시뮬레이션형 문제는 
      처음 접해보았다. 시물레이션 문제처럼 상하좌우로 움직이는 것을 구현하는게 핵심인 것 같다. 
   -[미로탈출 코드(Escape_the_Maze.py)](https://github.com/Jjackson-dev/Algorithm/blob/main/code/Escape_the_Maze.py)

<br/>

---

<br/>

## 참고목록
### 책 
- 프로그래밍 대회에서 배우는 알고리즘 문제해결전략 - 구종만, 인사이트
- 파이썬 알고리즘 인터뷰 - 박상길, 책만

### 코딩테스트 플랫폼
- [leetcode](https://leetcode.com/)
- [프로그래머스](https://programmers.co.kr/)

### 그 외 
- [동빈나 유튜브](https://www.youtube.com/channel/UChflhu32f5EUHlY7_SetNWw)

---
## 알고리즘 종류 

### PS 입문

1. 체계적으로 문제 풀기 *
2. 코딩과 디버깅 *
3. 분석과 증명 *
4. brute-force *
5. 정렬
6. 재귀 * 
7. 분할 정복
8. 구간 합
9. 투 포인터 *
10. 수학 기초
11. 큐 *
12. 스택 *
13. 트리 기초
14. 탐색(BFS, DFS) *
15. 그래프 기초
16. 백 트래킹
17. 우선순위 큐

### PS 초급

1. 이분 탐색(parametric search)
2. 그리디 *
3. DP 기초 *
4. 좌표 압축
5. 수학 초급(소수 판정)
6. union-find
7. MST(크루스칼, 프림)
8. 다익스트라
9. 플로이드
10. 벨만 포드
11. 위상정렬
12. bitwise operation
13. trie
14. 기하 기초
15. 삼분 탐색(tenary search)

### PS 중급

1. 정수론(페르마 소정리, 에라토스 테네스)
2. DP 중급(tree DP, bitwise DP, ..)
3. 세그먼트 트리
4. plane sweeping
5. sqrt decomposition
6. offline query
7. binary lifting, LCA in tree
8. 큰거 작은거
9. meet in the middle
10. KMP
11. 해싱(라빈 카프)
12. Z algorithm
13. euler tour trick
14. SCC, 2-SAT
15. convex hull
16. 포함 배제의 원리
17. constructive
18. randomize
19. interactive

### PS 고급

1. 수학(확장 유클리드, 중국인의 나머지 정리, 가우스 소거법)
2. 세그먼트 트리 lazy propagation
3. merge sort tree
4. persistent segment tree
5. 단절점, 단절선
6. BCC
7. 이분 매칭
8. 네트워크 플로우
9. MCMF
10. min cut
11. Suffix Array
12. manacher
13. 아호 코라식
14. 스프라그-그런디
15. PBS
16. DP 최적화(Convex hull trick)
17. DP 최적화(D&C opt)
18. DP 최적화(knuth opt)

### PS 고급+

1. Heavy-light decomposition
2. centroid decomposition
3. offline dynamic connectivity
4. 수학(뫼비우스 반전 공식, 번사이드 보조정리, 홀의 결혼 정리)
5. FFT
6. connection profile DP
7. DP 최적화(Slope trick)
8. DP 최적화(Aliens trick)
9. DP 최적화(monotone queue opt)
10. DP 최적화(Hirschberg)
11. kitamasa
12. splay tree
13. link cut tree
14. general matching
15. matroid
16. eertree
17. voronoi





