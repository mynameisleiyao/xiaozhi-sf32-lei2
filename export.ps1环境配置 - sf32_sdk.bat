# 设置执行策略并执行导出脚本
& "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe" -ExecutionPolicy Bypass -NoExit -File "G:\Desktop\ProjectJamal\SF32_GITEE\SDK\sifli-sdk\export.ps1"

# 切换到项目目录
Set-Location "G:\Desktop\ProjectJamal\SF32_GITEE\xiaozhi-sf32-lei2\xiaozhi-sf32-lei2\app\boards\sf32lb52-xty-ai-tht"

# 执行构建命令
scons --board=sf32lb52-xty-ai-tht -j14

# 暂停等待用户输入
pause