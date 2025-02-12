def maxCoins(piles):
    piles.sort(reverse=True)
    print(piles)
    fin = 0
    x = int(len(piles) / 3)
    for j in range(1, len(piles) - x, 2):
        print(piles[j])
        fin += piles[j]

    return fin



print(maxCoins([2,4,1,2,7,8]))