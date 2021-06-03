#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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