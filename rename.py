import os
import re
import sys


def get_all_paths(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            paths.append(os.path.join(root, name))
        for name in dirs:
            paths.append(os.path.join(root, name))
    return paths


def get_alldir_paths(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            paths.append(os.path.join(root, name))
    return paths


def main(input_path):
    # 指定されたディレクトリ内のファイルを取得
    files = [
        f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))
    ]

    # ファイル名の先頭にある数字を抽出する正規表現パターン
    pattern = re.compile(r"^(\d+)_")

    # ファイル名とその先頭ナンバーを格納するリスト
    file_list = []

    for filename in files:
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            file_list.append((filename, number))

    # 先頭ナンバーでソート
    file_list.sort(key=lambda x: x[1])

    # 新しいナンバーを割り当ててファイルをリネーム
    for idx, (filename, _) in enumerate(file_list, start=1):
        new_number = "{:03d}".format(idx)
        # 古いナンバーを新しいナンバーに置き換え
        new_filename = pattern.sub(f"{new_number}_", filename, count=1)
        old_path = os.path.join(input_path, filename)
        new_path = os.path.join(input_path, new_filename)
        print(f'"{filename}" を "{new_filename}" にリネームします')
        os.rename(old_path, new_path)


# 使用例
print("リネーム開始")
directory = "C:\\Users\\oreno\\Documents\\yaruo_matome\\test"

all_paths = get_alldir_paths(directory)
print("取得したパス一覧:")
for path in all_paths:
    print(path)
    main(path)


##main(directory)
