# 프로그래머스 # 해시 # 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    
    for i,v in enumerate(phone_book[:-1]):
        if phone_book[i+1].startswith(v): return False
        
    return True
