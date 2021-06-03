#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решить индивидуальное задание 2 лабораторной работы 7,
# оформив каждую команду в виде отдельной функции.

import re
import json

def write():
      with open("t.json", 'w') as f:
         json.dump(p, f)
def read():
      with open("t.json", "r") as f:
        tx = json.load(f)
        text = re.compile(r'[.|!|?|…]')
        s = (filter(lambda y: y[0:1] == "-", [y.strip() for y in text.split(tx)]))
        print(sorted(s))

if __name__ == '__main__':
  p = input("Предложение для записи в словарь:")
  write()
  read()