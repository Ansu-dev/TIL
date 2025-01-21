import sys

input =  sys.stdin.readline
N = int(input())

def main():
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(matrix)
    # 신맛과 쓴맛의 차이가 가장 작은 요리
    # 신맛은 곱이고, 쓴맛은 합

    # 각 경우의조합을 생각해야하므로 브루트-포스가 적합

main()

