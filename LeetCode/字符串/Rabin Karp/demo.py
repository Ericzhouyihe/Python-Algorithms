BASE = 256
MOD = 10**9 + 7

def compute_hash(str):
    h = 0
    for ch in str:
        h = (h * BASE + ord(ch)) % MOD
    return h

def rabinKarp(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0 or n < m:
        return -1

    pattern_hash = compute_hash(pattern)
    window_hash = compute_hash(text[:m])

    # 预先计算
    power = pow(BASE, m - 1, MOD)

    for i in range(n - m + 1):
        # 检查哈希是否匹配
        if window_hash == pattern_hash:
            # 必须逐字符验证，避免碰撞
            if text[i : i + m] == pattern:
                return i

        # 如果不是最后一个窗口，滚动哈希
        if i < n - m:
            window_hash = ((window_hash - ord(text[i]) * power) * BASE + ord(text[i + m])) % MOD

    return -1

def list_rabinKarp(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0 or n < m:
        return []

    pattern_hash = compute_hash(pattern)
    window_hash = compute_hash(text[:m])

    # 预先计算
    power = pow(BASE, m - 1, MOD)
    match = []

    for i in range(n - m + 1):
        if pattern_hash == window_hash and text[i:i + m] == pattern:
            match.append(i)
            
        # 不是最后一个窗口
        if i < n - m:
            window_hash = ((window_hash - ord(text[i]) * power) * BASE + ord(text[i + m])) % MOD

    return match

if __name__ == '__main__':
    text = "hello worldhello world"
    pattern = 'world'
    print(rabinKarp(text, pattern))
    print(list_rabinKarp(text, pattern))
