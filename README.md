# Algorithm

알고리즘을 공부하며 문제 해결을 위한 핵심아이디어나 실패했던 삽질들을 저장해두기 위한 저장소입니다.

굳이 하나의 플렛폼을 이용하지 않고 여러 플랫폼이나 책 등의 예시문제를 풀면서 작성했습니다. 

[참고 목록](#참고목록)

[알고리즘종류](#알고리즘-종류)

## Context

 - [Hash table](#hash-table)
 - [Array](#array)
 - [Linked List](#linked-list)
 - [Stack/Queue](#stack-queue)
 - [Sorting](#sorting)
 - [BFS(Breath-First-Search)](#BFS)

 
 
---

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
  - _Runtime: __896 ms, faster than 25.08%__ of Python online submissions for Best Time to Buy and Sell Stock._<br/>
    _Memory Usage: __22.4 MB, less than 34.63%__ of Python online submissions for Best Time to Buy and Sell Stock._
  - [Sell Stock 코드(Sell_Stock.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/Sell_Stock.py)
  
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
   - [연결리스트팬린드롬 코드(linked_list_palindrome.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/linked_list_palindrome.py)
   - [런너방식 설명](https://github.com/hsu-201458085/Python_Study)
   - [런너방식 코드(linked_lisr_palindrome_runner.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/linked_list_palindrome_runner.py)

 ### [연결리스트] Leetcode : 21. Merge Two Sorted Lists (Easy)
 Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
   - Easy 난이도임에도 불구하고 해결하지 못한걸 보니 연결리스트 문제가 취약하다. 
   - 해결하지 못했다. -> 시도 : 연결리스트를 리스트로 바꾼 뒤 +와 sorted로 날먹하려던걸 실패 
   - 해결방법 : 재귀로 비교해가면서 넣기 
   - [MergeSortedList 코드 (merge_sorted_list.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/merge_sorted_list.py)
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
- [반복을 이용한 코드(Reverse_iteration.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/Reverse_iteration.py)
- 재귀의 방식은
  - node.next = prev에 맞추어 먼저 나온게 맨 뒤로 가도록한다. (prev의 기본값은 None)
  - 다음 node는 next로 지정해 재귀적으로 reverse(next, node)를 반복하면 node가 새로운 prev가 되어 뒤집어진다. 
  - 기저조건은 node가 빌 때까지 이다. (if not node)
- [재귀를 이용한코드(Reverse_recursion.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/Reverse_recursion.py)
- 코드는 재귀가 더 간편해 보이지만 시간복잡도 공간복잡도는 반복이 훨씬 좋은 효율을 보였다. 반복은 Leetcode기준 전부 90%보다 상위인 높은 효율이였지만
  재귀에서는 시간복잡도는 70% 정도 더 앞서있었고 공간복잡도는 5% 보다 앞서서 반복보다 안좋은 효율을 보였다.
    
    
  ## Stack Queue
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
  - [Sort list 코드(Sort_list.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/Sort_list.py)
  
  ## BFS
  ### [너비우선탐색] 동빈나님 유튜브 예제 : 미로탈출 최소 거리?
   - N x M 모양의 미로에서 시작은 (1,1) 탈출구는 (n,m)으로 시작부터 탈출구까지의 최단거리를 찾는 문제이다. 
   - 미로의 각 지역마다 1 혹은 0 숫자가 지정되어있는데 1이 지나갈 수 있는 위치 0은 지나갈 수 없는 위치이다. 
   - 중요조건: 정답은 항상 있으며 시작지점과 탈출지점은 항상 1이다. 
   - 해결방법: 이동에 비용이 전부 동일하기 때문에 최단경로를 찾기 위해 BFS가 적합했다. 
   - BFS를 전공 책에서만 볼때는 Node들이 각자 어떻게 이어져있는지 나와있는 2차원배열이 보통이였는데 시뮬레이션형 문제는 
      처음 접해보았다. 시물레이션 문제처럼 상하좌우로 움직이는 것을 구현하는게 핵심인 것 같다. 
   -[미로탈출 코드(Escape_the_Maze.py)](https://github.com/hsu-201458085/Algorithm/blob/main/code/Escape_the_Maze.py)

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





