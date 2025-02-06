# 계단을 올라가고 있다. 한 번 올라갈 때 마다 1 step 또는 2 steps 올라갈 수 있다. 문제에서 정수형 배열
# cost가 주어지는데, cost[i]는 i번 째 계단을 밟았을 때 지불해야 하는 비용이다.

# 처음 시작은 index 0 또는 1중 한 곳에서 시작할 수 있다.

# 이 계단의 꼭대기에 도착하기 위해 지불해야하는 비용의 최소비용을 반환하라.

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

# 완전탐색으로 => 재귀
costs = [10,15,20,17,1]


def dfs(n):
    # O(2^n) -> 2가지 경우의수가 무수히 많을수 있기 때문에
    return min(dfs(n-1) + costs[n-1], dfs(n-2) + costs[n-2]) # 둘중 최소값을 구한다.

# 완전탐색의 문제점인 중복의 계산을 없애버린다.


memo = {}
# DP를 통함 => 재귀 or 루프
def dp(n):
    # top-down
    # top을 기준으로 top-1, top-2의 비용 2가지
    # 누적값 + 이전의 단계에서 최소비용
    # if n == 0 and n == 1: # O(N)
    #     return 0
    # if n not in memo: # memo에 아무것도 없을 경우엔
    #     memo[n] = min(dp(n-1) + costs[n-1], dp(n-2) + costs[n-2])

    # bottom-up
    # 시작점부터 비용을 기억하며 top까지
    memo[0] = 0 # 0층까지 가는 비용
    memo[1] = 0 # 1층까지 가는 비용
    for i in range(2, n+1): # O(N)
        memo[i] = min(memo[i-1]+costs[i-1], memo[i-2]+costs[i-2]) # 처음부터 순서대로 올라간다.

    return memo[n] # 메모리에 저장된 n번째 값을 반환

print(dp(5))