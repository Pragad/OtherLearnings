@echo off
call :commandAndOutput > C:\Pragadheesh\b807725_unit_test_results.txt 2>&1
pause
exit /b

:commandAndOutput
echo on
echo "Burt807725 Unit Test Results1"
for /l %%x in (1, 1, 3) do (
   echo %%x
   dir *
)
@echo off
exit /b

