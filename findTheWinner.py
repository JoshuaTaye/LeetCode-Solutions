def findTheWinner(n, k):
    arr = [i for i in range(1, n+1)]
    j = k - 1
    i = 0
    while True:
        while i < len(arr):
            if j > 0:
                j -= 1
            else:
                arr.remove(i % n)
                j = k - 1
            i += 1
            if len(arr) == 1:
                return arr[0]


print(findTheWinner(3, 1))