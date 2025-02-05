def square_string(arr):
    for i in range(len(arr)):
        if (len(arr[i]) % 2) != 0:
            print("NO")
        elif arr[i][:int((len(arr[i]))/2)] == arr[i][int(len(arr[i])/2):]:
            print("YES")
        else:
            print("NO")


n = int(input())
lst = []
for k in range(n):
    lst.append(input())
square_string(lst)
