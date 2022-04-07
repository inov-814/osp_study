#!/usr/bin/python

def aver():
    print("average numbers? ",end='')
    A = list(map(int,input().split()))
    total = 0
    for i in range(len(A)):
        total += A[i]
    average = total/len(A)
    print("result = {}".format(average))

if __name__ == '__main__':
    aver()
