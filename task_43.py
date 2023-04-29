"""
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:        Вывод:
1 2 3 2 3    2
"""
import random
N = int(input("Введите количество элементов массива: "))

def CreateArray(n):
    array = []
    for i in range(n):
        array.append(random.randint(-10, 10))
    return array

def QualityPairs(array):
    count = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                count+=1
    return count

array = CreateArray(N)
print(array)
print(QualityPairs(array))
