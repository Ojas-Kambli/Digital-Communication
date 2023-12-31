# -*- coding: utf-8 -*-
"""Copy of DC Exp 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttTKTCrQ-bOa8R4_X7iDh__ajAk2D6ux
"""

import numpy as np

M=np.array([1,0,1,1,0,1])
print("The message is : ",M)
Mx=np.poly1d(M)
print("The message polynomial is :\n",Mx)

d=np.array([1,0,1,1])
print("The generator is : ",d)

L=len(d)
print("The length of the generator is : ",L)

dx=np.poly1d(d)
print("The generator polynomial :\n",dx)

t=np.zeros((L,))
t[0]=1
tx=np.poly1d(t)
aMx=np.polymul(Mx,tx)
print("The shifted message is :\n",aMx)

qx,rx=np.polydiv(aMx,dx)
r=rx.c%2
print("The parity bits are : ",r)

lc=len(M)+L-1
c=np.zeros((lc))
for i in range(len(M)):
  c[i]=M[i]
lr=len(r)
for i in range(lr):
  c[(lc-1)-i]=r[(lr-1)-i]
print("The codeword is : ",c)

R=c
loc=4
R[loc]=int(not R[loc])
Rx=np.poly1d(R)
print("The received message is : ",R)
print("The received polynomial is :\n",Rx)

Qx,Rex=np.polydiv(Rx,dx)
Re=Rex.c%2
print(Re)
f=0
for i in Re:
  if i!=0:
    f+=1
if f==0:
  print("No error detected")
else:
  print("Error detected")