def shiftingLetters(s, shifts):
    s = list(s)
    ar = [0] * len(s)
    for i in shifts:
        if i[2] == 1:
            ar[i[0]] += 1
            if i[1]  < len(ar)-1:
                ar[i[1]+1] -= 1
        else:
            ar[i[0]] -= 1
            if i[1]  < len(ar)-1:
                ar[i[1]+1] += 1
    ps = [ar[0]]
    for i in range(1, len(ar)):
        ps.append(ar[i] + ps[i-1])
    print(ps)
    for j in range(len(s)):
        curr = (ord(s[j]) - ord('a') + ps[j]) % 26
        print(curr)
        s[j] = chr(curr + ord('a'))
    return ("".join(s))


# print(shiftingLetters("dztz",[[0,0,0],[1,1,1]] ))
print((ord("z") - ord("a") - 2)%26 + ord("a"))
print()










#     offsets = [0]*(len(s)+1)
#     for start, end, direction in shifts:
#         if direction == 1:
#             offsets[start] += 1
#             offsets[end + 1] -= 1
#         else:
#             offsets[start] -= 1
#             offsets[end + 1] += 1
#     newoffsets = [0] * len(offsets)
#     newoffsets[0] = offsets[0]
#     for i in range(len(s)):
#         newoffsets[i] = offsets[i] + offsets[i-1]
#     ans = []
#     for i in range(len(s)):
#         curr = (ord(s[i]) - ord('a') + newoffsets[i]) % 26
#         ans.append(chr(curr + ord('a')))
#     return "".join(ans)