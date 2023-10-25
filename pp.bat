@echo off

@rem 引数から.pyファイル名を受け取り、引数を渡して実行する
@rem 例: pp pyファイル名 引数

set pyfile=%1
set pyarg_1=%2
set pyarg_2=%3
set pyarg_3=%4
set pyarg_4=%5

@rem pyファイル名がなければログを出力し終了
if "%pyfile%"=="" (
    echo "pyファイル名を指定してください"
    goto end
)

@rem このディレクトリのパスを取得し、変数に格納
@REM set current_dir=%~dp0
@REM echo %current_dir%

echo starting python...
python %~dp0/python/%pyfile%.py %pyarg_1% %pyarg_2% %pyarg_3% %pyarg_4%
