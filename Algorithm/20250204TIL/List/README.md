# 20250204 TIL
Today I Learned


* 리스트
* 배열


### 리스트
* Array List -> list라는 함수로 구현이 되어있음
  * Array
  * Dynamic Array

* Linked List
  * Node


#### 배열
````text
💡배열의 특성
1. 고정된 저장 공간(fixed-size)
2. 순차 적인 데이터 저장(order)
````
배열은 선언시에 size를 정하여 해당 size만큼의 연속된 메모리를 할당 받아 data를 연속적/순차적으로 저장

----

#### 동적 배열(List)
````text
💡선언 이후에 size를 변경할 수 없는 정적배열(Static Array)과 다르게 동적배열(Dynamic Array)는 size를 늘릴 수 있다.
````
동적 배열은 배열의 크기를 변경할 수 있는 배열, fixed-size인 정적 배열의 한계점을 보안
기존에 할당된 size를 초과 하게 되면, size를 늘린 배열을 새로 선언 하고 그곳 으로 모든 데이터를 옮긴다.


----

#### 연결 리스트(Linked List)
````text
💡Linked List
Linked List는 Node라는 구조체가 연결되는 형식으로 데이터를 저장하는 자료구조<br/>
Node는 데이터 값과 next node의 주소값을 저장한다. Liked List는 메모리상에서는 비연속적으로 저장이 되어있지만,<br/>
각각의 node가 next node의 메모리 주소값을 가리킴으로써 논리적인 연속성을 갖게 된다.
````
````python
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
    def append(self, value):
      new_node = Node(value)
      if self.next is None:
        self.head = new_node
      # 맨 뒤에 node가 new_node를 가리켜야 한다.
      else:
        pass
        
# 노드의 값 지정
first = Node(1)
second = Node(2)
third = Node(3)

# 노드의 연결
first.next = second
second.next = third
first.value = 6
````
````python
class LinkedList:
    def __init__(self, value = 0, next = None):
        self.head = None
        self.tail = None
    def append(self, value): # O(N)
      new_node = Node(value)
      
      # 시간복잡도 O(1)
      if self.head is None:
        self.head = new_node
      else: # 맨 뒤의 node가 new_node를 가리켜야 한다.
        self.tail.next = new_node
        self.tail = self.tail.next
      
      # 시간복잡도 O(N)
      # if self.head is None:
      #   self.head = new_node
      # # 맨 뒤에 node가 new_node를 가리켜야 한다.
      # else:
      #   current = self.head
      #   while current.next: # 현재 노드이 next가 None인지 판별
      #     current = current.next
      #   current.next = new_node
        
    def get(self, idx): # O(N)
      current = self.head
      for _ in range(idx):
        current = current.next
      return current.value
    

    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next    
            current.next = new_node
    
    def insert(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head # 헤드를 new_node뒤로 옮긴후
            self.head = new_node # new_ndoe를 헤드로 지정
        else:
            current = self.head
            for _ in range(idx-1): # 목표 index앞까지만 반복문
                current = current.next # 현재 노드는 목표 index앞 노드
            new_node.next = current.next # 새로운 노드 뒤로 현재 노드의 next를 연결
            current.next = new_node   # 현재 노드 뒤로 새로운 노드를 연결
      
    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next # garbage collector가 알아서 처리해준다.
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next
            current.next = current.next.next

    def print(self):
        current = self.head
        while(current):
            print(current.value, end="")
            current = current.next    
            if current:
                print("->", end="")
        print()
````
