# # english_tutor.py
# from mcp.server.fastmcp import FastMCP
# import sys
# import logging
# import json
# import random
# from datetime import datetime
# from typing import Dict, List, Optional

# logger = logging.getLogger('EnglishTutor')

# # Fix UTF-8 encoding for Windows console
# if sys.platform == 'win32':
#     sys.stderr.reconfigure(encoding='utf-8')
#     sys.stdout.reconfigure(encoding='utf-8')

# # Create an MCP server for English tutoring
# mcp = FastMCP("EnglishTutor")

# # 对话话题库
# CONVERSATION_TOPICS = {
#     "beginner": [
#         {"topic": "自我介绍", "description": "介绍你的姓名、年龄、爱好和来自哪里", "key_phrases": ["My name is...", "I am ... years old", "I like...", "I come from..."]},
#         {"topic": "日常生活", "description": "谈论你的日常活动和习惯", "key_phrases": ["I usually...", "Every day...", "In the morning/afternoon/evening..."]},
#         {"topic": "家庭", "description": "介绍你的家庭成员", "key_phrases": ["I have...", "My father/mother/brother/sister...", "We live in..."]},
#         {"topic": "食物与饮料", "description": "谈论你喜欢和不喜欢的食物", "key_phrases": ["I like/love...", "I don't like...", "My favorite food is..."]},
#     ],
#     "intermediate": [
#         {"topic": "旅行经历", "description": "分享你去过的地方和旅行体验", "key_phrases": ["I have been to...", "It was amazing/interesting...", "I experienced..."]},
#         {"topic": "工作与学习", "description": "讨论你的工作或学习情况", "key_phrases": ["I work as...", "I'm studying...", "My major is...", "I'm responsible for..."]},
#         {"topic": "兴趣爱好", "description": "深入讨论你的兴趣和爱好", "key_phrases": ["I'm interested in...", "I've been doing... for...", "What I enjoy most is..."]},
#         {"topic": "文化差异", "description": "讨论不同国家的文化差异", "key_phrases": ["In my country...", "I think the difference is...", "It's interesting that..."]},
#     ],
#     "advanced": [
#         {"topic": "社会问题", "description": "讨论当前的社会问题和你的看法", "key_phrases": ["From my perspective...", "One of the major issues is...", "I believe that..."]},
#         {"topic": "科技发展", "description": "讨论科技对生活的影响", "key_phrases": ["Technology has revolutionized...", "The impact of... is significant", "In the future..."]},
#         {"topic": "环境保护", "description": "讨论环境问题和解决方案", "key_phrases": ["We need to address...", "The consequences of... are...", "A possible solution would be..."]},
#         {"topic": "职业规划", "description": "讨论职业目标和未来计划", "key_phrases": ["My long-term goal is...", "I plan to...", "I'm working towards..."]},
#     ]
# }

# # 常见语法错误模式
# COMMON_GRAMMAR_ERRORS = {
#     "subject_verb_agreement": "主谓不一致",
#     "tense_error": "时态错误",
#     "article_error": "冠词使用错误",
#     "preposition_error": "介词使用错误",
#     "word_order": "词序错误",
#     "plural_singular": "单复数错误",
# }

# # 学习进度存储（实际应用中应使用数据库）
# student_progress = {}

# @mcp.tool()
# def generate_conversation_topic(level: str = "intermediate", custom_interest: Optional[str] = None) -> dict:
#     """
#     生成适合学生水平的对话话题和场景。
    
#     参数:
#     - level: 学生的英语水平 (beginner/intermediate/advanced)
#     - custom_interest: 可选，学生感兴趣的特定话题
    
#     返回包含话题、描述、关键短语和对话启动器的字典。
#     """
#     try:
#         if level not in CONVERSATION_TOPICS:
#             level = "intermediate"
        
#         topics = CONVERSATION_TOPICS[level]
#         selected_topic = random.choice(topics)
        
#         # 生成对话启动器
#         conversation_starters = [
#             f"Let's talk about {selected_topic['topic'].lower()}. Can you tell me about it?",
#             f"I'd like to hear your thoughts on {selected_topic['topic'].lower()}.",
#             f"Could you share your experience with {selected_topic['topic'].lower()}?",
#         ]
        
#         result = {
#             "success": True,
#             "level": level,
#             "topic": selected_topic["topic"],
#             "description": selected_topic["description"],
#             "key_phrases": selected_topic["key_phrases"],
#             "conversation_starter": random.choice(conversation_starters),
#             "tips": f"在这个话题中，试着使用提供的关键短语，并尽可能详细地表达你的想法。"
#         }
        
#         if custom_interest:
#             result["custom_note"] = f"已根据你的兴趣 '{custom_interest}' 选择相关话题。"
        
#         logger.info(f"Generated topic: {selected_topic['topic']} for level: {level}")
#         return result
        
#     except Exception as e:
#         logger.error(f"Error generating topic: {e}")
#         return {"success": False, "error": str(e)}


# @mcp.tool()
# def correct_grammar(student_text: str, provide_explanation: bool = True) -> dict:
#     """
#     检查和纠正学生的英语语法错误。
    
#     参数:
#     - student_text: 学生输入的英语文本
#     - provide_explanation: 是否提供详细的错误解释
    
#     返回纠正后的文本、错误类型和学习建议。
#     """
#     try:
#         # 这里是简化的演示，实际应用中应该集成专业的语法检查API
#         # 如 LanguageTool API, Grammarly API 等
        
#         corrections = []
#         corrected_text = student_text
#         tips = []
        
#         # 示例：检查一些常见错误模式
#         error_patterns = {
#             "he don't": ("he doesn't", "subject_verb_agreement", "第三人称单数动词应该用doesn't而不是don't"),
#             "she don't": ("she doesn't", "subject_verb_agreement", "第三人称单数动词应该用doesn't而不是don't"),
#             "I goed": ("I went", "tense_error", "go的过去式是不规则变化went，不是goed"),
#             "a apple": ("an apple", "article_error", "元音音素前应该用an而不是a"),
#             "informations": ("information", "plural_singular", "information是不可数名词，没有复数形式"),
#         }
        
#         for error, (correction, error_type, explanation) in error_patterns.items():
#             if error.lower() in student_text.lower():
#                 corrections.append({
#                     "error": error,
#                     "correction": correction,
#                     "type": COMMON_GRAMMAR_ERRORS.get(error_type, error_type),
#                     "explanation": explanation if provide_explanation else None
#                 })
#                 corrected_text = corrected_text.replace(error, correction)
        
#         # 生成学习建议
#         if corrections:
#             error_types = set(c["type"] for c in corrections)
#             tips = [f"建议重点练习：{', '.join(error_types)}"]
#         else:
#             tips = ["很好！没有发现明显的语法错误。继续保持！"]
        
