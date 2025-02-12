from collections import Counter

def frequencySort(s):
    freq = Counter(s)
    store = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    res = []
    for i in store:
        for _ in range(i[1]):
            res.append(i[0])
    return "".join(res)
    # x = (sorted(freq.values(), reverse=True))
    # res = []
    # for j in x:
    #     for key, value in freq:
    #         if freq[key] == j:
    #             for k in range(freq[key]):
    #                 print("yes", key)
    #                 res.append(key)
    #             # freq.pop(key)
    #             print(freq)
    # return "".join(res)


print(frequencySort("loveleetttccode"))