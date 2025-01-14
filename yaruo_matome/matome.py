import os
import shutil
import sys


def main():
    # コマンドライン引数でパスを指定（指定がない場合はカレントディレクトリ）
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    else:
        target_path = "."

    # 指定されたパスが存在するか確認
    if not os.path.exists(target_path):
        print(f"Error: The specified path '{target_path}' does not exist.")
        return

    # ファイルを走査
    for filename in os.listdir(target_path):
        full_path = os.path.join(target_path, filename)

        # ディレクトリはスキップ
        if os.path.isdir(full_path):
            continue

        # 拡張子などを含むファイル名をアンダースコアで分割
        parts = filename.split("_")

        # アンダースコアで分割した結果が2つ以上あれば(最低でも [0, 1] がある)
        if len(parts) > 1:
            # フォルダ名を作成
            folder_name = parts[1]

            # フォルダの作成 (既に存在している場合はスキップ)
            folder_path = os.path.join(target_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            # パスのデバッグ情報を出力
            print(
                f"DEBUG: Moving file from '{full_path}' to '{os.path.join(folder_path, filename)}'"
            )

            try:
                # ファイルを移動
                shutil.move(full_path, os.path.join(folder_path, filename))
            except FileNotFoundError as e:
                print(f"ERROR: {e}")
                print(
                    f"DEBUG: Source: {full_path}, Destination: {os.path.join(folder_path, filename)}"
                )


if __name__ == "__main__":
    main()
