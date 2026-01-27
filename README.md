# 🎓 ENGLISH TUTOR MCP SERVER - HƯỚNG DẪN SỬ DỤNG

## 📋 Tổng quan

Đây là một MCP (Model Context Protocol) Server được thiết kế để dạy tiếng Anh giao tiếp cho người Việt Nam, đặc biệt là trẻ em. Hệ thống được xây dựng dựa trên khung CEFR (Common European Framework of Reference for Languages).

## 🎯 Đặc điểm nổi bật

### ✨ Cấu trúc dữ liệu đầy đủ theo yêu cầu:
- **Từ vựng chi tiết**: Mỗi từ có phiên âm, nghĩa tiếng Việt, và câu ví dụ song ngữ
- **Câu hỏi dẫn dắt**: 8-10 câu hỏi để duy trì hội thoại tự nhiên
- **Đoạn văn mẫu**: 3 mức độ (basic, intermediate, advanced) với bản dịch
- **Tình huống đóng vai**: Chi tiết bối cảnh, vai trò, mục tiêu và câu mở đầu

### 🎓 Hỗ trợ đa cấp độ CEFR:
- **A1** (Beginner): FAMILY, PETS, COLORS
- **A2** (Elementary): SHOPPING, và nhiều chủ đề khác
- **B1** (Intermediate): TRAVEL, và nhiều chủ đề khác
- Dễ dàng mở rộng thêm cấp độ B2, C1, C2

### 🛠️ Công cụ (Tools) đầy đủ:

1. **list_all_topics(level)** - Liệt kê tất cả chủ đề theo cấp độ
2. **get_topic_vocabulary(level, topic)** - Lấy từ vựng chủ đề
3. **get_guiding_questions(level, topic)** - Lấy câu hỏi dẫn dắt
4. **get_sample_paragraphs(level, topic)** - Lấy đoạn văn mẫu
5. **get_role_play_scenarios(level, topic)** - Lấy tình huống đóng vai
6. **start_conversation(level, topic)** - Bắt đầu buổi học
7. **correct_grammar_pro(student_text)** - Kiểm tra ngữ pháp
8. **evaluate_response(student_response, topic, level)** - Đánh giá câu trả lời
9. **pronunciation_tips(word_or_phrase)** - Gợi ý phát âm

## 📚 Cấu trúc dữ liệu mẫu

### Ví dụ một chủ đề hoàn chỉnh (FAMILY - Cấp A1):

```python
"FAMILY": {
    "topic_name": "FAMILY (GIA ĐÌNH)",
    
    # 1. Bộ từ vựng
    "vocabulary": [
        {
            "word": "Mother",
            "phonetic": "/ˈmʌðər/",
            "meaning": "Mẹ",
            "example": "My mother is a teacher.",
            "example_vi": "Mẹ tôi là giáo viên."
        },
        # ... 10+ từ vựng
    ],
    
    # 2. Câu hỏi dẫn dắt
    "guiding_questions": [
        {
            "question": "How many people are there in your family?",
            "question_vi": "Gia đình bạn có bao nhiêu người?"
        },
        # ... 8-10 câu hỏi
    ],
    
    # 3. Đoạn văn mẫu
    "sample_paragraphs": [
        {
            "level": "basic",
            "text": "My name is Mai. I am 8 years old...",
            "text_vi": "Tên tôi là Mai. Tôi 8 tuổi..."
        },
        # ... 2-3 đoạn văn
    ],
    
    # 4. Tình huống đóng vai
    "role_play_scenarios": [
        {
            "scenario_name": "Giới thiệu gia đình với bạn mới",
            "context": "Học viên đang giới thiệu...",
            "ai_role": "Bạn học mới...",
            "student_role": "Giới thiệu về các thành viên...",
            "goal": "Luyện tập nói về số lượng...",
            "opening_line": "Hi! I'm new here...",
            "opening_line_vi": "Chào bạn! Mình là học sinh mới..."
        },
        # ... 3-5 tình huống
    ]
}
```

