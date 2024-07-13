def plusOne(a):
    st = ''.join(a)
    return int(st) + 1
lst = input().strip('[').strip(']').split(',')
plusOne(lst)
