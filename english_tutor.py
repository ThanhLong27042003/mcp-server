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


