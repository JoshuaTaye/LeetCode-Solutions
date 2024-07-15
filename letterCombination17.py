def letter_combinations(nums):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    combinations = []
    for num in nums:
        num = int(num)
        i = ((num - 2) * 3) + 1
        if num == 7:
            st = alphabet[i - 1: i + 3]
        elif num == 9:
            st = alphabet[i: i + 4]
        elif num == 8:
            st = alphabet[i: i + 3]
        else:
            st = alphabet[i - 1:i + 2]
        letters.append(st)
    product = 1
    for i in range(len(letters)):
        product *= len(letters[i])
    for i in range(len(letters)):
        for k in range(len(letters[i])):
            word = ''
            for j in range(len(letters)):
                word += letters[j][k]
            combinations.append(word)
    return combinations


digits = "23"
print(letter_combinations(digits))
