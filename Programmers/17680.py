# 2018 KAKAO BLIND RECRUITMENT  lv2.  [1차] 캐시


def solution(cacheSize, cities):
    cache = []
    time = 0
    
    for c in cities:
        c = c.lower()
        
        if c in cache:
            cache.remove(c)
            cache.append(c)
            time += 1
        else:
            cache.append(c)
            time += 5
        
        if cacheSize:
            cache = cache[-cacheSize:]
        else:
            cache = []
    
    return time


    # better case
    import collections
    cache = collections.deque(maxlen=cacheSize)
