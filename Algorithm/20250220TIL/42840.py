# O(n)
def solution(answers):
    answer = []

    # 수포자1,2,3의 각 문제를 찍는 패턴을 하드코딩
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    # answers를 순회하며 각 student마다 맞춘 점수를 기입
    score = [0,0,0] # 3명의 학생으로 정해짐
    for i, a in enumerate(answers): # O(n)
        if a == student1[i % len(student1)]: # student1의 찍는 패턴을 반복하기 위해 나머지 연산을 사용
            score[0] += 1
        if a == student2[i % len(student2)]:
            score[1] += 1
        if a == student3[i % len(student3)]:
            score[2] += 1

    max_score = max(score)
    for i, s in enumerate(score): # O(1) => 3개로 정해져있기때문에
        if max_score == s:
            answer.append(i + 1) # 인덱스는 0번부터 시작하니까
    return answer


# 총 10000문제 이므로 2^4승 => n^2 문제로 풀순 없다

print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]