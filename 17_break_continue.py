arr = [1,2,3,4,5,6,7,8,9,10]

for i in arr:
    if i % 3 == 0:
        break
    print(i)

for i in arr:
    if i % 3 == 0:
        continue
    print(i)