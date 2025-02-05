def from_s_to_t(arr):
    def isRelative(st1, st2):
        ind = 0
        pointer = 0
        while pointer < len(st1) and ind < len(st2):
            if st1[pointer] not in st2[ind:]:
                return False
            else:
                ind = st2.index(st1[pointer]) + 1
            pointer += 1
        return True
    for i in range(len(arr)):
        if len(arr[i][0]) > len(arr[i][1]):
            print("NO")
        elif arr[i][0] == arr[i]:
            print("YES")
        elif not isRelative(arr[i][0], arr[i][1]):
            print("NO")
        else:
            agg = list(arr[i][0])
            check = list(arr[i][2])
            if not isRelative(arr[i][1], agg + check):
                print("NO")
            else:
                isIn = True
                l = 0
                a = 0
                while a < len(arr[i][1]):
                    if arr[i][1][a] not in agg[l:] and arr[i][1][a] not in check:
                        print("NO")
                        isIn = False
                        break
                    else:
                        if arr[i][1][a] not in agg[l:]:
                            check.remove(arr[i][1][a])
                        else:
                            l += 1
                        a += 1
                if isIn:
                    if i == 2:
                        print("awo awo ezi na", "a is", a)
                    if a < len(arr[i][1]):
                        print("NO")
                    else:
                        print("YES")
lst = []
n = int(input())
for k in range(n):
    x = []
    for j in range(3):
        x.append(input())
    lst.append(x)
from_s_to_t(lst)

# use two pointers and a hashmap to track the frequency of elements in arr[i][2]

