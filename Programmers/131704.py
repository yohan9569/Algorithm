# 연습문제 lv2. 택배상자


def solution(order):
    order.reverse()
    stack = [0]
    belt = 1
    ans = 0
    
    while order:
        if belt == order[-1]:
            ans += 1
            belt += 1
            order.pop()
        elif stack[-1] == order[-1]:
            ans += 1
            stack.pop()
            order.pop()
        elif belt < order[-1]:
            stack.append(belt)
            belt += 1
        else:
            break
    
    return ans
