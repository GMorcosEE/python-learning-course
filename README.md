# Python Learning Course

A structured, hands-on Python course for beginners. Learn Python through 15 weeks of progressive exercises, from basics to advanced topics including OOP, testing, and external libraries.

## Prerequisites

- No prior programming experience required
- Basic computer literacy (file management, text editing)
- Willingness to experiment and learn from mistakes

## Getting Started

### Option 1: Using Gitpod (Recommended)
1. Click the Gitpod button or open this repository in Gitpod
2. Wait for the environment to build (installs Python automatically)
3. Navigate to `python-practice/` directory
4. Start with `week1-basics/01_variables.py`

### Option 2: Local Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/GMorcosEE/python-learning-course.git
   cd python-learning-course
   ```

2. Ensure Python 3.11+ is installed:
   ```bash
   python3 --version
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start learning:
   ```bash
   cd python-practice
   python3 week1-basics/01_variables.py
   ```

## Course Structure

### Weeks 1-2: Python Basics
- Variables and data types
- String and number operations
- User input and output
- Basic calculations

### Weeks 3-4: Control Flow
- If/elif/else statements
- Comparison and logical operators
- For and while loops
- Loop control (break, continue)

### Weeks 5-6: Data Structures
- Lists (creation, manipulation, methods)
- Dictionaries (key-value pairs)
- List comprehensions
- Nested data structures

### Weeks 7-8: Functions
- Function definition and calling
- Parameters and return values
- Variable arguments (*args, **kwargs)
- Lambda functions
- Type hints

### Weeks 9-10: File Operations
- Reading and writing text files
- Working with CSV files
- JSON data handling
- File system operations

### Weeks 11-12: Object-Oriented Programming
- Classes and objects
- Methods and attributes
- Inheritance and polymorphism
- Magic methods and properties
- Encapsulation

### Week 13: Error Handling
- Try/except blocks
- Exception types
- Custom exceptions
- Context managers
- Defensive programming

### Week 14: Testing
- Unit testing with unittest/pytest
- Test-driven development (TDD)
- Assertions and test cases
- Mocking and fixtures

### Week 15: External Libraries
- HTTP requests with requests library
- Data analysis with pandas
- Working with APIs
- Data manipulation

## How to Use This Course

1. **Follow the order** - Each week builds on previous concepts
2. **Read the comments** - Every file has explanations
3. **Run the code** - Execute files to see output
4. **Complete TODOs** - Practice exercises reinforce learning
5. **Experiment** - Modify code and observe changes
6. **Build projects** - Each week ends with a mini project

## Running Exercises

```bash
# Navigate to python-practice directory
cd python-practice

# Run any exercise file
python3 week1-basics/01_variables.py

# Run mini projects
python3 week5-data-structures/03_shopping_list.py
```

## Progress Tracking

Track your progress in `python-practice/PROGRESS.md`. Check off completed exercises and update your stats.

## Mini Projects

Each week includes a practical mini project:
- **Week 3:** Number guessing game
- **Week 4:** Multiplication table generator
- **Week 5:** Shopping list manager
- **Week 6:** Phonebook application
- **Week 7:** Calculator with functions
- **Week 8:** Text analyzer
- **Week 9:** Note-taking app
- **Week 10:** Contact manager with JSON
- **Week 11:** Bank account system (OOP)
- **Week 12:** Game character system (OOP)
- **Week 13:** Robust file processor
- **Week 14:** Tested calculator
- **Week 15:** Weather data analyzer

## Testing Your Code

Run tests for mini projects:
```bash
# Run all tests
pytest python-practice/tests/

# Run specific test file
pytest python-practice/tests/test_calculator.py

# Run with verbose output
pytest -v
```

## Troubleshooting

### Python not found
- Ensure Python 3.11+ is installed: `python3 --version`
- Check PATH environment variable includes Python

### Module not found
- Activate virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

### Permission denied
- On Unix/Linux: `chmod +x script.py`
- Or run with: `python3 script.py`

### Import errors
- Ensure you're in the correct directory
- Check file names match import statements

## Learning Tips

- **Don't rush** - Understanding beats speed
- **Read error messages** - They explain what went wrong
- **Use print()** - Debug by printing variable values
- **Google errors** - You're not the first to encounter them
- **Take breaks** - Learning requires rest
- **Review regularly** - Revisit earlier weeks

## Additional Resources

- [Official Python Documentation](https://docs.python.org/3/)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Real Python Tutorials](https://realpython.com/)
- [Python Tutor (Visualize Code)](https://pythontutor.com/)

## Contributing

Found a bug or have a suggestion? Feel free to:
1. Open an issue
2. Submit a pull request
3. Share your completed projects

## License

This course is open source and available for educational purposes.

---

**Ready to start?** Head to `python-practice/week1-basics/01_variables.py` and begin your Python journey!
