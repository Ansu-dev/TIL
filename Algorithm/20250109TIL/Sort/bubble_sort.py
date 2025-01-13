input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    # 이 부분을 채워보세요!
    # O(N^2)
    for i in range(len(array) - 1): # 모든과정의 인덱스 O(N)
        for j in range(len(array) - i - 1): # 각 라운드 마다 비교하는 횟수 O(N)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]  # swap  # i, i+1번째 원소 swap

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))