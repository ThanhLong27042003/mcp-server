# english_tutor_enhanced.py
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

# ========================================
# CƠ SỞ DỮ LIỆU TỪ VỰNG VÀ CHỦ ĐỀ
# ========================================

LESSON_DATABASE = {
    "A1": {
        "FAMILY": {
            "topic_name": "FAMILY (GIA ĐÌNH)",
            "vocabulary": [
                {
                    "word": "Family",
                    "phonetic": "/ˈfæməli/",
                    "meaning": "Gia đình",
                    "example": "I love my family.",
                    "example_vi": "Tôi yêu gia đình mình."
                },
                {
                    "word": "Mother",
                    "phonetic": "/ˈmʌðər/",
                    "meaning": "Mẹ",
                    "example": "My mother is a teacher.",
                    "example_vi": "Mẹ tôi là giáo viên."
                },
                {
                    "word": "Father",
                    "phonetic": "/ˈfɑːðər/",
                    "meaning": "Bố",
                    "example": "My father works in an office.",
                    "example_vi": "Bố tôi làm việc ở văn phòng."
                },
                {
                    "word": "Sister",
                    "phonetic": "/ˈsɪstər/",
                    "meaning": "Chị/Em gái",
                    "example": "I have one younger sister.",
                    "example_vi": "Tôi có một em gái."
                },
                {
                    "word": "Brother",
                    "phonetic": "/ˈbrʌðər/",
                    "meaning": "Anh/Em trai",
                    "example": "My brother is 10 years old.",
                    "example_vi": "Em trai tôi 10 tuổi."
                },
                {
                    "word": "Grandmother",
                    "phonetic": "/ˈɡrænmʌðər/",
                    "meaning": "Bà",
                    "example": "My grandmother lives with us.",
                    "example_vi": "Bà tôi sống cùng chúng tôi."
                },
                {
                    "word": "Grandfather",
                    "phonetic": "/ˈɡrænfɑːðər/",
                    "meaning": "Ông",
                    "example": "My grandfather is very kind.",
                    "example_vi": "Ông tôi rất tốt bụng."
                },
                {
                    "word": "Parents",
                    "phonetic": "/ˈperənts/",
                    "meaning": "Bố mẹ",
                    "example": "My parents work hard.",
                    "example_vi": "Bố mẹ tôi làm việc chăm chỉ."
                },
                {
                    "word": "Live",
                    "phonetic": "/lɪv/",
                    "meaning": "Sống",
                    "example": "I live with my parents.",
                    "example_vi": "Tôi sống cùng bố mẹ."
                },
                {
                    "word": "Love",
                    "phonetic": "/lʌv/",
                    "meaning": "Yêu",
                    "example": "We love each other.",
                    "example_vi": "Chúng tôi yêu thương nhau."
                }
            ],
            "guiding_questions": [
                {
                    "question": "How many people are there in your family?",
                    "question_vi": "Gia đình bạn có bao nhiêu người?"
                },
                {
                    "question": "Can you tell me about your mom/dad?",
                    "question_vi": "Bạn có thể kể cho mình nghe về mẹ/bố của bạn không?"
                },
                {
                    "question": "What does your father/mother do?",
                    "question_vi": "Bố/mẹ bạn làm nghề gì?"
                },
                {
                    "question": "Do you have any brothers or sisters?",
                    "question_vi": "Bạn có anh chị em nào không?"
                },
                {
                    "question": "What do you like to do with your family?",
                    "question_vi": "Bạn thích làm gì cùng gia đình?"
                },
                {
                    "question": "Who do you look like in your family?",
                    "question_vi": "Bạn giống ai trong gia đình?"
                },
                {
                    "question": "What is your mom/dad like?",
                    "question_vi": "Mẹ/bố bạn là người thế nào? (tính cách)"
                },
                {
                    "question": "Do you live with your grandparents?",
                    "question_vi": "Bạn có sống cùng ông bà không?"
                },
                {
                    "question": "Who cooks in your family?",
                    "question_vi": "Ai nấu ăn trong gia đình bạn?"
                },
                {
                    "question": "Do you help your parents at home?",
                    "question_vi": "Bạn có giúp bố mẹ việc nhà không?"
                }
            ],
            "sample_paragraphs": [
                {
                    "level": "basic",
                    "text": "My name is Mai. I am 8 years old. There are four people in my family. I have a mom, a dad, and a younger brother. I love my family very much.",
                    "text_vi": "Tên tôi là Mai. Tôi 8 tuổi. Gia đình tôi có 4 người. Tôi có mẹ, bố và một em trai. Tôi yêu gia đình mình rất nhiều."
                },
                {
                    "level": "intermediate",
                    "text": "I live with my parents and my older sister. My father is a doctor and my mother is a nurse. They both work at the hospital. My sister is 15 years old. She helps me with my homework every day.",
                    "text_vi": "Tôi sống với bố mẹ và chị gái. Bố tôi là bác sĩ và mẹ tôi là y tá. Cả hai đều làm việc ở bệnh viện. Chị tôi 15 tuổi. Chị ấy giúp tôi làm bài tập mỗi ngày."
                },
                {
                    "level": "advanced",
                    "text": "My family is very close-knit. Every Sunday, we have dinner together at my grandmother's house. My dad is funny and always makes us laugh. My mom is kind and caring. She cooks delicious meals for us. Although we sometimes argue, we always support each other.",
                    "text_vi": "Gia đình tôi rất gắn bó. Mỗi Chủ nhật, chúng tôi ăn tối cùng nhau tại nhà bà. Bố tôi hài hước và luôn làm chúng tôi cười. Mẹ tôi tốt bụng và chu đáo. Bà nấu những bữa ăn ngon cho chúng tôi. Mặc dù đôi khi chúng tôi cãi nhau, nhưng chúng tôi luôn ủng hộ nhau."
                }
            ],
            "role_play_scenarios": [
                {
                    "scenario_name": "Giới thiệu gia đình với bạn mới",
                    "context": "Học viên đang giới thiệu gia đình mình với một người bạn mới ở trường.",
                    "ai_role": "Bạn học mới, tò mò muốn biết về gia đình của học viên.",
                    "student_role": "Giới thiệu về các thành viên trong gia đình.",
                    "goal": "Luyện tập nói về số lượng thành viên, nghề nghiệp, và mối quan hệ.",
                    "opening_line": "Hi! I'm new here. Nice to meet you! Can you tell me about your family?",
                    "opening_line_vi": "Chào bạn! Mình là học sinh mới. Rất vui được gặp bạn! Bạn có thể kể cho mình nghe về gia đình bạn không?"
                },
                {
                    "scenario_name": "Xem ảnh gia đình",
                    "context": "Học viên đang ở nhà bạn và bạn ấy hỏi về gia đình.",
                    "ai_role": "Bạn thân của học viên, đang xem ảnh gia đình và đặt câu hỏi.",
                    "student_role": "Mô tả từng người trong ảnh (ngoại hình, tính cách).",
                    "goal": "Luyện miêu tả ngoại hình và tính cách.",
                    "opening_line": "Wow, is this your family photo? Who is this person here?",
                    "opening_line_vi": "Wao, đây là ảnh gia đình bạn à? Người này là ai thế?"
                },
                {
                    "scenario_name": "Kể về ngày nghỉ cuối tuần",
                    "context": "Học viên kể về những hoạt động cuối tuần với gia đình.",
                    "ai_role": "Bạn bè quan tâm đến hoạt động của học viên.",
                    "student_role": "Chia sẻ hoạt động cuối tuần với gia đình.",
                    "goal": "Luyện tập kể chuyện về thời gian với gia đình.",
                    "opening_line": "What did you do with your family last weekend?",
                    "opening_line_vi": "Bạn đã làm gì với gia đình cuối tuần vừa rồi?"
                }
            ]
        },
        "PETS": {
            "topic_name": "PETS (THÚ CƯNG)",
            "vocabulary": [
                {
                    "word": "Dog",
                    "phonetic": "/dɔːɡ/",
                    "meaning": "Chó",
                    "example": "I have a small dog.",
                    "example_vi": "Tôi có một con chó nhỏ."
                },
                {
                    "word": "Cat",
                    "phonetic": "/kæt/",
                    "meaning": "Mèo",
                    "example": "My cat is very cute.",
                    "example_vi": "Con mèo của tôi rất dễ thương."
                },
                {
                    "word": "Pet",
                    "phonetic": "/pet/",
                    "meaning": "Thú cưng",
                    "example": "Do you have any pets?",
                    "example_vi": "Bạn có thú cưng nào không?"
                },
                {
                    "word": "Fish",
                    "phonetic": "/fɪʃ/",
                    "meaning": "Cá",
                    "example": "I have three fish in my tank.",
                    "example_vi": "Tôi có ba con cá trong bể."
                },
                {
                    "word": "Bird",
                    "phonetic": "/bɜːrd/",
                    "meaning": "Chim",
                    "example": "My bird can sing beautifully.",
                    "example_vi": "Con chim của tôi hót rất hay."
                },
                {
                    "word": "Rabbit",
                    "phonetic": "/ˈræbɪt/",
                    "meaning": "Thỏ",
                    "example": "My rabbit loves carrots.",
                    "example_vi": "Con thỏ của tôi thích ăn cà rốt."
                },
                {
                    "word": "Feed",
                    "phonetic": "/fiːd/",
                    "meaning": "Cho ăn",
                    "example": "I feed my dog every morning.",
                    "example_vi": "Tôi cho chó ăn mỗi sáng."
                },
                {
                    "word": "Play",
                    "phonetic": "/pleɪ/",
                    "meaning": "Chơi",
                    "example": "I play with my cat after school.",
                    "example_vi": "Tôi chơi với mèo sau giờ học."
                },
                {
                    "word": "Cute",
                    "phonetic": "/kjuːt/",
                    "meaning": "Dễ thương",
                    "example": "Your pet is so cute!",
                    "example_vi": "Thú cưng của bạn dễ thương quá!"
                },
                {
                    "word": "Take care of",
                    "phonetic": "/teɪk ker ʌv/",
                    "meaning": "Chăm sóc",
                    "example": "I take care of my pet every day.",
                    "example_vi": "Tôi chăm sóc thú cưng mỗi ngày."
                }
            ],
            "guiding_questions": [
                {
                    "question": "Do you have any pets?",
                    "question_vi": "Bạn có thú cưng nào không?"
                },
                {
                    "question": "What kind of pet do you have?",
                    "question_vi": "Bạn có loại thú cưng gì?"
                },
                {
                    "question": "What is your pet's name?",
                    "question_vi": "Tên thú cưng của bạn là gì?"
                },
                {
                    "question": "What does your pet look like?",
                    "question_vi": "Thú cưng của bạn trông như thế nào?"
                },
                {
                    "question": "What does your pet like to do?",
                    "question_vi": "Thú cưng của bạn thích làm gì?"
                },
                {
                    "question": "How do you take care of your pet?",
                    "question_vi": "Bạn chăm sóc thú cưng như thế nào?"
                },
                {
                    "question": "Do you play with your pet?",
                    "question_vi": "Bạn có chơi với thú cưng không?"
                },
                {
                    "question": "What do you feed your pet?",
                    "question_vi": "Bạn cho thú cưng ăn gì?"
                }
            ],
            "sample_paragraphs": [
                {
                    "level": "basic",
                    "text": "I have a pet dog. His name is Max. Max is brown and white. He is very friendly. I love my dog very much.",
                    "text_vi": "Tôi có một con chó. Tên nó là Max. Max có màu nâu và trắng. Nó rất thân thiện. Tôi yêu chó của mình rất nhiều."
                },
                {
                    "level": "intermediate",
                    "text": "I have a cat named Mimi. She is two years old. Mimi has soft gray fur and green eyes. Every morning, I feed her and brush her fur. She likes to play with a ball of yarn. Sometimes she sleeps on my bed.",
                    "text_vi": "Tôi có một con mèo tên Mimi. Nó hai tuổi. Mimi có bộ lông màu xám mềm mại và đôi mắt xanh. Mỗi sáng, tôi cho nó ăn và chải lông. Nó thích chơi với cuộn len. Đôi khi nó ngủ trên giường của tôi."
                }
            ],
            "role_play_scenarios": [
                {
                    "scenario_name": "Giới thiệu thú cưng",
                    "context": "Học viên đang giới thiệu thú cưng của mình cho bạn.",
                    "ai_role": "Bạn bè thích thú về thú cưng.",
                    "student_role": "Giới thiệu và kể về thú cưng.",
                    "goal": "Mô tả ngoại hình và tính cách thú cưng.",
                    "opening_line": "Oh, you have a pet? Tell me about it!",
                    "opening_line_vi": "Ồ, bạn có thú cưng à? Kể cho mình nghe đi!"
                }
            ]
        },
        "COLORS": {
            "topic_name": "COLORS (MÀU SẮC)",
            "vocabulary": [
                {
                    "word": "Red",
                    "phonetic": "/red/",
                    "meaning": "Màu đỏ",
                    "example": "I like red apples.",
                    "example_vi": "Tôi thích táo đỏ."
                },
                {
                    "word": "Blue",
                    "phonetic": "/bluː/",
                    "meaning": "Màu xanh dương",
                    "example": "The sky is blue.",
                    "example_vi": "Bầu trời màu xanh."
                },
                {
                    "word": "Yellow",
                    "phonetic": "/ˈjeloʊ/",
                    "meaning": "Màu vàng",
                    "example": "My bag is yellow.",
                    "example_vi": "Cặp của tôi màu vàng."
                },
                {
                    "word": "Green",
                    "phonetic": "/ɡriːn/",
                    "meaning": "Màu xanh lá",
                    "example": "Trees are green.",
                    "example_vi": "Cây cối màu xanh."
                },
                {
                    "word": "Black",
                    "phonetic": "/blæk/",
                    "meaning": "Màu đen",
                    "example": "I have black shoes.",
                    "example_vi": "Tôi có giày đen."
                },
                {
                    "word": "White",
                    "phonetic": "/waɪt/",
                    "meaning": "Màu trắng",
                    "example": "Snow is white.",
                    "example_vi": "Tuyết màu trắng."
                },
                {
                    "word": "Pink",
                    "phonetic": "/pɪŋk/",
                    "meaning": "Màu hồng",
                    "example": "She wears a pink dress.",
                    "example_vi": "Cô ấy mặc váy hồng."
                },
                {
                    "word": "Orange",
                    "phonetic": "/ˈɔːrɪndʒ/",
                    "meaning": "Màu cam",
                    "example": "I eat an orange fruit.",
                    "example_vi": "Tôi ăn trái cây màu cam."
                },
                {
                    "word": "Purple",
                    "phonetic": "/ˈpɜːrpl/",
                    "meaning": "Màu tím",
                    "example": "Grapes are purple.",
                    "example_vi": "Nho màu tím."
                },
                {
                    "word": "Brown",
                    "phonetic": "/braʊn/",
                    "meaning": "Màu nâu",
                    "example": "My dog is brown.",
                    "example_vi": "Con chó của tôi màu nâu."
                }
            ],
            "guiding_questions": [
                {
                    "question": "What is your favorite color?",
                    "question_vi": "Màu sắc yêu thích của bạn là gì?"
                },
                {
                    "question": "What color is your shirt?",
                    "question_vi": "Áo của bạn màu gì?"
                },
                {
                    "question": "What color do you see around you?",
                    "question_vi": "Bạn thấy màu gì xung quanh?"
                },
                {
                    "question": "What color is the sky?",
                    "question_vi": "Bầu trời màu gì?"
                }
            ],
            "sample_paragraphs": [
                {
                    "level": "basic",
                    "text": "I like many colors. My favorite color is blue. The sky is blue. The ocean is blue. I have a blue backpack.",
                    "text_vi": "Tôi thích nhiều màu. Màu yêu thích của tôi là xanh dương. Bầu trời màu xanh. Đại dương màu xanh. Tôi có một cái ba lô xanh."
                }
            ],
            "role_play_scenarios": [
                {
                    "scenario_name": "Tìm đồ vật theo màu",
                    "context": "Học viên và AI đang chơi trò tìm đồ vật theo màu.",
                    "ai_role": "Người hướng dẫn trò chơi.",
                    "student_role": "Tìm và nói tên đồ vật có màu được yêu cầu.",
                    "goal": "Luyện nhận biết và nói tên màu sắc.",
                    "opening_line": "Let's play a color game! Can you find something red?",
                    "opening_line_vi": "Chúng ta chơi trò màu sắc nhé! Bạn có thể tìm thứ gì màu đỏ không?"
                }
            ]
        }
    },
    "A2": {
        "SHOPPING": {
            "topic_name": "SHOPPING (MUA SẮM)",
            "vocabulary": [
                {
                    "word": "Shop",
                    "phonetic": "/ʃɑːp/",
                    "meaning": "Cửa hàng",
                    "example": "I go to the shop every week.",
                    "example_vi": "Tôi đến cửa hàng mỗi tuần."
                },
                {
                    "word": "Buy",
                    "phonetic": "/baɪ/",
                    "meaning": "Mua",
                    "example": "I want to buy a new shirt.",
                    "example_vi": "Tôi muốn mua một chiếc áo mới."
                },
                {
                    "word": "Price",
                    "phonetic": "/praɪs/",
                    "meaning": "Giá",
                    "example": "What is the price of this bag?",
                    "example_vi": "Giá của chiếc túi này là bao nhiêu?"
                },
                {
                    "word": "Expensive",
                    "phonetic": "/ɪkˈspensɪv/",
                    "meaning": "Đắt",
                    "example": "This watch is too expensive.",
                    "example_vi": "Chiếc đồng hồ này quá đắt."
                },
                {
                    "word": "Cheap",
                    "phonetic": "/tʃiːp/",
                    "meaning": "Rẻ",
                    "example": "I found a cheap book.",
                    "example_vi": "Tôi tìm được một quyển sách rẻ."
                },
                {
                    "word": "Discount",
                    "phonetic": "/ˈdɪskaʊnt/",
                    "meaning": "Giảm giá",
                    "example": "There is a 20% discount today.",
                    "example_vi": "Hôm nay có giảm giá 20%."
                },
                {
                    "word": "Pay",
                    "phonetic": "/peɪ/",
                    "meaning": "Trả tiền",
                    "example": "I will pay by card.",
                    "example_vi": "Tôi sẽ trả bằng thẻ."
                },
                {
                    "word": "Customer",
                    "phonetic": "/ˈkʌstəmər/",
                    "meaning": "Khách hàng",
                    "example": "The customer is always right.",
                    "example_vi": "Khách hàng luôn đúng."
                }
            ],
            "guiding_questions": [
                {
                    "question": "Do you like shopping?",
                    "question_vi": "Bạn có thích mua sắm không?"
                },
                {
                    "question": "Where do you usually shop?",
                    "question_vi": "Bạn thường mua sắm ở đâu?"
                },
                {
                    "question": "What do you like to buy?",
                    "question_vi": "Bạn thích mua gì?"
                },
                {
                    "question": "Do you prefer online shopping or going to stores?",
                    "question_vi": "Bạn thích mua hàng online hay đến cửa hàng?"
                }
            ],
            "sample_paragraphs": [
                {
                    "level": "basic",
                    "text": "I like shopping. I go to the mall every weekend. I usually buy clothes and shoes. Sometimes the prices are high, but I wait for discounts.",
                    "text_vi": "Tôi thích mua sắm. Tôi đến trung tâm thương mại mỗi cuối tuần. Tôi thường mua quần áo và giày. Đôi khi giá cao, nhưng tôi chờ giảm giá."
                }
            ],
            "role_play_scenarios": [
                {
                    "scenario_name": "Mua quần áo ở cửa hàng",
                    "context": "Học viên đang ở cửa hàng quần áo và muốn mua một chiếc áo.",
                    "ai_role": "Nhân viên bán hàng.",
                    "student_role": "Khách hàng hỏi về sản phẩm.",
                    "goal": "Luyện tập hỏi giá, kích cỡ và màu sắc.",
                    "opening_line": "Hello! Can I help you find something today?",
                    "opening_line_vi": "Xin chào! Tôi có thể giúp bạn tìm gì hôm nay không?"
                }
            ]
        }
    },
    "B1": {
        "TRAVEL": {
            "topic_name": "TRAVEL (DU LỊCH)",
            "vocabulary": [
                {
                    "word": "Destination",
                    "phonetic": "/ˌdestɪˈneɪʃn/",
                    "meaning": "Điểm đến",
                    "example": "Paris is my dream destination.",
                    "example_vi": "Paris là điểm đến mơ ước của tôi."
                },
                {
                    "word": "Journey",
                    "phonetic": "/ˈdʒɜːrni/",
                    "meaning": "Chuyến đi",
                    "example": "The journey was long but enjoyable.",
                    "example_vi": "Chuyến đi dài nhưng thú vị."
                },
                {
                    "word": "Luggage",
                    "phonetic": "/ˈlʌɡɪdʒ/",
                    "meaning": "Hành lý",
                    "example": "Don't forget to check your luggage.",
                    "example_vi": "Đừng quên kiểm tra hành lý của bạn."
                },
                {
                    "word": "Accommodation",
                    "phonetic": "/əˌkɑːməˈdeɪʃn/",
                    "meaning": "Chỗ ở",
                    "example": "We booked accommodation near the beach.",
                    "example_vi": "Chúng tôi đặt chỗ ở gần bãi biển."
                },
                {
                    "word": "Itinerary",
                    "phonetic": "/aɪˈtɪnəreri/",
                    "meaning": "Lịch trình",
                    "example": "We planned a detailed itinerary for the trip.",
                    "example_vi": "Chúng tôi lên lịch trình chi tiết cho chuyến đi."
                },
                {
                    "word": "Explore",
                    "phonetic": "/ɪkˈsplɔːr/",
                    "meaning": "Khám phá",
                    "example": "I love to explore new places.",
                    "example_vi": "Tôi thích khám phá những nơi mới."
                }
            ],
            "guiding_questions": [
                {
                    "question": "Have you traveled to any interesting places?",
                    "question_vi": "Bạn đã đi đến nơi nào thú vị chưa?"
                },
                {
                    "question": "Where would you like to travel in the future?",
                    "question_vi": "Bạn muốn đi du lịch đâu trong tương lai?"
                },
                {
                    "question": "What do you usually do when you travel?",
                    "question_vi": "Bạn thường làm gì khi đi du lịch?"
                },
                {
                    "question": "Do you prefer traveling alone or with friends?",
                    "question_vi": "Bạn thích đi du lịch một mình hay với bạn bè?"
                }
            ],
            "sample_paragraphs": [
                {
                    "level": "intermediate",
                    "text": "Last summer, I traveled to Japan. It was an amazing experience. I visited Tokyo, Kyoto, and Osaka. The food was delicious, and the people were very friendly. I especially loved the temples in Kyoto. I hope to visit Japan again someday.",
                    "text_vi": "Mùa hè năm ngoái, tôi đã đi du lịch Nhật Bản. Đó là một trải nghiệm tuyệt vời. Tôi đã thăm Tokyo, Kyoto và Osaka. Đồ ăn rất ngon và người dân rất thân thiện. Tôi đặc biệt yêu thích những ngôi chùa ở Kyoto. Tôi hy vọng sẽ quay lại Nhật Bản một ngày nào đó."
                }
            ],
            "role_play_scenarios": [
                {
                    "scenario_name": "Đặt phòng khách sạn",
                    "context": "Học viên đang gọi điện để đặt phòng khách sạn.",
                    "ai_role": "Nhân viên lễ tân khách sạn.",
                    "student_role": "Khách hàng muốn đặt phòng.",
                    "goal": "Luyện đặt phòng, hỏi giá và tiện nghi.",
                    "opening_line": "Good morning! Grand Hotel, how may I help you?",
                    "opening_line_vi": "Chào buổi sáng! Khách sạn Grand, tôi có thể giúp gì cho bạn?"
                }
            ]
        }
    }
}

