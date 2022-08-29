# k04_2.py

import nagatomo_amida as amida

kuji = {1:4, 2:3, 3:1, 4:5, 5:2} # {ID:goal}形式のdict
L = [] # 横棒のリスト

for ID, goal in kuji.items():
    now = amida.getstate(L, ID) # 既にある横棒Lの操作後における，IDの現在地を返す

    if now == goal: # IDの現在地がすでにgoalにあるならこのifブロックより後の処理を飛ばして次の繰り返しへ
        continue

    lines = amida.genroutes(now,goal) # IDが現在地nowからgoalに移るまでの横棒リストを返す．

    L.extend(lines) # 既存のリストの後ろにlineを加える

L = amida.reduct(L) # Lの中で連続する同じ横棒を省略する

amida.plot(L,kuji) # あみだくじを描画する
