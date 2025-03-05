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
    def backtracking(start,current):
        nonlocal answer
        if current: # 빈 조합은 제외하고 저장
            print(current)
            # 후보키를 판별


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