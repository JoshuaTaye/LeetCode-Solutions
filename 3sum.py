def threeSum(n):
    lst = []
    for i in range(len(n)):
        n[i] = int(n[i])
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            for k in range(j+1, len(n)):
                print(i,j,k)
                l=[]
                if i != j != k:
                    if (n[i] + n[j] + n[k] == 0):
                        l.append(n[i])
                        l.append(n[j])
                        l.append(n[k])
                if len(l) > 0 and sorted(l) not in lst:
                    lst.append(sorted(l))
    # for i in range(len(lst)):
    #     if len(lst[i])> 3:
    #         while len(lst[i])>3:
    #             lst[i] = lst[i][:-1]
    return lst
nums = input().strip('[').strip(']').split(',')
print(threeSum(nums))