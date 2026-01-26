# 小智MCP接入配置和使用指南

## 📋 目录
1. [获取小智MCP接入点](#获取小智mcp接入点)
2. [配置环境](#配置环境)
3. [启动服务器](#启动服务器)
4. [验证连接](#验证连接)
5. [使用示例](#使用示例)
6. [常见问题](#常见问题)

---

## 🔌 获取小智MCP接入点

### 方式一：从小智官方获取

1. **联系小智团队**
   - 向小智机器人的开发团队申请MCP接入权限
   - 获取您的专属 MCP_ENDPOINT 地址
   - 格式通常为：`wss://mcp.xiaozhi.ai/connect?token=YOUR_TOKEN`

2. **获取的信息包括：**
   - MCP端点地址 (WebSocket URL)
   - 访问令牌 (Token)
   - 可能的其他认证信息

### 方式二：查看小智后台配置

如果您有小智的管理后台访问权限：
1. 登录小智管理后台
2. 进入"开发者设置"或"MCP配置"
3. 查看或生成您的MCP接入点地址

---

## ⚙️ 配置环境

### 步骤1: 安装依赖

```bash
cd /Users/zhoumenglong/Documents/Code/ai_gen/MCP/mcp-calculator

# 安装所需依赖
pip install -r requirements.txt

# 或者使用pip3
pip3 install -r requirements.txt
```

**依赖包括：**
- `websockets` - WebSocket通信
- `mcp` - MCP协议支持
- `python-dotenv` - 环境变量管理
- `pydantic` - 数据验证
- `mcp-proxy` - MCP代理

### 步骤2: 配置环境变量

#### 方法A：使用 .env 文件（推荐）

在项目根目录创建 `.env` 文件：

```bash
# 创建 .env 文件
cat > .env << 'EOF'
# 小智MCP接入点配置
MCP_ENDPOINT=wss://your-xiaozhi-mcp-endpoint.com/connect

# 如果需要token认证，添加到URL中
# MCP_ENDPOINT=wss://mcp.xiaozhi.ai/connect?token=YOUR_TOKEN_HERE

# 其他可选配置
# LOG_LEVEL=INFO
EOF
```

**示例 .env 内容：**
```env
# 替换为您实际的小智MCP端点
MCP_ENDPOINT=wss://mcp.xiaozhi.ai/connect?token=abc123xyz789

# 如果使用自签名SSL证书，需要禁用SSL验证
MCP_DISABLE_SSL_VERIFY=true
```

#### 方法B：直接设置环境变量

**macOS/Linux:**
```bash
# 临时设置（当前终端会话有效）
export MCP_ENDPOINT="wss://your-xiaozhi-mcp-endpoint.com/connect"

# 永久设置（添加到 ~/.zshrc 或 ~/.bashrc）
echo 'export MCP_ENDPOINT="wss://your-xiaozhi-mcp-endpoint.com/connect"' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell):**
```powershell
# 临时设置
$env:MCP_ENDPOINT = "wss://your-xiaozhi-mcp-endpoint.com/connect"

# 永久设置（系统环境变量）
[System.Environment]::SetEnvironmentVariable('MCP_ENDPOINT', 'wss://your-xiaozhi-mcp-endpoint.com/connect', 'User')
```

### 步骤3: 验证配置

```bash
# 检查环境变量是否设置成功
echo $MCP_ENDPOINT

# 或者在Python中检查
python3 -c "import os; print(os.getenv('MCP_ENDPOINT'))"
```

---

## 🚀 启动服务器

### 方式一：启动单个服务器（英语家教）

```bash
cd /Users/zhoumenglong/Documents/Code/ai_gen/MCP/mcp-calculator

# 使用python3启动
python3 mcp_pipe.py english_tutor.py
```

**成功启动的标志：**
```
INFO - MCP_PIPE - Connecting to WebSocket server...
INFO - MCP_PIPE - Successfully connected to WebSocket server
INFO - MCP_PIPE - Started server process: python3 english_tutor.py
```

### 方式二：启动所有配置的服务器

```bash
# 启动配置文件中所有启用的服务器
python3 mcp_pipe.py
```

这将同时启动：
- ✅ `english-tutor` - 英语口语家教
- ✅ `local-stdio-calculator` - 计算器（如果启用）
- ⏭️ 跳过禁用的服务器

### 方式三：后台运行

```bash
# macOS/Linux - 使用nohup后台运行
nohup python3 mcp_pipe.py english_tutor.py > english_tutor.log 2>&1 &

# 查看日志
tail -f english_tutor.log

# 停止服务
# 查找进程ID
ps aux | grep mcp_pipe
# 终止进程
kill <PID>
```

---

## ✅ 验证连接

### 1. 检查日志输出

**正常连接的日志：**
```
2025-10-16 18:45:23 - MCP_PIPE - INFO - [english_tutor.py] Connecting to WebSocket server...
2025-10-16 18:45:24 - MCP_PIPE - INFO - [english_tutor.py] Successfully connected to WebSocket server
2025-10-16 18:45:24 - MCP_PIPE - INFO - [english_tutor.py] Started server process: python3 english_tutor.py
```

**异常情况：**
```
# 如果看到这个，说明环境变量未设置
ERROR - MCP_PIPE - Please set the `MCP_ENDPOINT` environment variable

# 如果看到这个，说明无法连接到小智服务器
ERROR - MCP_PIPE - Connection error: [Errno 61] Connection refused
```

### 2. 在小智管理后台验证

1. 登录小智管理后台
2. 查看"MCP服务器状态"或"已连接服务"
3. 应该能看到 `english-tutor` 服务已连接
4. 查看服务提供的工具列表（应该显示7个工具）

### 3. 测试工具调用

在小智的测试界面（如果有）尝试调用：

```json
{
  "tool": "generate_conversation_topic",
  "params": {
    "level": "intermediate"
  }
}
```

应该返回一个话题及相关信息。

---

## 💬 使用示例

### 场景1：学生开始学习

**学生对小智说：**
> "我想练习英语口语"

**小智的处理流程：**

1️⃣ **调用工具：generate_conversation_topic**
```json
{
  "tool": "generate_conversation_topic",
  "params": {
    "level": "intermediate"
  }
}
```

2️⃣ **小智收到响应并回复学生：**
> "太好了！今天我们来聊聊'旅行经历'吧。你能告诉我你去过的一个令你印象深刻的地方吗？
> 
> 💡 可以使用这些短语：
> - I have been to...
> - It was amazing/interesting...
> - I experienced...
> 
> 开始吧！"

---

### 场景2：评估学生回答

**学生回答：**
> "I have been to Japan last year. The food was amazing and I visited many temples."

**小智调用工具：**

1️⃣ **评估回答质量**
```json
{
  "tool": "evaluate_response",
  "params": {
    "student_response": "I have been to Japan last year. The food was amazing and I visited many temples.",
    "expected_topic": "travel",
    "level": "intermediate"
  }
}
```

2️⃣ **检查语法错误**
```json
{
  "tool": "correct_grammar",
  "params": {
    "student_text": "I have been to Japan last year",
    "provide_explanation": true
  }
}
```

3️⃣ **小智综合反馈：**
> "很好！你的回答得分 85分 🌟
> 
> ✅ 优点：
> - 内容充实，描述详细
> - 使用了相关词汇
> 
> 💡 语法建议：
> 'I have been to Japan last year' 应该改为 'I went to Japan last year'
> 因为 'last year' 是明确的过去时间点，应该使用一般过去时。
> 
> ✏️ 正确的表达：
> 'I went to Japan last year. The food was amazing and I visited many temples.'"

---

### 场景3：角色扮演练习

**学生说：**
> "我想练习实际对话场景"

**小智调用：**
```json
{
  "tool": "create_practice_scenario",
  "params": {
    "scenario_type": "daily_conversation",
    "level": "beginner"
  }
}
```

**小智回复：**
> "好的！我们来做一个角色扮演练习 🎭
> 
> **场景：咖啡店点餐**
> - 你的角色：顾客
> - 我的角色：咖啡店店员
> 
> **你的目标：**
> 1. 打招呼
> 2. 点一杯咖啡和小吃
> 3. 询问价格
> 4. 付款
> 
> **可以使用的短语：**
> - I'd like to order...
> - How much is...?
> - Can I have...?
> 
> 准备好了吗？我来开始：
> 
> 'Good morning! Welcome to our coffee shop. What would you like to order today?'"

---

### 场景4：查看学习进度

**学生说：**
> "我学得怎么样？"

**小智调用：**
```json
{
  "tool": "track_progress",
  "params": {
    "student_id": "student_12345",
    "session_data": {
      "topic": "travel",
      "score": 85,
      "duration": 30,
      "level": "intermediate"
    }
  }
}
```

**小智回复：**
> "让我看看你的学习进度 📊
> 
> **学习统计：**
> - 总学习次数：15次
> - 涵盖话题：8个
> - 平均得分：82.5分
> - 进步趋势：稳步提升 ↗️
> 
> **最近5次得分：**
> 78 → 80 → 85 → 82 → 85
> 
> **本次会话：**
> - 话题：旅行经历
> - 得分：85分
> - 用时：30分钟
> 
> 👏 做得很好！你在稳步进步。建议继续保持每周3-4次的练习频率。"

---

## 🔧 配置文件说明

### mcp_config.json 结构

```json
{
  "mcpServers": {
    "english-tutor": {
      "type": "stdio",
      "command": "python3",
      "args": ["english_tutor.py"],
      "description": "英语口语家教1v1服务",
      "disabled": false
    },
    "local-stdio-calculator": {
      "type": "stdio",
      "command": "python3",
      "args": ["-m", "calculator"],
      "disabled": true
    }
  }
}
```

**配置参数说明：**
- `type`: 传输类型（stdio/sse/http）
- `command`: 启动命令
- `args`: 命令参数
- `description`: 服务描述
- `disabled`: 是否禁用（true=禁用，false=启用）

### 启用/禁用服务

**禁用计算器服务，只启用英语家教：**
```json
{
  "mcpServers": {
    "english-tutor": {
      "type": "stdio",
      "command": "python3",
      "args": ["english_tutor.py"],
      "disabled": false
    },
    "local-stdio-calculator": {
      "type": "stdio",
      "command": "python3",
      "args": ["-m", "calculator"],
      "disabled": true
    }
  }
}
```

---

## 🐛 常见问题

### Q1: 提示 "Please set the MCP_ENDPOINT environment variable"

**原因：** 未设置MCP端点地址

**解决：**
```bash
# 设置环境变量
export MCP_ENDPOINT="wss://your-mcp-endpoint.com"

# 或创建.env文件
echo 'MCP_ENDPOINT=wss://your-mcp-endpoint.com' > .env
```

---

### Q2: SSL证书验证失败 "CERTIFICATE_VERIFY_FAILED"

**错误信息：**
```
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain
```

**原因：** 小智MCP服务器使用了自签名SSL证书

**解决方法（推荐）：**

设置环境变量禁用SSL验证：

```bash
# 方法1: 在.env文件中添加
echo 'MCP_DISABLE_SSL_VERIFY=true' >> .env

# 方法2: 临时设置环境变量
export MCP_DISABLE_SSL_VERIFY=true

# 然后重新启动服务器
python mcp_pipe.py english_tutor.py
```

**Windows (PowerShell):**
```powershell
$env:MCP_DISABLE_SSL_VERIFY = "true"
python mcp_pipe.py english_tutor.py
```

**完整的.env配置示例：**
```env
MCP_ENDPOINT=wss://your-mcp-endpoint.com
MCP_DISABLE_SSL_VERIFY=true
```

**日志确认：**
成功禁用SSL验证后，应该看到：
```
INFO - [english_tutor.py] SSL verification disabled (self-signed certificate mode)
INFO - [english_tutor.py] Successfully connected to WebSocket server
```

> ⚠️ **安全提示**: 仅在开发/测试环境或使用自签名证书时禁用SSL验证。生产环境建议使用正规CA签发的证书。

---

### Q3: 连接失败 "Connection refused"

**可能原因：**
1. MCP端点地址错误
2. 网络问题
3. 小智服务器未启动
4. Token过期或无效

**解决步骤：**
```bash
# 1. 检查端点地址是否正确
echo $MCP_ENDPOINT

# 2. 测试网络连接
ping your-domain.com

# 3. 检查端点格式（应该是wss://开头）
# 正确: wss://mcp.xiaozhi.ai/connect
# 错误: http://mcp.xiaozhi.ai/connect

# 4. 联系小智团队验证Token是否有效
```

---

### Q4: 服务启动但小智看不到工具

**检查清单：**

1. ✅ 服务器是否成功连接？
   ```bash
   # 查看日志，应该有 "Successfully connected"
   ```

2. ✅ 服务器进程是否正常运行？
   ```bash
   ps aux | grep mcp_pipe
   ps aux | grep english_tutor
   ```

3. ✅ 在小智后台是否能看到服务？
   - 登录小智管理后台
   - 检查MCP服务状态

4. ✅ 工具是否正确注册？
   - 应该能看到7个工具
   - 工具名称应该正确显示

---

### Q5: Python命令未找到

**问题：**
```
command not found: python
```

**解决：**
```bash
# 使用python3
python3 mcp_pipe.py english_tutor.py

# 或者修改配置文件，将command改为"python3"
```

**更新配置文件：**
```json
{
  "english-tutor": {
    "type": "stdio",
    "command": "python3",  // 从"python"改为"python3"
    "args": ["english_tutor.py"]
  }
}
```

---

### Q6: 服务意外断开，如何自动重连？

**好消息：** mcp_pipe.py 已内置自动重连机制！

**特性：**
- ✅ 自动检测连接断开
- ✅ 指数退避重连（1s, 2s, 4s, 8s...最多600s）
- ✅ 无限重试直到连接成功

**日志示例：**
```
INFO - [english_tutor.py] Connection closed
INFO - [english_tutor.py] Waiting 2s before reconnection attempt 1...
INFO - [english_tutor.py] Connecting to WebSocket server...
INFO - [english_tutor.py] Successfully connected to WebSocket server
```

---

### Q7: 如何查看详细日志？

**启用调试日志：**

修改 `mcp_pipe.py` 第38行：
```python
# 从 INFO 改为 DEBUG
logging.basicConfig(
    level=logging.DEBUG,  # 改这里
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

或者运行时重定向日志：
```bash
python3 mcp_pipe.py english_tutor.py 2>&1 | tee server.log
```

---

## 📱 小智端配置（给小智管理员）

如果您是小智的管理员，需要在小智后台配置MCP服务器：

### 1. 添加MCP服务器

在小智后台添加新的MCP服务器：
- **服务器名称**: 英语口语家教
- **服务器ID**: english-tutor
- **连接方式**: WebSocket
- **工具数量**: 7个

### 2. 配置工具权限

为小智配置可以调用的工具：
- ✅ generate_conversation_topic
- ✅ correct_grammar
- ✅ suggest_vocabulary
- ✅ evaluate_response
- ✅ pronunciation_tips
- ✅ track_progress
- ✅ create_practice_scenario

### 3. 配置调用策略

建议配置：
- **自动调用**: 根据对话上下文智能选择工具
- **调用频率**: 无限制
- **超时时间**: 30秒
- **错误重试**: 3次

---

## 📞 技术支持

### 遇到问题？

1. **查看日志**
   ```bash
   tail -f server.log
   ```

2. **运行测试**
   ```bash
   python3 test_english_tutor.py
   ```

3. **检查配置**
   ```bash
   cat .env
   cat mcp_config.json
   ```

4. **联系支持**
   - 查看 [ENGLISH_TUTOR_README.md](ENGLISH_TUTOR_README.md)
   - 查看 [QUICKSTART_ENGLISH_TUTOR.md](QUICKSTART_ENGLISH_TUTOR.md)

---

## ✅ 快速检查清单

启动前检查：
- [ ] 已安装所有依赖 (`pip install -r requirements.txt`)
- [ ] 已设置 MCP_ENDPOINT 环境变量
- [ ] 已配置 mcp_config.json
- [ ] 已启用 english-tutor 服务（disabled: false）
- [ ] Python3 可用 (`python3 --version`)

启动后检查：
- [ ] 日志显示 "Successfully connected"
- [ ] 进程正常运行 (`ps aux | grep mcp_pipe`)
- [ ] 小智后台能看到服务
- [ ] 可以成功调用工具

---

**祝您使用愉快！🎉**

如有任何问题，请参考文档或联系技术支持。

