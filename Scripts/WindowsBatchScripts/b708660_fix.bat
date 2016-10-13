@echo off
call :commandAndOutput > C:\b780660_unit_test_results_fix.txt 2>&1
pause
exit /b

:commandAndOutput
echo on
echo "Burt780660 Unit Test Results. With Fix cMode."
W:
dir
dir *
dir "*>"
dir "*>sh"
dir "*>sh.txt"
dir "**>sh.txt"
dir "**********>sh.txt"
dir "**********>sfdasdh.txt"
dir "**********>sfdasdh*.txt"
dir "*
dir "**
dir "**********
dir "*.txt"
dir "a*.txt" 
dir "a?fkdjs.txt"
dir "a?fkdjs*kf.txt"
dir "*"
dir "*p"
dir "p*"
dir ">*p"
dir "*>p"
dir " 
dir "h?jh******sh.txt"
dir "<<<<<<<<<< 
dir "**************<<<<<<<<<<
dir "<<<<<<<<<<>>>>fdhj
dir "<<<<<<<<<<>>>>fdhj"
dir "**************<<<<<<<<<<>>>>fdhj"
dir "<<" 
dir "<"
dir "< <"
dir "* *"
dir "* <"
dir "< *"
dir "< 
dir "<>>t"
dir "<??t"
dir "<-<" 
dir "<-<<" 
dir "**<><>" 
dir "**********<<<<HDJJ"
dir "**********>>>DKS.TXT" 
dir "*****************>>>>>>>>.txt" 
dir "<<<<<<<<<<<<<<<<<<<>>.txt" 
dir "<<<<<<<<<<>>>sh.txt"
dir "<<<<<<<<<<>>abc" 
dir "**************<<<<<<<<<<sdkl" 
@echo off
exit /b