# 20250117 TIL
Today I Learned


* 항해99 1일 1코테 스터디


### ❗️ 백준 2470 - 두 용액

#### 두 포인터를 이용해 절대값 최소를 찾기
````python
import sys
input =  sys.stdin.readline

N = int(input())

def main():
    solutions = list(map(int, input().split()))
    # 용액의 특성값을 오름차순 정렬
    solutions.sort()

    # 두 포인터 초기화
    left, right = 0, N - 1 # 배열의 가장 작은 인덱스, 배열의 끝 인덱스

    min_abs_sum = float('inf')
    result = (solutions[left], solutions[right])

    # 두 포인터 이동
    # 이 과정을 left가 right보다 작을 때 까지 반복
    while left < right:
        # left와 right가 가리키는 두 용액의 합을 계산
        current_sum = solutions[left] + solutions[right]
        abs_sum = abs(current_sum)

        # 절대값이 지금까지 찾은 최소 절대값보다 작으면, 해당 최소 값을 저장
        if abs_sum < min_abs_sum:
            min_abs_sum = abs_sum
            # 절대값 최소를 찾았으니 해당 인덱스의 인자를 오름차순으로 저장
            result = (solutions[left], solutions[right])

        # 합이 정확히 0이라면, 가장 최적의 해이므로 즉시 종료
        if current_sum == 0:
            break
        elif current_sum < 0:
            # 합이 0보다 작다면, 합을 더 크게 만들기 위해 left 포인터를 오른쪽으로 한칸 이동
            left += 1
        else:
            # 합이 0보다 크다면, 합을 더 작게 만들기 위해 right 포인터를 왼쪽으로 한 칸 이동
            right -= 1

    print(result[0], result[1])

main()
````
1. 현재 left와 right가 가리키는 두 용액의 합 current_sum을 계산
2. current_sum의 절대값이 현재까지 최소 절대값 min_abs_sum보다 작으면, 이 두 용액을 결과로 저장
3. current_sum이 0보다 작으면, 합을 더 크게 만들기 위해 left를 오른쪽으로 이동
4. current_sum이 0보다 크면, 합을 더 작게 만들기 위해 right를 왼쪽으로 이동
5. current_sum이 정확이 0이면 최적의 해
6. 위 가정을 left가 right보다 작을 때까지 반복
7. 시간복잡도: O(N)


````text
💡 왜 두 포인터 일 까?
 - 포인터의 이동으로 최적의 값을 찾기 위해서
 - 합이 특정 값에 가까운 두수 찾기
 - 특정 합을 가지는 두 수 찾기
 - 부분 배열의 합 계산
 - 문자열에서 특정 조건을 만족하는 부분 문자열 찾기
 - 배열에서 중복 제거 또는 특정 조건을 만족하도록 배열 수정
````

* 선형 배열에서 두가지 인자를 비교하여 어떠한 결과를 도출할 경우 사용하는 것 같음
