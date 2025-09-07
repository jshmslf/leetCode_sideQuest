def longestCommonPrefix(strs: list[str]) -> str:
    res = ""

    for i in range(len(strs[0])):                   # strs[0] -> flower, len(flower) -> 6, range(6)
        for word in strs:                              # in letters in flowers
            if i == len(word) or word[i] != strs[0][i]:   # if i reach the length of s which is 6 OR s[i]=f is not equat to strs[0][i]
                return res
        res += strs[0][i]

    return res


print(longestCommonPrefix(["flower", "flow", "flight"]))

"""
[flower, flow, flight]

flower
^
flow
^


"""