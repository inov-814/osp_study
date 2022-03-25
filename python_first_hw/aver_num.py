#!/usr/bin/python

n = int(input("몇 개의 숫자를 입력? : "))
print("{}개의 숫자를 입력하세요".format(n))
A = list(map(int,input().split()))
print("{}개의 숫자의 합 : ".format(n),end = '')
total = 0
for i in range(n):
    total += A[i]
print(total)
average = total/n
print("{}개의 숫자의 평균 : {}".format(n,average))