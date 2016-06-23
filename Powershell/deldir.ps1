$i = 1
cd C:\pragadhe
do {
    $str = "sh"
    cd "$($str)$($i)"
    Remove-Item -Recurse .\*
    cd ..
    $i++
}
while ($i -le 20)
