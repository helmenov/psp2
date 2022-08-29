from k01 import harada_myclass as my

x = my.Frac(1,10)
y = my.Frac(1,5)

z1 = x + y
z2 = x - y
z3 = x * y
z4 = x / y

print(f'{x}+{y}={z1}')
print(f'{x}-{y}={z2}')
print(f'{x}*{y}={z3}')
print(f'{x}/{y}={z4}')
