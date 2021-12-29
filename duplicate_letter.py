def removedup(string1):
    new = ""
    for ch in string1:
        if ch not in new:
            new = new + ch
    print(new)


removedup("helllooo")
