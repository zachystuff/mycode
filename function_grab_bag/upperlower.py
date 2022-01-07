def countupperlower(word: str):
    upper = 0
    lower = 0
    for letter in word:
        if letter.isupper():
            upper += 1
        else:
            lower += 1

