#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решить индивидуальное задание 2 лабораторной работы 7,
# оформив каждую команду в виде отдельной функции.

import re
import json

import sys

if __name__ == '__main__':

    def addtobase():
        name = input("Фамилия, Имя? ")
        number = input("Номер телефона? ")
        print("Дата рождения:")
        day = input("День")
        month = input("Месяц")
        year = input("Год")
        bases = {
            'name': name,
            'number': number,
            'day': day,
            'month': month,
            'year': year
        }
        base.append(bases)
    def sortbase():
        if len(base) > 1:
            base.sort(key=lambda item: item.get('name', ''))

    def formatbase():
     line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
     )
     print(line)
     print(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "№",
            "Ф.И.",
            "Номер телефона",
            "Дата рождения"
        )
     )
     print(line)
     for idx, bases in enumerate(base, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                bases.get('name', ''),
                bases.get('number', ''),
                bases.get('month', 0)
            )
        )
     print(line)
    def selectbase():
        parts = command.split(' ', maxsplit=2)
        sel = (parts[1])
        count = 0
        for bases in base:
            if bases.get('month') == sel:
                count += 1
                print(
                    '{:>4}: {}'.format(count, bases.get('name', ''))
                )
        if count == 0:
            print("В этом месяце ни у кого нет дня рождения.")
    def read():
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'r') as f:
                base = json.load(f)
    def files():
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                json.dump(base, f)
    def helps():
        print("Список команд:\n")
        print("add - добавить работника;")
        print("list - вывести список работников;")
        print("select <месяц> - запросить людей, у которых в этом месяце день рождения;")
        print("help - отобразить справку;")
        print("exit - завершить работу с программой.")
    def error():
        print(f"Неизвестная команда {command}", file=sys.stderr)

    base = []
    while True:
     command = input(">>> ").lower()
     if command == 'exit':
        break
     elif command == 'add':
        addtobase()
        sortbase()
     elif command == 'list':
        formatbase()
     elif command.startswith('select '):
         selectbase()
     elif command.startswith('load '):
         read()
     elif command.startswith('save '):
         files()
     elif command == 'help':
         helps()
     else:
        error()
