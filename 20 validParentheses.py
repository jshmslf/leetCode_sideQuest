def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
    }

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
        
    return True if not stack else False



print(isValid("()()()()(((())))"))


"""
s -> ([])
stack

for c in s -> c = [ '(', '[', ']', ')' ]
                          ^

1st step:
    c = [ '(', '[', ']', ')' ]
           ^

    c => '('
    is not closing
    c => '(' append 
    stack[ '(' ]

2nd step:
    c = [ '(', '[', ']', ')' ]
                ^

    c => '['
    is not closing
    c => '[' append
    stack[ '(', '[', ]

3rd step:
    c = [ '(', '[', ']', ')' ]
                     ^

    c => ']'
    is closing
    stack[-1] / '[' && closeToOpen[']'] => [ and since they are equal, stack.pop!
    



"""