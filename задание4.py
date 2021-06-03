#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. Функция getInput() не имеет параметров, запрашивает ввод с клавиатуры и возвращает
# в основную программу полученную строку.
# 2. Функция testInput() имеет один параметр. В теле она проверяет, можно ли переданное
# ей значение преобразовать к целому числу. Если можно, возвращает логическое True.
# Если нельзя – False.
# 3. Функция strToInt() имеет один параметр. В теле преобразовывает переданное значение
# к целочисленному типу. Возвращает полученное число.
# 4. Функция printInt() имеет один параметр. Она выводит переданное значение на экран и
# ничего не возвращает.

if __name__ == '__main__':
 def getinput():
    return(input('Введите число: '))
 def testinput(n):
    try:
        n = int(n); return True
    except: return False
 def strtoint(n):
     return(int(n))
 def printint(n):
     print(n)
 n = getinput()
 isintable = testinput(n)
 if isintable:
     printint(strtoint(n))
 else:
     print("Введенное число не целое")