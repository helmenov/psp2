# coding: utf-8
from k01 import harada_myfunc as my

x = (1,10) # 0.1
y = (1,5)  # 0.2

z1 = my.Frac_add(x,y)
z2 = my.Frac_sub(x,y)
z3 = my.Frac_mul(x,y)
z4 = my.Frac_dev(x,y)

print(f'{x}+{y}={z1}')
print(f'{x}-{y}={z2}')
print(f'{x}*{y}={z3}')
print(f'{x}/{y}={z4}')
