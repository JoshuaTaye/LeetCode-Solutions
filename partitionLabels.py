from collections import Counter


def partitionLabels(s):
    partitions = [1]
    hm = {}
    for i in range(len(s)):
        ind = i + 1
        while ind+1 < len(s):
            boundary = 0
            if s[ind] == s[i]:
                boundary = ind
            ind += 1
        print("Boundary for ", s[i], ":", boundary)

    print(partitions)




print(partitionLabels("ababcbacadefegdehijhklij"))