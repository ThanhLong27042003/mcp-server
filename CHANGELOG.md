# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-16

### Added
- Initial release of MCP English Tutor
- 7 professional English tutoring tools:
  - `generate_conversation_topic` - Generate conversation topics based on student level
  - `correct_grammar` - Detect and correct grammar errors with explanations
  - `suggest_vocabulary` - Recommend relevant vocabulary and phrases
  - `evaluate_response` - Evaluate student responses with detailed feedback
  - `pronunciation_tips` - Provide pronunciation guidance
  - `track_progress` - Track learning progress and analyze improvement
  - `create_practice_scenario` - Create role-play scenarios for real-world practice
- Support for 3 difficulty levels (beginner, intermediate, advanced)
- Rich topic library with 12+ conversation topics
- Multiple practice scenarios (daily conversation, business, travel)
- Comprehensive vocabulary database
- SSL certificate handling for self-signed certificates
- Automatic reconnection with exponential backoff
- Complete documentation in Chinese and English

### Features
- **Topic Generation**: 12+ topics across 3 difficulty levels
- **Grammar Correction**: Real-time error detection and correction
- **Vocabulary Learning**: Context-aware vocabulary recommendations
- **Response Evaluation**: Multi-dimensional assessment (content, structure, complexity)
- **Pronunciation Guidance**: Tips for common pronunciation challenges
- **Progress Tracking**: Learning analytics and improvement analysis
- **Role-play Scenarios**: 6+ realistic conversation scenarios

### Technical
- Built on MCP (Model Context Protocol) framework
- WebSocket communication with automatic reconnection
- SSL/TLS support with self-signed certificate handling
- Modular design for easy extension
- Comprehensive error handling and logging
- Type hints and documentation

### Documentation
- Complete setup and configuration guide
- API documentation for all tools
- Usage examples and best practices
- Troubleshooting guide
- Chinese and English documentation

## [Unreleased]

### Planned
- Integration with professional grammar APIs (LanguageTool, Grammarly)
- Voice recognition and pronunciation assessment
- AI-powered conversation partner integration
- Database persistence for learning data
- Advanced learning analytics and reporting
- Multi-language support
- Custom topic creation
- Learning path recommendations
