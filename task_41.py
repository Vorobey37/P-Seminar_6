"""
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод:        Ввод:
5            5
1 2 3 4 5    1 5 1 5 1
Вывод:       Вывод:
0            2

"""
import random
N = int(input("Введите количество элементов первого массива: "))

def CreateArray(n):
    array = []
    for i in range(n):
        array.append(random.randint(-10, 10))
    return array

def Elements(array):
    count = 0
    for i in range(len(array)-1):
        if array[i] > array[i+1] and array[i] > array[i-1]:
            count+=1
    if array[len(array)-1] > array[len(array)-2] and array[len(array)-1] > array[0]:
        count+=1
    return count

array = CreateArray(N)
print(array)
print(Elements(array))
