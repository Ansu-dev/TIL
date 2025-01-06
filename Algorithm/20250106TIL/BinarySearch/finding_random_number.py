finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def solution(target, array):
    # 먼저 배열 정렬 -> 이진탐색은 순차적으로 증가하는 배열해야한다.(무작위 배열은 이진탐색 불가)
    sort_array = sorted(array)
    print(sort_array)
    cur_min = 0
    cur_max = len(sort_array) - 1
    cur_guess = (cur_min + cur_max) // 2
    while cur_min <= cur_max:
        if sort_array[cur_guess] == target:
            return True
        elif sort_array[cur_guess] < target:
            # cur_guess는 탐색을 했으니 1개 큰인덱스부터 검사
            cur_min = cur_guess + 1
        else: # cur_guess는 탐색을 했으니 1개 작은인덱스 부터 검사
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2
    return False


result = solution(finding_target, finding_numbers)
print(result)