def valid(st):
    st = st.strip('"')
    # par = 0
    # square = 0
    # curly = 0
    # inner = False
    lst = list(st)
    j = 0
    while j < (len(lst) -1):
        if (lst[j] == '[' and lst[j+1] == ']') or (lst[j] == '(' and lst[j+1] == ')') or (lst[j] == '{' and lst[j+1] == '}'):
            del lst[j+1]
            del lst[j]
            # print('progress', lst)
            j = 0
            continue
        j += 1
    # print(lst)
    if len(lst) == 0:
        return True
    else: return False
    # for i in st:
    #     if i == '(':
    #         if square or curly:
    #             inner = True
    #         par += 1
    #     elif i == ')':
    #         if inner and not (square or curly):
    #             par -= 1
    #     elif i == '{':
    #         curly += 1   
    #     elif i == '}':
    #         if not (square or par):
    #             curly -= 1    
    #     elif i == '[':
    #         square += 1
    #     elif i == ']':
    #         if not (par or curly):
    #             square -= 1        
    # if par or square or curly:
    #     return False
    # return True
#     print()
stri = input()
print(valid(stri))
 
