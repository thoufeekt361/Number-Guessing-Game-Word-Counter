# 🎮 Number Guessing Game & Word Counter

A beginner-friendly Python programming project developed as part of **InternCircle – Python Programming Internship (Project 02)**.

This project combines two interactive Python applications into a single menu-driven program: a Number Guessing Game with a scoring system and a Word Counter that analyzes text files and displays word frequency statistics.

## 📌 Project Overview

The application provides two functionalities:

- **Number Guessing Game:** Generates a random number between 1 and 100. Players have seven attempts to guess the correct number and earn points based on their performance.
- **Word Counter:** Reads a text file, removes punctuation, counts word frequencies, and displays the top 10 most frequently used words.

## ✨ Features

### 1. Number Guessing Game
- Generates a random number using Python's `random` module.
- Allows users to guess a number between 1 and 100.
- Provides helpful hints such as Too High and Too Low.
- Limits the game to seven attempts.
- Includes an automatic scoring system.
- Tracks the player's best score.
- Supports replay functionality.
- Handles invalid user inputs.

### 2. Word Counter
- Reads text files using Python file handling.
- Converts text into lowercase.
- Removes punctuation marks.
- Counts total and unique words.
- Uses `collections.Counter` for frequency analysis.
- Displays the top 10 most common words.
- Handles missing files with a friendly error message.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Random | Random number generation |
| String | Punctuation removal |
| Collections.Counter | Word frequency analysis |
| File Handling | Reading text files |
| VS Code | Development environment |

## 📂 Project Structure

```text
Python-Project-02/
│
├── main.py
├── sample.txt
├── README.md
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/thoufeekt361/Number-Guessing-Game-Word-Counter.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Number-Guessing-Game-Word-Counter
```

### Step 3: Check Python Installation

```bash
python --version
```

Python 3.10 or newer is recommended.

### Step 4: Run the Application

```bash
python main.py
```

## 🚀 How to Use

After running the program, the following menu appears:

```text
====================================
       PYTHON PROGRAMMING PROJECT
====================================
1. Number Guessing Game
2. Word Counter
3. Quit

Enter your choice (1-3):
```

- Enter `1` to play the Number Guessing Game.
- Enter `2` to analyze a text file.
- Enter `3` to exit the application.

For the Word Counter, provide a text file name such as `sample.txt`. Make sure the file is available in the project directory.

## 🏆 Scoring System

The Number Guessing Game starts with 100 points.

- Correct guess on the first attempt: 100 points.
- Each incorrect valid guess reduces the potential score by 10 points.
- Minimum score: 0 points.
- Maximum attempts: 7.

**Formula:**

```text
Score = 100 - (Incorrect Attempts × 10)
```

## 📊 Sample Output

### Number Guessing Game

```text
Enter your guess: 50
Too low! Try a higher number.

Enter your guess: 75
Too high! Try a lower number.

Enter your guess: 65
Congratulations! You guessed correctly!

---------- GAME RESULTS ----------
Total attempts: 3
Your score: 80
Best score: 80
```

### Word Counter

```text
========== WORD COUNT RESULTS ==========

Total words: 25
Unique words: 16

---------- TOP 10 MOST COMMON WORDS ----------
Word                 Frequency
------------------------------
python                       4
programming                  3
is                           2
easy                         2
```

*Note: The actual output depends on the contents of the input text file.*

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Python functions and modular programming.
- Conditional statements and loops.
- Random number generation.
- Exception handling and input validation.
- File handling operations.
- String manipulation.
- Dictionary-based counting.
- Sorting and displaying frequency results.

## 🔮 Future Improvements

- Add difficulty levels to the guessing game.
- Store player scores in a file.
- Support multiple text file formats.
- Add graphical user interface (GUI).
- Generate detailed word analysis reports.

## 👨‍💻 Author

**Thoufeek T**

Python Programming Intern – InternCircle

GitHub: [@thoufeekt361](https://github.com/thoufeekt361)

LinkedIn: [Thoufeek T](https://linkedin.com/in/thoufeek-t-60838a358)

## 📜 Acknowledgement

This project was developed as part of the **InternCircle Python Programming Internship – Project 02**.

Special thanks to InternCircle for providing the learning opportunity and project guidance.

---

⭐ If you find this project useful, feel free to explore the repository!
