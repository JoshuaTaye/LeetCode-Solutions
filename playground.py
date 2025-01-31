# #
# #
# # #
# # # Bubble Sort
# # def bubble_sort(arr):
# #     for i in range(len(arr)):
# #         for j in range(len(arr) - i - 1):
# #             if arr[j] > arr[j + 1]:
# #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# #     return arr
# #
# #
# # #
# # #
# # # Selection Sort
# # def selection_sort(arr):
# #     for i in range(len(arr)):
# #         minIndex = i
# #         for j in range(i + 1, len(arr)):
# #             if arr[j] < arr[minIndex]:
# #                 minIndex = j
# #         arr[i], arr[minIndex] = arr[minIndex], arr[i]
# #     return arr
# #
# #
# # #
# # #
# # # Insertion Sort
# # def insertion_sort(arr):
# #     for i in range(1, len(arr)):
# #         for j in range(i - 1, -1, -1):
# #             if arr[j] > arr[j + 1]:
# #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# #     print(arr)
# #
# #
# # # Counting Sort
# # def counting_sort(arr):
# #     newArr = [0] * (max(arr) + 1)
# #     for i in arr:
# #         newArr[i] += 1
# #     ind = 0
# #     for i in range(len(newArr)):
# #         if newArr[i] > 0:
# #             for k in range(newArr[i]):
# #                 arr[ind] = i
# #                 ind += 1
# #     print(arr)
# #
# #
# # def counting_search_with_negative(arr):
# #     minElt = min(arr)
# #     newArr = [0] * (max(arr) - min(arr) + 1)
# #     for i in arr:
# #         newArr[i + abs(minElt)] += 1
# #     print(newArr)
# #     ind = 0
# #     for i in range(len(newArr)):
# #         if newArr[i] > 0:
# #             for k in range(newArr[i]):
# #                 arr[ind] = i - abs(minElt)
# #                 ind += 1
# #     print(arr)
# #
# #
# # # ar = [-12, -5, -4, -4, 2, 2, 2, 3, 4, 6]
# # def binary_search_recursion(arr, x):
# #     print("here")
# #     md = len(arr) // 2
# #     if len(arr) == 1 and arr[0] != x:
# #         return -1
# #     elif arr[md] == x:
# #         return "Found"
# #     elif arr[md] > x:
# #         return binary_search_recursion(arr[:md], x)
# #     else:
# #         return binary_search_recursion(arr[md:], x)
# #
# #
# # # print(binary_search_recursion(ar, 6))
# #
# # def binary_search(ar, x):
# #     l = 0
# #     r = len(ar) - 1
# #     while l <= r:
# #         print("here")
# #         m = l + (r - l) // 2
# #         if x == ar[m]:
# #             return "Found"
# #         elif x < ar[m]:
# #             r = m
# #         else:
# #             l = m + 1
# #     return -1
# #
# #
# # # print(binary_search(ar, -12))
# #
# # # Two Pointers parallel pointers
# # def is_sorted(ar):
# #     left = 0
# #     right = 1
# #     while right < len(ar):
# #         if ar[left] > ar[right]:
# #             return False
# #         left += 1
# #         right += 1
# #     return True
# #
# #
# # # print(is_sorted(ar))
# #
# # ar1 = [-4, -5, 1, 2, 4, 12, 12, 16]
# # ar2 = [-10, -1, 0, 3, 4, 5, 12, 12, 12, 16]
# #
# #
# # # separate array pointers
# # def merge(ar1, ar2):
# #     arf = []
# #     p1, p2 = 0, 0
# #     while p1 < len(ar1) and p2 < len(ar2):
# #         if ar1[p1] < ar2[p2]:
# #             arf.append(ar1[p1])
# #             p1 += 1
# #         elif ar1[p1] >= ar2[p2]:
# #             arf.append(ar2[p2])
# #             p2 += 1
# #     return arf
# #
# #
# # # print(merge(ar1, ar2))
# #
# # # colliding pointers
# # def colliding_window(ar):
# #     n = 13
# #     l = 0
# #     r = len(ar) - 1
# #     while l <= r:
# #         if ar[r] + ar[l] < n:
# #             l += 1
# #         elif ar[r] + ar[l] > n:
# #             r -= 1
# #         else:
# #             return l, r
# #
# #
# # # print(colliding_window(ar1))
# #
# # # ar = [4, 0, 0, 1, 3]
# #
# #
# # # Seeker and Placeholder
# # def seeker_and_placeholder(ar):
# #     checker = 0
# #     next = 0
# #     while checker < len(ar):
# #         if ar[checker] != 0:
# #             ar[checker], ar[next] = ar[next], ar[checker]
# #             next += 1
# #             checker += 1
# #         else:
# #             checker += 1
# #     return ar
# #
# # # print(seeker_and_placeholder(ar))
# #
# # # for-while combo
# # ar11 = [2,2,5,6]
# # ar22 = [3,4,6,12]
# # def for_while(ar1, ar2):
# #     ind = 0
# #     ind2 = 0
# #     elts = [0] * len(ar2)
# #     while ind < len(ar2):
# #         while ind2 < len(ar1):
# #             print(elts)
# #             if ar1[ind2] >= ar2[ind]:
# #                 elts[ind] = ind2
# #                 break
# #             ind2 += 1
# #         ind += 1
# #     elts[-1] = ind2
# #     return elts
# #
# # # print(for_while(ar11, ar22))
# # arv = [-4, -5, 3, 2, 4, -4, -12, 2, 2, 6]
# # #sliding window
# # def maximumSum(ar, k):
# #     left = 0
# #     right = left + k
# #     summ = 0
# #     for i in range(k):
# #         summ += ar[i]
# #     # print(summ)
# #     maxSum = 0
# #     while right < len(ar):
# #         print(summ, summ - ar[left] + ar[right])
# #         summ = summ - ar[left] + ar[right]
# #         maxSum = max(summ, maxSum)
# #         # print(maxSum)
# #         left += 1
# #         right += 1
# #     return maxSum
# # # print(maximumSum(arv, 4))
# #
# # ar_2d = [[-4, -5, 3, 2, 4, -4, -12, 2, 2, 6], [-10, -1, 0, 3, 4, 5, 12, 12, 12, 16],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# #
# # def two_d_max(ar, k):
# #     top = 0
# #     bottom = top + k[0]
# #     maxSum = 0
# #     while bottom <= len(ar):
# #         summ = 0
# #         for i in range(top, bottom):
# #             for j in range(0, k[1]):
# #                 summ += ar[i][j]
# #         left = 0
# #         right = left + k[1]
# #         while right < len(ar[1]):
# #             for i in range(top, bottom):
# #                 summ = summ - ar[i][left] + ar[i][right]
# #             maxSum = max(maxSum, summ)
# #             left += 1
# #             right += 1
# #         top += 1
# #         bottom += 1
# #     return maxSum
# # # print(two_d_max(ar_2d, [2,4]))
# #
# # def anagrams(s, p):
# #     t_mapp, an, mapp, left, right = [], 0, [], 0, len(p)
# #     while right <= len(s):
# #         if sorted(s[left:right]) == sorted(p):
# #             an += 1
# #         left += 1
# #         right += 1
# #     return an
# #
# # print(anagrams("cbadabac", "abc"))
# #
# # def longest_unique_substring(s):
# #     left, right, arr, maxLen = 0, 0, [], 0
# #     while right < len(s):
# #         if s[right] in arr:
# #             arr.remove(arr[0])
# #         else:
# #             arr.append(s[right])
# #             left -= 1
# #         left += 1
# #         right += 1
# #         maxLen = max(maxLen, len(arr))
# #     return maxLen
# #
# # # print(longest_unique_substring("abebebcd"))
# #
# # class StaticArrays:
# #     def __init__(self, arr, capacity, length):
# #         self.arr = arr
# #         self.capacity = capacity
# #         self.length = length
# #
# #     def insertEnd(self, value):
# #         self.arr.append = value
# #         self.length += 1
# #     def removeEnd(self):
# #         self.arr.pop()
# #         self.length -= 1
# #     def insertMiddle(self, index, value):
# #         self.arr.append(self.arr[-1])
# #         self.length += 1
# #         for i in range(self.length -1, index-1, -1):
# #             self.arr[i] = self.arr[i - 1]
# #         self.arr[index - 1] = value
# #         if self.length > self.capacity:
# #             print("error: capacity exceeded!")
# #         else:
# #             print(self.arr)
# #         self.length += 1
# #
# #     def removeMiddle(self, index):
# #         self.arr.removeAt(index)
# #
# #     def printArr(self):
# #         for i in self.arr:
# #             print(i)
# #
# # # newArr = StaticArrays([0, 1, 2, 3, 4, 5, 6, 7, 8], 10,9 )
# # # newArr.insertMiddle(5, 20)
# # # array =[1,2,3,4,5]
# # # size = len(array)
# # # for index in range(0, 2 * size):
# # #      value = array[index % size]
# # #      print(value)
# #
# # # print("val: ",3%4)
# # # new_ar = [0,1,2,3,4,5,6]
# # # def prefix_Sum(arr):
# # #     ps = [0]*(len(arr)+1)
# # #     for i in range(1, len(arr)):
# # #         ps[i+1] += arr[i] + ps[i]
# # #     return ps
# # #
# # # print(prefix_Sum(new_ar))
# # # from collections import deque
# # # q = deque()
# # # q.appendleft(1)
# # # q.appendleft(2)
# # # q.appendleft(3)
# # # print(q)
# # # s.append("one")
# # # s.append("two")
# # # s.append("three")
# # # s.append("four")
# # # s.pop()
# # # print(s)
# # # queue uses a loosely coupled producer consumer problem.
# #
# #
# # def bubbleSort(arr):
# #     for i in range(len(arr)):
# #         for j in range(i, len(arr)):
# #             if arr[j] < arr[i]:
# #                 arr[j], arr[i] = arr[i], arr[j]
# #     return arr
# #
# # # print(bubbleSort(arr))
# #
# from collections import deque
#
#
# #
# # ar = [5,43 ,4, 45, 4, 34, 56634, 5435, 1]
# # def selectionSort(arr):
# #     start = 0
# #     while start < len(arr):
# #         minn = float("inf")
# #         for i in range(start, len(arr)):
# #             if arr[i] < minn:
# #                 minIndex = i
# #                 minn = arr[i]
# #         arr[start], arr[minIndex] = arr[minIndex], arr[start]
# #         start += 1
# #     return arr
# # # print(selectionSort(ar))
# #
# # def mergeSortedArrays(arr1, arr2):
# #     p1 = 0
# #     p2 = 0
# #     newArr = []
# #     while p1 < len(arr1) and p2 < len(arr2):
# #         if arr1[p1] <= arr2[p2]:
# #             newArr.append(arr1[p1])
# #             p1 += 1
# #         elif arr1[p1] > arr2[p2]:
# #             newArr.append(arr2[p2])
# #             p2 += 1
# #     while p1 < len(arr1):
# #         newArr.append(arr1[p1])
# #         p1 +=1
# #     while p2 < len(arr2):
# #         newArr.append(arr2[p2])
# #         p2 +=1
# #
# #     # print(arr1[p1], arr2[p2])
# #     return newArr
# #
# # # print(mergeSortedArrays([10,15,22,80],[5,8,11,15,70,90, 100, 110]))
# #
# # def addToANumber(arr, t):
# #     l = 0
# #     r = len(arr) - 1
# #     while l < r < len(arr):
# #         add = arr[l] + arr[r]
# #         if add == t:
# #             return [l, r]
# #         if add < t:
# #             l += 1
# #         else:
# #             r -= 1
# #     return -1
# #
# #
# # # print(addToANumber([5,8,11,15,70,90, 100, 110], 101))
# #
# # def groupElements(arr):
# #     placer = 0
# #     for  seeker in range(1, len(arr)):
# #         if arr[seeker] != 0:
# #             arr[seeker], arr[placer] = arr[placer], arr[seeker]
# #             placer += 1
# #     return arr
# #
# # # print(groupElements([0,4,0,1,3]))
# #
# # def checkLess(arr1, arr2):
# #     p2 = 0
# #     p1 = 0
# #     ar = []
# #     num = 0
# #     while p2 < len(arr2):
# #         while p1 < len(arr1):
# #             if arr1[p1] >= arr2[p2]:
# #                 break
# #             num += 1
# #             p1 += 1
# #         ar.append(num)
# #         p2 += 1
# #     return ar
# #
# #
# #
# # # print(checkLess([10,15,22,80],[5,8,11,15,70,90, 100, 110]))
# #
# # def longestSubstring(s):
# #     left = 0
# #     right = 0
# #     maxLen = 0
# #     sub = ""
# #     while left <= right < len(s):
# #         if s[right] not in sub:
# #             sub += s[right]
# #             maxLen = max(maxLen, right-left + 1)
# #             right += 1
# #         else:
# #             left += 1
# #             sub = sub[1:]
# #         print(sub)
# #     return maxLen
# # # print(longestSubstring("abcbad"))
#
# def selectionSort(ar):
#     start = 0
#     minn = float("inf")
#     while start < len(ar):
#         curI = start
#         for i in range(start, len(ar)):
#             if ar[i] < minn:
#                 minn = ar[i]
#                 curI = i
#         ar[start], ar[curI] = ar[curI], ar[start]
#         start += 1
#     return ar
#
# # print(selectionSort(ar))
#
# def insertionSort(ar):
#     for i in range(1, len(ar)):
#         for j in range(i-1, -1, -1):
#             if ar[j] > ar[j+1]:
#                 ar[j], ar[j+1] = ar[j+1], ar[j]
#     return ar
#
# # print(insertionSort(ar))
#
# # def insertion_sort(arr):
# #     for i in range(1, len(arr)):
# #         for j in range(i - 1, -1, -1):
# #             if arr[j] > arr[j + 1]:
# #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# #     print(arr)
#
# # def insertionSort(arr):
# #     index = 1
# #     while index < len(arr):
# #         for l in range(index-1, -1, -1):
# #             if arr[index] < arr[l]:
# #                 arr[index], arr[l] = arr[l], arr[index]
# #                 index -= 1
# #         index += 1
# #     return arr
# #
# # print(insertionSort(ar))
#
# def isPalindrome(st):
#     q = deque()
#     for i in range(len(st)):
#         if st[i] not in q:
#             q.append(st[i])
#         else:
#             q.remove(st[i])
#     if len(q) <= 1:
#         return True
#     return False
#
# # print(isPalindrome("maisanunasiam"))
#
# def countSubstringsSameStartAndEnd(st):
#     l = 0
#     res = len(st)
#     while l < len(st):
#         r = l + 1
#         while r < len(st):
#             if st[l] == st[r]:
#                 res += 1
#             r += 1
#         l += 1
#     return res
# # print(countSubstringsSameStartAndEnd("zzzz"))
#
# # ar = [10, 4, 5, 3, 2, 4, 4, 12, 2, 2, 6]
#
# ar = [10, 4, -5, 3, 2, 4, -4, -12, 2, 2, 6]
# def countingSort(ar):
#     minn = abs(min(ar))
#     newAr = [0] * (max(ar) +minn+1)
#     for i in ar:
#         newAr[i+minn] += 1
#     ind = 0
#     for i in range(len(newAr)):
#         if newAr[i] > 0:
#             for j in range(newAr[i]):
#                 ar[ind] = i-minn
#                 ind += 1
#     return ar
# # print(countingSort(ar))
#
# x = [1, 1, 1, 1, 1]
# ps = [0]
# for i in range(len(x)):
#     ps.append(x[i] + ps[i])
# print(ps)


# def swap_case(l):
#     s = list(l)
#     for i in range(len(l)):
#         if s[i].upper() == s[i]:
#             s[i] = s[i].lower()
#         elif s[i].lower() == s[i]:
#             s[i] = s[i].upper()
#     return "".join(s)
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


