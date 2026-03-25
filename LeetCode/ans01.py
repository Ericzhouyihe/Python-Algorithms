import time


def fibo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibo(i - 1) + fibo(i - 2)


# 记录开始时间
start = time.time()

count = 1

while count < 100000:
    fibo(20)
    count += 1

print(fibo(20))

# 记录结束时间
end = time.time()
duration_ms = end - start

# 1277秒
print(f"程序运行时间：{duration_ms} 秒")
