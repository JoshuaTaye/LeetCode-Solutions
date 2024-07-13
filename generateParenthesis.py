def generateParenthesis(n):
    lst=[]
    for i in range(n):
        s = ''
        for j in range(i):
            s += '('
        for j in range(i):
            s += ')'
        for j in range(n - i):
            s += '('
        for j in range(n - i):
            s += ')'
        lst.append(s)
    print(lst)
num = int(input())
generateParenthesis(num)