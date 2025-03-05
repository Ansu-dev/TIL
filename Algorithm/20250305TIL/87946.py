# 던전의 행은 1이상 8이하
# 던저의 열은 2


# k: 현재 피로도
# dungeons [최소 필요도, 소모 피로도]
def solution(k, dungeons):
    answer = 0
    # 최대 8개의 던저이 올수 있으므로 8! -> 8개의 던전을 모두 시작점으로 보고 남은 던전으로 조합을 생성해 모드 탐색
    # dungeons의 길이만큼 순열하는 index 배열을 생성
    index_arr = [i for i, _ in enumerate(dungeons)]
    # 해당 배열로 순열
    def backtracking(current):
        nonlocal answer
        if len(current) == len(dungeons):
            # 현재 current를 가지고 던전을 바로 순회하여 경우의 수의 탐험 수를 얻을수 있음
            # 브루트포스 코드를 넣는다. -> 메모리 절약
            # 조합한 순열을 돌면서 제일 많이 갈수 있는 경우를 answer에 담는다.
            current_k = k  # 경우의 수가 시작할 때마다 현재 피로도 초기화
            visited_count = 0
            for i in current:  # n^2
                min_k = dungeons[i][0]
                use_k = dungeons[i][1]
                if current_k >= min_k:
                    current_k -= use_k
                    visited_count += 1

            answer = max(visited_count, answer)  # 이중 더 큰것을 저장
            return
        for i in index_arr:
            if i not in current: # 중복 순열 방지
                current.append(i)
                backtracking(current)
                current.pop()# 한 차례 백트래킹이 끝났다면 마지막 인자를 pop해서 다른 조합도 가능하도록 만든다.

    backtracking(current=[])

    return answer


print(solution(80, [[80,20],[50,40],[30,10]])) # 3