def container (h):
    max = 0
    for i in range(len(h)):
        for j in range(i+1, len(h)):
                area = min(int(h[j]),int(h[i])) * (j - i)
                print(area)
                if area > max:
                    max = area
    print(max)
# height = input().strip('[').strip(']').split(',')
container([1,8,6,2,5,4,8,3,7])