def maxScore(cardPoints, k):
    n = len(cardPoints)
    p = n - k
    min_sum = 0
    i = 0
    while i < p:
        min_sum += cardPoints[i]
        i += 1
    # print(i, min_sum)
    left  = 0
    right = i
    curr_sum = min_sum
    while right < n:
        # print(cardPoints[left:right + 1])
        curr_sum = curr_sum - cardPoints[left] + cardPoints[right]
        min_sum = min(min_sum, curr_sum)
        left += 1
        right += 1
    # print(min_sum)
    return sum(cardPoints) - min_sum

print(maxScore([1,2,3,4,5,6,1], 3))