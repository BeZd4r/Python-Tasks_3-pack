from random import randint

lst = [randint(-100,100) for _ in range(100)]

print(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] > lst[j]:
            num = lst[j]
            lst[j] = lst[i]
            lst[i] = num
print(lst)


