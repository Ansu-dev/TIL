# 20250114 TIL
Today I Learned


* 항해99 1일 1코테 스터디


### ❗️ 백준 1654 - 랜선 자르기

#### 이분 탐색을 활용해 최대 길이 구하기
````python
import sys
input =  sys.stdin.readline

N, K = map(int, input().split())


def binary_search(lines, target):
    min_len = 1
    max_len = max(lines)
    length = 0

    # 최소 길이가 최대길이보다 작을때 까지만 반복한다.
    while min_len <= max_len:
        # 각 랜선중 중간길이에서 몇개를 만들수 있는지 확인
        mid_len = (min_len + max_len) // 2
        #  중간 랜선 길이로 각 랜선을 나누어 몇개를 만들수 있는지 확인
        total = sum(line // mid_len for line in lines)
        print('total : ', total)
        # 목표로하는 개수의 이상이므로 더 작은 길이로 시도
        if total >= target: # 최대의 개수를 구하는거니 target보다 이상이어도 상과없음
            length = mid_len
            min_len = mid_len + 1
        else: # 더 작은 길이로 시도
            max_len = mid_len - 1

        print('length : ', length)
        print('mid : ', mid_len)

    return length

def main():
    lines = []
    for _ in range(N):
        line = int(input())
        lines.append(line)

    # 이분탐색으로 target의 숫자를 찾아낸다.
    result = binary_search(lines, K)
    print(result)

main()
````


1. 각 랜선에서 가장큰 랜선의 길이를 최대 길이로 설정
2. 최소 길이가 최대 길이보다 작거나 같을 경우에만 계속해서 반복
3. 각 랜선을 중간 길이에 나눴을 때의 몫들이 target으로 하는 K보다 같거나 커질 때 해당 랜선 길이가 랜선의 개수 최대를 만들수 있다 가정
4. 만약 target으로 하는 길이보다 랜선의 길이가 못미칠 경우는 중간 길이 - 1을 최대 길이로 갱신하며 최대 길이를 찾음
5. 이진 탐색은 O(log M) 시간 복잡도로 문제를 해결


````text
💡 왜 이분 탐색을 사용할 까?
 - 탐색의 범위가 크다, 선형 탐색(모든 가능한 길이를 하나씩 시도하는 방법)은 비효율적
 - 조건을 만족하는 판별 필요 -> 문제는 "조건을 만족하는 최대값"을 찾는 문제로, 이진 탐색과 잘 맞음
 - 특정 길이를 기준(target)으로 조건을 만족하는지 판단할 수 있어, 이진 탐색을 적용하기 용이합니다.
````