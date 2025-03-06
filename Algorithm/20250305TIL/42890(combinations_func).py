from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 가능한 속성의 모든 인덱스 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    # 유일성
    unique = []
    for i in combi:
        # 유일성을 확인하기위해 해당 조합에 모든 row를 대입
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:  # 유일성, 겹치지 않고 모든 row가 나온다면 유일성 만족
            put = True

            for x in unique:
                if set(x).issubset(set(i)):  # 최소성, x가 i의 부분집이 아닐 경우에 최소성 만족
                    put = False
                    break

            if put: unique.append(i)

    return len(unique)