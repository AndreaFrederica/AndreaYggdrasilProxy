Write-Output "AndreaYggdrasilProxy Build Tools For pwsh"

$outputName = "AndreaYggdrasilProxy"
$buildPath = "build"
$sourceFile = "launcher.py"

if($Env:OS -eq "Windows_NT"){
    $outputName = $outputName + ".exe"
    $nuitkaBuildTarget = $sourceFile.replace(".py", ".exe")
}else{
    $outputName = $outputName + ".bin"
    $nuitkaBuildTarget = $sourceFile.replace(".py", ".bin")
}

if(Test-Path("./$buildPath/$outputName")){
    Remove-Item("./$buildPath/$outputName")
}
if(Test-Path("./$buildPath/$nuitkaBuildTarget")){
    Remove-Item("./$buildPath/$nuitkaBuildTarget")
}

#? 保证奇怪的兼容性
$output = python3 -m nuitka
# 判断输出的长度是否大于 100
if ($output.Length -gt 100) {
    python3 -m nuitka --follow-imports --standalone --onefile --show-memory  --show-progress --include-package=requests --output-dir=$buildPath $sourceFile
} else {
    nuitka --follow-imports --standalone --onefile --show-memory  --show-progress --include-package=requests --output-dir=$buildPath $sourceFile
}


Move-Item ./$buildPath/$nuitkaBuildTarget ./$buildPath/$outputName