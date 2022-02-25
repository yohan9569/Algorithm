# 프로그래머스 # 탐욕법 # 조이스틱

# 풀이 방법: 매 시점마다 최소 거리로 이동. (왼쪽 오른쪽 거리가 같은 경우에 오른 쪽 선택.)


def get_left_dis(cur_idx, name, my_input):
    dis=0
    while True:
        if name[cur_idx] != my_input[cur_idx]:
            return cur_idx, dis
        dis += 1
        cur_idx -= 1
        if cur_idx == -1:
            cur_idx = len(name)-1

def get_right_dis(cur_idx, name, my_input):
    dis=0
    while True:
        if name[cur_idx] != my_input[cur_idx]:
            return cur_idx, dis
        dis += 1
        cur_idx += 1
        if cur_idx == len(name):
            cur_idx = 0

def solution(name):
    name = list(name)
    my_input = list("A" * len(name))
    alphabet_d = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                 [i if i<14 else 26-i for i in range(26)]))

    ans = 0
    cur_idx = 0
    while True:
        if name == my_input:
            return ans

        left_idx, left_dis = get_left_dis(cur_idx, name, my_input)
        right_idx, right_dis = get_right_dis(cur_idx, name, my_input)

        if left_dis < right_dis:
            # cur_idx = right_idx
            # ans += right_dis
            cur_idx = left_idx
            ans += left_dis
        # elif left_dis == right_dis:  ???
        else: 
            cur_idx = right_idx
            ans += right_dis
            # cur_idx = left_idx
            # ans += left_dis

        my_input[cur_idx] = name[cur_idx]
        ans += alphabet_d[name[cur_idx]]
        # print(my_input, ans)

        
        
'''
통과는 했으나, 반례가 있는 것 같다.
예) CANAAAAANAN 의 경우 처음에 최소 거리인 왼쪽을 선택하는 것보다 오른쪽 선택하는 게 빠르다.
그리디가 아닌 다른 방식으로 접근해서 푸는 게 더 옳을 것 같다.
'''
