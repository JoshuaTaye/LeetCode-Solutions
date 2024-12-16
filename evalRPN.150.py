from collections import deque


def evalRpn(tokens):
    # value = int(tokens[0])
    stack = deque()
    # stack.append(value)
    operations = ["+","-","/", "*"]
    for i in range(len(tokens)):
        if tokens[i] not in operations :
            stack.append(int(tokens[i]))
        else:
            if tokens[i] == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x + y)
                print(stack, x, y)
            if tokens[i] == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x * y)
                print(stack, x, y)

            if tokens[i] == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
                print(stack, x, y)

            if tokens[i] == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y / x))
                print(stack, x, y)
    return stack[0]
print(evalRpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))