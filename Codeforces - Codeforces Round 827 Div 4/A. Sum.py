def sum(arr):
    for i in range(len(arr)):
        arr[i].sort(reverse=True)
        if arr[i][0] == arr[i][1] + arr[i][2]:
            print("YES")
        else:
            print("NO")
n = int(input())
lst = []
for i in range(n):
    x = list(map(int, input().split()))
    lst.append(x)
sum(lst)

