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
2. 순차적인 데이터 저장(order)
````
배열은 선언시에 size를 정하여 해당 size만큼의 연속된 메모리를 할당 받아 data를 연속적/순차적으로 저장

#### 동적배열(List)
````text
💡선언 이후에 size를 변경할 수 없는 정적배열(Static Array)과 다르게 동적배열(Dynamic Array)는 size를 늘릴 수 있다.
````
동적 배열은 배열의 크기를 변경할 수 있는 배열, fixed-size인 정적배열의 한계점을 보안
기존에 할당된 size를 초과하게 되면, size를 늘린 배열을 새로 선언하고 그곳으로 모든 데이터를 옮긴다.
