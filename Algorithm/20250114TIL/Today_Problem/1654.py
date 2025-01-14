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

    lines.sort() # 이분 탐색을 위한 오름차순 정렬

    # 이분탐색으로 target의 숫자를 찾아낸다.
    result = binary_search(lines, K)
    print(result)

main()
