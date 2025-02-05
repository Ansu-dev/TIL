# 계단을 올라가고 있다. 이 계단의 꼭대기에 도착하려면 n개의 steps만큼 올라가야 한다. 한 번 올라갈 때
# 마다 1 step 또는 2 steps 올라갈 수 있다. 꼭대기에 도달하는 방법의 개수는 총 몇 가지 일까요?

# 1 <= n  45

# 1걸음 또는 2걸음 걸음수 있음 총 경우의 수는 몇 가지?
def solution(n):
    # 1과 2를 더해 n을 만들수 있는 조합
    return

print(solution(2)) # 2 -> 1step + 1step, 2 steps
print(solution(3)) # 3 -> 1 step + 1step + 1step, 1step + 2steps, 2steps + 1step