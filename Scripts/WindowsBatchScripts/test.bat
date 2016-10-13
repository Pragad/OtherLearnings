@echo off
echo "dir" > asd.txt 2>&1
dir >> asd.txt 2>&1
dir >> asd.txt 2>&1
dir >> asd.txt 2>&1
echo 'dir "*.txt"' >> asd.txt 2>&1
dir "*.txt" >> asd.txt 2>&1
echo dir '"*.pdf"' >> asd.txt 2>&1
dir "*.pdf" >> asd.txt 2>&1

pause
