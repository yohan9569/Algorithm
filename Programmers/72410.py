# 2021 KAKAO BLIND RECRUITMENT. lv1. 신규 아이디 추천


import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[^\uAC00-\uD7A30-9a-z-_.]", "", new_id)
    new_id = re.sub(r"[.]+", ".", new_id)
    new_id = re.sub(r"^[.]|[.]$", "", new_id)
    if not new_id:
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = re.sub(r"[.]$", "", new_id)
    if len(new_id) < 3:
        new_id = new_id + new_id[-1]*(3-len(new_id))
    return new_id
