@echo off
call :commandAndOutput > out.txt 2>&1
pause
exit /b

:commandAndOutput
echo on
dir
dir "*.pdf"
dir "*.txt"
@echo off
exit /b
