@rem 新しいディレクトリを作成し、VSCodeで開く
@echo off
mkdir %1
cd %1
git init
type nul > README.md
git add .
git commit -m "First commit"
code .