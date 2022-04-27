# programmers heap 42626번 더 맵게 lv2

import heapq as hq


def solution(scov, K):
    heap = []
    
    for v in scov:
        hq.heappush(heap, v)
        
    n=0
    
    while len(heap)>1:
        if heap[0] >= K:
            break
            
        mix = hq.heappop(heap) + hq.heappop(heap)*2
        hq.heappush(heap, mix)
        n += 1
        
    if len(heap)==1 and heap[0]<K: 
        return -1
      
    return n
