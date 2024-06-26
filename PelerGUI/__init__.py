from tkinter import *
from tkinter import ttk
from tkinter import messagebox

__version__ = '0.0.1'
__author__ = "Peler"

INFO = messagebox.showinfo
WARNING = messagebox.showwarning
ERROR = messagebox.showerror


def pprint(text, title="pprint", message_type=INFO):
    INFO(title, text)


def pinput(text, title="pinput"):
    parent = Tk()
    parent.withdraw()  # Hide the main window

    def on_ok(*args):
        nonlocal entered_text
        entered_text = entry.get()
        top.destroy()

    def on_cancel():
        nonlocal entered_text
        entered_text = None
        top.destroy()

    entered_text = None

    top = Toplevel(parent)
    top.title(title)

    # Entry
    label_entry = ttk.Label(top, text=text)
    label_entry.pack(pady=5)

    entry = ttk.Entry(top)
    entry.pack(padx=10, pady=5)
    entry.bind("<Return>", on_ok)  # Bind the Return key to the on_ok function

    # Buttons
    button_frame = ttk.Frame(top)
    button_frame.pack(pady=10)

    ok_button = ttk.Button(button_frame, text="OK", command=on_ok)
    ok_button.pack(side=LEFT, padx=5)

    cancel_button = ttk.Button(button_frame, text="Cancel", command=on_cancel)
    cancel_button.pack(side=LEFT, padx=5)

    # Center the window on the screen
    top.update_idletasks()  # Update window to get correct dimensions
    window_width = top.winfo_width()
    window_height = top.winfo_height()
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    top.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    parent.wait_window(top)

    if entered_text is None:
        entered_text = ""

    return entered_text


if __name__ == '__main__':
    pinput("aaaa")
