# 이진탐색
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 메뉴 오름차순 정렬
    #
    # # O(NlogN) + O(M) * O(logN) = O((N+M)*log(N))
    # shop_menus.sort() # 메뉴의 길이가 N -> O(NlogN)
    # for order in orders: # 주문의 길이가 M 이라고 한다면 O(M)
    #     # 주문이 menu에 포함이 되어있는지 판별
    #     if not is_exist_target_number_binary(order, menus): # O(logN) -> 이진탐색 굉장히 비효율
    #         return False
    #
    # return True


    # 집합 자료형 사용
    # O(N) + O(M) * O(1) = O(N + M)
    menus_set = set(menus) # O(N)
    for order in orders: # O(M)
        if order in menus_set: # O(1)
            return False
    return True





def is_exist_target_number_binary(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            # cur_guess는 탐색을 했으니 1개 큰인덱스부터 검사
            cur_min = cur_guess + 1
        else:  # cur_guess는 탐색을 했으니 1개 작은인덱스 부터 검사
            cur_max = cur_guess - 1
        cur_guess = (cur_min + cur_max) // 2
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)