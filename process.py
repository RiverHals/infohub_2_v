import time
start = time.time()
for i in range(1000):
    print(i)
    time.sleep(1)
end = time.time()
print()
print(str(end - start))