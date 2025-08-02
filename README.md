# 🧮 Pro Calculator (Streamlit App)

**Pro Calculator** is a responsive, interactive calculator built with [Streamlit](https://streamlit.io/) and Python.  
It allows users to input expressions via keyboard or on-screen buttons, with safe backend evaluation using Python's `ast` module to prevent code injection and runtime errors.

---

## 🔍 Features

- ⌨️ **Keyboard + Mouse Input**: Type expressions or click buttons
- 🔐 **Secure Evaluation**: Uses Abstract Syntax Trees (`ast`) for safe expression parsing
- ❌ **Error Handling**: Gracefully catches division by zero or invalid inputs
- 🔁 **Result Reuse**: Use the result of one calculation as the next input
- 🎨 **Interactive UI**: Built-in button grid and real-time updates with Streamlit session state

---

## 📁 Project Structure

pro-calculator/
├── app.py # Streamlit code for the calculator
├── requirements.txt # Python dependencies
├── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pro-calculator.git
cd pro-calculator
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Start the Streamlit App
bash
Copy
Edit
streamlit run app.py
📦 requirements.txt
txt
Copy
Edit
streamlit
If you add more features later (e.g., NumPy, Matplotlib), update this file accordingly.

🔧 Technologies Used
Python 3.x

Streamlit – for building the web app interface

AST Module – for secure mathematical expression parsing

🧠 How it Works
The app reads the user's expression and parses it using Python’s ast module, allowing only basic arithmetic operations:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Exponentiation (**)

Unary minus (e.g., -5)

All unsafe code execution is prevented — no eval() is used.

👨‍💻 Author
Afzal Shah
AI Intern | Machine Learning Enthusiast | CS Student
📍 NCAI-UET Lahore
📧 [Your Email or LinkedIn if you'd like to add]
