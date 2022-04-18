# 백준 정렬 1181번 단어 정렬

print(*sorted(sorted(set([x.rstrip() for x in [*open(0)][1:]])), key=len))


# 알파벳 순 한번, 길이 순 한번. 실행 순서는 거꾸로 여야 우리가 원하는 순서로 정렬.
# rstrip 안 해서 '출력 형식이 잘못되었습니다' 엄청 떴었음.
# sorted 에 뭘 넣든 리스트로 반환됨.
