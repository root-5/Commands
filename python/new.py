import os
import sys

# 引数
new_project_dir = sys.argv[1]

# 現在のディレクトリを取得、変数に格納
current_dir = os.getcwd()

# 新しいディレクトリを作成し、移動
os.system("mkdir " + new_project_dir)
os.chdir(new_project_dir)

# 正しく移動できたか確認し、移動できていない場合はログを出力して終了
if os.getcwd() != current_dir + "\\" + new_project_dir:
    print(os.getcwd())
    print("ディレクトリの移動に失敗しました")
    exit()

# README.mdを作成
os.system("echo # " + new_project_dir + " >> README.md")

# .gitignoreを作成
os.system("echo .vscode/ >> .gitignore")

# git管理を設定
os.system("git init")

# ローカルリポジトリにコミット
os.system("git add .")
os.system("git commit -m \"first commit\"")

# VSCodeで開く
os.system("code .")