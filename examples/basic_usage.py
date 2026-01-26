#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic usage example for MCP English Tutor
英语口语家教MCP服务器基础使用示例
"""

import asyncio
import json
from english_tutor import (
    generate_conversation_topic,
    correct_grammar,
    suggest_vocabulary,
    evaluate_response,
    pronunciation_tips,
    track_progress,
    create_practice_scenario
)

async def demo_english_tutor():
    """演示英语家教功能"""
    print("🎓 MCP English Tutor - 功能演示")
    print("=" * 50)
    
    # 1. 生成对话话题
    print("\n1️⃣ 生成对话话题")
    topic_result = generate_conversation_topic(level="intermediate")
    print(f"话题: {topic_result['topic']}")
    print(f"描述: {topic_result['description']}")
    print(f"关键短语: {', '.join(topic_result['key_phrases'])}")
    
    # 2. 模拟学生回答
    print("\n2️⃣ 模拟学生回答")
    student_response = "I have been to Japan last year. It was amazing experience. I love the food and culture."
    print(f"学生回答: {student_response}")
    
    # 3. 评估回答
    print("\n3️⃣ 评估学生回答")
    evaluation = evaluate_response(
        student_response=student_response,
        expected_topic="travel",
        level="intermediate"
    )
    print(f"得分: {evaluation['score']}")
    print(f"优点: {', '.join(evaluation['feedback']['strengths'])}")
    
    # 4. 语法纠错
    print("\n4️⃣ 语法纠错")
    grammar_result = correct_grammar(student_response, provide_explanation=True)
    print(f"纠正后: {grammar_result['corrected_text']}")
    print(f"错误数量: {grammar_result['corrections_count']}")
    
    # 5. 词汇推荐
    print("\n5️⃣ 词汇推荐")
    vocab_result = suggest_vocabulary(context="travel", level="intermediate")
    print(f"推荐词汇数量: {vocab_result['count']}")
    for vocab in vocab_result['vocabulary'][:3]:  # 显示前3个
        print(f"  - {vocab['word']}: {vocab['meaning']}")
    
    # 6. 发音建议
    print("\n6️⃣ 发音建议")
    pronunciation_result = pronunciation_tips("think")
    print(f"发音技巧: {pronunciation_result['general_tips'][0]}")
    
    # 7. 创建练习场景
    print("\n7️⃣ 创建练习场景")
    scenario_result = create_practice_scenario(
        scenario_type="daily_conversation",
        level="beginner"
    )
    print(f"场景: {scenario_result['title']}")
    print(f"设定: {scenario_result['setting']}")
    
    # 8. 跟踪进度
    print("\n8️⃣ 跟踪学习进度")
    progress_result = track_progress(
        student_id="demo_student",
        session_data={
            "topic": "travel",
            "score": evaluation['score'],
            "duration": 30,
            "level": "intermediate"
        }
    )
    print(f"总学习次数: {progress_result['total_sessions']}")
    print(f"平均得分: {progress_result['average_score']}")
    print(f"进步分析: {progress_result['progress_analysis']}")
    
    print("\n✅ 演示完成！所有7个工具都正常工作。")

if __name__ == "__main__":
    asyncio.run(demo_english_tutor())