## 🚀 Quy trình dạy học

### Bước 1: Xác định trình độ và chủ đề
```python
# AI hỏi trình độ học viên
# Sau đó gọi:
list_all_topics(level="A1")

# Học viên chọn chủ đề, AI gọi:
start_conversation(level="A1", topic="FAMILY")
```

### Bước 2: Cung cấp tài liệu
```python
# Khi học viên cần từ vựng:
get_topic_vocabulary(level="A1", topic="FAMILY")

# Khi cần câu hỏi thêm:
get_guiding_questions(level="A1", topic="FAMILY")

# Khi cần tham khảo mẫu:
get_sample_paragraphs(level="A1", topic="FAMILY")

# Khi đóng vai:
get_role_play_scenarios(level="A1", topic="FAMILY")
```

### Bước 3: Kiểm tra và đánh giá
```python
# 1. LUÔN kiểm tra ngữ pháp trước
result = correct_grammar_pro("There is 4 people in my family")

# 2. Nếu có lỗi (total_errors > 0):
#    - Giải thích lỗi
#    - Yêu cầu sửa lại
#    - KHÔNG đánh giá

# 3. Nếu không có lỗi (total_errors == 0):
evaluate_response(
    student_response="There are 4 people in my family",
    expected_topic="FAMILY",
    level="A1"
)

# 4. Nếu học viên hỏi về phát âm:
pronunciation_tips("mother")
```

## 📝 Cách thêm chủ đề mới

### Bước 1: Chọn cấp độ và tên chủ đề
```python
# Ví dụ: Thêm chủ đề FOOD vào cấp độ A1
"A1": {
    "FOOD": {
        # ... nội dung
    }
}
```

### Bước 2: Điền đầy đủ 4 phần

#### 1. Vocabulary (10-15 từ)
```python
"vocabulary": [
    {
        "word": "Apple",
        "phonetic": "/ˈæpl/",
        "meaning": "Táo",
        "example": "I eat an apple every day.",
        "example_vi": "Tôi ăn một quả táo mỗi ngày."
    },
    # ... thêm từ vựng
]
```

#### 2. Guiding Questions (8-10 câu)
```python
"guiding_questions": [
    {
        "question": "What is your favorite food?",
        "question_vi": "Món ăn yêu thích của bạn là gì?"
    },
    # ... thêm câu hỏi
]
```

#### 3. Sample Paragraphs (3 mức độ)
```python
"sample_paragraphs": [
    {
        "level": "basic",
        "text": "I like pizza. Pizza is delicious...",
        "text_vi": "Tôi thích pizza. Pizza rất ngon..."
    },
    {
        "level": "intermediate",
        "text": "My favorite food is Vietnamese pho...",
        "text_vi": "Món ăn yêu thích của tôi là phở Việt Nam..."
    },
    {
        "level": "advanced",
        "text": "In my opinion, food is not just about nutrition...",
        "text_vi": "Theo tôi, đồ ăn không chỉ là dinh dưỡng..."
    }
]
```

#### 4. Role Play Scenarios (3-5 tình huống)
```python
"role_play_scenarios": [
    {
        "scenario_name": "Gọi món ở nhà hàng",
        "context": "Học viên đang ở nhà hàng và muốn gọi món.",
        "ai_role": "Phục vụ nhà hàng",
        "student_role": "Khách hàng",
        "goal": "Luyện tập gọi món, hỏi về đồ ăn",
        "opening_line": "Good evening! Are you ready to order?",
        "opening_line_vi": "Chào buổi tối! Bạn sẵn sàng gọi món chưa?"
    },
    # ... thêm tình huống
]
```

## 🎨 Ví dụ về một buổi học

