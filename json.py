import os
import json


def build_tree(path):
    tree = {"name": os.path.basename(path), "tags": ["歴史"]}
    files = []
    dirs = []

    for entry in os.scandir(path):
        if entry.is_file() and entry.name.endswith(".txt"):
            files.append(entry.name)
        elif entry.is_dir():
            sub_tree = build_tree(entry.path)
            if sub_tree:
                dirs.append({entry.name: sub_tree})

    if files or dirs:
        if files:
            tree["files"] = files
        if dirs:
            tree["dirs"] = dirs
        return tree
    else:
        return None


def main():
    folder_path = input("フォルダのパスを入力してください: ")

    if not os.path.exists(folder_path):
        print("指定されたフォルダが存在しません。")
        return

    tree = build_tree(folder_path)

    if tree is None:
        print("指定されたフォルダに.txtファイルが見つかりませんでした。")
        return

    json_file_path = os.path.join(folder_path, "yaruo.json")
    with open(json_file_path, "w", encoding="utf-8") as f:
        json.dump(tree, f, ensure_ascii=False, indent=4)

    print(f"JSONファイルが作成されました: {json_file_path}")


if __name__ == "__main__":
    main()
