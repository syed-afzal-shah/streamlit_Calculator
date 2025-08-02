import streamlit as st

st.set_page_config(page_title="Pro Calculator", layout="centered")
st.title("🧮 Pro Calculator (Keyboard + Mouse)")

# Step 1: Setup session state
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "result" not in st.session_state:
    st.session_state.result = ""

# Step 2: Text input box (keyboard)
user_input = st.text_input("Type expression:", value=st.session_state.expression, key="input_box")

# Only update expression if user typed something different
if user_input != st.session_state.expression:
    st.session_state.expression = user_input

# Step 3: Button Grid
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "⌫"]
]

def evaluate_expression():
    try:
        # Only evaluate if expression is not empty or just operators
        if st.session_state.expression.strip() and any(char.isdigit() for char in st.session_state.expression):
            result = eval(st.session_state.expression)
            st.session_state.result = str(result)
            # st.session_state.expression = st.session_state.result  # Optional: reuse result
        else:
            st.session_state.result = "Invalid Input"
    except ZeroDivisionError:
        st.session_state.result = "Error: Division by zero"
    except Exception as e:
        st.session_state.result = f"Error: {str(e)}"


def handle_click(btn):
    if btn == "C":
        st.session_state.expression = ""
        st.session_state.result = ""
    elif btn == "⌫":
        st.session_state.expression = st.session_state.expression[:-1]
    elif btn == "=":
        evaluate_expression()
    else:
        st.session_state.expression += btn

# Step 4: Show buttons
for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            handle_click(btn)

# Step 5: Display current expression & result
st.markdown("### 📝 Expression")
st.code(st.session_state.expression)

st.markdown("### ✅ Result")
st.code(st.session_state.result if st.session_state.result else "...")