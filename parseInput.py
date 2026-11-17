def parseInput(s):
    specs = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
    ]
    lower,upper,special = False,False,False
    for x in s:
        if x.isalnum() and x == x.lower():
            lower = True
        if x.isalnum() and x == x.upper():
            upper = True
        if x in specs:
            special = True
    return lower,upper,special,len(s)