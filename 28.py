def strStr(haystack: str, needle: str) -> int:
    if haystack == "":
        return 0
    
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i: i + len(needle)] == needle:
            return i
        
    return -1


print(strStr("butsad", "sad"))

# return what array start the matches w/ needle