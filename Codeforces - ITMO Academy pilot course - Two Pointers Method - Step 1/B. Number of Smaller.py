x = list(map(int, input().split()))
ar1 = list(map(int, input().split()))
ar2 = list(map(int, input().split()))
pointer = 0
lst = []
for i in range(len(ar2)):
    while pointer < len(ar1) and ar2[i] > ar1[pointer]:
        pointer += 1
    lst.append(str(pointer))
print(" ".join(lst))
