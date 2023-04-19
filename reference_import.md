# importについて

## module(*.py)のimportの仕方

`main.py`で`MODULE.py`内の関数`FUNC()`や変数`VAR`を使いたい時，以下のように宣言する．

```{python}
from PATH_OF_PACKAGE import MODULE

RES1 = MODULE.FUNC()
RES2 = MODULE.VAR
```

もしくは，

```
from PATH_OF_MODULE import FUNC, VAR

RES1 = FUNC()
RES2 = VAR
```

`PATH_OF_PACKAGE`は，`MODULE.py`があるディレクトリの「パス」であり，`PATH_OF_MODULE`は，`MODULE.py`のパスである．

## PATHについて

一般的に「パス」の表し方は，
1. 絶対パス
2. 相対パス
3. システムパス
の3つがあります．

`C:\Users\kotaro\Documents\psp2\foo\bar\pee.py`
のパスを上記3つのそれぞれで表現してみましょう．

### **絶対パス**

絶対パスは，
```
C:\Users\kotaro\Documents\psp2\foo\bar\pee.py
```
です．

最も根源となっているディレクトリ（root,ルート）からどうディレクトリを移動して辿りつくかが書かれている完全な表現です．

### **相対パス**

相対パスは，呼び出し元の絶対パスとの相対関係で表現するものです．

- 例えば，

    ```
    C:\Users\kotaro\Documents\psp2\foo\bar\main.py
    ```

    から呼び出すのであれば，**同じ階層にpee.py**を呼び出すので，相対パスは

    ```
    .\pee.py
    ```

    となります．`.\`は現在地(`pwd`)を表します．
- 例えば，

    ```
    C:\Users\kotaro\Documents\psp2\foo\main.py
    ```

    から呼び出すのであれば，**同じ階層のbarの下のpee.py**を呼び出すので，現在地`.\`を使って，

    ```
    .\bar\pee.py
    ```

    となります．

- 例えば，

    ```
    C:\Users\kotaro\Documents\psp2\foo\bar\don\main.py
    ```

    から呼び出すのであれば，**1つ上の階層にあるpee.py**を呼び出すので，

    ```
    ..\pee.py
    ```

    となります．`..\`は1つ上の階層を表します．

### **システムパス**

システムパスは，環境変数が設定されていたときに表現できます．例えば環境変数`PATH`に`C:\Users\kotaro\Documents\psp2`が含まれていれば，それを絶対パスから削った

```
foo\bar
```

がシステムパスです．

ちなみに現在地`.\`も環境変数に含まれることが多いので，先の「相対パス」に記した例にある`.\`が含まれているものは`.\`を省略して構わないことが多いです．（常にそうではないので注意）

## ディレクトリとファイル

- Windowsでは，`\`をつけてディレクトリの中のファイルを表します．つけてないものは，ディレクトリかファイルそのものです．
- Mac，*NIXでは，`\`ではなく`/`です．

## include文に現れるパス

基本的に，

```{python}
from PATH import FOO
```

と書きますが，`FOO`の部分には階層を書かず，`PATH`に階層を書きます．

pythonでは階層を`\`や`/`ではなく，`.`と表現します．
- 現在地や1つ上の階層を表す表現はありません．つまり`.\`や`../`などはなく，「相対パス表現」はありません

また，「絶対パス表現」も使えません．したがって，`PATH`部分には，`.`を必要に応じて使った「システムパス」のみでパスを表現します．

pythonのシステムパスの環境変数には，次が定義されている．
- 「現在地」
    - `import`が書かれた呼び出し元の.pyファイルの階層
- 「プロジェクトルート」
    - `.venv`ディレクトリと同じ階層．`.venv`が無ければ，プロジェクトルートは存在しない．
- 「サイトパッケージ」
    - `.venv/lib/pythonX.YY/site-packages/`．`.venv`が無ければ，システムのsite-packages
- 「PYTHONPATH」
    - Windowsの環境変数や，mac/linuxの.bashrcなどで設定
- 「サイトパッケージ/.pth」
    - 追加したい環境変数を書く

最終的に上記のすべてをまとめたpythonのシステムパス(環境変数)は，次の2行を書いたpythonコードを動かすことで知ることができる．

```{python}
import sys
print(sys.path)
```

ちなみに，このリストの順にモジュールを探索するため，このリストにあるパスの下に同じ名前のファイルがある場合，先に見つけられたファイルがインポートされる．

## importをやめる

`from X.Y import a as b`したあとにこの`b`のインポートをやめたいときは，

```{.python}
del b
```

すればよい．
