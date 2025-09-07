# 1.board搜索路径

    app\project\SConstruct

## Prepare environment

PrepareEnv(board_search_path="../boards")

## 3 配置非SDK 板级支持包Kconfig

cd到Kconfig根目录
menuconfig --board sf32lb52-xty-ai-tht --board_search_path "G:\Desktop\ProjectJamal\SF32_GITEE\xiaozhi-sf32-lei2\xiaozhi-sf32-lei2\app\boards" Kconfig