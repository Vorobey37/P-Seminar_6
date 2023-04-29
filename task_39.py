"""
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
"""
import random
N = int(input("Введите количество элементов первого массива: "))
M = int(input("Введите количество элементов первого массива: "))

def CreateArray(n):
    array = []
    for i in range(n):
        array.append(random.randint(-10, 10))
    return array

def DifferenceArray(array1, array2):
    array3 = []
    count = 0
    for i in array1:
        for j in array2:
            if i == j:
                count+=1
        if count == 0:
            array3.append(i)
        else:
            count = 0
    return array3

def DifferenceArray2(array1, array2):
    array3 = []
    #count = 0
    for i in array1:
        #count +=1
        if i in array2:
            pass
        else: 
            array3.append(i)
    return array3

firstArray = CreateArray(N)
secondArray = CreateArray(M)
print(firstArray)
print(secondArray)
finallyArray = DifferenceArray(firstArray, secondArray)
print(finallyArray)
finallyArray2 = DifferenceArray2(firstArray, secondArray)
print(finallyArray2)
