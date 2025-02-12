def minMovesToSeat(seats, students):
    students.sort()
    seats.sort()
    res = 0
    for i in range(len(seats)):
        res += abs(students[i] - seats[i])
    return res


print(minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]))