# ["학번", "이름", "전공", "학년"]
# 유일한 학번을 가짐
# 이름은 같은 이름이 존재 -> 후보키가 될 수 없음
# 이름 + 전공을 함께 한다면 후보키가 될 수 있음
# 이름 + 전공 + 학년을 최소성을 만족하지 못해서 후보 키가 될 수 없다.
# 학번, 이름+전공 => 후보키 가능

# 유일성: 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
# 최소성: 유일성을 가진 키를 구성하는 속성, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성
# 전공+이름 -> 이름+전공 같기 때문에 순열이 아닌 조합을 사용
def solution(relation):
    answer = 0
    columns = [i for i, _ in enumerate(relation[0])] # 컬럼 8이하
    # 컬럼의 모든 조합을 만듬
    found_keys = [] # 후보키 목록
    def backtracking(start,current):
        nonlocal answer
        if current: # 빈 조합은 제외하고 저장
            # 1. 유일성 체크
            seen = set() # 유일성 검사를 위해 중복이 없는 튜플들을 저장할 set()을 생성
            for row in relation:
                key = tuple(row[i] for i in current) # 현재 선택된 컬럼 조합으로 튜플 생성
                seen.add(key) # relation에서 조합된 튜플의 key를 기준으로 값을 모두 넣음
            if len(seen) == len(relation): # 중복이 없으면 유일성 만족 -> 해당 tuple의 Key를 기준으로 모든 row의 개수가 relation의 개수와 동일할 시
                # 2. 최소성 체크
                is_minimal = True
                for key in found_keys:
                    # set(A).issubset(set(B)) -> 집합A가 집합 B의 부분집합이면 True 반환
                    if set(key).issubset(set(current)): # 기존 후보키(key)가 현재 컬럼 조합(current)의 부분집합이면 현재 조합은 최소성을 위배
                        is_minimal = False
                        break # 현재 for문을 중단
                # 최소성을 만족할 경우에만
                if is_minimal:
                    # 후보키로 인정
                    found_keys.append(current[:]) # 리스트 복사
                    answer += 1

        for i in range(start, len(columns)):
            current.append(columns[i])
            backtracking(i + 1, current)
            current.pop() # 백트래킹 -> 가능한 조합을 다시 살핌

    backtracking(start=0, current=[]) # 중복 조합을 방지하기 위해 시작 위치를 넘김


    # 조합을 가지고 모든 튜플을 순회하며 유일성을 만족하는지 확인
    # 유일성을 만족하는 키 중에 최소성을 만족하는 조합만 후보키로 선택
    # 브루트 포스로 모든 튜플을 순회해야함
    # row는 20이하 20!

    return answer


print(
    solution(
        [
            ["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]
        ]
    )
) # 2