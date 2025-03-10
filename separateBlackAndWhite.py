from collections import Counter


def minimumSteps(s):
    print(Counter(s))
    s = list(map(int, s))
    r = len(s) - 1
    swaps = 0
    print(s)
    placeholder = len(s) - 1
    seeker = 0
    while sorted(s) != s:
        while placeholder > 1 and s[placeholder] == 1:
            placeholder -= 1
        while seeker < len(s)-1 and s[seeker] == 0:
            seeker += 1
        swaps += placeholder - seeker
        s[seeker], s[placeholder] = s[placeholder], s[seeker]
        placeholder -= 1
        seeker += 1
    return swaps



print(minimumSteps("11000111"))