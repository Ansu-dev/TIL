import sys
input =  sys.stdin.readline

n = int(input()) # 수열의 크기
sequences = list(map(int, input().split()))
x = int(input()) #

def main():
    sequences.sort() # O(N log N)
    count = 0 # x를 만족하는 쌍의 개수
    left, right = 0, n - 1 # left: 가장 작은 index, right: 가장 큰 index

    # 자연수x가 주어졌을 때 ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성
    while left < right:
        # left, right를 두고 작은 수와 큰수를 더해가며 x와 비교
        sequence_sum = sequences[left] + sequences[right]

        if sequence_sum == x:
            count += 1
            # 일치하는 쌍을 찾았을 땐 한칸씩 좁혀가며 다시 비교
            left += 1
            right -= 1
        elif sequence_sum < x: # x보다 작으면 left를 한칸 늘림
            left += 1
        else: # x보다 크면 right를 한칸 줄이고
            right -= 1

    # 해당 조건을 만족하는 쌍의 개수를 출력
    print(count)

main()