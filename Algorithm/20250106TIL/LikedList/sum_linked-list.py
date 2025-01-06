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
    # 링크드 리스트이 각 숫자를 1개의 숫자로 합치는 과정
    def sum(self):
        cur = self.head
        str_num = str(cur.data)
        while cur.next is not None:
            cur = cur.next
            str_num += str(cur.data)
        return str_num


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    return int(linked_list_1.sum()) + int(linked_list_2.sum())



    # 딩코딩코 해결방법
    # def get_single_linked_list_sum(linked_list):
    #     sum = 0
    #     cur = linked_list.head
    #     while cur is not None:
    #         sum = sum * 10 + cur.data
    #         cur = cur.next
    #
    #     return sum
    #
    # def get_linked_list_sum(linked_list_1, linked_list_2):
    #     sum_1 = get_single_linked_list_sum(linked_list_1)
    #     sum_2 = get_single_linked_list_sum(linked_list_2)
    #
    #     return sum_1 + sum_2





linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))