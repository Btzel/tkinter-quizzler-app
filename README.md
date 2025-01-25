# Tkinter Quizzler App
An interactive quiz application built with Python using Tkinter and the Open Trivia Database API, featuring dynamic question fetching and score tracking.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![API](https://img.shields.io/badge/OpenTrivia-API-red)
![Quiz](https://img.shields.io/badge/Interactive-Quiz-green)

## 🎯 Overview
This project creates an engaging quiz experience where users:
1. Answer true/false questions
2. See questions from various categories
3. Track their score in real-time
4. Continue with new question sets
5. View difficulty levels

## 🎮 App Features
### Interactive Elements
- Dynamic question display
- True/False buttons
- Score tracking
- Category indicators
- Difficulty levels

### Data Management
- API integration
- Question bank handling
- Score calculation
- Progress tracking

## 🔧 Technical Components
### Question Management System
```python
def check_answer(self, user_answer, correct_answer, score, window):
    if correct_answer.lower() == user_answer.lower():
        score += 1

    if not self.still_has_questions():
        will_continue = messagebox.askyesno(
            title="We're done with questions!",
            message="If you want to continue playing, press yes"
        )
        if will_continue:
            self.get_new_questions()
        else:
            window.quit()

    return score
```

### Key Features
1. **Question Handling**
   - API data fetching
   - Question formatting
   - HTML unescaping
   - Category display

2. **Game Flow**
   - Score tracking
   - Progress monitoring
   - Continuous play option
   - Session management

3. **Data Processing**
   - API response handling
   - Question bank creation
   - Answer validation
   - Error management

## 💻 Implementation Details
### Class Structure
- `Question`: Question data model
- `QuestionRequester`: API interaction
- `QuizBrain`: Game logic
- `Interface`: UI management

### Data Management
- API data fetching
- Question formatting
- Score tracking
- Session handling

## 🚀 Usage
1. Install required packages:
```bash
pip install requests
pip install tkinter
```

2. Run the application:
```bash
python main.py
```

3. Play the quiz:
   - Read the question
   - Select True/False
   - Track your score
   - Continue or end game

## 🎯 Game Rules
1. Answer True/False questions
2. Score points for correct answers
3. Complete question sets
4. Choose to continue or end
5. Track total score

## 🛠️ Project Structure
```
quizzler-app/
├── main.py             # Application core
├── quiz_brain.py       # Game logic
├── question_model.py   # Data model
├── data.py            # API handling
└── images/            # UI assets
    ├── true.png
    └── false.png
```

## 📊 Features
### Input Processing
- API data handling
- User answer validation
- Continue/exit options
- Error handling

### Output Management
- Score display
- Question presentation
- Category information
- Difficulty indicators

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL