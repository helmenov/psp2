# coding: utf-8
# myfunc.py
def gcd(p,q):
    """ pとqの最大公約数
    """
    while p % q !=0:
        old_p = p
        old_q = q
        p = old_q
        q = old_p % old_q
    
    return q

def Frac_reduction(x):
    """ 分数をタプルで表したxを約分して，新しいタプルyに変換
    """
    num = x[0]
    den = x[1]
    Ngcd = gcd(num, den)
    new_num = num//Ngcd
    new_den = den//Ngcd
    y = (new_num, new_den)

    return y