#         result = {
#             "success": True,
#             "original_text": student_text,
#             "corrected_text": corrected_text,
#             "corrections": corrections,
#             "corrections_count": len(corrections),
#             "tips": tips,
#             "overall_assessment": "优秀" if len(corrections) == 0 else "良好" if len(corrections) <= 2 else "需要改进"
#         }
        
#         logger.info(f"Grammar check completed: {len(corrections)} corrections found")
#         return result
        
#     except Exception as e:
#         logger.error(f"Error in grammar correction: {e}")
#         return {"success": False, "error": str(e)}


# @mcp.tool()
# def suggest_vocabulary(context: str, level: str = "intermediate") -> dict:
#     """
#     根据对话上下文推荐相关词汇和短语。
    
#     参数:
#     - context: 当前对话的上下文或话题
#     - level: 学生的英语水平
    
#     返回相关词汇、短语、例句和使用场景。
#     """
#     try:
#         # 词汇库示例（实际应用中应该有完整的词汇数据库）
#         vocabulary_database = {
#             "travel": {
#                 "beginner": [
#                     {"word": "destination", "meaning": "目的地", "example": "Paris is my dream destination."},
#                     {"word": "luggage", "meaning": "行李", "example": "Don't forget to check your luggage."},
#                     {"word": "journey", "meaning": "旅程", "example": "The journey was long but enjoyable."},
#                 ],
#                 "intermediate": [
#                     {"word": "itinerary", "meaning": "行程", "example": "We planned a detailed itinerary for the trip."},
#                     {"word": "accommodation", "meaning": "住宿", "example": "We booked accommodation near the beach."},
#                     {"word": "venture", "meaning": "冒险；探险", "example": "We ventured into the mountains."},
#                 ],
#                 "advanced": [
#                     {"word": "wanderlust", "meaning": "旅行癖；漫游癖", "example": "Her wanderlust led her to 50 countries."},
#                     {"word": "nomadic", "meaning": "游牧的；流浪的", "example": "He lives a nomadic lifestyle."},
#                     {"word": "embark", "meaning": "开始；从事", "example": "They embarked on a journey across Asia."},
#                 ]
#             },
#             "work": {
#                 "beginner": [
#                     {"word": "colleague", "meaning": "同事", "example": "My colleagues are very friendly."},
#                     {"word": "office", "meaning": "办公室", "example": "I work in an office downtown."},
#                     {"word": "meeting", "meaning": "会议", "example": "We have a meeting at 2 PM."},
#                 ],
#                 "intermediate": [
#                     {"word": "deadline", "meaning": "截止日期", "example": "The deadline for this project is next Friday."},
#                     {"word": "collaborate", "meaning": "合作", "example": "We collaborate with the marketing team."},
#                     {"word": "efficiency", "meaning": "效率", "example": "We need to improve our efficiency."},
#                 ],
#                 "advanced": [
#                     {"word": "synergy", "meaning": "协同作用", "example": "The synergy between teams increased productivity."},
#                     {"word": "delegate", "meaning": "委派；授权", "example": "Learn to delegate tasks effectively."},
#                     {"word": "stakeholder", "meaning": "利益相关者", "example": "We need to consider all stakeholders."},
#                 ]
#             }
#         }
        
#         # 简单的关键词匹配
#         matched_category = "general"
#         for category in vocabulary_database:
#             if category in context.lower():
#                 matched_category = category
#                 break
        
#         # 获取词汇
#         if matched_category in vocabulary_database:
#             vocab_list = vocabulary_database[matched_category].get(level, vocabulary_database[matched_category]["intermediate"])
#         else:
#             # 默认返回工作相关词汇
#             vocab_list = vocabulary_database["work"].get(level, vocabulary_database["work"]["intermediate"])
        
#         result = {
#             "success": True,
#             "context": context,
#             "level": level,
#             "category": matched_category,
#             "vocabulary": vocab_list,
#             "count": len(vocab_list),
#             "study_tip": "建议每天学习3-5个新词汇，并尝试在对话中使用它们。"
#         }
        
#         logger.info(f"Suggested {len(vocab_list)} vocabulary items for context: {context}")
#         return result
        
#     except Exception as e:
#         logger.error(f"Error suggesting vocabulary: {e}")
#         return {"success": False, "error": str(e)}


# @mcp.tool()
# def evaluate_response(student_response: str, expected_topic: str, level: str = "intermediate") -> dict:
#     """
#     评估学生的回答质量，提供详细反馈。
    
#     参数:
#     - student_response: 学生的英语回答
#     - expected_topic: 预期的话题或问题
#     - level: 学生的英语水平
    
#     返回评分、优点、改进建议和鼓励。
#     """
#     try:
#         # 评估维度
#         word_count = len(student_response.split())
#         sentence_count = student_response.count('.') + student_response.count('!') + student_response.count('?')
        
#         # 评分标准（简化版）
#         score = 0
#         feedback = {
#             "strengths": [],
#             "improvements": [],
#             "encouragement": ""
#         }
        
#         # 长度评估
#         if word_count >= 50:
#             score += 3
#             feedback["strengths"].append("回答内容充实，表达详细")
#         elif word_count >= 30:
#             score += 2
#             feedback["strengths"].append("回答内容适中")
#         else:
#             score += 1
#             feedback["improvements"].append("尝试提供更详细的回答，增加更多细节和例子")
        
#         # 句子结构
#         if sentence_count >= 3:
#             score += 2
#             feedback["strengths"].append("使用了多个句子，结构清晰")
#         else:
#             feedback["improvements"].append("尝试使用更多句子来表达，让内容更有层次")
        
#         # 复杂度（简单检测）
#         complex_indicators = ["because", "although", "however", "moreover", "furthermore", "therefore"]
#         complex_count = sum(1 for word in complex_indicators if word in student_response.lower())
#         if complex_count >= 2:
#             score += 3
#             feedback["strengths"].append("使用了连接词，展现了较好的逻辑思维")
#         elif complex_count >= 1:
#             score += 2
#             feedback["strengths"].append("使用了连接词")
#         else:
#             feedback["improvements"].append("尝试使用连接词（如because, however, moreover）使表达更连贯")
        
#         # 话题相关性（简单检测）
#         if expected_topic.lower() in student_response.lower():
#             score += 2
#             feedback["strengths"].append("紧扣话题，内容相关")
        
#         # 标准化分数到0-100
#         final_score = min(100, (score / 10) * 100)
        
#         # 生成鼓励语
#         if final_score >= 80:
#             feedback["encouragement"] = "太棒了！你的表达非常好，继续保持这个水平！💪"
#         elif final_score >= 60:
#             feedback["encouragement"] = "做得不错！你在进步，继续努力！👍"
#         else:
#             feedback["encouragement"] = "不错的尝试！每次练习都是进步，继续加油！🌟"
        
#         result = {
#             "success": True,
#             "score": round(final_score, 1),
#             "level": level,
#             "statistics": {
#                 "word_count": word_count,
#                 "sentence_count": sentence_count,
#                 "complex_structures": complex_count
#             },
#             "feedback": feedback,
#             "next_steps": [
#                 "继续练习类似话题的表达",
#                 "尝试使用今天学到的新词汇",
#                 "录音练习，注意发音和语调"
#             ]
#         }
        
