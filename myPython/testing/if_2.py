nums = [1, 5, 7, 11, 16, 18]
array1 = []
for num in nums:
    if num < 5:
        array1.append(num-1)
    elif num > 15:
        array1.append(num+1)
    else:
        array1.append(num)

array2 = [{num<5: num-1, num>15: num+1}.get(True, num) for num in nums]

print(array1, array2, sep="\n")