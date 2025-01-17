import sys
input =  sys.stdin.readline

N, S = map(int, input().split())

def main():
    sequences = list(map(int, input().split()))

    left, right = 0, 0 # 투 포인터를 배열의 시작점에 위치
    current_sum = 0 # 현재 윈도우의 합을 저장
    min_length = N + 1 # 가능한 최소 길이를 저장하는 변수로, 초기값은 배열의 최대 길이보다 큰 값으로 설정 -> 아직 최소값이 결정 되지 않았따.

    # 무한 루프
    while True:
        # current_sum이 S이상인 경우
        if current_sum >= S:
            # 현재 저장된 길이와 S가 넘은 부분합의 길이중 더 짧은것을 저장
            min_length = min(min_length, right - left) # current_sum은 left -1인자를 합한것
            # 현재의 합에 시작점의 인자를 빼주고
            current_sum -= sequences[left]
            # left를 한칸 이동한다. -> 가장 짧은 길이를 얻기 위함
            left += 1
        elif right == N: # right가 끝지점에 도달했을 경우 무한 루프를 멈춤
            break
        else:
            # 윈도우를 확장하기 위해 right 포인터 이동
            current_sum += sequences[right]
            right += 1 # 미리 right를 앞칸으로 옮겨놓고 다음을 비교함, current_sum은 이전right의 인자를 합친것

    if min_length == N + 1: # 최소 길이가 초깃값 그대로 일 경우
        return 0

    return min_length

print(main())

# 왜 정렬을 하면 안되는지
# 슬라이딩 윈도우의 특성 - 연속된 부분 수열의 합을 다루므로, 수열의 원래 순서가 중요
# 연속된 -> 조건을 위반하기 때문에 정렬을 하면 안됨
#