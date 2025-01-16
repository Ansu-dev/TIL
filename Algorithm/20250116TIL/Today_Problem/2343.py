import sys
input =  sys.stdin.readline

N, M = map(int, input().split())


def binary_search(lecture_lengths, target):
    min_size = max(lecture_lengths) # 강의에서 블루레이가 가장 큰값이 최소
    max_size = sum(lecture_lengths) # 모든 강의의 블루레이 합

    result = min_size # 초깃값에 최소 사이즈를 넣음

    while min_size <= max_size:
        mid_size = (min_size + max_size) // 2
        count = 1 # 필요한 블루레이 개수 (최소 1개)
        total = 0 # 현재 블루레이에 녹화된 강의 총 길이

        for length in lecture_lengths:
            if (total + length) > mid_size:
                # 현재 블루레이에선 녹화 할 수 없으니 다른 블루레이로 이동
                count += 1
                total = length # 새로운 블루레이에서 시작
            else:
                # 현재 블루레이에 녹화 추가
                total += length

        if count <= target:
            # 현재 mid_size 값이 가능하므로, 더 작은 값을 시도
            result = mid_size
            max_size = mid_size - 1
        else:
            # 현재 mid_size 값이 불 가능하므로, 더 큰 값을 시도
            min_size = mid_size + 1

    return result


def main():
    lecture_lengths = list(map(int, input().split()))

    result = binary_search(lecture_lengths, M)
    print(result)

main()


# 블루레이에 총 N개의 강의가 들어가는데, 블루레이를 녹화할 때 가의의 순서가 바뀌면 안됨
# 얼마나 팔릴지 아직 알 수 없기 때문에, 블루레이의 개수를 가급적 줄이려고함, 오랜 고민 끝에 M개의 블루레이에 모든 기타 강의 동영상을 녹화하기러함
# 이 때 블루레이의 크기(녹화 가능한 길이)를 최소로 한다. 단, M개의 블루레이는 모두 같은 크기


# 강의는 총 9개, 블루레이는 총 3개
# 1번 블루레이에는 1,2,3,4,5
# 2번 블루레이에는 6,7,3번
# 3번 블루레이에는 8,9
# 를 각각 넣으면 각 블루레이의 크기는 15,13,17이 왼다. 블루레이의 크기는 모두 같아야 하기 때문에, 블루레이의 크기는 17이 된다.
# 17보다 더 작은 크기를 가지는 블루레이는 만들 수 없다.
