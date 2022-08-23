#1042
"""PROBLEM:
1042 - Simple Sort
ANSWER:
Accepted
LANGUAGE:
Python 3.4 (Python 3.4.3) [+1s]
RUNTIME:
0.064s
FILE SIZE:
141 Bytes
MEMORY:
-
SUBMISSION:
5/29/22, 9:37:23 PM"""
x,y,z=map(int,input().split())
lvalu= [x,y,z]
lvalu.sort()
print("%d\n%d\n%d"%(lvalu[0],lvalu[1],lvalu[2]))
print("\n%d\n%d\n%d"%(x,y,z))