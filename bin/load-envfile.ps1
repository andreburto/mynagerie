param(
    [parameter(mandatory)]
    [String]$env_file
)

foreach($line in Get-Content $env_file) {
    $parts = $line.Split('=', 2);
    [Environment]::SetEnvironmentVariable($parts[0], $parts[1]);
}