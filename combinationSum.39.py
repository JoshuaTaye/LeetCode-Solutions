def combinationSum(candidates, target):
    candidates.sort()
    results = [[]]
    total = 0
    multiplier = 1
    i = 0
    while i < len(candidates):
        if candidates[i] * multiplier < target:
            multiplier += 1
            results[i].append(candidates[i])
            total += candidates[i]
            if target - total in candidates:
                results[i].append(target - total)
            continue
        i += 1
    print(results)


print(combinationSum([2, 3, 6, 7], 7))
