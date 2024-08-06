def fillingBookcaseShelves(books, shelfWidth):
    height = 0
    currentHeight = 0
    currentWidth = 0
    print(books)
    for i in range(len(books)):
        if books[i][1] > currentHeight:
            currentHeight = books[i][1]
        if books[i][0] + currentWidth <= shelfWidth:
            currentWidth += books[i][0]
        else:
            print(currentWidth, currentHeight)
            height += currentHeight
            currentWidth = books[i][0]
            currentHeight = books[i][1]
    height += currentHeight
    return height


print(fillingBookcaseShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
