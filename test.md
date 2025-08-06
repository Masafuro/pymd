# 計算テスト

{%py
price = 1200
qty = 3
total = price * qty


# 表現は事前変換が必要
char_num = 7 #表示文字数（カンマ含む）
format_spec = f">{char_num},"

qty =   format(qty, format_spec)
price = format(price, format_spec)
total = format(total, format_spec)

%}

単価: {{ price }} 円  
数量: {{ qty }} 個  
合計: {{ total  }} 円
