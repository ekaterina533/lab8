#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Решите следующую задачу: напишите функцию, которая считывает с клавиатуры числа и
# перемножает их до тех пор, пока не будет введен 0. Функция должна возвращать
# полученное произведение. Вызовите функцию и выведите на экран результат ее работы.

if __name__ == '__main__':
  def test():
    a = 1
    n = 1
    while n!=0:
      a *= n
      n = int(input("Введите число: "))
    print("Произведение чисел:", a)
  test()
