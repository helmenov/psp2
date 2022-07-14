# amida.py

def getstate(L, ID):
    """
    始点IDが，横線リストLのあとにどこに移動するかを返す
    """
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
     [3,4]]
    というリストを作って返す．
    """

    # write codes in here

    return lines


def plot(L,kuji):
    """
    横線リストLに基づいて，あみだくじを描画する．縦線の数はlen(kuji)
    """
    for i in range(len(kuji)):
        print(f'{i+1} ',end='')
    print('')
    for i in range(len(kuji)):
        print('| ',end='')
    print('')

    for line in L:               # 横棒リストを読みながら，あみだくじの行を描画
        for i in range(1,len(kuji)):
            if i == line[0]:
                print('|-',end='')
            else:
                print('| ',end='')
        print(f'| {line}')

    for i in range(len(kuji)):
        print('| ',end='')
    print('\n')


def reduct(L):
    """
    L に2回連続する同一横線が無くなるよう修正する
    """
    # write codes in here

    return L


def insert(exchange, slice, before):
    """before(List of List)のslice番号に，exchange(List)を挿入

    """
    # write codes in here

    return L


def fix(L,kuji):
    """
    kuji を満たすように L に横線を追加する
    """
    return L
