# Contributing to MCP English Tutor

Thank you for your interest in contributing to MCP English Tutor! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request, please:

1. Check if the issue already exists in the [Issues](https://github.com/your-username/mcp-english-tutor/issues) section
2. Create a new issue with a clear title and description
3. Include steps to reproduce the issue (for bugs)
4. Provide your environment details (OS, Python version, etc.)

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

### Prerequisites

- Python 3.7+
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mcp-english-tutor.git
   cd mcp-english-tutor
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .[dev]  # Install development dependencies
   ```

4. Run tests:
   ```bash
   pytest tests/
   ```

## Code Style

### Python Code

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions small and focused
- Use meaningful variable and function names

### Documentation

- Update README.md for significant changes
- Add docstrings for new functions
- Update CHANGELOG.md for new features or bug fixes
- Write clear commit messages

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=english_tutor

# Run specific test file
pytest tests/test_english_tutor.py
```

### Writing Tests

- Write tests for new functionality
- Test both success and error cases
- Use descriptive test names
- Mock external dependencies

## Project Structure

```
mcp-english-tutor/
├── english_tutor.py      # Main MCP server
├── mcp_pipe.py          # Communication pipe
├── tests/               # Test files
├── docs/                # Documentation
├── examples/            # Usage examples
├── requirements.txt     # Dependencies
├── setup.py            # Package configuration
└── README.md           # Project documentation
```

## Areas for Contribution

### High Priority

- [ ] Add more conversation topics
- [ ] Improve grammar error detection
- [ ] Add pronunciation assessment
- [ ] Create more practice scenarios
- [ ] Add learning analytics

### Medium Priority

- [ ] Support for other languages
- [ ] Integration with external APIs
- [ ] Advanced progress tracking
- [ ] Custom topic creation
- [ ] Voice recognition support

### Low Priority

- [ ] Web interface
- [ ] Mobile app
- [ ] Advanced AI features
- [ ] Multi-user support

## Code of Conduct

Please be respectful and constructive in all interactions. We aim to create a welcoming environment for all contributors.

## Questions?

If you have questions about contributing, please:

1. Check the documentation in the `docs/` folder
2. Open an issue with the "question" label
3. Contact the maintainers

Thank you for contributing to MCP English Tutor! 🎉
