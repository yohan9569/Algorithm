# programmers 72411 lv2 카카오 - 매뉴 리뉴얼


##### 풀이 계획
# course의 원소(코스의 길이)마다 베스트인 친구들을 뽑아낸다.
#     주문마다 원하는 길이만큼의 조합을 만든다.
#     그중 가장 빈도가 높은 친구들을 리턴한다.
# 모든 단계에서 정렬을 주의한다. (출력 기준도 그렇고, counter 할 때도 'wx' 와 'xw' 다르게 취급)

##### (원래 계획)
# course 원소마다 dict를 만든다.
# 원소마다 그 원소만큼 order의 조합을 만들고 키 지정, 또 나오면 하나씩 추가
# 각 dict마다 max_value key를 ans에 담는다.



from itertools import combinations as cb
from collections import Counter as ct


def best(orders, n):
    '''
    코스의 길이가 주어지면 그 길이에 맞춰 주문의 조합을 만든다.
    가장 많이 주문된 조합의 리스트를 리턴한다.
    '''
    case = []
    for o in orders:
        case.extend([*cb(o,n)])

    cnt = ct(case)
    if len(cnt): # n이 최대 주문 길이보다 긴 경우 에러남.
        max_val = max(cnt.values())
    else: return []

    if max_val>1:
        ans = [''.join(k) for k in cnt.keys() if cnt[k]==max_val]
        return ans
    else: 
        return []

    ''' 우수 코드
    most_ordered = collections.Counter(order_combinations).most_common()
    result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ] 
    extend 안 해도 된다.. 위의 두 조건문이 불필요..
    '''


def solution(orders, course):
    orders = [''.join(sorted(o)) for o in orders] # 각 주문은 정렬되어있지 않음. wx와 xw는 다르게 취급됨.
    ans = set() # 지금 보니까 리스트여도 될 듯.
    
    for i in course:
        ans.update(best(orders, i))
        
    return sorted(ans)


''' 우수코드 참고 후 개선 ver. 근데 성능은 위에가 더 좋았다.
def best(orders, n):
    case=[]
    for o in orders:
        case+=[*cb(o,n)]
    cnt=ct(case).most_common()
    res=[''.join(k) for k,v in cnt if v>1 and v==cnt[0][1]]
    return res

def solution(orders, cs):
    orders=[''.join(sorted(o)) for o in orders]
    ans=[]
    for i in cs:
        ans+=best(orders, i)
    return sorted(ans)
'''


solution(["XYZ", "XWY", "WXA"],[2,3,5])
