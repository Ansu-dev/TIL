# O(n) 시간복잡도
def solution(sizes):
    answer = 0
    # 명함을 회전시킬 수 있으므로, 각 명함에서 더 작은 수는 세로, 더 큰수는 가로로 맞춰줌
    rotated = [sorted(card) for card in sizes] # O(1) => 명함 한 개는 길이가 2인 배열이므로, 정렬에 걸리는 시간은 상수 시간

    # 각 인덱스에서 가장 큰 수들만 뽑아서 명함지갑을 생성
    max_width = max(row[0] for row in rotated) # O(n)
    max_height = max(row[1] for row in rotated) # O(n)

    answer = max_width * max_height
    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133