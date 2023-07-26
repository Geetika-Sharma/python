nums = [54, 22, 40, 490, 127817, 99]

evens = []

for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens)

## List comprehension way

evenList = [ num for num in nums if num %2 == 0]
print(evenList)