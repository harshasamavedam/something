@echo off

REM Change to the project directory
cd /d D:\weekend_try\extract_ven

REM Activate the virtual environment
call scripts\activate.bat


REM change the project directory 

cd /d D:\weekend_try  

REM run requirements.txt 

pip install -r requirements.txt

python Main.py

pause


