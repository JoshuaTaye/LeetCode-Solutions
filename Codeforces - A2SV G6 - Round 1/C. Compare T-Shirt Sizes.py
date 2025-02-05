def compare(arr):
    for i in range(len(arr)):
        if arr[i][0] == arr[i][1]:
            print("=")
        elif arr[i][0][-1] != arr[i][1][-1]:
            if arr[i][0][-1] == "L":
                print(">")
            elif arr[i][0][-1] == "S":
                print("<")
            elif arr[i][1][-1] == "L":
                print("<")
            elif arr[i][1][-1] == "S":
                print(">")
        else:
            if arr[i][0][-1] == "S":
                if len(arr[i][0]) > len(arr[i][1]):
                    print("<")
                else:
                    print(">")
            else:
                if len(arr[i][0]) > len(arr[i][1]):
                    print(">")
                else:
                    print("<")





n = int(input())
lst = []
for k in range(n):
    x = list(map(str, input().split()))
    lst.append(x)
compare(lst)