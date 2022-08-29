# k04_3.py

import zen_amida as amida

kuji = {1:4, 2:3, 3:1, 4:5, 5:2} # {ID:goal}形式のdict
before = [[1, 2], [2, 3], [3, 4], [2, 3], [1, 2], [2, 3], [1, 2], [2, 3], [3, 4], [4, 5], [3, 4], [2, 3]] # 既存の横棒のリスト

amida.plot(before,kuji) # あみだくじを描画する

L = amida.insert([1,2], 1, before) # [1,2]をリストprevのスライス1に挿入する

amida.plot(L,kuji) # 改変されたあみだくじを描画する

after = amida.fix(L, kuji) # Lの後ろに補正を加える．

amida.reduct(after)

amida.plot(after,kuji) # あみだくじを再描画
