def generate(cur, open, closed, n):
    """Correct braces structure"""
    if len(cur) == 2*n:
        print(cur)
        return
    if open < n:
        generate(cur + '(', open + 1, closed, n)
    if closed < open:
        generate(cur + ')', open, closed + 1, n)


def parens(n):
    generate('', 0, 0, n)


def is_palindrom(st):
    i = 0
    j = -1
    while i < len(st) + j:
        if not st[i].isalpha():
            i += 1
            continue
        if not st[j].isalpha():
            j -= 1
            continue
        if st[i].lower() != st[j].lower():
            return False
        i += 1
        j -= 1
    return True
