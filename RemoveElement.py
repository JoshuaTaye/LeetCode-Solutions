def removeElement(n, v):
    i = 0
    while i < len(n):
        if n[i] == v:
            n.remove(n[i])
        else:
            i += 1
    return n


val = 3
nums = [3,2,2,3]
print(removeElement(nums,val))