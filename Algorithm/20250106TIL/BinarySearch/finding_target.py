# Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다. 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.

# N이라는 미지수를 수식화 해야함 -> 시간 복잡도
# 1 ~ N
# 1 ~ N/2
# 1 ~ N/4
# 1 ~ N/8
# k번 탐색 -> 1 ~ N/2^K

# k번 탐색하면 -> N/2^K개가 남는다.

# N/2^K -> 1이 되려면
# N = 2^K -> log2(N) = K

# K번 탐색을 하면 우리가 원하는 딱 1개의 원소를 찾을 수 있다.
# O(log(N))-> 점점 줄어드는 경우는 log(N)이다.

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def solution(target, array):
    find_count = 0
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2
    # 최소인덱스가 최대 인덱스보다 작을 때까지 반복
    while cur_min <= cur_max:
        find_count += 1
        if array[cur_guess] == target:
            print(find_count)
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else: # target < guess
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2
    print(find_count)
    return False


result = solution(finding_target, finding_numbers)
print(result)