# Lưu tiến độ học tập
student_progress = {}

# ========================================
# TOOLS
# ========================================

@mcp.tool()
def list_all_topics(level: Optional[str] = None) -> dict:
    """
    Liệt kê tất cả các chủ đề có sẵn theo cấp độ.
    
    Tham số:
    - level: Cấp độ (A1, A2, B1, B2, C1, C2). Nếu không chỉ định, sẽ liệt kê tất cả.
    
    Trả về: Danh sách các chủ đề theo cấp độ.
    """
    try:
        if level and level in LESSON_DATABASE:
            topics = {
                "level": level,
                "topics": list(LESSON_DATABASE[level].keys()),
                "count": len(LESSON_DATABASE[level])
            }
        else:
            topics = {}
            for lvl in LESSON_DATABASE:
                topics[lvl] = list(LESSON_DATABASE[lvl].keys())
        
        return {
            "success": True,
            "data": topics
        }
    except Exception as e:
        logger.error(f"Error listing topics: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def get_topic_vocabulary(level: str, topic: str) -> dict:
    """
    Lấy bộ từ vựng của một chủ đề cụ thể.
    LƯU Ý: Luôn sử dụng tool này khi bắt đầu một chủ đề mới để lấy từ vựng.
    
    Tham số:
    - level: Cấp độ (A1, A2, B1, etc.)
    - topic: Tên chủ đề (VD: FAMILY, PETS, TRAVEL)
    
    Trả về: Danh sách từ vựng với phiên âm, nghĩa và ví dụ.
    """
    try:
        if level not in LESSON_DATABASE:
            return {"success": False, "error": f"Cấp độ {level} không tồn tại."}
        
        if topic not in LESSON_DATABASE[level]:
            return {"success": False, "error": f"Chủ đề {topic} không tồn tại ở cấp độ {level}."}
        
        lesson = LESSON_DATABASE[level][topic]
        
        return {
            "success": True,
            "level": level,
            "topic": lesson["topic_name"],
            "vocabulary": lesson["vocabulary"],
            "total_words": len(lesson["vocabulary"])
        }
    except Exception as e:
        logger.error(f"Error getting vocabulary: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def get_guiding_questions(level: str, topic: str) -> dict:
    """
    Lấy câu hỏi dẫn dắt hội thoại cho một chủ đề.
    LƯU Ý: Sử dụng để có câu hỏi dẫn dắt học viên trong hội thoại.
    
    Tham số:
    - level: Cấp độ
    - topic: Tên chủ đề
    
    Trả về: Danh sách câu hỏi song ngữ Anh-Việt.
    """
    try:
        if level not in LESSON_DATABASE or topic not in LESSON_DATABASE[level]:
            return {"success": False, "error": "Chủ đề hoặc cấp độ không tồn tại."}
        
        lesson = LESSON_DATABASE[level][topic]
        
        return {
            "success": True,
            "level": level,
            "topic": lesson["topic_name"],
            "questions": lesson["guiding_questions"],
            "total_questions": len(lesson["guiding_questions"])
        }
    except Exception as e:
        logger.error(f"Error getting questions: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def get_sample_paragraphs(level: str, topic: str) -> dict:
    """
    Lấy đoạn văn mẫu cho một chủ đề.
    LƯU Ý: Dùng để cung cấp mẫu cho học viên tham khảo.
    
    Tham số:
    - level: Cấp độ
    - topic: Tên chủ đề
    
    Trả về: Đoạn văn mẫu với bản dịch.
    """
    try:
        if level not in LESSON_DATABASE or topic not in LESSON_DATABASE[level]:
            return {"success": False, "error": "Chủ đề hoặc cấp độ không tồn tại."}
        
        lesson = LESSON_DATABASE[level][topic]
        
        return {
            "success": True,
            "level": level,
            "topic": lesson["topic_name"],
            "paragraphs": lesson["sample_paragraphs"],
            "total_paragraphs": len(lesson["sample_paragraphs"])
        }
    except Exception as e:
        logger.error(f"Error getting paragraphs: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def get_role_play_scenarios(level: str, topic: str) -> dict:
    """
    Lấy tình huống đóng vai cho một chủ đề.
    LƯU Ý: Sử dụng để tạo bài tập đóng vai thực tế.
    
    Tham số:
    - level: Cấp độ
    - topic: Tên chủ đề
    
    Trả về: Danh sách tình huống đóng vai chi tiết.
    """
    try:
        if level not in LESSON_DATABASE or topic not in LESSON_DATABASE[level]:
            return {"success": False, "error": "Chủ đề hoặc cấp độ không tồn tại."}
        
        lesson = LESSON_DATABASE[level][topic]
        
        return {
            "success": True,
            "level": level,
            "topic": lesson["topic_name"],
            "scenarios": lesson["role_play_scenarios"],
            "total_scenarios": len(lesson["role_play_scenarios"])
        }
    except Exception as e:
        logger.error(f"Error getting scenarios: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def start_conversation(level: str, topic: str) -> dict:
    """
    Bắt đầu một buổi học với chủ đề cụ thể.
    LƯU Ý: Đây là tool đầu tiên cần gọi khi học viên muốn bắt đầu học.
    
    Tham số:
    - level: Cấp độ của học viên (A1, A2, B1, etc.)
    - topic: Chủ đề muốn học (VD: FAMILY, PETS, TRAVEL)
    
    Trả về: Thông tin đầy đủ về bài học bao gồm từ vựng, câu hỏi, mẫu và tình huống.
    """
    try:
        if level not in LESSON_DATABASE:
            available_levels = list(LESSON_DATABASE.keys())
            return {
                "success": False,
                "error": f"Cấp độ {level} không tồn tại. Các cấp độ có sẵn: {', '.join(available_levels)}"
            }
        
        if topic not in LESSON_DATABASE[level]:
            available_topics = list(LESSON_DATABASE[level].keys())
            return {
                "success": False,
                "error": f"Chủ đề {topic} không tồn tại ở cấp độ {level}. Các chủ đề có sẵn: {', '.join(available_topics)}"
            }
        
        lesson = LESSON_DATABASE[level][topic]
        
        # Chọn ngẫu nhiên một câu hỏi để bắt đầu
        opening_question = random.choice(lesson["guiding_questions"])
        
        result = {
            "success": True,
            "level": level,
            "topic": lesson["topic_name"],
            "vocabulary_count": len(lesson["vocabulary"]),
            "opening_question": opening_question["question"],
            "opening_question_vi": opening_question["question_vi"],
            "tip": f"Hãy bắt đầu bằng cách trả lời câu hỏi trên. Cố gắng sử dụng từ vựng liên quan đến chủ đề {lesson['topic_name']}!",
            "available_tools": [
                "get_topic_vocabulary - Xem từ vựng chủ đề",
                "get_guiding_questions - Xem các câu hỏi dẫn dắt",
                "get_sample_paragraphs - Xem đoạn văn mẫu",
                "get_role_play_scenarios - Xem tình huống đóng vai"
            ]
        }
        
        logger.info(f"Started conversation: {level} - {topic}")
        return result
        
    except Exception as e:
        logger.error(f"Error starting conversation: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def correct_grammar_pro(student_text: str) -> dict:
    """
    Kiểm tra và sửa lỗi ngữ pháp tiếng Anh cho học viên.
    LƯU Ý: Luôn luôn sử dụng công cụ này để kiểm tra ngữ pháp trước khi đánh giá.

    Tham số:
    - student_text: Đoạn văn tiếng Anh mà học viên nói
    
    Trả về: Bản tóm tắt chi tiết các lỗi, vị trí và gợi ý thay thế.
    """
    try:
        url = "https://api.languagetool.org/v2/check"
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
        
        logger.info(f"Grammar check: {results['total_errors']} errors found")
        return results

    except Exception as e:
        logger.error(f"Error in grammar check: {str(e)}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def evaluate_response(student_response: str, expected_topic: str, level: str = "A1") -> dict:
    """
    Đánh giá chất lượng câu trả lời của học viên.
    LƯU Ý: Chỉ sử dụng SAU KHI kiểm tra ngữ pháp và không có lỗi.
    
    Tham số:
    - student_response: Câu trả lời của học viên
    - expected_topic: Chủ đề đang học
    - level: Cấp độ học viên
    
    Trả về: Điểm số, phản hồi và gợi ý cải thiện.
    """
    try:
        word_count = len(student_response.split())
        sentence_count = student_response.count('.') + student_response.count('!') + student_response.count('?')

        score = 0
        feedback = {
            "strengths": [],
            "improvements": [],
            "encouragement": ""
        }

        # Đánh giá độ dài
        if word_count >= 50:
            score += 3
            feedback["strengths"].append("Câu trả lời đầy đủ, diễn đạt chi tiết")
        elif word_count >= 30:
            score += 2
            feedback["strengths"].append("Câu trả lời vừa phải")
        else:
            score += 1
            feedback["improvements"].append("Hãy cố gắng trả lời chi tiết hơn, thêm ví dụ")

        # Đánh giá cấu trúc câu
        if sentence_count >= 3:
            score += 2
            feedback["strengths"].append("Sử dụng nhiều câu, cấu trúc rõ ràng")
        else:
            feedback["improvements"].append("Hãy dùng nhiều câu hơn để diễn đạt mạch lạc")

        # Đánh giá độ phức tạp
        complex_indicators = ["because", "although", "however", "moreover", "furthermore", "therefore"]
        complex_count = sum(1 for word in complex_indicators if word in student_response.lower())
        if complex_count >= 2:
            score += 3
            feedback["strengths"].append("Sử dụng liên từ tốt, thể hiện tư duy logic")
        elif complex_count >= 1:
            score += 2
            feedback["strengths"].append("Có sử dụng liên từ")
        else:
            feedback["improvements"].append("Hãy thử dùng liên từ (because, however, moreover)")

        # Đánh giá liên quan chủ đề
        if expected_topic.lower() in student_response.lower():
            score += 2
            feedback["strengths"].append("Bám sát chủ đề")

        final_score = min(100, (score / 10) * 100)

        if final_score >= 80:
            feedback["encouragement"] = "Rất tuyệt! Bạn diễn đạt rất tốt! 💪"
        elif final_score >= 60:
            feedback["encouragement"] = "Làm tốt lắm! Bạn đang tiến bộ! 👍"
        else:
            feedback["encouragement"] = "Nỗ lực tốt! Tiếp tục cố gắng nhé! 🌟"

        result = {
            "success": True,
            "score": round(final_score, 1),
            "level": level,
            "statistics": {
                "word_count": word_count,
                "sentence_count": sentence_count,
                "complex_structures": complex_count
            },
            "feedback": feedback
        }

        logger.info(f"Evaluated response: score={final_score}")
        return result

    except Exception as e:
        logger.error(f"Error evaluating response: {e}")
        return {"success": False, "error": str(e)}


@mcp.tool()
def pronunciation_tips(word_or_phrase: str) -> dict:
    """
    Cung cấp gợi ý phát âm cho từ hoặc cụm từ.
    LƯU Ý: Luôn gọi tool này khi học viên hỏi về phát âm.
    
    Tham số:
    - word_or_phrase: Từ hoặc cụm từ cần hướng dẫn
    
    Trả về: Hướng dẫn phát âm chi tiết.
    """
    try:
        pronunciation_guide = {
            "th": {
                "sounds": ["θ (thin)", "ð (this)"],
                "tip": "Đặt đầu lưỡi chạm nhẹ vào mặt sau răng trên",
                "common_errors": "Dễ phát thành 's' hoặc 'z'",
                "practice_words": ["think", "this", "mother", "thank"]
            },
            "r": {
                "sounds": ["ɹ (red)"],
                "tip": "Cuộn đầu lưỡi lên nhưng không chạm vào trong miệng",
                "common_errors": "Dễ phát thành âm 'r' trong tiếng Việt",
                "practice_words": ["red", "right", "road", "around"]
            },
            "v": {
                "sounds": ["v (very)"],
                "tip": "Răng trên chạm nhẹ vào môi dưới, dây thanh rung",
                "common_errors": "Dễ nhầm với âm 'w'",
                "practice_words": ["very", "view", "voice", "victory"]
            }
        }

        tips = []
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

        result = {
            "success": True,
            "word_or_phrase": word_or_phrase,
            "specific_tips": tips if tips else "Không phát hiện khó khăn phát âm đặc biệt",
            "general_recommendation": "Nên nghe phát âm chuẩn trên Cambridge Dictionary hoặc Google Translate"
        }

        logger.info(f"Provided pronunciation tips for: {word_or_phrase}")
        return result

    except Exception as e:
        logger.error(f"Error getting pronunciation tips: {e}")
        return {"success": False, "error": str(e)}


# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")