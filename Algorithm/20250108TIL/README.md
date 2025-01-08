# 20250108 TIL
Today I Learned

* 링크드 리스트
* 이진탐색
* 재귀 함수


### Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
[6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때, 
                  # 끝에서 2번째 값은 7을 반환해야 합니다!
````python
    def get_kth_node_from_last(self, k):
        # 구현해보세요!

        # 전체 링크드 리스트이 길이가 몇인지 알아야함


        # 끝에서부터 k번째
        length = 1 # 시작노드의 길이
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            length += 1
        print("length is ", length)

        # 끝에서 몇번째 인지 반환
        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next
        return cur
````
* 모든 링크드 리스트이 길이를 구한다.
* 링크드 리스트의 길이에서 k만큼 빼고, 그만큼 이동시킨다.
* 뺀 길이 만큼 반복하며 노드를 반환한다.



### Q. 배달의 민족 배달 가능 여부
배달의 민족 서버 개발자로 입사했다.
상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.

그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.

````python
menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "만두"]
````

````python
def is_available_to_order(menus, orders):
    # 메뉴 오름차순 정렬
    #
    # # O(NlogN) + O(M) * O(logN) = O((N+M)*log(N))
    # shop_menus.sort() # 메뉴의 길이가 N -> O(NlogN)
    # for order in orders: # 주문의 길이가 M 이라고 한다면 O(M)
    #     # 주문이 menu에 포함이 되어있는지 판별
    #     if not is_exist_target_number_binary(order, menus): # O(logN) -> 이진탐색 굉장히 비효율
    #         return False
    #
    # return True


    # 집합 자료형 사용
    # O(N) + O(M) * O(1) = O(N + M)
    menus_set = set(menus) # O(N)
    for order in orders: # O(M)
        if order in menus_set: # O(1)
            return False
    return True
````
* 해당 문제는 이진탐색이 훨씬 비효율적
* 집합 자료형 (중복을 제거하는)사용하면 훨씬 시간복잡도가 효율적


### Q. 더하거나 빼거나
````text
음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
````

````python
numbers = [1, 1, 1, 1, 1]
target_number = 3
````


````python
def solution(numbers, target):
    all_ways = []

    answer = 0

    def recursive(array, cur_index, cur_sum):
        if cur_index == len(array):
            all_ways.append(cur_sum)
            return
        print(cur_index, cur_sum)
        # 바로뒤의 인덱스 인자에 따라 경우의수가 2가지이다. +인지 -인지
        recursive(array, cur_index + 1, cur_sum + array[cur_index])
        recursive(array, cur_index + 1, cur_sum - array[cur_index])

    recursive(numbers, 0, 0)

    for way in all_ways:
        if target == way:
            answer += 1

    return answer
````

````text
          (0, 0)        # 시작점: 인덱스 0, 합 0
         /     \
   (1, +1)   (1, -1)     # 첫 번째 숫자 1을 더하거나 뺌
    /    \     /    \
(2, +3)(2, -1)(2, +1)(2, -3)  # 두 번째 숫자 2를 더하거나 뺌
````
* (0, 0)에서 시작하여 첫 번째 숫자 1을 더하거나 빼는 두 갈래로 분기합니다.
* 각 분기에서 두 번째 숫자 2를 더하거나 빼는 두 갈래로 다시 분기합니다.
* 최종적으로 합이 1인 경우는 두 가지입니다: (2, +1)과 (2, +1).

### 재귀함수를 사용한 해결 방법의 흐름
1. 시작점: 인덱스 0, 현재 합 0.
2. 각 숫자마다 두 가지 선택:
   * 더하기: 현재 합에 숫자를 더함.
   * 빼기: 현재 합에서 숫자를 뺌.
3. 모든 숫자를 처리한 후:
   현재 합이 target과 일치하면 카운트를 증가시킴.