@echo off
call :commandAndOutput > C:\Pragadheesh\b780660_unit_test_results.txt 2>&1
pause
exit /b

:commandAndOutput
echo on
echo "Burt780660 Unit Test Results1"
dir
dir *
dir "*>"
dir "*>sh"
dir "*>sh.txt"
dir "**>sh.txt"
dir "**********>sh.txt"
dir "**********>sfdasdh.txt"
dir "**********>sfdasdh*.txt"
dir "*.txt"
dir "a*.txt"
dir "a?fkdjs.txt"
dir "a?fkdjs*kf.txt"
dir "*"
dir "*p"
dir "p*"
dir ">*p"
dir "*>p"
dir "h?jh******sh.txt"
@echo off
exit /b