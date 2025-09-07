# rtconfig.py for SF32LB52-xty-ai-tht with SCons+Kconfig system

import os
import sys

# ==================== 基础配置 ====================
CHIP = "SF32LB52"
CHIP_TYPE = "SF32LB52"
MCU = "cortex-m33"

# ==================== 工具链配置 ====================
# Arm GNU Toolchain 路径
EXEC_PATH = r"D:\ToolChains\arm-gnu\14.3 rel1\bin"
CROSS_COMPILE = "arm-none-eabi-"

CC = CROSS_COMPILE + "gcc.exe"
CXX = CROSS_COMPILE + "g++.exe"
AS = CROSS_COMPILE + "gcc.exe"
AR = CROSS_COMPILE + "ar.exe"
LINK = CROSS_COMPILE + "gcc.exe"
SIZE = CROSS_COMPILE + "size.exe"
OBJCOPY = CROSS_COMPILE + "objcopy.exe"
OBJDUMP = CROSS_COMPILE + "objdump.exe"

# ==================== CPU架构配置 ====================
CPU = "cortex-m33"
FPU = "fpv5-sp-d16"
FLOAT_ABI = "hard"

# ==================== 编译标志 ====================
COMMON_FLAGS = f"-mcpu={CPU} -mthumb -mfpu={FPU} -mfloat-abi={FLOAT_ABI}"

CFLAGS = f"{COMMON_FLAGS} -ffunction-sections -fdata-sections -Os -std=gnu11 -Wall"
CFLAGS += " -Wno-unused-parameter -Wno-unused-function -Wno-unused-variable"

CXXFLAGS = f"{COMMON_FLAGS} -ffunction-sections -fdata-sections -Os -std=gnu++11 -Wall"
CXXFLAGS += " -fno-rtti -fno-exceptions -fno-threadsafe-statics"

ASFLAGS = f"{COMMON_FLAGS} -x assembler-with-cpp"

# 链接标志 - 根据Kconfig配置动态生成
LFLAGS = f"{COMMON_FLAGS} -Wl,--gc-sections -specs=nano.specs"

# ==================== 路径配置 ====================
# 项目根路径
PROJECT_ROOT = r"G:\Desktop\ProjectJamal\SF32_GITEE\xiaozhi-sf32-lei2\xiaozhi-sf32-lei2"

# 板级配置路径
BOARD_DIR = os.path.join(PROJECT_ROOT, "app", "boards", "sf32lb52-xty-ai-tht")
BASE_BOARD_DIR = os.path.join(PROJECT_ROOT, "app", "boards", "sf32lb52-xty-ai_base")

# SDK路径
SDK_DIR = r"G:\Desktop\ProjectJamal\SF32_GITEE\SDK\sifli-sdk"

# ==================== 包含路径 ====================
INCLUDE_PATHS = [
    BOARD_DIR,
    # os.path.join(BOARD_DIR, "../include"),  # 板级通用include
    # os.path.join(BASE_BOARD_DIR, "../include"),  # 基础板级include
    # os.path.join(PROJECT_ROOT, "app", "include"),  # 应用include
    # os.path.join(SDK_DIR, "include"),  # SDK include
]

# ==================== 根据Kconfig.board的配置 ====================
# 这些配置对应Kconfig.board中的设置
KCONFIG_DEFINES = [
    "ASIC=1",  # config ASIC bool default y
    "TOUCH_IRQ_PIN=41",  # config TOUCH_IRQ_PIN int default 41
    'LCD_PWM_BACKLIGHT_INTERFACE_NAME="pwm2"',  # string default "pwm2"
    "LCD_PWM_BACKLIGHT_CHANEL_NUM=4",  # int default 4
    "LCD_BACKLIGHT_CONTROL_PIN=1",  # int default 1
    "RGBLED_CONTROL_PIN=44",  # int default 44
    "PA_EN_LEVEL=1",  # bool default y -> 1
    "PA_EN_PIN=10",  # int default 10
]

# ==================== 预处理器定义 ====================
DEFINES = [
    # 芯片相关
    f"CHIP_{CHIP}",
    "USE_STDPERIPH_DRIVER",
    "HSE_VALUE=8000000",
    "__CORTEX_M33",
    # 板级标识
    "BSP_USING_BOARD_SF32LB52_XTY_AI_THT",
    "BOARD_SF32LB52_XTY_AI_THT",
    # 从Kconfig导入的配置
] + KCONFIG_DEFINES

# ==================== 构建配置 ====================
BUILD_TYPE = "release"
DEBUG = False

if BUILD_TYPE == "debug":
    CFLAGS += " -g -O0 -DDEBUG"
    CXXFLAGS += " -g -O0 -DDEBUG"
    DEFINES.append("DEBUG=1")
else:
    CFLAGS += " -Os -DNDEBUG"
    CXXFLAGS += " -Os -DNDEBUG"
    DEFINES.append("NDEBUG=1")

# ==================== 输出目录配置 ====================
# 根据SConscript的组织方式
OUTPUT_DIR = "build"
BUILD_DIR = f"build_sf32lb52-xty-ai-tht_hcpu"  # 根据您的构建输出目录调整


# ==================== SCons 环境配置 ====================
def get_scons_environment():
    """返回SCons构建环境配置"""
    env_config = {
        # 工具链配置
        "CC": get_tool_path(CC),
        "CXX": get_tool_path(CXX),
        "AS": get_tool_path(AS),
        "AR": get_tool_path(AR),
        "LINK": get_tool_path(LINK),
        "OBJCOPY": get_tool_path(OBJCOPY),
        # 编译标志
        "CFLAGS": CFLAGS,
        "CXXFLAGS": CXXFLAGS,
        "ASFLAGS": ASFLAGS,
        "LFLAGS": LFLAGS,
        # 路径配置
        "CPPPATH": INCLUDE_PATHS,
        "DEFINES": DEFINES,
        # 构建参数
        "BUILD_TYPE": BUILD_TYPE,
        "CHIP": CHIP,
        "MCU": MCU,
    }

    return env_config


def get_tool_path(tool_name):
    """获取完整的工具路径"""
    if EXEC_PATH and os.path.exists(EXEC_PATH):
        return os.path.join(EXEC_PATH, tool_name)
    return tool_name


# ==================== 环境验证 ====================
def validate_environment():
    """验证构建环境"""
    print("Validating build environment for SF32LB52-xty-ai-tht...")

    # 检查工具链
    tools = [CC, CXX, AS, AR, OBJCOPY]
    missing_tools = []

    for tool in tools:
        tool_path = get_tool_path(tool)
        if not os.path.exists(tool_path):
            missing_tools.append(tool)

    if missing_tools:
        print(f"Missing tools: {missing_tools}")
        return False

    # 检查必要的目录
    required_dirs = [BOARD_DIR, BASE_BOARD_DIR]  # , os.path.join(SDK_DIR, "include")]
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            print(f"Missing directory: {dir_path}")
            return False

    print("✅ Build environment is valid!")
    return True


# ==================== 配置信息 ====================
def print_configuration():
    """打印配置信息"""
    print("=" * 60)
    print("SF32LB52-xty-ai-tht Build Configuration")
    print("=" * 60)
    print(f"Board: sf32lb52-xty-ai-tht")
    print(f"Chip: {CHIP} ({MCU})")
    print(f"Toolchain: {EXEC_PATH}")
    print(f"Build Type: {BUILD_TYPE}")
    print(f"KConfig Defines: {len(KCONFIG_DEFINES)} items")
    print("=" * 60)


# 自动打印配置信息
if __name__ == "__main__":
    print_configuration()
    validate_environment()