#         logger.info(f"Evaluated response: score={final_score}, words={word_count}")
#         return result
        
#     except Exception as e:
#         logger.error(f"Error evaluating response: {e}")
#         return {"success": False, "error": str(e)}


# @mcp.tool()
# def pronunciation_tips(word_or_phrase: str) -> dict:
#     """
#     提供发音建议和技巧。
    
#     参数:
#     - word_or_phrase: 需要发音指导的单词或短语
    
#     返回发音指南、常见错误和练习建议。
#     """
#     try:
#         # 发音技巧数据库（示例）
#         pronunciation_guide = {
#             "th": {
#                 "sounds": ["θ (thin)", "ð (this)"],
#                 "tip": "舌尖轻触上齿背，让气流通过",
#                 "common_errors": "中文使用者容易发成 's' 或 'z' 音",
#                 "practice_words": ["think", "this", "mother", "thank"]
#             },
#             "r": {
#                 "sounds": ["ɹ (red)"],
#                 "tip": "舌尖向上卷但不接触口腔任何部位",
#                 "common_errors": "容易发成中文的'日'音",
#                 "practice_words": ["red", "right", "road", "around"]
#             },
#             "v": {
#                 "sounds": ["v (very)"],
#                 "tip": "上齿轻触下唇，声带振动",
#                 "common_errors": "容易和 'w' 音混淆",
#                 "practice_words": ["very", "view", "voice", "victory"]
#             }
#         }
        
#         # 检测需要特别注意的音素
#         tips = []
#         practice_suggestions = []
        
#         word_lower = word_or_phrase.lower()
#         for sound, guide in pronunciation_guide.items():
#             if sound in word_lower:
#                 tips.append({
#                     "sound": sound,
#                     "sounds_like": guide["sounds"],
#                     "tip": guide["tip"],
#                     "common_error": guide["common_errors"],
#                     "practice_words": guide["practice_words"]
#                 })
        
#         # 通用建议
#         general_tips = [
#             "注意重音位置，可以查字典确认",
#             "模仿母语者的发音，可以使用在线词典的发音功能",
#             "录下自己的发音，与标准发音对比",
#             "放慢速度，确保每个音都发准确"
#         ]
        
#         result = {
#             "success": True,
#             "word_or_phrase": word_or_phrase,
#             "specific_tips": tips if tips else "未发现特别需要注意的发音难点",
#             "general_tips": general_tips,
#             "recommendation": "建议使用在线词典（如 Cambridge Dictionary, Merriam-Webster）听标准发音",
#             "practice_method": "每天练习5-10分钟，重复朗读相同的单词和短语直到流利"
#         }
        
#         logger.info(f"Provided pronunciation tips for: {word_or_phrase}")
#         return result
        
#     except Exception as e:
#         logger.error(f"Error providing pronunciation tips: {e}")
#         return {"success": False, "error": str(e)}


# @mcp.tool()
# def track_progress(student_id: str, session_data: dict) -> dict:
#     """
#     跟踪和记录学生的学习进度。
    
#     参数:
#     - student_id: 学生唯一标识
#     - session_data: 本次学习会话的数据（包括话题、得分等）
    
#     返回学习统计和进步分析。
#     """
#     try:
#         # 初始化学生记录
#         if student_id not in student_progress:
#             student_progress[student_id] = {
#                 "sessions": [],
#                 "total_sessions": 0,
#                 "topics_covered": set(),
#                 "average_score": 0,
#                 "start_date": datetime.now().isoformat()
#             }
        
#         # 添加会话数据
#         session_entry = {
#             "date": datetime.now().isoformat(),
#             "topic": session_data.get("topic", "未指定"),
#             "score": session_data.get("score", 0),
#             "duration": session_data.get("duration", 0),
#             "level": session_data.get("level", "intermediate")
#         }
        
#         student_progress[student_id]["sessions"].append(session_entry)
#         student_progress[student_id]["total_sessions"] += 1
#         student_progress[student_id]["topics_covered"].add(session_data.get("topic", "未指定"))
        
#         # 计算平均分
#         all_scores = [s["score"] for s in student_progress[student_id]["sessions"]]
#         student_progress[student_id]["average_score"] = sum(all_scores) / len(all_scores)
        
#         # 分析进步
#         progress_analysis = "稳步提升"
#         if len(all_scores) >= 3:
#             recent_avg = sum(all_scores[-3:]) / 3
#             earlier_avg = sum(all_scores[:-3]) / len(all_scores[:-3]) if len(all_scores) > 3 else all_scores[0]
            
#             if recent_avg > earlier_avg + 10:
#                 progress_analysis = "显著进步"
#             elif recent_avg > earlier_avg:
#                 progress_analysis = "稳步提升"
#             elif recent_avg < earlier_avg - 10:
#                 progress_analysis = "需要更多练习"
#             else:
#                 progress_analysis = "保持稳定"
        
#         result = {
#             "success": True,
#             "student_id": student_id,
#             "total_sessions": student_progress[student_id]["total_sessions"],
#             "topics_covered": len(student_progress[student_id]["topics_covered"]),
#             "average_score": round(student_progress[student_id]["average_score"], 1),
#             "current_session": session_entry,
#             "progress_analysis": progress_analysis,
#             "recent_scores": all_scores[-5:],  # 最近5次得分
#             "recommendation": "建议每周至少练习3-4次，每次20-30分钟" if student_progress[student_id]["total_sessions"] < 10 else "保持良好的学习习惯！"
#         }
        
#         logger.info(f"Updated progress for student: {student_id}, total sessions: {student_progress[student_id]['total_sessions']}")
#         return result
        
#     except Exception as e:
#         logger.error(f"Error tracking progress: {e}")
#         return {"success": False, "error": str(e)}


# @mcp.tool()
# def create_practice_scenario(scenario_type: str = "daily_conversation", level: str = "intermediate") -> dict:
#     """
#     创建角色扮演练习场景。
    
#     参数:
#     - scenario_type: 场景类型 (daily_conversation/business/travel/interview)
#     - level: 难度级别
    
