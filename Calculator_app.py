import streamlit as st
import ast
import operator

# ---------------------------
# Safe Evaluator using AST
# ---------------------------

# Define supported operators
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def safe_eval(expr):
    try:
        node = ast.parse(expr, mode='eval').body
        return evaluate_node(node)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Invalid Input"

def evaluate_node(node):
    if isinstance(node, ast.Num):  # e.g. 5
        return node.n
    elif isinstance(node, ast.BinOp):  # e.g. 5 + 6
        return operators[type(node.op)](evaluate_node(node.left), evaluate_node(node.right))
    elif isinstance(node, ast.UnaryOp):  # e.g. -5
        return operators[type(node.op)](evaluate_node(node.operand))
    else:
        raise ValueError("Unsupported operation")

# ---------------------------
# Streamlit App
# ---------------------------

st.set_page_config(page_title="Pro Calculator", layout="centered")
st.title("🧮 Pro Calculator (Keyboard + Mouse)")

# Session state setup
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "result" not in st.session_state:
    st.session_state.result = ""

# Input field
user_input = st.text_input("⌨️ Type expression:", value=st.session_state.expression, key="input_box")

# Sync session state
if user_input != st.session_state.expression:
    st.session_state.expression = user_input

# Button grid layout
buttons = [
    ["7", "8", "9", "➗"],
    ["4", "5", "6", "✖️"],
    ["1", "2", "3", "➖"],
    ["0", ".", "=", "➕"],
    ["C", "⌫"]
]

# Button click handler
def handle_click(btn):
    if btn == "C":
        st.session_state.expression = ""
        st.session_state.result = ""
    elif btn == "⌫":
        st.session_state.expression = st.session_state.expression[:-1]
    elif btn == "=":
        if st.session_state.expression:
            cleaned = st.session_state.expression.replace("➗", "/").replace("✖️", "*").replace("➕", "+").replace("➖", "-")
            result = safe_eval(cleaned)
            st.session_state.result = str(result)
    else:
        st.session_state.expression += btn

# Show buttons
for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            handle_click(btn)

# Expression display
st.markdown("### 🧾 Current Expression")
st.code(st.session_state.expression if st.session_state.expression else "...")

# Result display
st.markdown("### 📊 Output")
if "Error" in st.session_state.result or "Invalid" in st.session_state.result:
    st.error(st.session_state.result)
elif st.session_state.result:
    st.success(st.session_state.result)
else:
    st.info("Waiting for input...")

# Reuse result toggle
if st.session_state.result and st.checkbox("🔁 Use result as next input"):
    st.session_state.expression = st.session_state.result
    st.session_state.result = ""
