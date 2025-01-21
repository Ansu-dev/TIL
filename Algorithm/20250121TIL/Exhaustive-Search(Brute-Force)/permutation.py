# nums = [1, 2, 3, 4]로 만들수 있는 모든 순열

def solution(numbers):
    # 나올 수 있는 순열을 만들어야함

    # 백트래킹을 이용(재귀를 이용)
    def backtrack(current):
        # base case - 입력받은 배열의 길이가 같다면 current에 담긴 배열을 answer에 담는다.
        if len(current) == len(numbers):
            answer.append(current[:]) # 1차원 배열을 또다른 배열에 append
            return # 재귀에서 return 4가 되기전까지 반복 될듯

        # 백트래킹 재귀를 통해서 current배열에 순열을 쌓는다.
        for num in numbers: # 1 ~ 4 까지 루트 노드를 반복한다.
            if num not in current: # current안에 없는 숫자만 다시 반복
                # key point
                current.append(num) # 현재 상태
                backtrack(current) # 되돌아 가고
                current.pop() # 현재 상태를 빼줌

    answer = []
    backtrack([])
    return answer

print(solution([1, 2, 3, 4]))