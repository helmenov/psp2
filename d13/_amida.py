# amida.py

def getstate(L, ID):
    state = ID
    for l,r in L:
        if state == l:
            state = r
        elif state == r:
            state = l
    now = state
    return now


def genroutes(now,goal):
    """ nowからgoalまで移動するための横棒リストを作る

    Args:
        now (int): 現在位置
        goal (int): 行き先

    ex) now,goal = 1,4 なら
    [[1,2],
     [2,3],
     [3,4],
     [2,3],
     [1,2]]
    というリストを作って返す．
    """

    lines = []
    if now <= goal:
        for i in range(now+1,goal+1):
            lines.append([i-1, i])
        for i in range(goal-1,now,-1):
            lines.append([i-1, i])
    else:
        for i in range(now,goal,-1):
            lines.append([i-1,i])
        for i in range(goal+2,now+1):
            lines.append([i-1,i])
    return lines

def plot(L,kuji):
    for i in range(len(kuji)):
        print(f'{i+1} ',end='')
    print('')
    for i in range(len(kuji)):
        print('| ',end='')
    print('')

    for line in L:               # 横棒リストを読みながら，あみだくじの行を描画
        for i in range(1,len(kuji)):
            if i in line and i == min(line):
                print('|-',end='')
            else:
                print('| ',end='')
        print(f'| {line}')

    for i in range(len(kuji)):
        print('| ',end='')
    print('\n')

def reduct(L):
    for i in range(len(L)-1,0,-1):
        if L[i] == L[i-1]:
            del L[i]
            del L[i-1]
            i = i-2
    return L



def insert(exchange, slice, before):
    """before(List of List)のslice番号に，exchange(List)を挿入

    Args:
        exchange (_type_): _description_
        slice (_type_): _description_
        before (_type_): _description_
    """
    L = before.copy()
    L.insert(slice, exchange)
    return L

def fix(L,kuji):
    for ID, goal in kuji.items():
        now = getstate(L, ID) # 既にある横棒Lの操作後における，IDの現在地を返す

        if now == goal: # IDの現在地がすでにgoalにあるならこのifブロックより後の処理を飛ばして次の繰り返しへ
            continue

        lines = genroutes(now,goal) # IDが現在地nowからgoalに移るまでの横棒リストを返す．

        L.extend(lines)
    return L

