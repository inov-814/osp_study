#!/usr/bin/python
from my_pkg.aver_num import *
from my_pkg.fibo_num import *

while True:
    menu = int(input("Select menu: 1) average 2) fibonacci 3) exit ? "))
    if menu == 3:
        print("exit the program...")
        print()
        exit(0)
    elif menu == 1:
        aver()
    elif menu == 2:
        fibo()
    else:
        print("wrong menu")
    print()
