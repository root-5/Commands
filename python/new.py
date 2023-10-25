import os
import subprocess
import sys

# 引数
new_project_dir = sys.argv[1]

# 現在のディレクトリを取得、変数に格納
current_dir = os.getcwd()

# 新しいディレクトリを作成
try:
    subprocess.check_call(['mkdir',new_project_dir],shell=True)
except:
    print('ディレクトリの作成に失敗しました')
    exit()

# 新しいディレクトリに移動
try:
    os.chdir(new_project_dir)
except:
    print('ディレクトリの移動に失敗しました')
    exit()

# README.mdを作成
subprocess.call(['echo','#',new_project_dir,'>>','README.md'],shell=True)

# .gitignoreを作成
subprocess.call(['echo','.vscode/','>>','.gitignore'],shell=True)

# git管理を設定
subprocess.call(['git','init'],shell=True)

# ローカルリポジトリにコミット
subprocess.call(['git','add','.'],shell=True)
subprocess.call(['git','commit','-m','\'first commit\''],shell=True)

# VSCodeで開く
subprocess.call(['code','.'],shell=True)

# powershellを閉じる