#     返回场景描述、角色设定和对话提示。
#     """
#     try:
#         scenarios = {
#             "daily_conversation": {
#                 "beginner": {
#                     "title": "咖啡店点餐",
#                     "setting": "你在一家咖啡店，想要点一杯咖啡和一些小吃",
#                     "your_role": "顾客",
#                     "ai_role": "咖啡店店员",
#                     "objectives": ["打招呼", "点餐", "询问价格", "付款", "说谢谢"],
#                     "useful_phrases": [
#                         "I'd like to order...",
#                         "How much is...?",
#                         "Can I have...?",
#                         "Here you are.",
#                         "Thank you!"
#                     ]
#                 },
#                 "intermediate": {
#                     "title": "租房看房",
#                     "setting": "你正在寻找新公寓，现在要和房东看房并了解详情",
#                     "your_role": "租房者",
#                     "ai_role": "房东",
#                     "objectives": ["询问房租和押金", "了解房间设施", "询问附近交通", "讨论租约条款"],
#                     "useful_phrases": [
#                         "How much is the monthly rent?",
#                         "Is the apartment furnished?",
#                         "What's included in the rent?",
#                         "Are pets allowed?",
#                         "When can I move in?"
#                     ]
#                 }
#             },
#             "business": {
#                 "intermediate": {
#                     "title": "商务会议",
#                     "setting": "你正在参加一个项目进度会议",
#                     "your_role": "项目成员",
#                     "ai_role": "项目经理",
#                     "objectives": ["汇报进度", "讨论问题", "提出建议", "确认下一步行动"],
#                     "useful_phrases": [
#                         "I've completed...",
#                         "We're facing some challenges with...",
#                         "I suggest we...",
#                         "What's our next step?",
#                         "Let me clarify..."
#                     ]
#                 },
#                 "advanced": {
#                     "title": "商务谈判",
#                     "setting": "你代表公司与潜在合作伙伴进行合作谈判",
#                     "your_role": "商务代表",
#                     "ai_role": "合作方代表",
#                     "objectives": ["介绍合作方案", "讨论条款", "处理异议", "达成共识"],
#                     "useful_phrases": [
#                         "We propose...",
#                         "That's a valid concern...",
#                         "Perhaps we could compromise on...",
#                         "Let's find a win-win solution...",
#                         "I believe we can reach an agreement..."
#                     ]
#                 }
#             },
#             "travel": {
#                 "beginner": {
#                     "title": "机场问路",
#                     "setting": "你在机场，需要找到登机口",
#                     "your_role": "旅客",
#                     "ai_role": "机场工作人员",
#                     "objectives": ["询问登机口位置", "询问如何到达", "确认时间"],
#                     "useful_phrases": [
#                         "Excuse me, where is gate...?",
#                         "How do I get to...?",
#                         "Is it far from here?",
#                         "Thank you for your help!"
#                     ]
#                 },
#                 "intermediate": {
#                     "title": "酒店入住",
#                     "setting": "你刚到达酒店准备办理入住",
#                     "your_role": "酒店客人",
#                     "ai_role": "前台接待",
#                     "objectives": ["办理入住", "询问设施", "提出特殊要求", "了解周边信息"],
#                     "useful_phrases": [
#                         "I have a reservation under...",
#                         "What time is breakfast served?",
#                         "Could I have a room with...?",
#                         "What are some good restaurants nearby?"
#                     ]
#                 }
#             }
#         }
        
#         # 获取场景
#         if scenario_type not in scenarios:
#             scenario_type = "daily_conversation"
        
#         scenario_category = scenarios[scenario_type]
#         if level not in scenario_category:
#             level = "intermediate" if "intermediate" in scenario_category else list(scenario_category.keys())[0]
        
#         selected_scenario = scenario_category[level]
        
#         result = {
#             "success": True,
#             "scenario_type": scenario_type,
#             "level": level,
#             "title": selected_scenario["title"],
#             "setting": selected_scenario["setting"],
#             "your_role": selected_scenario["your_role"],
#             "ai_role": selected_scenario["ai_role"],
#             "objectives": selected_scenario["objectives"],
#             "useful_phrases": selected_scenario["useful_phrases"],
#             "start_prompt": f"场景设定: {selected_scenario['setting']}\n你的角色: {selected_scenario['your_role']}\n请开始对话吧！",
#             "tips": "尽量使用自然的语言表达，不要担心犯错。重要的是开口练习！"
#         }
        
#         logger.info(f"Created practice scenario: {selected_scenario['title']}")
#         return result
        
#     except Exception as e:
#         logger.error(f"Error creating practice scenario: {e}")
#         return {"success": False, "error": str(e)}


# # Start the server
# if __name__ == "__main__":
#     mcp.run(transport="stdio")


# english_tutor.py
from mcp.server.fastmcp import FastMCP
import sys
import logging
import json
import random
from datetime import datetime
from typing import Dict, List, Optional
import requests

logger = logging.getLogger('EnglishTutor')

# Fix UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stderr.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

# Create an MCP server for English tutoring
mcp = FastMCP("EnglishTutor")

# 对话话题库
CONVERSATION_TOPICS = {
    "beginner": [
        {"topic": "Giới thiệu bản thân", "description": "Giới thiệu tên, tuổi, sở thích và quê quán của bạn", "key_phrases": ["My name is...", "I am ... years old", "I like...", "I come from..."]},
        {"topic": "Cuộc sống hàng ngày", "description": "Nói về các hoạt động và thói quen hàng ngày của bạn", "key_phrases": ["I usually...", "Every day...", "In the morning/afternoon/evening..."]},
        {"topic": "Gia đình", "description": "Giới thiệu các thành viên trong gia đình của bạn", "key_phrases": ["I have...", "My father/mother/brother/sister...", "We live in..."]},
        {"topic": "Thức ăn và đồ uống", "description": "Nói về những món ăn bạn thích và không thích", "key_phrases": ["I like/love...", "I don't like...", "My favorite food is..."]},
    ],
    "intermediate": [
        {"topic": "Trải nghiệm du lịch", "description": "Chia sẻ những nơi bạn đã từng đến và trải nghiệm du lịch", "key_phrases": ["I have been to...", "It was amazing/interesting...", "I experienced..."]},
        {"topic": "Công việc và học tập", "description": "Thảo luận về công việc hoặc tình hình học tập của bạn", "key_phrases": ["I work as...", "I'm studying...", "My major is...", "I'm responsible for..."]},
        {"topic": "Sở thích", "description": "Thảo luận sâu về sở thích của bạn", "key_phrases": ["I'm interested in...", "I've been doing... for...", "What I enjoy most is..."]},
        {"topic": "Sự khác biệt văn hóa", "description": "Thảo luận về sự khác biệt văn hóa giữa các quốc gia", "key_phrases": ["In my country...", "I think the difference is...", "It's interesting that..."]},
    ],
    "advanced": [
        {"topic": "Vấn đề xã hội", "description": "Thảo luận về các vấn đề xã hội hiện nay và quan điểm của bạn", "key_phrases": ["From my perspective...", "One of the major issues is...", "I believe that..."]},
        {"topic": "Phát triển khoa học công nghệ", "description": "Thảo luận về ảnh hưởng của công nghệ đối với cuộc sống", "key_phrases": ["Technology has revolutionized...", "The impact of... is significant", "In the future..."]},
        {"topic": "Bảo vệ môi trường", "description": "Thảo luận về các vấn đề môi trường và giải pháp", "key_phrases": ["We need to address...", "The consequences of... are...", "A possible solution would be..."]},
        {"topic": "Định hướng nghề nghiệp", "description": "Thảo luận về mục tiêu nghề nghiệp và kế hoạch tương lai", "key_phrases": ["My long-term goal is...", "I plan to...", "I'm working towards..."]},
    ]
}

