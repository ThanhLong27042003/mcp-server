#!/bin/bash

# 英语口语家教 MCP Server 快速配置脚本
# 使用方法: ./setup.sh

echo "================================================"
echo "   英语口语家教 MCP Server - 快速配置"
echo "================================================"
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 步骤1: 检查Python
echo "📋 步骤1: 检查Python环境..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓${NC} 找到Python: $PYTHON_VERSION"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PYTHON_VERSION=$(python --version)
    echo -e "${GREEN}✓${NC} 找到Python: $PYTHON_VERSION"
else
    echo -e "${RED}✗${NC} 错误: 未找到Python，请先安装Python 3.7+"
    exit 1
fi
echo ""

# 步骤2: 安装依赖
echo "📦 步骤2: 安装依赖包..."
if [ -f "requirements.txt" ]; then
    echo "正在安装依赖..."
    $PYTHON_CMD -m pip install -r requirements.txt --quiet
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} 依赖安装成功"
    else
        echo -e "${RED}✗${NC} 依赖安装失败，请手动运行: pip install -r requirements.txt"
    fi
else
    echo -e "${YELLOW}⚠${NC} 未找到 requirements.txt"
fi
echo ""

# 步骤3: 配置MCP端点
echo "🔌 步骤3: 配置小智MCP接入点..."
echo ""
echo "请输入您的小智MCP端点地址（例如: wss://mcp.xiaozhi.ai/connect?token=xxx）"
echo -n "MCP_ENDPOINT: "
read MCP_ENDPOINT

if [ -z "$MCP_ENDPOINT" ]; then
    echo -e "${YELLOW}⚠${NC} 未输入MCP端点，跳过配置"
    echo "   您可以稍后手动设置: export MCP_ENDPOINT='您的端点地址'"
else
    # 创建或更新.env文件
    echo "MCP_ENDPOINT=$MCP_ENDPOINT" > .env
    echo -e "${GREEN}✓${NC} MCP端点已保存到 .env 文件"
    
    # 导出到当前shell
    export MCP_ENDPOINT="$MCP_ENDPOINT"
    echo -e "${GREEN}✓${NC} MCP端点已设置到当前环境"
fi
echo ""

# 步骤4: 更新配置文件
echo "⚙️  步骤4: 检查配置文件..."
if [ -f "mcp_config.json" ]; then
    echo -e "${GREEN}✓${NC} 找到配置文件 mcp_config.json"
    
    # 更新command为正确的python命令
    if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # macOS或Linux，使用sed更新配置
        if grep -q '"command": "python"' mcp_config.json; then
            # 备份原配置
            cp mcp_config.json mcp_config.json.backup
            # 更新python为python3
            sed -i.tmp 's/"command": "python"/"command": "python3"/g' mcp_config.json
            rm -f mcp_config.json.tmp
            echo -e "${GREEN}✓${NC} 已更新配置文件中的Python命令"
        fi
    fi
else
    echo -e "${YELLOW}⚠${NC} 未找到 mcp_config.json"
fi
echo ""

# 步骤5: 测试配置
echo "🧪 步骤5: 运行测试..."
if [ -f "test_english_tutor.py" ]; then
    $PYTHON_CMD test_english_tutor.py
    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✓${NC} 测试运行成功！"
    fi
else
    echo -e "${YELLOW}⚠${NC} 未找到测试文件"
fi
echo ""

# 显示后续步骤
echo "================================================"
echo "   ✅ 配置完成！"
echo "================================================"
echo ""
echo "🚀 后续步骤："
echo ""
echo "1. 启动英语家教服务器："
echo "   ${GREEN}$PYTHON_CMD mcp_pipe.py english_tutor.py${NC}"
echo ""
echo "2. 或启动所有配置的服务器："
echo "   ${GREEN}$PYTHON_CMD mcp_pipe.py${NC}"
echo ""
echo "3. 查看详细使用指南："
echo "   ${GREEN}cat 小智MCP配置使用指南.md${NC}"
echo ""
echo "📚 相关文档："
echo "   - 配置使用指南: 小智MCP配置使用指南.md"
echo "   - 详细功能文档: ENGLISH_TUTOR_README.md"
echo "   - 快速开始: QUICKSTART_ENGLISH_TUTOR.md"
echo ""

if [ ! -z "$MCP_ENDPOINT" ]; then
    echo "✨ 您的MCP端点已配置："
    echo "   $MCP_ENDPOINT"
    echo ""
    echo "现在可以直接运行："
    echo "   ${GREEN}$PYTHON_CMD mcp_pipe.py english_tutor.py${NC}"
else
    echo "⚠️  提醒: 启动前请先设置MCP_ENDPOINT："
    echo "   ${YELLOW}export MCP_ENDPOINT='wss://your-mcp-endpoint.com'${NC}"
fi
echo ""
echo "================================================"

