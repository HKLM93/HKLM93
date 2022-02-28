# 일부만 통과(시간초과가 나는 답)
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    result = {id: [] for id in id_list}  # 어떤 유저가 누구를 신고했는지 보여줌
    reported = []  # 신고당한 유저를 보여줌
    stop = []  # 정지당한 유저를 보여줌

    for i in set(report):
        report = i.split(' ')  # 신고한 내용을 보기 편하게 리스트로 표현
        reported.append(report[1])  # 신고당한 유저를 넣음
        result[report[0]].append(report[1])

    for j in reported:
        if reported.count(j) >= k:
            stop.append(j)

    stop = set(stop)  # 중복 제거

    for key, value in result.items():
        for s in stop:
            # 정지당한 유저를 신고했으면
            if s in value:
                # 메시지를 받는다.
                answer[id_list.index(key)] += 1

    return answer
####################################################################
# 시간 초과가 안 나는 답(구글링으로 찾았다)
def solution(id_list, report, k):
    db = {name: [] for i, name in enumerate(id_list)}
    reports = {name: 0 for i, name in enumerate(id_list)}

    for re in set(report):
        user = re.split(" ")[0]
        reported_user = re.split(" ")[1]
        db[user].append(reported_user)
        reports[reported_user] +=1

    answer = [0 for _ in range(len(id_list))]
    for key, values in db.items():
        for value in values:
            if reports[value] >=k:
                answer[id_list.index(key)] += 1
    return answer