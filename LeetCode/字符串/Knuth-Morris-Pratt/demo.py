def build_next(pattern):
    i = 0
    j = 1
    next = [0] * len(pattern)
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
            next[j] = i
            j += 1
        else:
            if i > 0:
                i = next[i - 1]
            else:
                next[j] = 0
                j += 1

    return next

def kmp_search(text, pattern):
    if not pattern:
        return 0

    next = build_next(pattern)
    i = j = 0
    m, n = len(text), len(pattern)

    while i < m:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == n:
            return i - j 
        elif i < m and text[i] != pattern[j]:
            if j > 0:
                j = next[j - 1]
            else:
                i += 1

    return -1

if __name__ == '__main__':
    text = "BBC ABCDAB ABCDABCDABDE"
    pattern = 'ABCDABD'
    print(kmp_search(text, pattern))
