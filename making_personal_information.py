def making_personal_information(s):
    if "@" in s:
        lst = s.split("@")
        lst[0] = lst[0][0].lower() + "*" * 5 + lst[0][-1].lower() + "@" + lst[1].lower()
        return "".join(lst)
    lst = list(s)
    for i in lst:
        if not i.isalnum():
            lst.remove(i)
    if len(lst) == 10:
        print("nananba")
        return "***-***-" + "".join(lst[-4:])
    elif len(lst) == 11:
        return "+*-***-***-" + "".join(lst[-4:])
    elif len(lst) == 12:
        return "+**-***-***-" + "".join(lst[-4:])
    else:
        return "+***-***-***-" + "".join(lst[-4:])





print(making_personal_information("1(234)567-890"))