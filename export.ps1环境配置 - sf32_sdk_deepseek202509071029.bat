@echo off
echo export.ps1
powershell -ExecutionPolicy Bypass -File "G:\Desktop\ProjectJamal\SF32_GITEE\SDK\sifli-sdk\export.ps1"
if %errorlevel% neq 0 (
    echo export.ps1 fail
    pause
    exit /b 1
)
echo set_env.bat
call "G:\Desktop\ProjectJamal\SF32_GITEE\SDK\sifli-sdk\set_env.bat" gcc
if %errorlevel% neq 0 (
    echo set_env.bat  fail
    pause
    exit /b 1
)


echo switch to location
cd /d "G:\Desktop\ProjectJamal\SF32_GITEE\xiaozhi-sf32-lei2\xiaozhi-sf32-lei2\app\boards\sf32lb52-xty-ai-tht"
if %errorlevel% neq 0 (
    echo switch fail
    pause
    exit /b 1
)

echo scons build
cd  "G:\Desktop\ProjectJamal\SF32_GITEE\xiaozhi-sf32-lei2\xiaozhi-sf32-lei2\app\project"
scons --board=sf32lb52-xty-ai-tht -j14
if %errorlevel% neq 0 (
    echo scons build fail
)

echo ok
pause