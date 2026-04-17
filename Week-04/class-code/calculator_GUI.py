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


# ── Main program ──────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg=BG)

display_var = tk.StringVar(value="0")
sub_var     = tk.StringVar(value="1")

# Outer Frame
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

# # Main display
tk.Label(disp_frame, textvariable=display_var,
            bg=DISPLAY_BG, fg=TEXT_MAIN,
            font=("Courier New", 36, "bold"), anchor="e",
            padx=14, pady=14, height=10, width=20).pack(fill="x")

# # Button grid
# grid = tk.Frame(outer, bg=BG)
# grid.pack()




root.mainloop()