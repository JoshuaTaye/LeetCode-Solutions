class LinkedList:
    def __init__(self, gno = 0, nxt= None):
        self.data = gno
        self.next = nxt

best_class = LinkedList(2 )
first_class = LinkedList(1)
third_class = LinkedList(3)
fourth_class = LinkedList(4)

best_class.next = first_class
first_class.next = third_class
third_class.next = fourth_class

curr = best_class
arr = []
while curr:
    print(curr.data)
    arr.append(curr.data)
    curr = curr.next
print(arr)

