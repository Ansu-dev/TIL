# 시간 초과 해결 필요
import sys
from itertools import permutations

input =  sys.stdin.readline

N = int(input())

# 안타: 1
# 2루타: 2
# 3루타: 3
# 홈런: 4
# 아웃: 0

def main():
    # 2차원 배열로
    S = [list(map(int, input().split())) for _ in range(N)]  # 각 이닝별 선수들의 결과

    # 1번 타자를 4번으로 고정했기 때문에
    players = [i for i in range(2, 10)] # 2번 선수부터 9번 선수
    max_score = 0

    # 8명의 선수 순열 생성
    for order in permutations(players):
        # 4번 타자에 1번 선수 배치
        batting_order = list(order[:3]) + [1] + list(order[3:])
        score = 0
        current_batter = 0 # 타순의 현재 타자 인덱스(이닝이 바꼈을 때도 여전히 해당 타자이므로 저장해놔야함)

        for inning in range(N): # 1번부터 9번까지 다 돌는 싸이클 -> 9번까지 3out이 되지 않았을 경우 다음 다음 이닝의 1번 타자부터 다시
            outs = 0
            bases = [0, 0, 0] # 1루, 2루, 3루에 주자가 있는지 여부
            while outs < 3: # 3out이 되기전까진 계속 무한루프
                player = batting_order[current_batter] # 현재 타석의 선수
                result = S[inning][player - 1] # 선수 번호는 1번 부터니까 -1을 해줘서 인덱스에 맞춰줘야함

                if result == 0:
                    outs += 1
                elif result == 1:
                    # 안타: 모든 주자와 타자가 한 루씩 진루
                    if bases[2]: # 3루에 주자가 있다면 득점
                        score += 1
                        bases[2] = 0
                    if bases[1]: # 2루에 주자가 있다면
                        bases[2] = 1
                        bases[1] = 0
                    if bases[0]: # 1루에 주자가 있다면
                        bases[1] = 1
                        bases[0] = 0
                    # 안타를 쳤기 때문에 1루는 타자가 들어감
                    bases[0] = 1
                elif result == 2: # 2루타: 모든 주자와 타자가 2개의 베이스씩 진루
                    if bases[2]:
                        score += 1
                        bases[2] = 0
                    if bases[1]:
                        score += 1
                        bases[1] = 0
                    if bases[0]:
                        bases[2] = 1
                        bases[0] = 0
                    bases[1] = 1
                elif result == 3: # 3루타: 모든 주자와 타자가 3개의 베이스씩 진루
                    if bases[2]:
                        score += 1
                        bases[2] = 0
                    if bases[1]:
                        score += 1
                        bases[1] = 0
                    if bases[0]:
                        score += 1
                        bases[0] = 0
                    bases[2] = 1
                elif result == 4:
                    score += sum(bases) + 1
                    bases = [0, 0, 0]

                # 9번 타자가 됐을 땐 다시 첫번째로 돌아가야하므로
                current_batter = (current_batter + 1) % 9 # 다음 타자로 이동

        if score > max_score:
            max_score = score

    print(max_score)

main()

# 왜 브루트 포스 인가?
# 최적의 타순을 찾기 위해서는 모든 가능성을 고려해야 함
    # 타순의 중요성 각 선수의 타격 결과(안타, 2루타, 3루타, 홈런, 아웃)는 타순에 따라 게임의 흐름과 득점에 영향을 미침
    # 순열의 필요성: 1번 선수를 제외한 나머지 8명을 다양한 순서로 배치해야함 -> 모든 가능한 순서를 고려
# 문제의 복잡성과 브루트 포스의 적합성
    # 순열의 수: 나머지 8명의 선수는 8!(40320)가지의 순서
    # N의 범위: 이닝 수 N은 최대 50이므로, 각 순열에 대해 이닝별 시뮬레이션을 수행
    # 총 연산량: 총 연산량은 약 40,320(순열) x 50(이닝) x 9(타순 당 타격) = 18,144,000


