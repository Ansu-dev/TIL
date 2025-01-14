# 20250113 TIL
Today I Learned


* 항해99 1일 1코테 스터디


### ❗️ 백준 2776 - 암기왕

#### Set을 이용한 집합으로 풀기
````python
import sys
input =  sys.stdin.readline
# T 테스트 케이스
T = int(input())

# 집합 set을 사용하여 풀이
# O(T * (N + M)) => 이진 탐색보다 효율적
for _ in range(T):
    # N 수첩1에 입력받을 정수의 개수
    N = int(input())
    note_1 = set(map(int, input().split())) # 집합 사용
    # M 수첩2에 입력받을 정수의 개수
    M = int(input())
    # 숫자 순서대로 있어야 하므로
    note_2 = list(map(int, input().split()))

    for num2 in note_2:
        if num2 in note_1:
            print(1)
        else:
            print(0)
````
* note_2 배열을 기준으로 note_1의 숫자가 note_2에 존재하는지 비교
* note_1을 list형태의 배열로 비교해도 되지만 시간복잡도가 M*N*T라는 O(N³)의 시간복잡도가 생김
* set을 통해 검색을 효율적으로 변경 => set함수의 시간복잡도는 O(1)
* 시간복잡도 O(T * (N + M))으로 이전 보다 훨씬 효율


````text
💡 Set
- 효율적인 검색: set은 해시 테이블(hash table)을 기반으로 구현되어 있다.
각 요소는 해시 값을 통해 저장 위치가 결정되므로, 평균적으로 O(1) 시간 복잡도로 요소의 추가, 삭제, 검색이 가능하다.
- 중복 제거: 리스트에서 중복된 요소를 제거하고자 할 때 유용하다.
- 집합 연산: 수학적인 집합 연산이 필요한 경우에 사용됩니다. 예를 들어, 두 그룹 간의 공통 사용자 찾기, 독립적인 항목 찾기 등에 유용하다.
````

----------------------------


#### 이진탐색을 이용해 풀기
````python3
import sys
input =  sys.stdin.readline
# T 테스트 케이스
T = int(input())

def binary_search(target, array):
    # 넘어오는 숫자를 이진탐색으로 존재 유무 유추
    cur_min = 0 # 최소 인덱스
    cur_max = len(array) - 1 # 최대 인덱스
    cur_guess = (cur_min + cur_max) // 2
    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return 1
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2
    return 0

# O(T * (N log N + M log N))
for _ in range(T):
    # N 수첩1에 입력받을 정수의 개수
    N = int(input())
    note_1 = list(map(int, input().split()))
    # 이진탐색을 위한 정렬
    note_1.sort()
    # M 수첩2에 입력받을 정수의 개수
    M = int(input())
    # 숫자 순서대로 있어야 하므로
    note_2 = list(map(int, input().split()))

    # num1을 오름차순으로 정렬하면 이진탐색으로 가능
    for num in note_2:
        # 이진탐색 함수
        print(binary_search(num, note_1))
````
* 이진탐색은 탐색하려는 배열이 순차적이야 가능
* note_1을 이진탐색을위해 정렬처리가 필수
* note_2의 인자를 target으로 하여 note_1 배열을 이진탐색
* 확률을 줄여나가며 target이 존재하는지 여부를 판단
* 일반적으로 target이 1개일 경우의 탐색은 매우 빠르지만, note_2를 순회하며 target을 찾아야하기 때문에

1. note_1의 정렬 -> 정렬 알고리즘의 시간 복잡도 O(NlogN)
2. note_2의 이진탐색 수행 -> O(M logN)
3. 각 테스트 케이스의 시간 복잡도 -> T
4. T * (M logN + N logN)