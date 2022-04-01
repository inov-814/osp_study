#!/usr/bin/python

def fibo():
    n = int(input("몇개의 피보나치 수를 생성? : "))
    frt = 1
    bck = 1
    fibo = []
    fibo.append(frt)
    if (n != 1):
        fibo.append(bck)
    if n > 2:
        for i in range(n-2):
            frt, bck = bck, frt+bck
            fibo.append(bck)
    print(",".join(map(str, fibo)))
    print("F{} = {}".format(n,fibo[n-1]))

if __name__ == '__main__':
    fibo()