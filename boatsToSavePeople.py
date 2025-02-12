def boats(people, limit):
    r = len(people) - 1
    l = 0
    count = 0
    while l < r:
        if people[r] + people[l] <= limit:
            l += 1
        count += 1
        r -= 1
    return count


print(boats([3,8,7,1,4], 9))