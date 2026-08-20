param(
    [string]$SkillsRoot = (Join-Path $PSScriptRoot '..\toolkit-skills')
)

$ErrorActionPreference = 'Stop'
$root = [System.IO.Path]::GetFullPath($SkillsRoot)
$errors = [System.Collections.Generic.List[string]]::new()
$skills = Get-ChildItem -LiteralPath $root -Directory | Sort-Object Name

foreach ($skill in $skills) {
    $entry = Join-Path $skill.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $entry)) {
        $errors.Add("$($skill.Name): 缺少 SKILL.md")
        continue
    }

    $content = Get-Content -LiteralPath $entry -Raw
    $match = [regex]::Match($content, '(?s)^---\s*\r?\n(.*?)\r?\n---')
    if (-not $match.Success) {
        $errors.Add("$($skill.Name): frontmatter 无效")
        continue
    }

    $frontmatter = $match.Groups[1].Value
    $nameMatch = [regex]::Match($frontmatter, '(?m)^name:\s*([^\r\n]+)')
    $descriptionMatch = [regex]::Match($frontmatter, '(?m)^description:\s*(.+)$')
    $declaredName = $nameMatch.Groups[1].Value.Trim(' ', '"', "'")
    $description = $descriptionMatch.Groups[1].Value.Trim(' ', '"', "'")

    if ($declaredName -ne $skill.Name) {
        $errors.Add("$($skill.Name): name 与目录不一致 ($declaredName)")
    }
    if ($declaredName -notmatch '^[a-z0-9-]{1,63}$') {
        $errors.Add("$($skill.Name): name 格式无效")
    }
    if ([string]::IsNullOrWhiteSpace($description) -or $description -match 'TODO') {
        $errors.Add("$($skill.Name): description 缺失或未完成")
    }
    if ($content -match '\[TODO[:\]]') {
        $errors.Add("$($skill.Name): 存在未完成 TODO")
    }

    $links = [regex]::Matches($content, '\]\((references/[^)#]+)')
    foreach ($link in $links) {
        $relative = $link.Groups[1].Value -replace '/', [System.IO.Path]::DirectorySeparatorChar
        $target = Join-Path $skill.FullName $relative
        if (-not (Test-Path -LiteralPath $target)) {
            $errors.Add("$($skill.Name): 引用不存在 $($link.Groups[1].Value)")
        }
    }
}

if ($errors.Count -gt 0) {
    $errors | ForEach-Object { Write-Error $_ }
    exit 1
}

Write-Output "PASS skills=$($skills.Count) root=$root"
