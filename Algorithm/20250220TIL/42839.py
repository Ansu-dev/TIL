import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    array = list(numbers)  # 각 숫자 조각을 리스트로 변환
    combination = set()    # 중복 제거를 위해 set 사용

    def backtracking(current, remaining):
        if current != "":
            combination.add(int(current))
            print(combination)
        if not remaining:
            return
        for i in range(len(remaining)):
            # remaining[i]를 사용하여 현재 재귀 단계에서 남아있는 숫자를 선택합니다.
            next_current = current + remaining[i]
            next_remaining = remaining[:i] + remaining[i+1:]
            backtracking(next_current, next_remaining)

    backtracking("", array)

    for num in combination:
        if is_prime(num):
            answer += 1

    return answer

# print(solution("17"))   # 3
print(solution("011"))  # 2