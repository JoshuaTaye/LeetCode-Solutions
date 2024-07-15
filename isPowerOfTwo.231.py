def is_power_of_two(n):
    i = 0
    while i < n:
        if 2 ** i == n:
            return True
        elif 2 ** i > n:
            return False
        i += 1


num = int(input())
print(is_power_of_two(num))