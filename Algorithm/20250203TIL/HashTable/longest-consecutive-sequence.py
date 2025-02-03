# 정렬되어 있지 않은 정수형 배열 nums가 주어졋다.
# nums 원소를 가지고 만들수 있는 가장 긴 연속된 수의 개수는 몇개인지 반환하시오.

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# 5번 정도 풀어봐야함
# hash set을 사용해도 됨
def solution(nums):
    dict = {}
    result = 0
    for num in nums: # O(N)
        dict[num] = True # 중복된 값을 걸러냄

    for num in dict: # O(1)
        # while문이 n번 반복되지 않도록 조건문 처리
        if num - 1 not in dict: # 현재 수보다 작은 연속된 수가 존재하지 않을 경우, 해당수가 연속된 수의 시작점임, O(1)
            count = 1 # 해당 시작점은 연속된수의 가장 처음 +1
            target = num + 1 # 다음수가 있는지 찾음
            while target in dict: # 딕셔너리에 연속된 수가 존재할 때까지 반복문, O(N) -> 독립적
                target += 1
                count += 1
            result = max(result, count) # 현재까지 연속된수가 최종 값과 어떤것이 큰지 판별하여 할당
    return result

print(solution([100,4,200,1,3,2])) # 4 -> [1,2,3,4]
print(solution([0,3,7,2,5,8,4,6,0,1])) # 9 -> [0,1,2,3,4,5,6,7,8]