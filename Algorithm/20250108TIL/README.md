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