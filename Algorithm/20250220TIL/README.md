# 20250204 TIL
Today I Learned

* 알고리즘
* 시간복잡도


### 알고리즘
* 문제 해결 방법: 어떠한 문제를 해결하기 위해 정해진 일련의 절차나 방법
* 자주쓰이는 문제 해결 방법(알고리즘)은 패턴화
  * BFS,DFS,Binary Search, Dijkstra 등
* 한 문제를 해결할 수 있는 알고리즘은 다양하다.
  * 각 문제에 적합한 알고리즘을 선택할 수 있어야 한다.
  * 알고리즘을 평가할 수 있어야 한다.
````text
💡시간복잡도와 공간복잡도
두개는 보통 trade-off관계이다. 실행시간을 줄이기 위해서는 메모리를 더 사용해야 하고<br/
메모리 사용량을 줄이다보면 실행시간이 늘어나게 된다. 코딩테스트에서는 보통 실행시간을 줄이는게 중요<br/>
하기 때문이다. 또한, 시간복잡도를 미리 계산하여 문제 조건을 딱 맞추면서도 구현하기 쉬운 알고리즘을 선택할 수 있는<br/>
방법을 찾아야 한다.
````

### 시간복잡도
O(N!) > O(2^n) > O(N^2) > O(NlogN) > O(N) > O(logN) > O(1)

````text
Step1(문제 이해하기) -> Step2(접근 방법) -> Step3(코드 설계) -> Step4(코드 구현)
----
👉시간복잡도 활용법 in 코테
1. 시간복잡도 이해하고 외우기
2. 제한 조건 보는 법
3. 다양한 접근
````

✅시간복잡도(Big-O)에 데이터의 크기(n)를 넣어서 나온 값이 100,000,000(10^8)이 넘으면 시간 제한 초과할 가능성이 있다.
* 제약조건 : 1 <= n <= 10^5 => O(N^2)으로 풀 수 없다.
* 제약조건 : 1 <= n <= 10^3 => O(N^2)으로 풀 수 있다.
* 제약조건 : 1 <= n <= 10^4 => O(N^2)으로 풀기 애매하다.
* 제약조건 : 1 <= n <= 7 => 어떠한 시간복잡도로 풀수 있다.

#### O(n)
````python
# case1
for i in range(n):
    print("proc") # O(1)

# case2
def find_max(arr):
    max_value = arr(0)
    n = len(arr)
    for i in range(n):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value
````

#### O(1)
````python
# case1
a = 7
b = 34
print("hello")

# case2
input(n)
for i in range(100): # O(1) => 더이상 n이 커지지 않기 때문에
    print(n)
````

#### O(n^2)
````python
# case1(O(n)
n = 10
for i in range(n): # O(n)
    print("hello")
for j in range(n): # O(n)
  print("bye")

# case2(O(n^2))
n = 10
for i in range(n): # O(n)
    for j in range(n): # O(n)
        print("hello")
````

#### O(nm)
````python
# case1 => 길이가 다른 두 배열 O(nm)
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7,8,10]
common = []
for i in range(len(list1)): # O(n)
    for j in range(len(list2)): # O(m)
        if list1[i] == list2[j]:
            common.append(list1[i])
````