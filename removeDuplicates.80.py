def removeDuplicates2(arr):
    mapp = {}
    i = 0
    while i < len(arr):
        if arr[i] in mapp:
            if mapp[arr[i]] < 2:
                mapp[arr[i]] += 1
            else:
                arr.remove(arr[i])
                i -= 1
        else:
            mapp[arr[i]] = 1
        i += 1
    print(mapp)
    return arr
print(removeDuplicates2([0,0,1,1,1,1,2,3,3]))