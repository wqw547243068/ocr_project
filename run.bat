:: windows bat �ű�

@echo off

SET "python=C:\Users\wqw\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11"
SET "npm=E:\program_file\npm.cmd"

::date
::time

dir .

echo �����־Ŀ¼

IF exist log (
  echo ��־Ŀ¼�Ѵ���
) ELSE (
  echo ��־Ŀ¼������,����...
  md log
)

echo ������˳���

python backend/flask_web.py >> log\log_backend.txt

REM UNKNOWN: {"type":"Redirect","op":{"text":">","type":"great"},"file":{"text":"log_backend.txt","type":"Word"}}

echo ����ǰ�˷���

cd ocr-ui

npm run dev >> log\log_foreend.txt

REM UNKNOWN: {"type":"Redirect","op":{"text":">","type":"great"},"file":{"text":"log_foreend.txt","type":"Word"}}
[ %?% EQU 0 ] && echo ��Ŀ�������, ���Է��� Web || echo ��Ŀ����ʧ��

echo OCR�����������

pause