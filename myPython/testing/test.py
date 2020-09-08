def sum(x):
    return x * 2
        
list1 = [1, 2, 3, 4]
#1
print(map(sum, list1))
#2
print([sum(num) for num in list1])