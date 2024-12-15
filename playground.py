ar = [-4, -5, 3, 2, 4, -4, -12, 2, 2, 6]


#
# Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


#
#
# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr


#
#
# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


# Counting Sort
def counting_sort(arr):
    newArr = [0] * (max(arr) + 1)
    for i in arr:
        newArr[i] += 1
    ind = 0
    for i in range(len(newArr)):
        if newArr[i] > 0:
            for k in range(newArr[i]):
                arr[ind] = i
                ind += 1
    print(arr)


def counting_search_with_negative(arr):
    minElt = min(arr)
    newArr = [0] * (max(arr) - min(arr) + 1)
    for i in arr:
        newArr[i + abs(minElt)] += 1
    print(newArr)
    ind = 0
    for i in range(len(newArr)):
        if newArr[i] > 0:
            for k in range(newArr[i]):
                arr[ind] = i - abs(minElt)
                ind += 1
    print(arr)


# ar = [-12, -5, -4, -4, 2, 2, 2, 3, 4, 6]
def binary_search_recursion(arr, x):
    print("here")
    md = len(arr) // 2
    if len(arr) == 1 and arr[0] != x:
        return -1
    elif arr[md] == x:
        return "Found"
    elif arr[md] > x:
        return binary_search_recursion(arr[:md], x)
    else:
        return binary_search_recursion(arr[md:], x)


# print(binary_search_recursion(ar, 6))

def binary_search(ar, x):
    l = 0
    r = len(ar) - 1
    while l <= r:
        print("here")
        m = l + (r - l) // 2
        if x == ar[m]:
            return "Found"
        elif x < ar[m]:
            r = m
        else:
            l = m + 1
    return -1


# print(binary_search(ar, -12))

# Two Pointers parallel pointers
def is_sorted(ar):
    left = 0
    right = 1
    while right < len(ar):
        if ar[left] > ar[right]:
            return False
        left += 1
        right += 1
    return True


# print(is_sorted(ar))

ar1 = [-4, -5, 1, 2, 4, 12, 12, 16]
ar2 = [-10, -1, 0, 3, 4, 5, 12, 12, 12, 16]


# separate array pointers
def merge(ar1, ar2):
    arf = []
    p1, p2 = 0, 0
    while p1 < len(ar1) and p2 < len(ar2):
        if ar1[p1] < ar2[p2]:
            arf.append(ar1[p1])
            p1 += 1
        elif ar1[p1] >= ar2[p2]:
            arf.append(ar2[p2])
            p2 += 1
    return arf


# print(merge(ar1, ar2))

# colliding pointers
def colliding_window(ar):
    n = 13
    l = 0
    r = len(ar) - 1
    while l <= r:
        if ar[r] + ar[l] < n:
            l += 1
        elif ar[r] + ar[l] > n:
            r -= 1
        else:
            return l, r


# print(colliding_window(ar1))

# ar = [4, 0, 0, 1, 3]


# Seeker and Placeholder
def seeker_and_placeholder(ar):
    checker = 0
    next = 0
    while checker < len(ar):
        if ar[checker] != 0:
            ar[checker], ar[next] = ar[next], ar[checker]
            next += 1
            checker += 1
        else:
            checker += 1
    return ar

# print(seeker_and_placeholder(ar))

# for-while combo
ar11 = [2,2,5,6]
ar22 = [3,4,6,12]
def for_while(ar1, ar2):
    ind = 0
    ind2 = 0
    elts = [0] * len(ar2)
    while ind < len(ar2):
        while ind2 < len(ar1):
            print(elts)
            if ar1[ind2] >= ar2[ind]:
                elts[ind] = ind2
                break
            ind2 += 1
        ind += 1
    elts[-1] = ind2
    return elts

# print(for_while(ar11, ar22))
arv = [-4, -5, 3, 2, 4, -4, -12, 2, 2, 6]
#sliding window
def maximumSum(ar, k):
    left = 0
    right = left + k
    summ = 0
    for i in range(k):
        summ += ar[i]
    # print(summ)
    maxSum = 0
    while right < len(ar):
        print(summ, summ - ar[left] + ar[right])
        summ = summ - ar[left] + ar[right]
        maxSum = max(summ, maxSum)
        # print(maxSum)
        left += 1
        right += 1
    return maxSum
# print(maximumSum(arv, 4))

ar_2d = [[-4, -5, 3, 2, 4, -4, -12, 2, 2, 6], [-10, -1, 0, 3, 4, 5, 12, 12, 12, 16],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

def two_d_max(ar, k):
    top = 0
    bottom = top + k[0]
    maxSum = 0
    while bottom <= len(ar):
        summ = 0
        for i in range(top, bottom):
            for j in range(0, k[1]):
                summ += ar[i][j]
        left = 0
        right = left + k[1]
        while right < len(ar[1]):
            for i in range(top, bottom):
                summ = summ - ar[i][left] + ar[i][right]
            maxSum = max(maxSum, summ)
            left += 1
            right += 1
        top += 1
        bottom += 1
    return maxSum
# print(two_d_max(ar_2d, [2,4]))

def anagrams(s, p):
    t_mapp, an, mapp, left, right = [], 0, [], 0, len(p)
    for i in range(right):
        t_mapp.append(p[i])
    t_mapp.sort()
    for k in range(left, right):
        mapp.append(s[k])
    if t_mapp == sorted(mapp):
        an += 1
    while right < len(s):
        mapp.remove(s[left])
        mapp.append(s[right])
        if t_mapp == sorted(mapp):
            an += 1
        left += 1
        right += 1
    return an

print(anagrams("bababa", "ba"))

def longest_unique_substring(s):
    left, right, arr, maxLen = 0, 0, [], 0
    while right < len(s):
        if s[right] in arr:
            arr.remove(arr[0])
        else:
            arr.append(s[right])
            left -= 1
        left += 1
        right += 1
        maxLen = max(maxLen, len(arr))
    return maxLen

# print(longest_unique_substring("abebebcd"))

class StaticArrays:
    def __init__(self, arr, capacity, length):
        self.arr = arr
        self.capacity = capacity
        self.length = length

    def insertEnd(self, value):
        self.arr.append = value
        self.length += 1
    def removeEnd(self):
        self.arr.pop()
        self.length -= 1
    def insertMiddle(self, index, value):
        self.arr.append(self.arr[-1])
        self.length += 1
        for i in range(self.length -1, index-1, -1):
            self.arr[i] = self.arr[i - 1]
        self.arr[index - 1] = value
        if self.length > self.capacity:
            print("error: capacity exceeded!")
        else:
            print(self.arr)
        self.length += 1

    def removeMiddle(self, index):
        self.arr.removeAt(index)

    def printArr(self):
        for i in self.arr:
            print(i)

# newArr = StaticArrays([0, 1, 2, 3, 4, 5, 6, 7, 8], 10,9 )
# newArr.insertMiddle(5, 20)
# array =[1,2,3,4,5]
# size = len(array)
# for index in range(0, 2 * size):
#      value = array[index % size]
#      print(value)

# print("val: ",3%4)
# new_ar = [0,1,2,3,4,5,6]
# def prefix_Sum(arr):
#     ps = [0]*(len(arr)+1)
#     for i in range(1, len(arr)):
#         ps[i+1] += arr[i] + ps[i]
#     return ps
#
# print(prefix_Sum(new_ar))
# from collections import deque
# q = deque()
# q.appendleft(1)
# q.appendleft(2)
# q.appendleft(3)
# print(q)
# s.append("one")
# s.append("two")
# s.append("three")
# s.append("four")
# s.pop()
# print(s)
# queue uses a loosely coupled producer consumer problem.
