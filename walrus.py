import time


def odd_num(nums):
    odds = [num for num in nums if num%2==1]
    time.sleep(1)
    return len(odds)

nums = [54, 22, 40, 490, 127817, 99]

t1 = time.time()
count=odd_num(nums)

if count > 1:
    print(count)
t2 = time.time()

print(f"Total time: {t2-t1} seconds")

## Walrus operator way
t3 = time.time()

if (n:=odd_num(nums)>1):
    print(n)

t4 = time.time()
print(f"Total time: {t4-t3} seconds")