# combine_file.ps1
$baseName = "Image2pdf"
$outputName = "Image2pdf.exe"

$parts = Get-ChildItem -Path "$baseName*" | Sort-Object Name
if ($parts.Count -eq 0) {
    Write-Host "Nenhum arquivo encontrado com o nome base fornecido."
    exit
}

$outputStream = [System.IO.File]::Create($outputName)
$totalParts = $parts.Count

foreach ($part in $parts) {
    $bytes = [System.IO.File]::ReadAllBytes($part.FullName)
    $outputStream.Write($bytes, 0, $bytes.Length)
    $progress = ($parts.IndexOf($part) + 1) / $totalParts * 100
    Write-Progress -Activity "Recombinando arquivo" -Status "Processando $($part.Name)" -PercentComplete $progress
}

$outputStream.Close()
Write-Host "Recombinacao concluida. O arquivo $outputName foi criado."