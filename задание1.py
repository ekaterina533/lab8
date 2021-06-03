#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    def positive():
        print("Положительное")
    def negative():
        print("Отрицательное")
    def test():
        a = int(input())
        if a > 0:
            positive()
        elif a < 0:
            negative()
    test()