```
Teacher (AI): Chào bạn! Mình là Mobi. Bạn đang ở trình độ nào? (A1, A2, B1...)

Student: A1

Teacher: [calls list_all_topics("A1")]
Tuyệt! Với A1, chúng ta có:
1. FAMILY (Gia đình) 👨‍👩‍👧‍👦
2. PETS (Thú cưng) 🐶🐱
3. COLORS (Màu sắc) 🎨
Bạn chọn chủ đề nào?

Student: Family

Teacher: [calls start_conversation("A1", "FAMILY")]
Perfect! Hãy trả lời: "How many people are there in your family?"

Student: Can I see vocabulary first?

Teacher: [calls get_topic_vocabulary("A1", "FAMILY")]
Được chứ! Đây là từ vựng:

📚 VOCABULARY:
1. Family /ˈfæməli/ - Gia đình
   → "I love my family."

2. Mother /ˈmʌðər/ - Mẹ
   → "My mother is a teacher."
[... hiển thị tất cả từ]

Bây giờ hãy trả lời câu hỏi nhé!

Student: There is 4 people in my family.

Teacher: [calls correct_grammar_pro("There is 4 people in my family.")]
Mình thấy 1 lỗi:

❌ "There is 4 people"
✅ Sửa: "There are 4 people"
💡 Với số nhiều phải dùng "are"

Bạn thử lại nhé!

Student: There are 4 people in my family.

Teacher: [calls correct_grammar_pro("There are 4 people in my family.")]
[calls evaluate_response(...)]

Excellent! Ngữ pháp đúng 100%! 🎉
⭐ Điểm: 75/100
👍 Điểm mạnh: Câu đúng ngữ pháp, bám chủ đề

Bây giờ hãy kể thêm về các thành viên nhé!
```

## 🔧 Cài đặt và chạy

### Yêu cầu:
```bash
pip install mcp requests
```

### Chạy server:
```bash
python english_tutor_enhanced.py
```

### Kết nối với Claude Desktop:

Thêm vào file config của Claude Desktop:
```json
{
  "mcpServers": {
    "english-tutor": {
      "command": "python",
      "args": ["/path/to/english_tutor_enhanced.py"],
      "env": {}
    }
  }
}
```

## 📊 Thống kê hiện tại

- **Cấp độ**: 3 (A1, A2, B1)
- **Tổng chủ đề**: 6
  - A1: FAMILY, PETS, COLORS
  - A2: SHOPPING
  - B1: TRAVEL
- **Từ vựng**: ~50+ từ
- **Câu hỏi**: ~40+ câu
- **Đoạn văn mẫu**: ~10+ đoạn
- **Tình huống đóng vai**: ~8+ tình huống

## 🎯 Kế hoạch mở rộng

### Thêm chủ đề cho A1:
- SCHOOL (Trường học)
- TOYS (Đồ chơi)
- WEATHER (Thời tiết)
- FOOD (Đồ ăn)
- CLOTHES (Quần áo)

### Thêm cấp độ cao hơn:
- B2: Business English, Academic English
- C1: Advanced topics (Science, Politics, Culture)
- C2: Professional topics

### Thêm tính năng:
- Theo dõi tiến độ chi tiết hơn
- Gamification (điểm thưởng, huy hiệu)
- Bài tập về nhà tự động
- Báo cáo tiến độ cho phụ huynh

## 💡 Gợi ý sử dụng

1. **Cho trẻ em**: Tập trung vào A1-A2 với chủ đề gần gũi
2. **Cho người lớn**: Có thể bắt đầu từ B1 với chủ đề thực tế hơn
3. **Luyện thi**: Sử dụng các cấp độ B2-C1
4. **Giao tiếp hàng ngày**: Tập trung vào tình huống đóng vai

## 🤝 Đóng góp

Để thêm chủ đề mới, chỉ cần:
1. Copy cấu trúc của một chủ đề có sẵn
2. Thay đổi nội dung phù hợp
3. Đảm bảo đầy đủ 4 phần: vocabulary, questions, paragraphs, scenarios
4. Test kỹ với tool start_conversation

## 📧 Liên hệ

Nếu có câu hỏi hoặc đề xuất, vui lòng liên hệ qua issues hoặc pull requests.

---

**Made with ❤️ for Vietnamese English learners**