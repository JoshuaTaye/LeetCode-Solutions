def furthestBuilding(h, br, la):
    lst = []
    for i in range(len(h)):
        h[i] = int(h[i])
    for i in range(len(h)-1):
        if h[i+1] > h[i]:
            lst.append(h[i+1] - h[i])   
        else:
            lst.append(0)
    # print(lst)
    for i in range(len(lst)):
        if lst[i] != 0:
            lz = sorted(lst)
            if br >= lst[i] and lst[i] < lz[-1 * la] or la == 0:
                while lst[i] > 0 and br > 0:
                    lst[i] -= 1
                    br -= 1
            else:
                lst[i] = 0
                la -= 1
    # print(lst, "la-", la, 'br-', br)
    final = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            final = i
            return final
    final = len(lst)
    return final


height = input().strip('[').strip(']').split(',')
bricks = int(input())
ladders = int(input())
print(furthestBuilding(height, bricks, ladders))

