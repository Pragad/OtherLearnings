$i = 1
cd C:\PRAGADHEESH
cd DEV
dir
do {
    $str = "hello"
    Write-Host "$($str)$($i)"
    $i++
}
while ($i -le 5)
