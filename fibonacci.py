times = int(input("How many fibbonaci numbers? > "))

arr = [0, 1]
for rep in range(times - 1):
    if rep != 0:
        arr.append(arr[rep] + arr[rep - 1])

print(str(arr).replace("[", "").replace("]", ""))