$i = 1
cd C:\pragadhe
do {
    $str = "sh"
#    Write-Host "$($str)$($i)"
    cd "$($str)$($i)"
    dir
    Remove-Item .\*
    cd ..
    $i++
}
while ($i -le 20)
