# T: 文本串，p: 模式串，d: 字符集大小（基数），q: 模数（质数）
def rabinKarp(T: str, p: str, d: int, q: int) -> int:
    n, m = len(T), len(p)
    if m == 0:
        return 0
    if n < m:
        return -1

    hash_p, hash_t = 0, 0

    # 计算 H(p) 与首个子串的哈希
    for i in range(m):
        hash_p = (hash_p * d + ord(p[i])) % q
        hash_t = (hash_t * d + ord(T[i])) % q

    # 使用 pow 的三参形式避免中间溢出
    power = pow(d, m - 1, q)  # d^(m-1) % q，用于移除最高位字符

    for i in range(n - m + 1):
        if hash_p == hash_t:
            # 避免冲突：逐字符核验
            match = True
            for j in range(m):
                if T[i + j] != p[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            # 滚动更新到下一个子串
            hash_t = (hash_t - power * ord(T[i])) % q  # 去掉最高位字符
            hash_t = (hash_t * d + ord(T[i + m])) % q  # 加入新字符

    return -1
