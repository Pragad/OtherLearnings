@echo off
call :commandAndOutput > C:\Pragadheesh\b807725_unit_test_results.txt 2>&1
pause
exit /b

:commandAndOutput
echo on
echo "Burt807725 Unit Test Results1"
net use * \\10.53.50.44\sh11
net use * \\10.53.50.44\sh11
net use * \\10.53.50.44\sh11
@echo off
exit /b