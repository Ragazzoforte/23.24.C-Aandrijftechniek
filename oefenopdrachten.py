import math as mp

PI = 3.14

A = 80/(10**6)
l_tot=0.4
mu_ijzer = 1000
mu_0 = (4*PI)/(10**7)
N=22000
I=12*10**-3
delta=0.15*10**-2

R_lucht = (delta)/(mu_0*A)
R_ijzer = (l_tot-delta)/(mu_0*mu_ijzer*A)
R_tot = R_lucht+R_ijzer

flux= N*I/R_tot
B = flux/A
H_ijzer = B/(mu_0*mu_ijzer)
H_lucht = B/(mu_0)

print(R_lucht,R_ijzer)
print("Reluctantie:",R_tot)
print("Flux:",flux)
print("Fluxdichtheid:",B)
print("Veldsterkte ijzer:",H_ijzer)
print("Veldsterkte lucht:",H_lucht)