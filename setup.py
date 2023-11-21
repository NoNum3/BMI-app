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

        # data
        self.height_int = ctk.IntVar(value=170)
        self.weight_float = ctk.DoubleVar(value=65)
        self.bmi_string = ctk.StringVar()
        self.update_bmi()

        # widgets
        ResultText(self, self.bmi_string)
        WeightInput(self)
        HeightInput(self, self.height_int)
        UnitSwitcher(self)

        self.mainloop()

    def update_bmi(self):
        height_meter = self.height_int.get() / 100
        weight_kg = self.weight_float.get()
        bmi_result = weight_kg / (height_meter**2)
        self.bmi_string.set(f"{bmi_result:.2f}")

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
    def __init__(self, parent, bmi_string):
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight="bold")
        super().__init__(
            parent, text="22", font=font, text_color=WHITE, textvariable=bmi_string
        )
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
        minus_button = ctk.CTkButton(
            self,
            text="-",
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNER_RADIUS,
        )
        minus_button.grid(
            row=0,
            column=0,
            sticky="ns",
            padx=8,
            pady=8,
        )
        plus_button = ctk.CTkButton(
            self,
            text="+",
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
            corner_radius=BUTTON_CORNER_RADIUS,
        )
        plus_button.grid(
            row=0,
            column=4,
            sticky="ns",
            padx=8,
            pady=8,
        )

        small_minus_button = ctk.CTkButton(
            self,
            text="-",
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
        )
        small_minus_button.grid(row=0, column=1, padx=4, pady=16, sticky="ns")
        small_plus_button = ctk.CTkButton(
            self,
            text="+",
            font=font,
            text_color=BLACK,
            fg_color=LIGHT_GRAY,
            hover_color=GRAY,
        )
        small_plus_button.grid(row=0, column=3, padx=4, pady=16, sticky="ns")


class HeightInput(ctk.CTkFrame):
    def __init__(self, parent, height_int):
        super().__init__(master=parent, fg_color=WHITE)
        self.grid(column=0, row=3, sticky="nsew", padx=10, pady=10)

        # widgets
        slider = ctk.CTkSlider(
            master=self,
            button_color=GREEN,
            button_hover_color=GRAY,
            progress_color=GREEN,
            fg_color=LIGHT_GRAY,
            corner_radius=BUTTON_CORNER_RADIUS,
            variable= height_int,
            from_= 100,
            to=220,
        )
        slider.pack(side = 'left', fill="x", expand=True, padx=10, pady=10)

        output_text = ctk.CTkLabel(
            master=self,
            text="1.70m",
            text_color=BLACK,
            font=ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE),
        )
        output_text.pack(padx=10, pady=10)


class UnitSwitcher(ctk.CTkLabel):
    def __init__(self, parent):
        super().__init__(
            master=parent,
            text="metric",
            text_color=DARK_GREEN,
            font=ctk.CTkFont(family=FONT, size=SWITCH_FONT_SIZE, weight="bold"),
        )
        self.grid(column=0, row=4, sticky="nsew", padx=10, pady=10)
        self.place(relx=0.98, rely=0.01, anchor="ne")


if __name__ == "__main__":
    App()
