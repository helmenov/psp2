# k04_2_1.py

import amida

kuji = {1:4, 2:3, 3:1, 4:5, 5:2}
L1 = [(1,2),(2,3),(3,4),(2,3),(2,3),(3,4),(3,4),(3,4),(2,3)]
L2 = amida.reduct(L1)

print('[before]')
amida.plot(L1,kuji)
print('[after]')
amida.plot(L2,kuji)

