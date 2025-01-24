# 20250124 TIL
Today I Learned


* Heap & Priority Queue

## 우선순위 큐
가장 높은 우선순위를 가진 데이터가 큐에서 먼저 추출되는 자료 구조

1. 리스트
   * enqueue() -> O(1) append만 이용
   * dequeue() -> O(N) 최소, 최대값을 찾아야 하므로
2. 정렬
   * enqueue() -> O(NlogN) 
   * dequeue() -> O(1)
3. 완전 이진 트리(가장 시간복잡도가 이상적) - Heap 자료구조 사용
   * enqueue() -> O(logN) 트리의 계층을 스왑해줘야하므로
   * dequeue() -> O(logN) 루트노드의 노드를 빼주고 다시 루트 노드를 우선순위에 맞게 스왑해줘야하므로

### Heap
완전 이진 트리형태의 자료구조

* min heap: 부모 노드의 값이 자식 노드의 값보다 작은 트리 형태의 자료구조
* max heap: 부모 노드의 값이 자식 노드의 값보다 큰 트리 형태의 자료구조

형제 노드 간에는 대소 관계가 정해지지 않는다.
Root 노드가 가장 큰(or 작은)값을 갖는다.

* 부모 노드: (i - 1) / 2
* 자식 노드: 2 * i + 1


#### min heap
````python
import heap

min_heap = [5, 3, 9, 4, 1, 2, 6]
heap.heapify(min_heap) # [1, 3, 2, 4, 5, 9, 6] 완전 이진 트리 형태로 만듬 O(N)

# dequeue
heap.heappop(min_heap) # [2, 3, 6, 4, 5, 9] O(logN)

# enqueue
heap.heappush(min_heap, 1) # [2, 3, 6, 4, 5, 9, 1] -> [1, 3, 2, 4, 5, 9, 6] O(logN)
````


#### max heap
````python
import heap

max_heap = [5, 3, 9, 4, 1, 2, 6]
heap._heapify_max(max_heap) # [9, 4, 6, 3, 1, 2, 5]  O(N)

# max_heap으로 pop을 하는 방법
max_heap = [i * -1 for i in max_heap] # max_heap에 -1을 곱해줌 => min_heap의 원리를 이용
heap.heapify(max_heap)  # [-9, -4, -6, -3, -1, -2, -5]
weight = heap.heappop(max_heap)
value = -1 * weight # 나온값에서 다시 -1을 곱해줌

# 튜플을 이용해 pop을 하는 방법
max_heap = [(-1 * i, i) for i in max_heap]
heap.heapify(max_heap)
weight, value = heap.heappop(max_heap)
````