# Các lỗi ngữ pháp thường gặp
COMMON_GRAMMAR_ERRORS = {
    "subject_verb_agreement": "Không hòa hợp chủ ngữ - động từ",
    "tense_error": "Lỗi thì",
    "article_error": "Lỗi sử dụng mạo từ",
    "preposition_error": "Lỗi giới từ",
    "word_order": "Sai thứ tự từ",
    "plural_singular": "Lỗi số ít/số nhiều",
}

# Lưu tiến độ học tập (trong thực tế nên dùng cơ sở dữ liệu)
student_progress = {}

@mcp.tool()
def generate_conversation_topic(level: str = "beginner", custom_interest: Optional[str] = None) -> dict:
    """
    Tạo chủ đề hội thoại và tình huống phù hợp với trình độ học viên.

    Tham số:
    - level: Trình độ tiếng Anh của học viên (beginner/intermediate/advanced)
    - custom_interest: Tuỳ chọn, chủ đề mà học viên quan tâm

    Trả về một dict chứa chủ đề, mô tả, cụm từ khóa và câu gợi ý bắt đầu hội thoại.
    """
    try:
        if level not in CONVERSATION_TOPICS:
            level = "beginner"
        
        topics = CONVERSATION_TOPICS[level]
        selected_topic = random.choice(topics)
        
        # Tạo câu gợi ý bắt đầu hội thoại
        conversation_starters = [
            f"Let's talk about {selected_topic['topic'].lower()}. Can you tell me about it?",
            f"I'd like to hear your thoughts on {selected_topic['topic'].lower()}.",
            f"Could you share your experience with {selected_topic['topic'].lower()}?",
        ]
        
        result = {
            "success": True,
            "level": level,
            "topic": selected_topic["topic"],
            "description": selected_topic["description"],
            "key_phrases": selected_topic["key_phrases"],
            "conversation_starter": random.choice(conversation_starters),
            "tips": f"Hãy thử sử dụng các cụm từ khóa được cung cấp và diễn đạt ý của bạn càng chi tiết càng tốt trong chủ đề này."
        }
        
        if custom_interest:
            result["custom_note"] = f"Đã chọn chủ đề liên quan dựa trên sở thích của bạn: '{custom_interest}'."
        
        logger.info(f"Generated topic: {selected_topic['topic']} for level: {level}")
        return result
        
    except Exception as e:
        logger.error(f"Error generating topic: {e}")
        return {"success": False, "error": str(e)}


# @mcp.tool()
# def correct_grammar(student_text: str, provide_explanation: bool = True) -> dict:
#     """
#     Kiểm tra và sửa lỗi ngữ pháp tiếng Anh cho học viên.
#     LƯU Ý SỬ DỤNG: Khi học viên đối thoại theo ngữ cảnh thì luôn luôn sử dụng công cụ này để kiểm tra ngữ pháp.

#     Tham số:
#     - student_text: Đoạn văn tiếng Anh do học viên nhập vào
#     - provide_explanation: Có cung cấp giải thích chi tiết lỗi hay không

#     Trả về: Văn bản đã sửa, loại lỗi và gợi ý học tập.
#     """
#     try:
#         # Đây là ví dụ đơn giản, thực tế nên tích hợp API kiểm tra ngữ pháp chuyên nghiệp
#         # Ví dụ: LanguageTool API, Grammarly API, v.v.

#         corrections = []
#         corrected_text = student_text
#         tips = []

#         # Ví dụ: kiểm tra một số lỗi phổ biến
#         error_patterns = {
#             "he don't": ("he doesn't", "subject_verb_agreement", "Động từ ngôi thứ ba số ít phải dùng 'doesn't' thay vì 'don't'"),
#             "she don't": ("she doesn't", "subject_verb_agreement", "Động từ ngôi thứ ba số ít phải dùng 'doesn't' thay vì 'don't'"),
#             "I goed": ("I went", "tense_error", "Quá khứ của 'go' là 'went', không phải 'goed'"),
#             "a apple": ("an apple", "article_error", "Trước nguyên âm phải dùng 'an' thay vì 'a'"),
#             "informations": ("information", "plural_singular", "'information' là danh từ không đếm được, không có dạng số nhiều"),
#         }

#         for error, (correction, error_type, explanation) in error_patterns.items():
#             if error.lower() in student_text.lower():
#                 corrections.append({
#                     "error": error,
#                     "correction": correction,
#                     "type": COMMON_GRAMMAR_ERRORS.get(error_type, error_type),
#                     "explanation": explanation if provide_explanation else None
#                 })
#                 corrected_text = corrected_text.replace(error, correction)

#         # Gợi ý học tập
#         if corrections:
#             error_types = set(c["type"] for c in corrections)
#             tips = [f"Nên tập trung luyện: {', '.join(error_types)}"]
#         else:
#             tips = ["Rất tốt! Không phát hiện lỗi ngữ pháp rõ ràng. Hãy tiếp tục phát huy!"]

#         result = {
#             "success": True,
#             "original_text": student_text,
#             "corrected_text": corrected_text,
#             "corrections": corrections,
#             "corrections_count": len(corrections),
#             "tips": tips,
#             "overall_assessment": "Xuất sắc" if len(corrections) == 0 else "Tốt" if len(corrections) <= 2 else "Cần cải thiện"
#         }

#         logger.info(f"Grammar check completed: {len(corrections)} corrections found")
#         return result

#     except Exception as e:
#         logger.error(f"Error in grammar correction: {e}")
#         return {"success": False, "error": str(e)}

@mcp.tool()
def correct_grammar_pro(student_text: str) -> dict:
    """
    Kiểm tra và sửa lỗi ngữ pháp tiếng Anh cho học viên.
    CÁCH SỬ DỤNG: Luôn luôn sử dụng công cụ này để kiểm tra ngữ pháp tiếng anh.

    Tham số:
    - student_text: Đoạn văn tiếng Anh mà học viên nói
    TRẢ VỀ: Một bản tóm tắt chi tiết các lỗi, vị trí và gợi ý thay thế để có thể giải thích lại cho học viên bằng tiếng việt.
    """

    try:
        url = "https://api.languagetool.org/v2/check"
        # Sử dụng POST để gửi được văn bản dài
        response = requests.post(url, data={'text': student_text, 'language': 'en-US'})
        response.raise_for_status()
        data = response.json()
        
        if not data.get('matches'):
            return {
                    "original_text": student_text,
                    "total_errors": 0,
                    "corrections": []
                }

        results = {
            "original_text": student_text,
            "total_errors": len(data['matches']),
            "corrections": []
        }

        for match in data['matches']:
            results["corrections"].append({
                "issue": match['message'],
                "suggested_replacements": [r['value'] for r in match['replacements']][:3],
                "wrong_part": match['context']['text'][match['context']['offset'] : match['context']['offset'] + match['context']['length']],
                "explanation": match['rule']['description'],
                "category": match['rule']['category']['name']
            })
        logger.info(f"Kết quả kiểm tra ngữ pháp:\n{results}")
        # Trả về dạng JSON string để AI dễ dàng phân tích
        return results

    except Exception as e:
        logger.error(f"Lỗi khi gọi tool sửa ngữ pháp: {str(e)}")
        return f"Lỗi khi gọi tool sửa ngữ pháp: {str(e)}"

