def sortPeople(ppl, heights):
    for i in range(len(heights)):
        for j in range(1, len(heights) - i):
            if heights[j] < heights[j-1]:
                heights[j], heights[j-1] = heights[j-1], heights[j]
                ppl[j], ppl[j - 1] = ppl[j-1], ppl[j]


print(sortPeople(["Mary","John","Emma"], [180,165,170]))