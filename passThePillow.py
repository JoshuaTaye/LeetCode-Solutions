def pass_the_pillow(n, time):
    pointer = 1
    count = 0
    reverse = False
    while count < time:
        if not reverse:
            if pointer == n - 1:
                reverse = True
            pointer += 1
        else:
            if pointer == 2:
                reverse = False
            pointer -= 1
        count += 1
    return pointer

print(pass_the_pillow(4, 5))