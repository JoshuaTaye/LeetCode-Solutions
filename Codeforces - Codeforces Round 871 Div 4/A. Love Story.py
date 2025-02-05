def love_story(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[i])):
            if arr[i][j] not in "codeforces"[j]:
                count += 1
        print(count)


n = int(input())
lst = []
for k in range(n):
    lst.append(input())
love_story(lst)