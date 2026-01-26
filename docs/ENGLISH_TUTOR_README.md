# 英语口语家教1v1 MCP Server

## 概述

这是一个专为小智机器人设计的英语口语家教MCP服务器，提供1对1的英语口语教学功能。通过多个专业工具，帮助学习者提升英语口语水平。

## 功能特性

### 🎯 1. 对话话题生成 (generate_conversation_topic)
根据学习者的英语水平生成合适的对话话题和场景。

**功能：**
- 支持三个难度级别：beginner（初级）、intermediate（中级）、advanced（高级）
- 提供话题描述、关键短语和对话启动器
- 可以根据学习者的兴趣定制话题

**使用示例：**
```python
generate_conversation_topic(
    level="intermediate",
    custom_interest="旅行"
)
```

**返回内容：**
- 话题名称和描述
- 关键短语列表
- 对话启动句
- 学习建议

---

### ✏️ 2. 语法纠错 (correct_grammar)
检查和纠正学习者的英语语法错误，提供详细的错误解释。

**功能：**
- 识别常见语法错误模式
- 提供纠正后的文本
- 详细的错误类型分类
- 个性化学习建议

**使用示例：**
```python
correct_grammar(
    student_text="He don't like apples.",
    provide_explanation=True
)
```

**检测的错误类型：**
- 主谓不一致
- 时态错误
- 冠词使用错误
- 介词使用错误
- 单复数错误

---

### 📚 3. 词汇推荐 (suggest_vocabulary)
根据对话上下文推荐相关的词汇和短语。

**功能：**
- 根据话题自动匹配相关词汇
- 提供词汇的中文含义和英文例句
- 按难度级别分类
- 包含使用场景说明

**使用示例：**
```python
suggest_vocabulary(
    context="talking about travel experiences",
    level="intermediate"
)
```

**词汇库类别：**
- 旅行 (travel)
- 工作 (work)
- 学习
- 日常生活
- 更多...

---

### 📊 4. 回答评估 (evaluate_response)
评估学习者的英语回答质量，提供详细的反馈和改进建议。

**评估维度：**
- 内容充实度（字数统计）
- 句子结构复杂度
- 逻辑连接词使用
- 话题相关性

**使用示例：**
```python
evaluate_response(
    student_response="I love traveling because it helps me learn about different cultures...",
    expected_topic="travel",
    level="intermediate"
)
```

**返回内容：**
- 0-100分的评分
- 详细的统计数据
- 优点和改进建议
- 鼓励语和下一步学习计划

---

### 🗣️ 5. 发音建议 (pronunciation_tips)
提供针对性的发音指导和技巧。

**功能：**
- 识别发音难点
- 提供发音技巧说明
- 指出常见错误
- 推荐练习单词

**使用示例：**
```python
pronunciation_tips(
    word_or_phrase="think"
)
```

**覆盖的发音难点：**
- th音 (θ/ð)
- r音
- v/w音的区分
- 重音位置

---

### 📈 6. 学习进度跟踪 (track_progress)
记录和分析学习者的学习进度。

**功能：**
- 记录每次学习会话
- 统计已学话题
- 计算平均得分
- 分析学习趋势

**使用示例：**
```python
track_progress(
    student_id="student_001",
    session_data={
        "topic": "travel",
        "score": 85,
        "duration": 30,
        "level": "intermediate"
    }
)
```

**跟踪数据：**
- 总学习次数
- 涵盖话题数量
- 平均得分
- 进步分析（显著进步/稳步提升/需要更多练习）

---

### 🎭 7. 角色扮演场景 (create_practice_scenario)
创建真实的对话场景，进行角色扮演练习。

**场景类型：**
- **日常对话** (daily_conversation)
  - 咖啡店点餐
  - 租房看房
  
- **商务场景** (business)
  - 商务会议
  - 商务谈判
  
- **旅行场景** (travel)
  - 机场问路
  - 酒店入住

