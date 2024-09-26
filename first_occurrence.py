def strStr(haystack='', needle=''):
    if needle in haystack:
        print(haystack.find(needle))
    else:
        print(-1)


haystack = "butsad"

needle = "sad"

strStr(haystack, needle)

    