# pymd
PHPのようにmarkdownにpythonを記述して、markdown文書を生成する。

## 使い方
> python render_pymd.py input.md output.md
input.md:変換するファイル
output.md:出力するファイル

## 構文
'''md

{%py
# pythonを書くところ

x = 10

%}

これは、{{ x }}です。
xの値がpythonから参照されて.mdに出力される。

'''