**使用示例：**
```python
create_practice_scenario(
    scenario_type="daily_conversation",
    level="beginner"
)
```

**返回内容：**
- 场景设定和背景
- 你的角色和AI的角色
- 对话目标
- 实用短语列表
- 开始提示

---

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 设置环境变量
```bash
export MCP_ENDPOINT=<your_mcp_endpoint>
```

### 3. 运行英语口语家教服务器

**方式一：单独运行**
```bash
python mcp_pipe.py english_tutor.py
```

**方式二：使用配置文件启动所有服务**
```bash
python mcp_pipe.py
```

## 典型使用场景

### 场景1：开始一次口语练习课

1. **生成话题**
```python
result = generate_conversation_topic(level="intermediate")
# 获得：话题"旅行经历"，关键短语，对话启动器
```

2. **学生开始回答**
学生根据话题进行英语表达...

3. **评估回答**
```python
evaluation = evaluate_response(
    student_response="学生的回答文本",
    expected_topic="travel",
    level="intermediate"
)
# 获得：评分、优点、改进建议
```

4. **纠正语法**
```python
corrections = correct_grammar(
    student_text="学生的回答文本",
    provide_explanation=True
)
# 获得：纠正后的文本、错误类型、学习建议
```

5. **推荐词汇**
```python
vocab = suggest_vocabulary(
    context="travel",
    level="intermediate"
)
# 获得：相关词汇、例句、使用场景
```

6. **记录进度**
```python
progress = track_progress(
    student_id="student_001",
    session_data={
        "topic": "travel",
        "score": evaluation["score"],
        "duration": 30
    }
)
# 获得：学习统计、进步分析
```

---

### 场景2：角色扮演练习

1. **创建场景**
```python
scenario = create_practice_scenario(
    scenario_type="daily_conversation",
    level="beginner"
)
# 场景：咖啡店点餐
```

2. **开始对话**
学生扮演顾客，AI扮演店员，进行真实对话练习...

3. **提供发音指导**
```python
tips = pronunciation_tips(word_or_phrase="coffee")
# 获得：发音技巧、常见错误、练习建议
```

---

## 技术特点

- **模块化设计**：每个功能都是独立的工具，可以灵活组合使用
- **渐进式学习**：支持初级、中级、高级三个难度级别
- **即时反馈**：实时评估和纠错，帮助学习者快速改进
- **数据驱动**：跟踪学习进度，提供个性化建议
- **真实场景**：提供丰富的角色扮演场景，模拟真实对话

## 扩展建议

未来可以集成以下功能：

1. **专业语法检查API**
   - LanguageTool
   - Grammarly API
   - 自定义NLP模型

2. **语音识别和评估**
   - 集成语音识别API
   - 发音准确度评分
   - 语调和流利度分析

3. **AI对话伙伴**
   - 集成大语言模型
   - 智能对话响应
   - 上下文理解

4. **学习分析**
   - 详细的学习报告
   - 弱点分析
   - 个性化学习路径

5. **多媒体内容**
   - 视频教学材料
   - 音频练习
   - 交互式练习题

## 配置说明

在 `mcp_config.json` 中的配置：

```json
{
  "english-tutor": {
    "type": "stdio",
    "command": "python",
    "args": ["english_tutor.py"],
    "description": "英语口语家教1v1服务 - 提供对话练习、语法纠错、词汇推荐等功能"
  }
}
```

## 与小智机器人的集成

小智机器人可以通过MCP协议调用这些工具，提供以下服务：

1. **智能对话引导**：根据学生水平自动选择合适的话题
2. **实时纠错**：在对话过程中实时检测和纠正错误
3. **个性化推荐**：根据对话内容推荐相关词汇和短语
4. **进度报告**：定期生成学习报告，展示进步情况
5. **场景模拟**：提供各种真实场景的对话练习

## 贡献

欢迎提交问题和改进建议！

## 许可证

MIT License

