

```python
import color_quest
```


```python
# create new question
Q0 = color_quest.Quest()
```


![png](test_k04_files/test_k04_1_0.png)



```python
# show question
Q0.quest()

# trial and eval
print(f'{Q0.eval([127,127,127]) = }')

# number of trials
print(f'{Q0.n = }')
# trials
print(f'{Q0.trials = }')
# dists
print(f'{Q0.dists = }')

```

    Trial #0
    	 (R,G,B)?
    Q0.eval([127,127,127]) = 126.38829059687451
    Q0.n = 1
    Q0.trials = [[127, 127, 127]]
    Q0.dists = [126.38829059687451]
    Trial #0
    	 (R,G,B)?
    Q0.eval([127,127,127]) = 126.38829059687451
    Q0.n = 1
    Q0.trials = [[127, 127, 127]]
    Q0.dists = [126.38829059687451]


# ニュートン法で解く


```python
import numpy as np
import color_quest

rg = np.random.default_rng()

# まず距離を測る3次元ベクトル(r,g,b)を3つ作る
t = np.array([
    [255,0,0],
    [0,255,0],
    [0,0,255]
    ])

Q = color_quest.Quest()

class GPS:
    def __init__(self,t):
        self.t = t
        d = list()
        for i in range(3):
            d.append(Q.eval(t[:,i]))
        self.d = np.array(d)

    def F(self,x):
        f0 = (self.t[:,0]-x).T @ (self.t[:,0]-x) - self.d[0]**2
        f1 = (self.t[:,1]-x).T @ (self.t[:,1]-x) - self.d[1]**2
        f2 = (self.t[:,2]-x).T @ (self.t[:,2]-x) - self.d[2]**2
        return np.array([f0,f1,f2])

    def J(self,x):
        return -2 * (self.t-x)

gps = GPS(t)
for i in range(3):
    print(f'trial#{i+1:02d}\t{gps.t[:,i]}\tError:{gps.d[i]}')

EPS = 1e-20
e  = 1e+20
x = rg.integers(low=0,high=255,size=(3,))
while True:
    d = Q.eval(x)
    n = Q.n
    print(f'trial#{n:02d}\t{x}\tError:{d}')
    if d < EPS:
        break

    J_k_inv = np.linalg.inv(gps.J(x))
    F_k = gps.F(x)
    Delta_x = -J_k_inv @ F_k
    #"""
    for i in range(3):
        y = x + Delta_x
        if y[i] > 255:
            Delta_x = (256-x[i])/Delta_x[i] * Delta_x
        if y[i] < 0:
            Delta_x = -x[i]/Delta_x[i] * Delta_x
    #"""
    x_new = x + Delta_x
    e = np.linalg.norm(x_new - x)
    x = x_new.copy().clip(min=0,max=255).astype(int)
    """
    if e < EPS :
        break
    """
print(f'{Q.rgb_truth = }')



```

    trial#01	[255   0   0]	Error:356.22745542700665
    trial#02	[  0 255   0]	Error:235.58013498595335
    trial#03	[  0   0 255]	Error:183.21571984958058
    trial#04	[219 194  98]	Error:220.1226930600296
    trial#05	[154 250 255]	Error:143.86104406683555
    trial#06	[ 61 201 244]	Error:43.30127018922193
    trial#07	[ 39 179 222]	Error:5.196152422706632
    trial#08	[ 36 176 219]	Error:0.0
    Q.rgb_truth = (36, 176, 219)
    trial#01	[255   0   0]	Error:356.22745542700665
    trial#02	[  0 255   0]	Error:235.58013498595335
    trial#03	[  0   0 255]	Error:183.21571984958058
    trial#04	[219 194  98]	Error:220.1226930600296
    trial#05	[154 250 255]	Error:143.86104406683555
    trial#06	[ 61 201 244]	Error:43.30127018922193
    trial#07	[ 39 179 222]	Error:5.196152422706632
    trial#08	[ 36 176 219]	Error:0.0
    Q.rgb_truth = (36, 176, 219)



![png](test_k04_files/test_k04_4_1.png)

