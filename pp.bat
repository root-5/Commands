@echo off

@rem ��������.py�t�@�C�������󂯎��A������n���Ď��s����
@rem ��: pp py�t�@�C���� ����

set pyfile=%1
set pyarg_1=%2
set pyarg_2=%3
set pyarg_3=%4
set pyarg_4=%5

@rem py�t�@�C�������Ȃ���΃��O���o�͂��I��
if "%pyfile%"=="" (
    echo "py�t�@�C�������w�肵�Ă�������"
    goto end
)

@rem ���̃f�B���N�g���̃p�X���擾���A�ϐ��Ɋi�[
@REM set current_dir=%~dp0
@REM echo %current_dir%

echo starting python...
python %~dp0/python/%pyfile%.py %pyarg_1% %pyarg_2% %pyarg_3% %pyarg_4%
