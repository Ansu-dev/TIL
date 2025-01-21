# numbs=[1, 2, 3, 4]에서 두 개의 원소를 선택해 만들 수 있는 모든 조합을 반환

def solution(numbers, k):
    answer = []
    def backtracking(start, current):
        if len(current) == k:
            answer.append(current[:])
            return

        # 시작 인덱스부터 끝 인덱스 까지
        for i in range(start, len(numbers)):
            current.append(numbers[i])
            backtracking(i + 1, current) # 다음 백트래킹일 될 때 현재 인덱스 다음부터 실행
            current.pop()

    backtracking(0, current = [])
    return answer


print(solution([1, 2, 3, 4], 2))