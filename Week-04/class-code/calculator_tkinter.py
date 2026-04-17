import tkinter as tk

# ── Palette ───────────────────────────────────────────────────────────────────
BG         = "#0f0f0f"
DISPLAY_BG = "#1a1a1a"
BTN_NUM    = "#1e1e1e"
BTN_OP     = "#2a2a2a"
BTN_EQUALS = "#ff6b00"
BTN_CLEAR  = "#3a1a1a"
TEXT_MAIN  = "#f5f5f5"
TEXT_DIM   = "#888888"
TEXT_OP    = "#ff9940"
HOVER_NUM  = "#2e2e2e"
HOVER_OP   = "#3a3a3a"
HOVER_EQ   = "#ff8c2a"
HOVER_CLR  = "#4a2020"
BORDER     = "#2a2a2a"

# ── State (global variables) ──────────────────────────────────────────────────
expression = ""

# ── Helper: format number nicely ──────────────────────────────────────────────
def format_number(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:.10g}"

# ── Button click handler ──────────────────────────────────────────────────────
def on_click(label):
    global expression

    if label == "C":
        expression = ""
        display_var.set("0")
        sub_var.set("")

    elif label == "=":
        try:
            expr = expression.replace("÷", "/").replace("×", "*").replace("−", "-")
            result = eval(expr)
            fmt = format_number(result)
            sub_var.set(expression + " =")
            display_var.set(fmt)
            expression = fmt
        except Exception:
            display_var.set("Error")
            expression = ""
            sub_var.set("")

    elif label == "±":
        cur = display_var.get()
        if cur not in ("0", "Error"):
            new = cur[1:] if cur.startswith("-") else "-" + cur
            display_var.set(new)
            if expression:
                expression = new

    elif label == "%":
        try:
            val = float(display_var.get()) / 100
            result = format_number(val)
            expression = result
            display_var.set(result)
            sub_var.set("")
        except Exception:
            pass

    elif label in ("÷", "×", "−", "+"):
        op_map = {"÷": "/", "×": "*", "−": "-", "+": "+"}
        op = op_map[label]
        cur = display_var.get()
        if expression and expression[-1] in "/*-+":
            expression = expression[:-1] + op
        else:
            expression = (expression or cur) + op
        sub_var.set(expression)
        display_var.set("0")

    elif label == ".":
        cur = display_var.get()
        if "." not in cur:
            new = cur + "."
            display_var.set(new)
            if not expression or expression[-1] in "/*-+":
                expression += new
            else:
                expression = expression[:-len(cur)] + new

    else:  # digit
        cur = display_var.get()
        new = label if cur in ("0", "Error") else cur + label
        display_var.set(new)
        if not expression or expression[-1] in "/*-+":
            expression += label
        else:
            expression = expression[:-len(cur)] + new

# ── Hover effect helpers ──────────────────────────────────────────────────────
def on_enter(btn, hover_color):
    btn.config(bg=hover_color)

def on_leave(btn, normal_color):
    btn.config(bg=normal_color)

# ── Create a single button ────────────────────────────────────────────────────
def make_button(parent, label, row, col, bg, fg, hover, colspan=1):
    btn = tk.Label(
        parent, text=label,
        bg=bg, fg=fg,
        font=("Courier New", 18, "bold"),
        width=1, height=1,
        cursor="hand2"
    )
    btn.grid(row=row, column=col, columnspan=colspan,
             padx=5, pady=5,
             ipadx=(68 * colspan + (colspan - 1) * 10) // 2 - 10,
             ipady=16, sticky="nsew")

    btn.bind("<Button-1>", lambda e: on_click(label))
    btn.bind("<Enter>",    lambda e: on_enter(btn, hover))
    btn.bind("<Leave>",    lambda e: on_leave(btn, bg))

# ── Build the full UI ─────────────────────────────────────────────────────────
def build_ui():
    # Outer frame
    outer = tk.Frame(root, bg=BG, padx=16, pady=16)
    outer.pack()

    # Display area
    disp_frame = tk.Frame(outer, bg=DISPLAY_BG, bd=0,
                          highlightthickness=1,
                          highlightbackground=BORDER)
    disp_frame.pack(fill="x", pady=(0, 12))

    # Sub-display (running expression)
    tk.Label(disp_frame, textvariable=sub_var,
             bg=DISPLAY_BG, fg=TEXT_DIM,
             font=("Courier New", 11), anchor="e",
             padx=14, pady=10).pack(fill="x")

    # Main display
    tk.Label(disp_frame, textvariable=display_var,
             bg=DISPLAY_BG, fg=TEXT_MAIN,
             font=("Courier New", 36, "bold"), anchor="e",
             padx=14, pady=14).pack(fill="x")

    # Button grid
    grid = tk.Frame(outer, bg=BG)
    grid.pack()

    buttons = [
        ("C",  0, 0, BTN_CLEAR,  TEXT_MAIN, HOVER_CLR, 1),
        ("±",  0, 1, BTN_OP,     TEXT_OP,   HOVER_OP,  1),
        ("%",  0, 2, BTN_OP,     TEXT_OP,   HOVER_OP,  1),
        ("÷",  0, 3, BTN_OP,     TEXT_OP,   HOVER_OP,  1),
        ("7",  1, 0, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("8",  1, 1, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("9",  1, 2, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("×",  1, 3, BTN_OP,     TEXT_OP,   HOVER_OP,  1),
        ("4",  2, 0, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("5",  2, 1, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("6",  2, 2, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("−",  2, 3, BTN_OP,     TEXT_OP,   HOVER_OP,  1),
        ("1",  3, 0, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("2",  3, 1, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("3",  3, 2, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("+",  3, 3, BTN_OP,     TEXT_OP,   HOVER_OP,  1),
        ("0",  4, 0, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 2),
        (".",  4, 2, BTN_NUM,    TEXT_MAIN, HOVER_NUM, 1),
        ("=",  4, 3, BTN_EQUALS, "#ffffff", HOVER_EQ,  1),
    ]

    for (label, row, col, bg, fg, hover, colspan) in buttons:
        make_button(grid, label, row, col, bg, fg, hover, colspan)

# ── Main program ──────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg=BG)

display_var = tk.StringVar(value="0")
sub_var     = tk.StringVar(value="")

build_ui()
root.mainloop()
