def removeComments(source):
    i = 0
    j = 0
    while j < len(source):
        j += 1
    while i < len(source):
        source[i] = source[i].strip(" ")
        if (source[i][:2] == "//") or (source[i][:2] == "/*" and source[i][-2:] == "*/"):
            source.remove(source[i])
            i += 1
        elif source[i][:2] == "/*":
            source[i] = source[i].strip(" ")
            while i < len(source) and source[i][-2:] != "*/":
                source.remove(source[i])
            if source[i][-2:] == "*/":
                source.remove(source[i])
                i += 1
        else:
            i += 1
    return source

print(removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))