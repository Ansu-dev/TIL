def solution(phone_book):
    # 어떤 번호가 다른 번호의 접두어인 경우 false
    # 그렇지 않으면 true

    # 119, 1195524421 접두어 이므로 false
    # 123 456 789 접두어가 없으므로 true

    # 1. hash map 생성
    hash_map = {}
    for phone in phone_book:
        hash_map[phone] = 1

    # 2. 접두어가 hash map에 존재하는지 찾기
    for phone in phone_book:
        arr = ""
        for num in phone:
            arr += num

            # 각 숫자에 한개씩 문자열을 비교해보며 해시맵에 존재하는 접두사가 있는지 판별
            # 3. 본인 자체일 경우는 제외
            if arr in hash_map and arr != phone:
                return False

    return True




print(solution(["119", "97674223", "1195524421"])) # False
print(solution(["123","456","789"])) # true
print(solution(["12","123","1235","567","88"])) # false