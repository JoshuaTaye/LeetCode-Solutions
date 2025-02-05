def find_Players_With_Zero_or_One_Losses(arr):
    hm = {}
    sett = set()
    for i in range(len(arr)):
        sett.update(arr[i])
        if arr[i][1] not in hm:
            hm[arr[i][1]] = 1
        else:
            hm[arr[i][1]] += 1
    res = []
    wins = []
    for k in sett:
        if k not in hm:
            wins.append(k)
    for key, value in hm.items():
        if value == 1:
            res.append(key)
        if value == 0:
            res.append(wins)
    return [wins, res]


print(find_Players_With_Zero_or_One_Losses([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))