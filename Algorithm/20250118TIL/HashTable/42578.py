def solution(clothes):
    # 각 종류 별로 최대 1가지 의상만 착용 가능
    # 최소 1개 이상의 의상을 착용
    # 동일한 종류의 의상끼리는 동시에 착용 불가
    # 같은 이름의 의상은 존재하지 않음


    answer = 1 # 곱셈의 항등원 역할 1로 초기화

    # 데이터 중복성을 빠르게 검사하기 위해서 해시 테이블을 사용
    hash_map = {}

    for name, category in clothes:
        if category in hash_map:
            hash_map[category] += 1 # 추가되는 의상부턴 2가지의 경우의 수가 생기므로
        else:
            hash_map[category] = 2 # 해당 카테고리를 입는 경우 + 입지 않는 경우 => 2가지 경우의 수

    print(hash_map)
    # 의상의 모든 경우의수를 answer에 더함
    # 의상은 1가지 종류씩 밖에 조합할 수 없음
    for value in hash_map.values():
        answer *= value

    # 최소 1개 이상의 의상을 입어야해서 모든 의상을 입지않는 1개의 경우의 수는 제외
    return answer - 1 # 해당 answer 조합에서 해당 의상 카테고리를 입지 않는 경우가 1개 포함되어있으므로 그 조합은 빼주어야함



print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) # 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) # 3