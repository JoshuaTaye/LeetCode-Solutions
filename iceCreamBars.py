def max_ice_cream_bars(costs, coins):
    costs.sort()
    print(costs)
    if costs[0] > coins:
        return 0
    cur_sum = 0
    i = 0
    while i < len(costs) and cur_sum + costs[i] < coins:
        cur_sum += costs[i]
        print(cur_sum)
        i += 1
    return i


print(max_ice_cream_bars([7,3,3,6,6,6,10,5,9,2], 56))