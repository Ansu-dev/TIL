# Q. 리스트[4, 9, 7, 5, 1]에서 두 개의 숫자를 더해서 12이 될 수 있나요?(중복x)

def solution(numbers, target):
    def backtracking(start, current):
        # 2개의 숫자를 이용하므로 len(current)가 2개가 됐을 때 숫자를 누적합을 해봄
        if len(current) == 2 and sum(numbers[i] for i in current) == target:
            return current

        for i in range(start, len(numbers)):
            current.append(i)
            ret = backtracking(i + 1,  current)
            if ret:
                return ret
            current.pop()
        return None

    return backtracking(0, [])

print(solution([4, 9, 7, 5, 1], 12))
