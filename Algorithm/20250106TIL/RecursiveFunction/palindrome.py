input = "abcba"

# 문제의 범위를 조금씩 좁혀나간다.
# count_down

# 문자열의 탐색범위를 좁혀나간다.

def is_palindrome(string):
    # 문자열의 맨앞과 맨뒤를 짤라서
    # n은 문자열의 길이
    # string[1:-1]
    if string[0] != string[-1]: # 맨앞과 맨뒤가 다르다면 무조건 틀림
        return False
    if len(string) <= 1: # 1개의 문자열은 무조건 회문이다.
        return True
    return is_palindrome(string[1:-1])


print(is_palindrome(input))