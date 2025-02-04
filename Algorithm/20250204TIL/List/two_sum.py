# 정수가 저장된 배열 nums가 주어졌을 때, nums의 원소중 두 숫자를 더해서 target이 될 수 있으면
# True 불가능하면 False를 반환하세요. 같은 원소를 두 번 사용할 수 없습니다.

# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9

# 완전탐색으로 시작
# 문제 상황을 단순화,극한화 하여 생각
# 어떤 자료구조를 사용하는게 가장 적합한지 결정
# 대놓고 특정 자료구조와 알고리즘을 묻는 문제도 많음
# 시간복잡도를 줄이기 위해 메모리를 사용하는 방법 -> 해시테이블

def solution(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    return False

print(solution([4,1,9,7,5,3,16], 14)) # True
print(solution([2,1,5,7], 4)) # False