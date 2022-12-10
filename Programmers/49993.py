# Summer/Winter Coding(~2018). lv2. 스킬트리


def solution(skill, skill_trees):
    ans = 0
    for tree in skill_trees:
        tmp = [skill.index(s) for s in tree if s in skill]
        if tmp == [*range(len(tmp))]:
            ans += 1
    return ans

        # better case
        # tmp = ''.join(s for s in tree if s in skill)
        # if tmp == skill[:len(tmp)]:
