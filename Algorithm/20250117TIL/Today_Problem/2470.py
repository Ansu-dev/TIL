import sys
input =  sys.stdin.readline

N = int(input())


# -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들수 있고
# 이 용액이 특성값이 0에 가장 가까운 용액이다.
# 알칼리성 욕액만 혹은 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우
# 주어진 배열에서 2가지 용액을 합쳐 0에 가장 가까운 2개의 수를 찾아야함
# 절대값이 가장 작은것을 찾으면 될듯..?
# 출력은 오름차순으로 출력


# 두 포인터를 사용하여 탐색
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