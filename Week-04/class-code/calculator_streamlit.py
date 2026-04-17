import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700&display=swap');

* { box-sizing: border-box; }

.stApp {
    background: #0a0a0f;
    font-family: 'Share Tech Mono', monospace;
}

.main .block-container {
    max-width: 420px;
    padding: 2rem 1rem;
    margin: auto;
}

h1 {
    font-family: 'Orbitron', monospace !important;
    color: #00ff9f !important;
    text-align: center;
    font-size: 1.4rem !important;
    letter-spacing: 0.3em;
    text-shadow: 0 0 20px #00ff9f88;
    margin-bottom: 1.5rem !important;
}

.display-box {
    background: #0d1117;
    border: 1px solid #00ff9f44;
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 0 30px #00ff9f11, inset 0 0 20px #00000044;
}

.display-expr {
    color: #00ff9f66;
    font-size: 0.85rem;
    min-height: 1.2rem;
    text-align: right;
    letter-spacing: 0.05em;
}

.display-value {
    color: #00ff9f;
    font-size: 2.4rem;
    text-align: right;
    text-shadow: 0 0 15px #00ff9f66;
    word-break: break-all;
    line-height: 1.2;
    margin-top: 0.3rem;
}

div[data-testid="column"] > div > div > div > button {
    width: 100% !important;
    height: 62px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 1.2rem !important;
    border-radius: 6px !important;
    border: 1px solid #1a2a1a !important;
    cursor: pointer !important;
    transition: all 0.1s ease !important;
    font-weight: 400 !important;
}

/* Number buttons */
div[data-testid="column"]:not(:last-child) > div > div > div > button {
    background: #111820 !important;
    color: #c8ffd4 !important;
    border-color: #1e3024 !important;
}

div[data-testid="column"]:not(:last-child) > div > div > div > button:hover {
    background: #1a2e22 !important;
    border-color: #00ff9f44 !important;
    box-shadow: 0 0 12px #00ff9f22 !important;
    color: #00ff9f !important;
}

div[data-testid="column"]:not(:last-child) > div > div > div > button:active {
    background: #00ff9f22 !important;
    box-shadow: 0 0 20px #00ff9f44 !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize state
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "display" not in st.session_state:
    st.session_state.display = "0"
if "just_evaluated" not in st.session_state:
    st.session_state.just_evaluated = False

def press(val):
    if val == "C":
        st.session_state.expression = ""
        st.session_state.display = "0"
        st.session_state.just_evaluated = False
    elif val == "⌫":
        if st.session_state.just_evaluated:
            st.session_state.expression = ""
            st.session_state.display = "0"
            st.session_state.just_evaluated = False
        elif st.session_state.expression:
            st.session_state.expression = st.session_state.expression[:-1]
            st.session_state.display = st.session_state.expression or "0"
    elif val == "=":
        try:
            expr = st.session_state.expression.replace("×", "*").replace("÷", "/")
            result = eval(expr)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            st.session_state.display = str(result)
            st.session_state.expression = str(result)
            st.session_state.just_evaluated = True
        except:
            st.session_state.display = "Error"
            st.session_state.expression = ""
            st.session_state.just_evaluated = False
    elif val == "+/-":
        try:
            if st.session_state.expression:
                result = eval(st.session_state.expression.replace("×", "*").replace("÷", "/"))
                toggled = -result
                if isinstance(toggled, float) and toggled.is_integer():
                    toggled = int(toggled)
                st.session_state.expression = str(toggled)
                st.session_state.display = str(toggled)
        except:
            pass
    elif val == "%":
        try:
            result = eval(st.session_state.expression.replace("×", "*").replace("÷", "/")) / 100
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            st.session_state.expression = str(result)
            st.session_state.display = str(result)
        except:
            pass
    else:
        if st.session_state.just_evaluated and val not in "×÷+-":
            st.session_state.expression = ""
        st.session_state.just_evaluated = False
        st.session_state.expression += val
        st.session_state.display = st.session_state.expression

st.markdown("<h1>CALCULATOR</h1>", unsafe_allow_html=True)

# Display
expr_shown = st.session_state.expression if not st.session_state.just_evaluated else ""
st.markdown(f"""
<div class="display-box">
    <div class="display-expr">{expr_shown}</div>
    <div class="display-value">{st.session_state.display}</div>
</div>
""", unsafe_allow_html=True)

# Button layout
buttons = [
    ["C", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "⌫", "="],
]

operator_style = """
<style>
.op-btn button {
    background: #0a1f14 !important;
    color: #00ff9f !important;
    border-color: #00ff9f33 !important;
}
.op-btn button:hover {
    background: #00ff9f22 !important;
    box-shadow: 0 0 15px #00ff9f33 !important;
}
.eq-btn button {
    background: #00ff9f !important;
    color: #000 !important;
    border-color: #00ff9f !important;
    font-weight: 700 !important;
}
.eq-btn button:hover {
    background: #33ffb5 !important;
    box-shadow: 0 0 25px #00ff9f88 !important;
}
.clear-btn button {
    background: #1a0a0a !important;
    color: #ff4466 !important;
    border-color: #ff446633 !important;
}
.clear-btn button:hover {
    background: #ff446622 !important;
    box-shadow: 0 0 15px #ff446633 !important;
}
</style>
"""
st.markdown(operator_style, unsafe_allow_html=True)

OPERATORS = {"÷", "×", "-", "+", "%", "+/-"}
CLEAR = {"C", "⌫"}

for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        with cols[i]:
            if btn == "=":
                st.markdown('<div class="eq-btn">', unsafe_allow_html=True)
            elif btn in CLEAR:
                st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
            elif btn in OPERATORS:
                st.markdown('<div class="op-btn">', unsafe_allow_html=True)

            st.button(btn, key=f"btn_{btn}_{row.index(btn)}", on_click=press, args=(btn,), use_container_width=True)

            if btn in {"="} | CLEAR | OPERATORS:
                st.markdown('</div>', unsafe_allow_html=True)
