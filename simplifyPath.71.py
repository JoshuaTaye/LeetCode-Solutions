from collections import deque


def simplifyPath(x):
    stack = deque()
    stack.append("/")
    path = x.split("/")
    while "" in path:
        path.remove("")
    absolute = ""
    for i in range(len(path)):
        if path[i] == "..":
            if stack[-1] != "/":
                stack.pop()
        elif path[i] == ".":
            continue
        else:
            stack.append(path[i])
    print(stack)
    for i in range(len(stack)):
        if stack[i] == "/":
            absolute += "/"
        else:
            absolute += stack[i] + "/"
    if len(absolute) > 1:
        absolute = absolute[:-1]
    return absolute
print(simplifyPath("/../"))