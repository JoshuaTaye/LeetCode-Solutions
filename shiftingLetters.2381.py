def shiftingLetters(s, shifts):
    offsets = [0]*(len(s)+1)
    for start, end, direction in shifts:
        if direction == 1:
            offsets[start] += 1
            offsets[end + 1] -= 1
        else:
            offsets[start] -= 1
            offsets[end + 1] += 1
    newoffsets = [0] * len(offsets)
    newoffsets[0] = offsets[0]
    for i in range(len(s)):
        newoffsets[i] = offsets[i] + offsets[i-1]
    ans = []
    for i in range(len(s)):
        curr = (ord(s[i]) - ord('a') + newoffsets[i]) % 26
        ans.append(chr(curr + ord('a')))
    return "".join(ans)
print(shiftingLetters("abc",[[0,1,0],[1,2,1],[0,2,1]] ))