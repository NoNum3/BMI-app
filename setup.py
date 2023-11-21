from typing import Optional, Tuple, Union
import customtkinter as ctk
from settings import *

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class App(ctk.CTk):
    def __init__(self):
        # window setup
        super().__init__(fg_color=GREEN)
        self.title("")
        self.geometry("400x400")
        self.resizable(False, False)
        self.change_title_bar_color()

        # layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

        # widgets
        ResultText(self)
        WeightInput(self)
        self.mainloop()

    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(
                HWND, 35, byref(c_int(TITLE_HEX_COLOR)), sizeof(c_int)
            )
        except Exception as e:
            # Handle the exception appropriately or log it
            print(f"Error: {e}")


class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight="bold")
        super().__init__(parent, text="22", font=font)
        self.grid(column=0, row=0, rowspan=2, sticky="nsew")


class WeightInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(column=0, row=2, sticky="nsew", padx=10, pady=10)

        # layout
        self.rowconfigure(0, weight=1, uniform="b")
        self.columnconfigure((0), weight=2, uniform="b")
        self.columnconfigure((1), weight=1, uniform="b")
        self.columnconfigure((2), weight=3, uniform="b")
        self.columnconfigure((3), weight=1, uniform="b")
        self.columnconfigure((4), weight=2, uniform="b")

        # widgets
        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        label = ctk.CTkLabel(self, text="70kg", text_color=BLACK)
        label.grid(row=0, column=2)

        # buttons
        minus_button = ctk.CTkButton(self, text="-", font=font)
        minus_button.grid(row=0, column=0, sticky="nsew")
        plus_button = ctk.CTkButton(self, text="+", font=font)
        plus_button.grid(row=0, column=4, sticky="nsew")


if __name__ == "__main__":
    App()
