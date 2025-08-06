import re
import argparse

def render_template(template_path, output_path):
    # 入力テンプレートと出力ファイルを表示
    print(f"変換対象ファイル: {template_path}")
    print(f"保存先ファイル: {output_path}")

    # テンプレートファイルを読み込む
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # {%py ... %} ブロック内のコードを抽出して実行し、変数コンテキストを作成
    code_blocks = re.findall(r'{%py(.*?)%}', content, re.DOTALL)
    context = {}
    for block in code_blocks:
        exec(block.strip(), {}, context)

    # コードブロックを削除
    rendered = re.sub(r'{%py.*?%}\n?', '', content, flags=re.DOTALL)

    # {{ var }} をコンテキストの値で置換
    def replace_variable(match):
        var_name = match.group(1).strip()
        return str(context.get(var_name, match.group(0)))
    rendered = re.sub(r'{{\s*(\w+)\s*}}', replace_variable, rendered)

    # レンダリング結果を出力ファイルに書き込む
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Markdown テンプレートをレンダリングします')
    parser.add_argument('template', help='テンプレートファイルのパス')
    parser.add_argument('output', help='出力ファイルのパス')
    args = parser.parse_args()

    # 指定されたファイルパスを表示
    print(f"テンプレートファイル: {args.template}")
    print(f"出力ファイル: {args.output}")

    render_template(args.template, args.output)