@mcp.tool()
def suggest_vocabulary(context: str, level: str = "beginner") -> dict:
    """
    Gợi ý từ vựng và cụm từ liên quan dựa trên ngữ cảnh hội thoại.
    LƯU Ý SỬ DỤNG: Sử dụng khi đã chọn được 1 chủ đề đối thoại. Mục đích để gợi ý 1 vài từ vựng liên quan đến chủ đề. Nếu tool này không trả về bất kỳ từ vựng gợi ý nào thì bạn hãy tự nghĩ ra 1 vài từ vựng để gợi ý.
    Tham số:
    - context: Ngữ cảnh hoặc chủ đề hội thoại hiện tại
    - level: Trình độ tiếng Anh của học viên

    Trả về: Danh sách từ vựng, cụm từ, ví dụ và tình huống sử dụng liên quan.
    """
    try:
        # Ví dụ về cơ sở dữ liệu từ vựng (thực tế nên có database đầy đủ)
        vocabulary_database = {
            "travel": {
                "beginner": [
                    {"word": "destination", "meaning": "Điểm đến", "example": "Paris is my dream destination."},
                    {"word": "luggage", "meaning": "Hành lý", "example": "Don't forget to check your luggage."},
                    {"word": "journey", "meaning": "Chuyến đi", "example": "The journey was long but enjoyable."},
                ],
                "intermediate": [
                    {"word": "itinerary", "meaning": "Lịch trình", "example": "We planned a detailed itinerary for the trip."},
                    {"word": "accommodation", "meaning": "Chỗ ở", "example": "We booked accommodation near the beach."},
                    {"word": "venture", "meaning": "Mạo hiểm; khám phá", "example": "We ventured into the mountains."},
                ],
                "advanced": [
                    {"word": "wanderlust", "meaning": "Đam mê du lịch; thích đi đây đó", "example": "Her wanderlust led her to 50 countries."},
                    {"word": "nomadic", "meaning": "Du mục; lang thang", "example": "He lives a nomadic lifestyle."},
                    {"word": "embark", "meaning": "Bắt đầu; dấn thân vào", "example": "They embarked on a journey across Asia."},
                ]
            },
            "work": {
                "beginner": [
                    {"word": "colleague", "meaning": "Đồng nghiệp", "example": "My colleagues are very friendly."},
                    {"word": "office", "meaning": "Văn phòng", "example": "I work in an office downtown."},
                    {"word": "meeting", "meaning": "Cuộc họp", "example": "We have a meeting at 2 PM."},
                ],
                "intermediate": [
                    {"word": "deadline", "meaning": "Hạn chót", "example": "The deadline for this project is next Friday."},
                    {"word": "collaborate", "meaning": "Hợp tác", "example": "We collaborate with the marketing team."},
                    {"word": "efficiency", "meaning": "Hiệu quả", "example": "We need to improve our efficiency."},
                ],
                "advanced": [
                    {"word": "synergy", "meaning": "Hiệu ứng cộng hưởng", "example": "The synergy between teams increased productivity."},
                    {"word": "delegate", "meaning": "Giao việc; ủy quyền", "example": "Learn to delegate tasks effectively."},
                    {"word": "stakeholder", "meaning": "Người liên quan/lợi ích", "example": "We need to consider all stakeholders."},
                ]
            }
        }

        # Ghép chủ đề dựa trên từ khóa đơn giản
        matched_category = "general"
        for category in vocabulary_database:
            if category in context.lower():
                matched_category = category
                break

        # Lấy danh sách từ vựng
        if matched_category in vocabulary_database:
            vocab_list = vocabulary_database[matched_category].get(level, vocabulary_database[matched_category]["beginner"])
        else:
            # Mặc định trả về từ vựng chủ đề công việc
            vocab_list = vocabulary_database["work"].get(level, vocabulary_database["work"]["beginner"])

        result = {
            "success": True,
            "context": context,
            "level": level,
            "category": matched_category,
            "vocabulary": vocab_list,
            "count": len(vocab_list),
            "study_tip": "Nên học 3-5 từ mới mỗi ngày và cố gắng sử dụng chúng trong hội thoại."
        }

        logger.info(f"Suggested {len(vocab_list)} vocabulary items for context: {context}")
        return result

    except Exception as e:
        logger.error(f"Lỗi khi gợi ý từ vựng: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def evaluate_response(student_response: str, expected_topic: str, level: str = "beginner") -> dict:
    """
    Đánh giá chất lượng câu trả lời của học viên, cung cấp phản hồi chi tiết.
    LƯU Ý SỬ DỤNG: Sử dụng sau khi kiểm tra lỗi ngữ pháp xong. Nếu có lỗi ngữ pháp thì không cần sử dụng tool này, nếu kiểm tra ngữ pháp đúng thì hãy sử dụng tool này.
    Tham số:
    - student_response: Câu trả lời tiếng Anh của học viên
    - expected_topic: Chủ đề hoặc câu hỏi dự kiến
    - level: Trình độ tiếng Anh của học viên

    Trả về: Điểm số, điểm mạnh, gợi ý cải thiện và lời động viên.
    """
    try:
        # Các tiêu chí đánh giá
        word_count = len(student_response.split())
        sentence_count = student_response.count('.') + student_response.count('!') + student_response.count('?')

        # Tiêu chuẩn chấm điểm (đơn giản)
        score = 0
        feedback = {
            "strengths": [],
            "improvements": [],
            "encouragement": ""
        }

        # Đánh giá độ dài câu trả lời
        if word_count >= 50:
            score += 3
            feedback["strengths"].append("Câu trả lời đầy đủ, diễn đạt chi tiết")
        elif word_count >= 30:
            score += 2
            feedback["strengths"].append("Câu trả lời vừa phải")
        else:
            score += 1
            feedback["improvements"].append("Hãy cố gắng trả lời chi tiết hơn, thêm ví dụ và ý phụ")

        # Đánh giá cấu trúc câu
        if sentence_count >= 3:
            score += 2
            feedback["strengths"].append("Sử dụng nhiều câu, cấu trúc rõ ràng")
        else:
            feedback["improvements"].append("Hãy dùng nhiều câu hơn để diễn đạt, giúp nội dung mạch lạc hơn")

        # Đánh giá độ phức tạp (kiểm tra đơn giản)
        complex_indicators = ["because", "although", "however", "moreover", "furthermore", "therefore"]
        complex_count = sum(1 for word in complex_indicators if word in student_response.lower())
        if complex_count >= 2:
            score += 3
            feedback["strengths"].append("Có sử dụng liên từ, thể hiện tư duy logic tốt")
        elif complex_count >= 1:
            score += 2
            feedback["strengths"].append("Có sử dụng liên từ")
        else:
            feedback["improvements"].append("Hãy thử dùng các liên từ (như because, however, moreover) để diễn đạt mạch lạc hơn")

        # Đánh giá mức độ liên quan chủ đề
        if expected_topic.lower() in student_response.lower():
            score += 2
            feedback["strengths"].append("Bám sát chủ đề, nội dung liên quan")

        # Chuẩn hóa điểm về thang 0-100
        final_score = min(100, (score / 10) * 100)

        # Sinh lời động viên
        if final_score >= 80:
            feedback["encouragement"] = "Rất tuyệt! Bạn diễn đạt rất tốt, hãy tiếp tục phát huy nhé! 💪"
        elif final_score >= 60:
            feedback["encouragement"] = "Làm tốt lắm! Bạn đang tiến bộ, hãy cố gắng hơn nữa! 👍"
        else:
            feedback["encouragement"] = "Nỗ lực tốt! Mỗi lần luyện tập là một bước tiến, tiếp tục cố gắng nhé! 🌟"

        result = {
            "success": True,
            "score": round(final_score, 1),
            "level": level,
            "statistics": {
                "word_count": word_count,
                "sentence_count": sentence_count,
                "complex_structures": complex_count
            },
            "feedback": feedback,
            "next_steps": [
                "Tiếp tục luyện tập các chủ đề tương tự",
                "Thử sử dụng các từ mới đã học hôm nay",
                "Luyện nói và ghi âm, chú ý phát âm và ngữ điệu"
            ]
        }

        logger.info(f"Đã đánh giá câu trả lời: score={final_score}, words={word_count}")
        return result

    except Exception as e:
        logger.error(f"Lỗi khi đánh giá câu trả lời: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def pronunciation_tips(word_or_phrase: str) -> dict:
    """
    Cung cấp gợi ý và mẹo phát âm.
    LƯU Ý SỬ DỤNG: Khi học viên đối thoại theo ngữ cảnh thì luôn luôn sử dụng công cụ này để kiểm tra phát âm.
    Tham số:
    - word_or_phrase: Từ hoặc cụm từ cần hướng dẫn phát âm

    Trả về: Hướng dẫn phát âm, lỗi thường gặp và gợi ý luyện tập.
    """
    try:
        # Cơ sở dữ liệu mẹo phát âm (ví dụ)
        pronunciation_guide = {
            "th": {
                "sounds": ["θ (thin)", "ð (this)"],
                "tip": "Đặt đầu lưỡi chạm nhẹ vào mặt sau răng trên, để luồng khí đi qua",
                "common_errors": "Người nói tiếng Trung dễ phát thành âm 's' hoặc 'z'",
                "practice_words": ["think", "this", "mother", "thank"]
            },
            "r": {
                "sounds": ["ɹ (red)"],
                "tip": "Cuộn đầu lưỡi lên nhưng không chạm vào bất kỳ vị trí nào trong khoang miệng",
                "common_errors": "Dễ phát thành âm 'r' trong tiếng Việt hoặc tiếng Trung",
                "practice_words": ["red", "right", "road", "around"]
            },
            "v": {
                "sounds": ["v (very)"],
                "tip": "Răng trên chạm nhẹ vào môi dưới, dây thanh rung",
                "common_errors": "Dễ nhầm với âm 'w'",
                "practice_words": ["very", "view", "voice", "victory"]
            }
        }

        # Kiểm tra các âm cần chú ý đặc biệt
        tips = []
        practice_suggestions = []

        word_lower = word_or_phrase.lower()
        for sound, guide in pronunciation_guide.items():
            if sound in word_lower:
                tips.append({
                    "sound": sound,
                    "sounds_like": guide["sounds"],
                    "tip": guide["tip"],
                    "common_error": guide["common_errors"],
                    "practice_words": guide["practice_words"]
                })

        # Gợi ý chung
        general_tips = [
            "Chú ý vị trí trọng âm, có thể tra từ điển để xác nhận",
            "Bắt chước phát âm của người bản xứ, sử dụng chức năng phát âm trên từ điển online",
            "Ghi âm lại phát âm của mình và so sánh với phát âm chuẩn",
            "Nói chậm lại để đảm bảo phát âm đúng từng âm"
        ]

        result = {
            "success": True,
            "word_or_phrase": word_or_phrase,
            "specific_tips": tips if tips else "Không phát hiện khó khăn phát âm đặc biệt",
            "general_tips": general_tips,
            "recommendation": "Nên nghe phát âm chuẩn trên từ điển online (như Cambridge Dictionary, Merriam-Webster)",
            "practice_method": "Luyện tập 5-10 phút mỗi ngày, lặp lại từ/cụm từ cho đến khi thành thạo"
        }

        logger.info(f"Đã cung cấp mẹo phát âm cho: {word_or_phrase}")
        return result

    except Exception as e:
        logger.error(f"Lỗi khi cung cấp mẹo phát âm: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def track_progress(student_id: str, session_data: dict) -> dict:
    """
    Theo dõi và ghi nhận tiến độ học tập của học viên.

    Tham số:
    - student_id: Mã định danh duy nhất của học viên
    - session_data: Dữ liệu buổi học hiện tại (bao gồm chủ đề, điểm số, v.v.)

    Trả về: Thống kê học tập và phân tích tiến bộ.
    """
    try:
        # Khởi tạo hồ sơ học viên nếu chưa có
        if student_id not in student_progress:
            student_progress[student_id] = {
                "sessions": [],
                "total_sessions": 0,
                "topics_covered": set(),
                "average_score": 0,
                "start_date": datetime.now().isoformat()
            }

        # Thêm dữ liệu buổi học mới
        session_entry = {
            "date": datetime.now().isoformat(),
            "topic": session_data.get("topic", "Chưa xác định"),
            "score": session_data.get("score", 0),
            "duration": session_data.get("duration", 0),
            "level": session_data.get("level", "beginner")
        }

        student_progress[student_id]["sessions"].append(session_entry)
        student_progress[student_id]["total_sessions"] += 1
        student_progress[student_id]["topics_covered"].add(session_data.get("topic", "Chưa xác định"))

        # Tính điểm trung bình
        all_scores = [s["score"] for s in student_progress[student_id]["sessions"]]
        student_progress[student_id]["average_score"] = sum(all_scores) / len(all_scores)

        # Phân tích tiến bộ
        progress_analysis = "Tiến bộ ổn định"
        if len(all_scores) >= 3:
            recent_avg = sum(all_scores[-3:]) / 3
            earlier_avg = sum(all_scores[:-3]) / len(all_scores[:-3]) if len(all_scores) > 3 else all_scores[0]

            if recent_avg > earlier_avg + 10:
                progress_analysis = "Tiến bộ rõ rệt"
            elif recent_avg > earlier_avg:
                progress_analysis = "Tiến bộ ổn định"
            elif recent_avg < earlier_avg - 10:
                progress_analysis = "Cần luyện tập thêm"
            else:
                progress_analysis = "Giữ vững phong độ"

        result = {
            "success": True,
            "student_id": student_id,
            "total_sessions": student_progress[student_id]["total_sessions"],
            "topics_covered": len(student_progress[student_id]["topics_covered"]),
            "average_score": round(student_progress[student_id]["average_score"], 1),
            "current_session": session_entry,
            "progress_analysis": progress_analysis,
            "recent_scores": all_scores[-5:],  # 5 điểm gần nhất
            "recommendation": "Nên luyện tập ít nhất 3-4 lần/tuần, mỗi lần 20-30 phút" if student_progress[student_id]["total_sessions"] < 10 else "Hãy duy trì thói quen học tập tốt!"
        }

        logger.info(f"Đã cập nhật tiến độ cho học viên: {student_id}, tổng số buổi: {student_progress[student_id]['total_sessions']}")
        return result

    except Exception as e:
        logger.error(f"Lỗi khi theo dõi tiến độ: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def create_practice_scenario(scenario_type: str = "daily_conversation", level: str = "beginner") -> dict:
    """
    Tạo tình huống luyện tập đóng vai.

    Tham số:
    - scenario_type: Loại tình huống (daily_conversation/business/travel/interview)
    - level: Mức độ khó

    Trả về: Mô tả tình huống, vai trò và gợi ý hội thoại.
    """
    try:
        scenarios = {
            "daily_conversation": {
                "beginner": {
                    "title": "Gọi món ở quán cà phê",
                    "setting": "Bạn đang ở một quán cà phê và muốn gọi một ly cà phê cùng một số đồ ăn nhẹ",
                    "your_role": "Khách hàng",
                    "ai_role": "Nhân viên quán cà phê",
                    "objectives": ["Chào hỏi", "Gọi món", "Hỏi giá", "Thanh toán", "Nói cảm ơn"],
                    "useful_phrases": [
                        "I'd like to order...",
                        "How much is...?",
                        "Can I have...?",
                        "Here you are.",
                        "Thank you!"
                    ]
                },
                "intermediate": {
                    "title": "Xem nhà thuê",
                    "setting": "Bạn đang tìm căn hộ mới, bây giờ bạn sẽ đi xem nhà và hỏi thông tin chi tiết với chủ nhà",
                    "your_role": "Người thuê nhà",
                    "ai_role": "Chủ nhà",
                    "objectives": ["Hỏi giá thuê và tiền đặt cọc", "Tìm hiểu tiện nghi phòng", "Hỏi về giao thông xung quanh", "Thảo luận điều khoản hợp đồng"],
                    "useful_phrases": [
                        "How much is the monthly rent?",
                        "Is the apartment furnished?",
                        "What's included in the rent?",
                        "Are pets allowed?",
                        "When can I move in?"
                    ]
                }
            },
            "business": {
                "intermediate": {
                    "title": "Họp dự án",
                    "setting": "Bạn đang tham gia một cuộc họp tiến độ dự án",
                    "your_role": "Thành viên dự án",
                    "ai_role": "Quản lý dự án",
                    "objectives": ["Báo cáo tiến độ", "Thảo luận vấn đề", "Đề xuất ý kiến", "Xác nhận bước tiếp theo"],
                    "useful_phrases": [
                        "I've completed...",
                        "We're facing some challenges with...",
                        "I suggest we...",
                        "What's our next step?",
                        "Let me clarify..."
                    ]
                },
                "advanced": {
                    "title": "Đàm phán kinh doanh",
                    "setting": "Bạn đại diện công ty tham gia đàm phán hợp tác với đối tác tiềm năng",
                    "your_role": "Đại diện kinh doanh",
                    "ai_role": "Đại diện đối tác",
                    "objectives": ["Giới thiệu phương án hợp tác", "Thảo luận điều khoản", "Xử lý phản đối", "Đạt được thỏa thuận"],
                    "useful_phrases": [
                        "We propose...",
                        "That's a valid concern...",
                        "Perhaps we could compromise on...",
                        "Let's find a win-win solution...",
                        "I believe we can reach an agreement..."
                    ]
                }
            },
            "travel": {
                "beginner": {
                    "title": "Hỏi đường ở sân bay",
                    "setting": "Bạn đang ở sân bay và cần tìm cổng lên máy bay",
                    "your_role": "Hành khách",
                    "ai_role": "Nhân viên sân bay",
                    "objectives": ["Hỏi vị trí cổng lên máy bay", "Hỏi cách đi đến đó", "Xác nhận thời gian"],
                    "useful_phrases": [
                        "Excuse me, where is gate...?",
                        "How do I get to...?",
                        "Is it far from here?",
                        "Thank you for your help!"
                    ]
                },
                "intermediate": {
                    "title": "Nhận phòng khách sạn",
                    "setting": "Bạn vừa đến khách sạn và chuẩn bị làm thủ tục nhận phòng",
                    "your_role": "Khách lưu trú",
                    "ai_role": "Lễ tân khách sạn",
                    "objectives": ["Nhận phòng", "Hỏi về tiện nghi", "Yêu cầu đặc biệt", "Tìm hiểu thông tin xung quanh"],
                    "useful_phrases": [
                        "I have a reservation under...",
                        "What time is breakfast served?",
                        "Could I have a room with...?",
                        "What are some good restaurants nearby?"
                    ]
                }
            }
        }

        # Lấy tình huống
        if scenario_type not in scenarios:
            scenario_type = "daily_conversation"

        scenario_category = scenarios[scenario_type]
        if level not in scenario_category:
            level = "beginner" if "beginner" in scenario_category else list(scenario_category.keys())[0]

        selected_scenario = scenario_category[level]

        result = {
            "success": True,
            "scenario_type": scenario_type,
            "level": level,
            "title": selected_scenario["title"],
            "setting": selected_scenario["setting"],
            "your_role": selected_scenario["your_role"],
            "ai_role": selected_scenario["ai_role"],
            "objectives": selected_scenario["objectives"],
            "useful_phrases": selected_scenario["useful_phrases"],
            "start_prompt": f"Tình huống: {selected_scenario['setting']}\nVai của bạn: {selected_scenario['your_role']}\nHãy bắt đầu hội thoại!",
            "tips": "Hãy cố gắng sử dụng ngôn ngữ tự nhiên, đừng ngại mắc lỗi. Quan trọng là bạn dám luyện nói!"
        }

        logger.info(f"Đã tạo tình huống luyện tập: {selected_scenario['title']}")
        return result

    except Exception as e:
        logger.error(f"Lỗi khi tạo tình huống luyện tập: {e}")
        return {"success": False, "error": str(e)}


# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")


