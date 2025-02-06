# 이 로봇은 m x n grid(격자)위에 있습니다. 로봇은 처음에 좌측 상단 모서리 (grid[0][0])에 위치해 있습니다.
# 로봇은 우측 하단 모서리 (grid[m-1][n-1])로 이동하려고 합니다. 로봇은 오른쪽이나 아래쪽으로만 움직일 수 있습니다.

# 두 정수 m과 n이 주어졌을 때, 로봇이 우측 하단 모서리에 도달할 수 있는 가능한 unique paths의 수를 반환하세요.

# 테스트 케이스는 답이 2 * 10^9이하가 되도록 생성합니다. -> 테스트케이스의 값이 완전탐색으로는 풀수 없다.

# 1 <= m,n <= 100

def unique_paths_top_down(m, n):
    memo = [[-1] * n for _ in range(m)]
    # O(MxN) => 10^4
    def dp(r, c):
        if r == 0 and c == 0:
            memo[r][c] = 1
            return memo[r][c]

        unique_path = 0
        if (r,c) not in memo:
            if r-1 >= 0:
                unique_path += dp(r-1, c)
            if c-1 >= 0:
                unique_path += dp(r, c-1)
            memo[r][c] = unique_path
        return memo[r][c] # 기억해놓은 unique_path를 꺼내옴
    return dp(m-1, n-1)

print(unique_paths_top_down(3, 7))


def unique_paths_bottom_up(m, n):
    memo = [[-1] * n for _ in range(m)]

    # 테이블 초기화
    # 바텀업은 초기화가 중요
    for r in range(m):
        memo[r][0] = 1
    for c in range(n):
        memo[0][c] = 1

    for r in range(1, m): # O(MxN)
        for c in range(1, n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]
    return memo[m-1][n-1]

print(unique_paths_bottom_up(3,7))