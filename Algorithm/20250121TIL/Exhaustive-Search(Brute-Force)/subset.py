# numbs=[1, 2, 3, 4]로 만들 수 있는 부분집합을 모두 반환하시오.

def solution(numbers):
    answer = []
    # 원소의 중복은 안됨 [1, 2, 3, 4] = [1, 3, 2, 4]
    # 원소가 0일 때 조합,
    # 원소 1개만 있을 때 조합
    # 원소 2개만 있을 때 조합
    # 원소 3개가 있을 때 조합
    # 원소 4개가 있을 때 조합
    def backtracking(start, current):
        if len(current) == k:
            answer.append(current[:])
            return

        # 시작 인덱스부터 끝 인덱스 까지
        for i in range(start, len(numbers)):
            current.append(numbers[i])
            backtracking(i + 1, current)  # 다음 백트래킹일 될 때 현재 인덱스 다음부터 실행
            current.pop()

    # 0개 부터 4개까지의 조합
    for k in range(len(numbers) + 1):
        backtracking(0, current=[])

    return answer

print(solution([1, 2, 3, 4]))