nums = [1,3,5,7,9,11,13,15,17,19]

# (1) 원래 형태 ..
array1 = []
for num in nums:
    if num != 0:
        if num < 10:
            array1.append(num-1)
        else:
            array1.append(num+1)

# (2) 축약형 !!
array2 = [num-1 if num < 10 else num+1 for num in nums if num != 0]

print(array1, array2, sep="\n")
# (1)번과 (2)번은 완전히 같은 것을 표현하고 있다
# 엄청난 기능이다!!!