# passCheck (Python Password Strength Checker)

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)

## Project Overview
**passCheck** is a **simple Python program** that evaluates the strength of a password based on **five key criteria**:
- Length ≥ 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (`!@#$%^&*(),.?":{}|<>`)

The program gives a **strength rating** (`Weak`, `Medium`, `Strong`) and suggests **improvements** for weak passwords.  

This project demonstrates **Python programming, regex usage, and problem-solving skills**. It's beginner-friendly and console-based.

---

## Features
- Handles **empty passwords** gracefully
- Evaluates password strength based on 5 criteria
- Provides actionable feedback on **missing criteria**
- Fully console-based (no external dependencies)

---

## How it Works
1. User enters a password.
2. The program checks each criterion using Python’s `re` module.
3. Counts the number of criteria met.
4. Assigns a **strength rating**:
   - Weak: 0–2 criteria met
   - Medium: 3–4 criteria met
   - Strong: All 5 criteria met
5. Prints **strength rating** and **criteria to improve**.

---

## How to Run

1. Install Python: [https://www.python.org/](https://www.python.org/)
2. Save the code in a file named `passCheck.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the file.
5. Run the program:

```bash
python passCheck.py
