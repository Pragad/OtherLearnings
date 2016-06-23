@echo off
call :commandAndOutput > C:\b780660_unit_test_results_1.txt 2>&1
pause
exit /b

:commandAndOutput
echo on
echo "Burt780660 Unit Test Results1. This is to test the '<<<>' scenario."
dir
dir "<<<<<<<<<<>>>>fdhj
dir "<<<<<<<<<<>>>>fdhj"
dir "**************<<<<<<<<<<>>>>fdhj"
dir "<<"
dir "<"
dir "< <"
dir "* *"
dir "* <"
dir "< *"
dir "<>>t"
dir "<??t"
dir "<-<"
dir "<-<"
dir "<-<<"
@echo off
exit /b