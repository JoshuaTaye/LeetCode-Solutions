def vus_and_cossack(arr):
    if arr[0]  <= arr[1] and arr[0] <= arr[2]:
        return "Yes"
    else:
        return "No"

lst = list(map(int, input().split()))
print(vus_and_cossack(lst))
