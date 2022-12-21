# 스택/큐 lv2. 다리를 지나는 트럭


from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    bridge_weight = 0
    truck_weights.reverse()
    ans = 0
    
    while truck_weights:
        bridge_weight -= bridge.pop()
        bridge.appendleft(0)
        if bridge_weight + truck_weights[-1] <= weight:
            bridge[0] = truck_weights.pop()
            bridge_weight += bridge[0]
        ans += 1
        
    return ans + bridge_length
