# 20250204 TIL
Today I Learned


* Dynamic Programming

````text
💡 문제에 대한 정답이 될 가능성이 있는 모든 해결책을 "체계적"이고 "효율적"으로 탐색하는 풀이법

1. 크고 복잡한 문제를 작은 문제들로 나눈다.(subproblem)

2. 하위 문제의 답을 계산한다.
   - 중복 계산해야 하는 하위 문제가 있다.(overlapping subproblem)
   - 한 번 계산한 결과는 메모리에 저장하여 재계산 하지 않도록 한다.(memoization, db table)

3. 하위 문제에 대한 답을 통해 원래 문제에 대한 답을 계산한다.(optimal substructure)
   - 최적 부분 구조: 하위 부분 문제에서 구한 최적의 답이 합쳐진 큰 문제의 최적의 답을 구할 수 있는 구조 
````

### Top-down
````python
memo = {} # 메모이제이션
def fibo(n):
    if n == 1 or n == 2:
        return 1
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2) # 재귀를 통한 탑다운
    return memo[n]
````
* 재귀 사용 => 구현시간이 빠르다.(실행시간이 느릴수도 있음)
* 재귀풀이에서 중복되는 계산값을 저장하여(memoization)동일한 함수 호출시 재활용 한다.
* hashtable 또는 list에 계산 결과를 저장한다.

### Bottom-up
````python
memo = {} # DP 테이블
def fibo(n):
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] # 점화식을 통한 바텀업
    return memo[n]
````
* 반복문 사용 => 실행시간이 빠르다.
* 더 작은 subproblem에 대한 계산결과를 DP table에 저장하여 더 큰 문제의 계산에 활용한다.
* hashtable 또는 list에 계산 결과를 저장한다.


----


* 완전탐색으로 시작
  * 하위문제로 나누기
  * 계산 결과 저장/재활용
* Overlapping subproblem
  * 문제를 하위 문제로 분해
  * 하위 문제의 계산값을 재사용
* Optimal substructure
  * 하위 문제의 최적 해법으로 원래 문제의 최적 해법을 구할 수 있다.
* Optimum value(최대, 최소), 방법의 개수 등을 구할 때
  * ~의 최소 비용은?
  * ~의 최대 이익은?
  * ~를 하는 방법의 개수는?
  * 특정 지점에 도달할 수 있는지?
* 미래의 계산이 앞선 계산 결과에 영향을 받을 때(분할 정복)


````text
❗️ DP  총정리

문제 풀이:
특정한 문제를 완전 탐색 알고리즘으로 접근해보고, 시간복잡도가 너무 높다면 DP를 적용할 수 있는지 생각
subproblem의 중복 여부를 판단하는것이 첫 번째 순서다.

구현 방법:  
1. 일단 재귀함수로 비효율적인 완전탐색 코드를 작성
2. 중복되는 subproblem의 계산 겨로가를 저장(memoization)한다.
3. 탑다운 -> 바텀업으로 코드 전환을 고려한다.


코테 출제:
DP는 문제에 적용하기에 어려운 개념이라서 코딩테스트에서는 기본에 충실한 문제 위주로 출제할 수 밖에 없다.
````
