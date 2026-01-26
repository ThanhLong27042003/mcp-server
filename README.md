# MCP English Tutor | MCP 英语口语家教

A professional English tutoring 1-on-1 MCP server for AI assistants, providing comprehensive oral English practice with 7 specialized tools.

专为AI助手设计的专业英语口语家教1v1 MCP服务器，提供全面的英语口语练习，包含7个专业工具。

## 🎯 Features | 功能特性

### 7 Professional English Tutoring Tools | 7个专业英语教学工具

| Tool | Function | 功能 |
|------|----------|------|
| `generate_conversation_topic` | Generate topics based on student level | 根据学生水平生成话题 |
| `correct_grammar` | Detect and correct grammar errors | 检测并纠正语法错误 |
| `suggest_vocabulary` | Recommend relevant vocabulary | 推荐相关词汇 |
| `evaluate_response` | Assess student responses | 评估学生回答 |
| `pronunciation_tips` | Provide pronunciation guidance | 提供发音指导 |
| `track_progress` | Track learning progress | 跟踪学习进度 |
| `create_practice_scenario` | Create role-play scenarios | 创建角色扮演场景 |

### Key Features | 核心特性

- 🎓 **3 Difficulty Levels** - Beginner, Intermediate, Advanced | 三个难度级别
- 📚 **12+ Topics** - Rich conversation topics | 12+个话题
- 🎭 **6+ Scenarios** - Real-world practice scenarios | 6+个场景
- 📊 **Progress Tracking** - Learning analytics | 学习分析
- 🔄 **Auto Reconnection** - Robust connection handling | 自动重连
- 🔒 **SSL Support** - Secure communication | SSL支持

## 🚀 Quick Start | 快速开始

### Installation | 安装

```bash
# Clone the repository
git clone https://github.com/your-username/mcp-english-tutor.git
cd mcp-english-tutor

# Install dependencies
pip install -r requirements.txt
```

### Configuration | 配置

1. **Set MCP endpoint** | 设置MCP端点:
```bash
export MCP_ENDPOINT="wss://your-mcp-endpoint.com"
export MCP_DISABLE_SSL_VERIFY=true  # For self-signed certificates
```

2. **Start the server** | 启动服务器:
```bash
python mcp_pipe.py english_tutor.py
```

### Usage with Xiaozhi | 与小智使用

Simply tell Xiaozhi: "我想练习英语口语" and it will automatically use the English tutoring tools!

只需对小智说："我想练习英语口语"，它会自动使用英语家教工具！

## 📖 Documentation | 文档

- [Complete Setup Guide](docs/小智MCP配置使用指南.md) | [完整配置指南](docs/小智MCP配置使用指南.md)
- [API Documentation](docs/ENGLISH_TUTOR_README.md) | [API文档](docs/ENGLISH_TUTOR_README.md)
- [Examples](tests/test_english_tutor.py) | [使用示例](tests/test_english_tutor.py)

## 📁 Project Structure | 项目结构

```
mcp-english-tutor/
├── english_tutor.py          # Main MCP server | 主MCP服务器
├── mcp_pipe.py              # Communication pipe | 通信管道
├── tests/                   # Test files | 测试文件
│   └── test_english_tutor.py
├── docs/                    # Documentation | 文档
│   ├── ENGLISH_TUTOR_README.md
│   └── 小智MCP配置使用指南.md
├── requirements.txt         # Dependencies | 依赖
├── setup.py                # Package config | 包配置
├── LICENSE                 # MIT License | MIT许可证
├── CONTRIBUTING.md         # Contributing guide | 贡献指南
└── README.md               # This file | 本文件
```

## 🤝 Contributing | 贡献

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

## 📄 License | 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

本项目采用MIT许可证 - 详情请查看 [LICENSE](LICENSE) 文件。

## 🆘 Support | 支持

- 📖 [Documentation](docs/) | [文档](docs/)
- 🐛 [Report Issues](https://github.com/your-username/mcp-english-tutor/issues) | [问题反馈](https://github.com/your-username/mcp-english-tutor/issues)
- 💬 [Discussions](https://github.com/your-username/mcp-english-tutor/discussions) | [讨论区](https://github.com/your-username/mcp-english-tutor/discussions)

---

**Made with ❤️ for English learners worldwide | 为全球英语学习者而制作** 🌍
