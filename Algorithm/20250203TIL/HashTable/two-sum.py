# 정수가 저장된 배열 nums이 주저졌을 때, nums의 원소중 두 숫자를 더해서
# target이 될 수 있으면 True 불가능하면 False를 반환하세요. 같은 원소를 두 번 사용할 수 없습니다.

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9


# 메모리를 사용하여 시간복잡도를 낮춤

# 시간복잡도 - O(N)
def solution(nums, target):
    # 2개의 숫자로 target이 되는지 검증하므로 target보다 큰 숫자는 딕셔너리에 넣지않음
    dict = {}
    for num in nums: # O(N)
        dict[num] = True # O(1)


    for num in nums: # O(N)
        needed_number = target - num # 어떤수에 타깃을 뺀 숫자
        # O(1)
        if needed_number in dict and needed_number != num: # 필요한 숫자가 딕셔너리에 있는지 판별, 필요한 수가 자기이 아니어야함
            return True # 있다면 해당 리스트에선 target이 되는 숫자 쌍이 있음

    return False # 반복문을 모두 돌아도 True가 나지 않았다면 target을 만들지 못함


print(solution([4,1,9,7,5,3,16], 14)) # True
print(solution([2,1,5,7], 4)) # False