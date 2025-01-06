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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        # 새로운 노드
        new_node = Node(value)
        # index번째에 새로운 노드를 넣어야함
        # index - 1 번째의 노드가 필요하다.

        # 만약 index가 음수가 된다면?
        if index == 0: # 따로 예외처리
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index-1)
        # next_node를 저장해놓는다
        next_node = prev_node.next

        prev_node.next = new_node
        # 새로운 Node를 연결후 이전의노드를 다시 연결해줌
        # 새로생긴 노드와 기존 자리에 있던 노드를 연결해줘야함
        next_node.next = next_node



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()