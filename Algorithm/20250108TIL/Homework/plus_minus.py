# 재귀함수
# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2
from array import array

numbers = [1, 1, 1, 1, 1]
target_number = 3


# [2, 3, 1]
# 0

# 모든 경우의 수를 다 써봐야함
# 1. +2 + 3 + 1 = 6
# 2. +2 + 3 - 1 = 4
# 3. +2 - 3 + 1 = 0 # 타겟!
# 4. +2 - 3 - 1 = -2
# 5. -2 + 3 + 1 = 2
# 6. -2 + 3 - 1 = 0 # 타겟!
# 7. -2 - 3 + 1 = -4
# 8. -2 - 3 - 1 = -6

# N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N - 1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면 된다는 소리

# [2,3]을 배치하는 경우의 수에서
# 맨 마지막 원소인 1을 더하냐 빼냐에 따라서 [2,3,1]의 경우의 수를 구할 수 있다.

def solution(numbers, target):
    all_ways = []

    answer = 0

    def recursive(array, cur_index, cur_sum):
        if cur_index == len(array):
            all_ways.append(cur_sum)
            return
        print(cur_index, cur_sum)
        # 바로뒤의 인덱스 인자에 따라 경우의수가 2가지이다. +인지 -인지
        recursive(array, cur_index + 1, cur_sum + array[cur_index])
        recursive(array, cur_index + 1, cur_sum - array[cur_index])

    recursive(numbers, 0, 0)

    for way in all_ways:
        if target == way:
            answer += 1

    return answer





print(solution(numbers, target_number))  # 5를 반환해야 합니다!