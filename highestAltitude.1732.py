def highestAltitude(gain):
    max = 0
    curr = 0
    for i in range(len(gain)):
        curr += gain[i]
        if curr > max:
            max = curr

    return max

print(highestAltitude([-5,1,5,0,-7]))