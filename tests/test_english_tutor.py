"""
英语口语家教MCP服务器测试脚本
演示所有可用的工具功能
"""

import subprocess
import json
import sys

def send_mcp_request(method, params):
    """向MCP服务器发送请求"""
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": f"tools/call",
        "params": {
            "name": method,
            "arguments": params
        }
    }
    return request

def print_section(title):
    """打印分隔线"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60 + "\n")

def test_generate_topic():
    """测试话题生成功能"""
    print_section("1. 测试话题生成 - generate_conversation_topic")
    
    print("📝 测试场景：为中级学生生成旅行相关话题")
    print("\n请求参数：")
    print(json.dumps({
        "level": "intermediate",
        "custom_interest": "旅行"
    }, indent=2, ensure_ascii=False))
    
    print("\n✅ 预期返回：")
    print("- 话题名称和描述")
    print("- 关键短语列表")
    print("- 对话启动句")
    print("- 学习建议")

def test_grammar_correction():
    """测试语法纠错功能"""
    print_section("2. 测试语法纠错 - correct_grammar")
    
    print("📝 测试场景：纠正学生的语法错误")
    test_text = "He don't like apples and I goed to the store yesterday."
    
    print(f"\n学生输入：\"{test_text}\"")
    print("\n请求参数：")
    print(json.dumps({
        "student_text": test_text,
        "provide_explanation": True
    }, indent=2, ensure_ascii=False))
    
    print("\n✅ 预期返回：")
    print("- 纠正后的文本")
    print("- 错误类型分类")
    print("- 详细的错误解释")
    print("- 学习建议")

def test_vocabulary_suggestion():
    """测试词汇推荐功能"""
    print_section("3. 测试词汇推荐 - suggest_vocabulary")
    
    print("📝 测试场景：推荐旅行相关词汇")
    print("\n请求参数：")
    print(json.dumps({
        "context": "talking about travel experiences",
        "level": "intermediate"
    }, indent=2, ensure_ascii=False))
    
    print("\n✅ 预期返回：")
    print("- 相关词汇列表")
    print("- 中文含义")
    print("- 英文例句")
    print("- 学习建议")

def test_evaluate_response():
    """测试回答评估功能"""
    print_section("4. 测试回答评估 - evaluate_response")
    
    print("📝 测试场景：评估学生关于旅行的回答")
    test_response = """I love traveling because it helps me learn about different cultures 
    and meet new people. Last year, I visited Japan and it was amazing. 
    However, the language barrier was challenging."""
    
    print(f"\n学生回答：\n{test_response}")
    print("\n请求参数：")
    print(json.dumps({
        "student_response": test_response,
        "expected_topic": "travel",
        "level": "intermediate"
    }, indent=2, ensure_ascii=False))
    
    print("\n✅ 预期返回：")
    print("- 评分（0-100）")
    print("- 详细统计数据")
    print("- 优点和改进建议")
    print("- 鼓励语")

def test_pronunciation_tips():
    """测试发音建议功能"""
    print_section("5. 测试发音建议 - pronunciation_tips")
    
    print("📝 测试场景：获取单词'think'的发音指导")
    print("\n请求参数：")
    print(json.dumps({
        "word_or_phrase": "think"
    }, indent=2, ensure_ascii=False))
    
    print("\n✅ 预期返回：")
    print("- 发音技巧")
    print("- 常见错误")
    print("- 练习单词")
    print("- 学习建议")

def test_track_progress():
    """测试学习进度跟踪功能"""
    print_section("6. 测试学习进度跟踪 - track_progress")
    
    print("📝 测试场景：记录学生的学习会话")
    print("\n请求参数：")
    print(json.dumps({
        "student_id": "student_001",
        "session_data": {
            "topic": "travel",
            "score": 85,
            "duration": 30,
            "level": "intermediate"
        }
    }, indent=2, ensure_ascii=False))
    
    print("\n✅ 预期返回：")
    print("- 总学习次数")
    print("- 涵盖话题数量")
    print("- 平均得分")
    print("- 进步分析")

def test_practice_scenario():
    """测试角色扮演场景功能"""
    print_section("7. 测试角色扮演场景 - create_practice_scenario")
    
    print("📝 测试场景：创建咖啡店点餐场景")
    print("\n请求参数：")
    print(json.dumps({
        "scenario_type": "daily_conversation",
        "level": "beginner"
    }, indent=2, ensure_ascii=False))
    
    print("\n✅ 预期返回：")
    print("- 场景设定")
    print("- 角色定义")
    print("- 对话目标")
    print("- 实用短语列表")
    print("- 开始提示")

def test_complete_session():
    """完整的学习会话流程演示"""
    print_section("💡 完整学习会话流程演示")
    
    print("这是一个典型的英语口语1v1学习流程：\n")
    
    steps = [
        {
            "step": 1,
            "title": "生成对话话题",
            "tool": "generate_conversation_topic",
            "description": "小智为学生生成一个适合其水平的话题"
        },
        {
            "step": 2,
            "title": "学生回答",
            "description": "学生根据话题用英语进行表达"
        },
        {
            "step": 3,
            "title": "评估回答质量",
            "tool": "evaluate_response",
            "description": "小智评估学生回答的质量并给出评分"
        },
        {
            "step": 4,
            "title": "纠正语法错误",
            "tool": "correct_grammar",
            "description": "小智检测并纠正学生的语法错误"
        },
        {
            "step": 5,
            "title": "推荐相关词汇",
            "tool": "suggest_vocabulary",
            "description": "小智推荐与话题相关的词汇和短语"
        },
        {
            "step": 6,
            "title": "发音指导",
            "tool": "pronunciation_tips",
            "description": "小智针对难点提供发音建议"
        },
        {
            "step": 7,
            "title": "记录学习进度",
            "tool": "track_progress",
            "description": "小智记录本次学习会话的数据"
        }
    ]
    
    for step_info in steps:
        print(f"步骤 {step_info['step']}: {step_info['title']}")
        if 'tool' in step_info:
            print(f"   工具: {step_info['tool']}")
        print(f"   说明: {step_info['description']}")
        print()

def main():
    """主测试函数"""
    print("\n" + "🎓" * 30)
    print("   英语口语家教1v1 MCP服务器 - 功能测试演示")
    print("🎓" * 30)
    
    print("\n📚 本测试脚本演示了所有可用的工具功能")
    print("   实际使用时，这些工具会通过MCP协议被小智机器人调用\n")
    
    # 运行所有测试
    test_generate_topic()
    test_grammar_correction()
    test_vocabulary_suggestion()
    test_evaluate_response()
    test_pronunciation_tips()
    test_track_progress()
    test_practice_scenario()
    test_complete_session()
    
    # 使用说明
    print_section("📖 使用说明")
    print("1. 确保已安装所有依赖：")
    print("   pip install -r requirements.txt\n")
    
    print("2. 设置MCP_ENDPOINT环境变量：")
    print("   export MCP_ENDPOINT=<your_mcp_endpoint>\n")
    
    print("3. 启动服务器：")
    print("   方式一（单独启动）：")
    print("   python mcp_pipe.py english_tutor.py\n")
    print("   方式二（启动所有配置的服务）：")
    print("   python mcp_pipe.py\n")
    
    print("4. 小智机器人可以通过MCP协议调用这些工具")
    
    print_section("✨ 服务器特点")
    features = [
        "🎯 7个专业英语教学工具",
        "📊 实时评估和反馈",
        "📈 学习进度跟踪",
        "🎭 真实场景模拟",
        "💡 个性化学习建议",
        "🌟 支持三个难度级别（初级/中级/高级）"
    ]
    
    for feature in features:
        print(f"   {feature}")
    
    print("\n" + "🎓" * 30)
    print("   测试演示完成！")
    print("🎓" * 30 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n测试被用户中断")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        sys.exit(1)

