def scoreOfParentheses(s):
    score = 0
    stack = []
    for i in range(len(s)):
        level = len(stack)
        if s[i] == "(":
            stack.append("(")
        else:
            score += level
            level -= 1
    return score
            