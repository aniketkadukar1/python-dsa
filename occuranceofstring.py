def strStr( haystack: str, needle: str) -> int:
        j, res = 0, 0
        if needle not in haystack:
             return -1
        if haystack[i] == needle[j]:
             j, res = 0, 0
        for i in range(len(haystack)):
            if j < len(needle) and haystack[i] == needle[j]:
                j +=1
                res = i + 1
        res = res - j

        return res 

haystack = "bbbbababbbaabbba"
needle = "abb"

print(strStr(haystack, needle))