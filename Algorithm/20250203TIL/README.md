# 20250203 TIL
Today I Learned

* 해시 테이블
* 딕셔너리

### 해시테이블
효율적인 탐색(빠른 탐색)을 위한 자료구조로써 key-value쌍의 데이터를 입력받는다.<br/>
hash function h에 key값을 입력으로 넣어 얻은 해시값 h(k)를 위치로 지정하여 key-value 데이터 쌍을 저장한다.<br/>
저장, 삭제, 검색의 시간복잡도는 모두 O(1)이다.

#### 딕셔너리(Dictionary)
````python
score = {
    'math': 97,
    'eng': 97,
    'kor': 89
} # 딕셔너리 선언
score['math'] = 45 # 덮어씀
print(score['math']) # 45
score['sci'] = 100
print(score['sci']) # 100

print('music' in score) # False | key가 존재하지 않음
if 'music' in score: # 딕셔너리에서 key 탐색 O(1)
    print(score['music'])
else:
    score['music'] = 0
````
