def romanToInt(s: str) -> int:
    convertion = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }

    res = 0

    for i in range(len(s)):
        print("s[i]: ",convertion[s[i]], end=", total: ")
        if i + 1 < len(s) and convertion[s[i]] < convertion[s[i+1]]:
            res -= convertion[s[i]]
        else:
            res += convertion[s[i]]
        print(res)
    return res

test = "IVIVIV"

print(romanToInt(test))

"""
IV
len = 2
range = 2, -> 0, 1

"""