# PowerShell virtual environment activation script

function global:deactivate ([switch]$NonDestructive) {
    if (Test-Path -Path Function:\_OLD_VIRTUAL_PROMPT) {
        Copy-Item -Path Function:\_OLD_VIRTUAL_PROMPT -Destination Function:prompt
        Remove-Item -Path Function:\_OLD_VIRTUAL_PROMPT
    }

    if (Test-Path -Path Env:_OLD_VIRTUAL_PYTHONHOME) {
        Copy-Item -Path Env:_OLD_VIRTUAL_PYTHONHOME -Destination Env:PYTHONHOME
        Remove-Item -Path Env:_OLD_VIRTUAL_PYTHONHOME
    }

    if (Test-Path -Path Env:_OLD_VIRTUAL_PATH) {
        Copy-Item -Path Env:_OLD_VIRTUAL_PATH -Destination Env:PATH
        Remove-Item -Path Env:_OLD_VIRTUAL_PATH
    }

    if (Test-Path -Path Env:VIRTUAL_ENV) {
        Remove-Item -Path env:VIRTUAL_ENV
    }

    if (!$NonDestructive) {
        Remove-Item -Path function:deactivate
    }
}

deactivate -nondestructive

$env:VIRTUAL_ENV = "C:\\Users\\user\\chat-app"

Copy-Item -Path Env:PATH -Destination Env:_OLD_VIRTUAL_PATH
$env:PATH = "$env:VIRTUAL_ENV\\Scripts;$env:PATH"

if (!$Env:VIRTUAL_ENV_DISABLE_PROMPT) {
    function global:_OLD_VIRTUAL_PROMPT { "" }
    Copy-Item -Path function:prompt -Destination function:_OLD_VIRTUAL_PROMPT
    function global:prompt {
        Write-Host -NoNewline -ForegroundColor Green "(venv) "
        _OLD_VIRTUAL_PROMPT
    }
    $env:VIRTUAL_ENV_PROMPT = "(venv) "
}
