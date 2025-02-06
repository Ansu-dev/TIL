# 계단을 올라가고 있다. 이 계단의 꼭대기에 도착하려면 n개의 steps만큼 올라가야 한다. 한 번 올라갈 때
# 마다 1 step 또는 2 steps 올라갈 수 있다. 꼭대기에 도달하는 방법의 개수는 총 몇 가지 일까요?

# 1 <= n  45

# 접근 방법 => 완전탐색
# 1. 크고 복잡한 문제를 하위 문제로 나눈다.
# 2. 하위 문제에 대한 답을 계산한다.
# 3. 하위 문제에 대한 답으로 원래 문제에 대한 답을 계산한다.

# 메모이제이션
memo = {}

# 1걸음 또는 2걸음 걸음수 있음 총 경우의 수는 몇 가지?
# n으로 도달하려면
# n - 1, n - 2 에서 와야한다.
# n - 1, n - 2에 도달할 수 있는 모든 경우의를 합친것
def cs(n):
    ## top-down 방식
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs(n-1)+cs(n-2) # 재귀

    ## bottom-up 방식
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2] # 점화식

    return memo[n]


print(cs(2)) # 2 -> 1step + 1step, 2 steps
print(cs(3)) # 3 -> 1 step + 1step + 1step, 1step + 2steps, 2steps + 1step