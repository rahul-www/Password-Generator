# Python Strong Password Generator

A security utility script that generates high-entropy random passwords. This project replaces manual character selection with Python's standard libraries to create secure strings of any length.

## 🚀 Features
- **Customizable Length:** Users define the exact length of the password.
- **Complex Character Pool:** Utilizes uppercase, lowercase, numbers, and special symbols (`!@#$`).
- **Memory Persistence:** Constructs the password in a list structure before joining, ensuring data integrity.
- **Error Handling:** Basic validation for integer input.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Modules:** - `import random` (for stochastic selection)
  - `import string` (for character constants)
- **Key Concepts:** Lists vs Strings, `.join()` method, Variable Scope (Global vs Local loop).

## 💻 How to Run
1. Ensure Python is installed.
2. Run the script:
   ```bash
   python passgenerator.py
