def itr(n):
    l = len(str(n))
    lst = []
    x = str(n)
    for i in x:
        lst.append(int(i) * 10**(l-1))
        l -= 1
    print(lst)
    roman  = ''
    for i in range(len(lst)):
        if (lst[i] % 1000) == 0:
            while lst[i] != 0:
                roman += 'M'
                lst[i] -= 1000
            continue
        elif lst[i]  == 900:
            roman += 'CM'
            continue
        elif 500< lst[i] < 900:
            roman += 'D'
            for i in range(0, lst[i]-500, 100):
                roman += 'C' 
        elif lst[i] == 500:
            roman += 'D'
            continue
        elif lst[i] == 400:
            roman += 'CD'
            continue
        elif (lst[i]%100) == 0:
            while lst[i] != 0:
                roman += 'C'
                lst[i] -= 100
            continue
        elif lst[i] == 90:
            roman += 'XC'
            continue
        elif 50< lst[i] < 90:
            roman += 'L'
            for i in range(0, lst[i]-50, 10):
                roman += 'X' 
        elif lst[i] == 50:
            roman += 'L'
            continue
        elif lst[i] == 40:
            roman += 'XL'
            continue
        elif (lst[i]< 40) and (lst[i]%10) == 0:
            while lst[i] != 0:
                roman += 'X'
                lst[i] -= 10
            continue
        elif lst[i] == 5:
            roman += 'V'
            continue
        elif lst[i] == 4:
            roman += 'IV'
            continue
        elif lst[i] == 9:
            roman += 'IX'
            continue
        elif lst[i] <= 3:
            for j in range(lst[i]):
                roman += 'I'
            continue
        elif lst[-1] > 5:
            roman += 'V'
            for i in range(lst[-1]-5):
                roman += 'I'
            continue
    print(roman)
x = int(input())
itr(x)
