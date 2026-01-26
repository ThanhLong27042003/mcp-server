#!/bin/bash

# MCP English Tutor Server Startup Script
# 英语口语家教 MCP Server 启动脚本
# Usage: ./start.sh

echo "================================================"
echo "   MCP English Tutor Server Startup"
echo "   英语口语家教 MCP Server 启动"
echo "================================================"
echo ""

# 检查MCP_ENDPOINT
if [ -z "$MCP_ENDPOINT" ]; then
    # 尝试从.env文件加载
    if [ -f ".env" ]; then
        echo "📄 从 .env 文件加载配置..."
        export $(cat .env | grep -v '^#' | xargs)
    fi
    
    if [ -z "$MCP_ENDPOINT" ]; then
        echo "❌ 错误: 未设置 MCP_ENDPOINT"
        echo ""
        echo "请使用以下方式之一设置："
        echo ""
        echo "方法1: 设置环境变量"
        echo "  export MCP_ENDPOINT='wss://your-endpoint.com'"
        echo "  export MCP_DISABLE_SSL_VERIFY=true"
        echo ""
        echo "方法2: 创建 .env 文件"
        echo "  cp .env.example .env"
        echo "  # 然后编辑 .env 文件，填入您的端点地址"
        echo ""
        exit 1
    fi
fi

# 自动启用SSL验证禁用（用于自签名证书）
if [ -z "$MCP_DISABLE_SSL_VERIFY" ]; then
    echo "⚠️  未设置 MCP_DISABLE_SSL_VERIFY，自动启用（用于自签名证书）"
    export MCP_DISABLE_SSL_VERIFY=true
fi

echo "✓ MCP端点: $MCP_ENDPOINT"
echo "✓ SSL验证: $([ "$MCP_DISABLE_SSL_VERIFY" = "true" ] && echo "已禁用（自签名证书模式）" || echo "已启用")"
echo ""
echo "🚀 正在启动服务器..."
echo "================================================"
echo ""

# 检测Python命令
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ 错误: 未找到Python"
    exit 1
fi

# 启动服务器
$PYTHON_CMD mcp_pipe.py english_tutor.py

