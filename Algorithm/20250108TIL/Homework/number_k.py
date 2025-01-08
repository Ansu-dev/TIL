# 링크드 리스트
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

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

    # def get_kth_node_from_last(self, k):
    #     slow = self.head
    #     fast = self.head
    #
    #     # k만큼 fast를 먼저 탐색
    #     for i in range(k):
    #         fast = fast.next
    #
    #     # slow, fast가 만나는 지점이 k번째 node
    #     while fast is not None:
    #         slow = slow.next
    #         fast = fast.next
    #
    #     return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!