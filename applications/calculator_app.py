
import tkinter as tk
from tkinter import ttk

import math

import pyperclip

from styling import CalculatorStyling


class Calculator(tk.Toplevel):
    def __init__(self, parent: tk.Tk):
        super().__init__(parent)

        # placing the GUI
        self.root_x: int = parent.winfo_x()
        self.root_y: int = parent.winfo_y()

        self.geometry(f"+{self.root_x}+{self.root_y}")
        self.resizable(False, False)

        # basic modification of GUI
        self.title("Calculator")
        self.iconbitmap(r"graphics/window-icon-32x32px.ico")

        # GUI styling
        self.style: CalculatorStyling = CalculatorStyling(self)
        self.configure(background=self.style.BACKGROUND_COLOR)

        # creating frames to logically separate everything in the GUI
        equation_frame: EquationFrame = EquationFrame(self,
                                                      style="BodyFrameCalc.TFrame")
        equation_frame.pack()

        button_frame: ButtonFrame = ButtonFrame(self,
                                                equation_frame.equation_display_entry,
                                                equation_frame.equation_var,
                                                style="BodyFrameCalc.TFrame")
        button_frame.pack(padx=5, pady=5)


class EquationFrame(ttk.Frame):
    def __init__(self, container: tk.Toplevel, **kwargs):
        super().__init__(container, **kwargs)

        # attributes
        self.equation_var: tk.StringVar = tk.StringVar(value="0")

        # display current expression
        self.equation_display_entry: ttk.Entry = ttk.Entry(self,
                                                           textvariable=self.equation_var,
                                                           font=("Arial", 16, "bold"),
                                                           width=34,
                                                           state="readonly",
                                                           justify=tk.CENTER,
                                                           style="EquationDisplayEntryCalc.TEntry")
        self.equation_display_entry.grid(row=0, column=0, pady=10)


class GeneralMethods:
    def __init__(self, equation_var: tk.StringVar, equation_text: str, copy_result_button: ttk.Button):

        # attributes
        # equation context
        self.equation_var: tk.StringVar = equation_var
        self.equation_text: str = equation_text

        # widget transfer (these attributes are required in the methods)
        self.copy_result_button: ttk.Button = copy_result_button

        # constants
        self.ERROR_SUFFIX: str = "Error"

    # methods - auxiliary methods that are needed in methods for the button_frame
    def handle_error(self, arithmetic_error=False, syntax_error=False, value_error=False):
        # React to ZeroDivisionError, SyntaxError, ValueError

        self.copy_result_button.configure(state=tk.DISABLED)

        if arithmetic_error:
            self.equation_var.set(f"Arithmetic {self.ERROR_SUFFIX}")
            self.equation_text = ""

        elif syntax_error:
            self.equation_var.set(f"Syntax {self.ERROR_SUFFIX}")
            self.equation_text = ""

        elif value_error:
            self.equation_var.set(f"Value {self.ERROR_SUFFIX}")
            self.equation_text = ""

    @staticmethod
    def round_result(result: float) -> str:
        return str(round(result, 5))

    @staticmethod
    def remove_leading_zeros_expression_start(number: str) -> int:
        while number.startswith("0"):
            number = number[1:]
        return number


class ButtonFrame(ttk.Frame):
    def __init__(self, container: tk.Toplevel, equation_display_entry: ttk.Entry, equation_var: tk.StringVar, **kwargs):
        super().__init__(container, **kwargs)

        # attributes
        # equation context
        self.equation_var: tk.StringVar = equation_var
        self.equation_text: str = ""

        # widget transfer
        self.equation_display_entry: ttk.Entry = equation_display_entry

        # constants
        self.SUPERSCRIPT_TWO: str = chr(0xB2)
        self.SQRT_SIGN: str = chr(0x221A)

        # creating the widgets
        # first row
        open_parentheses_button: ttk.Button = ttk.Button(self,
                                                         text="(",
                                                         command=lambda: self.button_press("("),
                                                         style="OperationButtonCalc.TButton")
        open_parentheses_button.grid(row=0, column=0, padx=2, pady=2)

        close_parentheses_button: ttk.Button = ttk.Button(self,
                                                          text=")",
                                                          command=lambda: self.button_press(")"),
                                                          style="OperationButtonCalc.TButton")
        close_parentheses_button.grid(row=0, column=1, padx=2, pady=2)

        switch_sign_button: ttk.Button = ttk.Button(self,
                                                    text="- / +",
                                                    command=self.switch_mathematical_sign_of_expression,
                                                    style="OperationButtonCalc.TButton")
        switch_sign_button.grid(row=0, column=2, padx=2, pady=2)

        self.copy_result_button: ttk.Button = ttk.Button(self,
                                                         text="Copy result!",
                                                         command=self.copy_result,
                                                         style="CopyResultButtonCalc.TButton")
        self.copy_result_button.grid(row=0, column=3, sticky=tk.EW, columnspan=2, padx=2, pady=2)
        self.copy_result_button.configure(state=tk.DISABLED)

        # second row
        button_1: ttk.Button = ttk.Button(self,
                                          text="1",
                                          command=lambda: self.button_press(1),
                                          style="BaseOptionButtonCalc.TButton")
        button_1.grid(row=1, column=0, padx=2, pady=2)

        button_2: ttk.Button = ttk.Button(self,
                                          text="2",
                                          command=lambda: self.button_press(2),
                                          style="BaseOptionButtonCalc.TButton")
        button_2.grid(row=1, column=1, padx=2, pady=2)

        button_3: ttk.Button = ttk.Button(self,
                                          text="3",
                                          command=lambda: self.button_press(3),
                                          style="BaseOptionButtonCalc.TButton")
        button_3.grid(row=1, column=2, padx=2, pady=2)

        delete_button: ttk.Button = ttk.Button(self,
                                               text="DEL",
                                               command=self.delete_last,
                                               style="OperationButtonCalc.TButton")
        delete_button.grid(row=1, column=3, padx=2, pady=2)

        all_clear_button: ttk.Button = ttk.Button(self,
                                                  text="AC",
                                                  command=self.all_clear,
                                                  style="OperationButtonCalc.TButton")
        all_clear_button.grid(row=1, column=4, sticky=tk.EW, columnspan=2, padx=2, pady=2)

        # third row
        button_4: ttk.Button = ttk.Button(self,
                                          text="4",
                                          command=lambda: self.button_press(4),
                                          style="BaseOptionButtonCalc.TButton")
        button_4.grid(row=2, column=0, padx=2, pady=2)

        button_5: ttk.Button = ttk.Button(self,
                                          text="5",
                                          command=lambda: self.button_press(5),
                                          style="BaseOptionButtonCalc.TButton")
        button_5.grid(row=2, column=1, padx=2, pady=2)

        button_6: ttk.Button = ttk.Button(self,
                                          text="6",
                                          command=lambda: self.button_press(6),
                                          style="BaseOptionButtonCalc.TButton")
        button_6.grid(row=2, column=2, padx=2, pady=2)

        plus_button: ttk.Button = ttk.Button(self,
                                             text="+",
                                             command=lambda: self.button_press("+"),
                                             style="OperationButtonCalc.TButton")
        plus_button.grid(row=2, column=3, padx=2, pady=2)

        minus_button: ttk.Button = ttk.Button(self,
                                              text="-",
                                              command=lambda: self.button_press("-"),
                                              style="OperationButtonCalc.TButton")
        minus_button.grid(row=2, column=4, padx=2, pady=2)

        # fourth row
        button_7: ttk.Button = ttk.Button(self,
                                          text="7",
                                          command=lambda: self.button_press(7),
                                          style="BaseOptionButtonCalc.TButton")
        button_7.grid(row=3, column=0, padx=2, pady=2)

        button_8: ttk.Button = ttk.Button(self,
                                          text="8",
                                          command=lambda: self.button_press(8),
                                          style="BaseOptionButtonCalc.TButton")
        button_8.grid(row=3, column=1, padx=2, pady=2)

        button_9: ttk.Button = ttk.Button(self,
                                          text="9",
                                          command=lambda: self.button_press(9),
                                          style="BaseOptionButtonCalc.TButton")
        button_9.grid(row=3, column=2, padx=2, pady=2)

        multiply_button: ttk.Button = ttk.Button(self,
                                                 text="*",
                                                 command=lambda: self.button_press("*"),
                                                 style="OperationButtonCalc.TButton")
        multiply_button.grid(row=3, column=3, padx=2, pady=2)

        divide_button: ttk.Button = ttk.Button(self,
                                               text="/",
                                               command=lambda: self.button_press("/"),
                                               style="OperationButtonCalc.TButton")
        divide_button.grid(row=3, column=4, padx=2, pady=2)

        # fifth row
        button_0: ttk.Button = ttk.Button(self,
                                          text="0",
                                          command=lambda: self.button_press(0),
                                          style="BaseOptionButtonCalc.TButton")
        button_0.grid(row=4, column=0, padx=2, pady=2)

        decimal_button: ttk.Button = ttk.Button(self,
                                                text=".",
                                                command=lambda: self.button_press("."),
                                                style="BaseOptionButtonCalc.TButton")
        decimal_button.grid(row=4, column=1, padx=2, pady=2)

        equals_button: ttk.Button = ttk.Button(self,
                                               text="=",
                                               command=self.perform_action,
                                               style="EqualsButtonCalc.TButton")
        equals_button.grid(row=4, column=2, padx=2, pady=2)

        square_button: ttk.Button = ttk.Button(self,
                                               text=f"x {self.SUPERSCRIPT_TWO}",
                                               command=self.square_of_expression,
                                               style="OperationButtonCalc.TButton")
        square_button.grid(row=4, column=3, padx=2, pady=2)

        sqrt_button: ttk.Button = ttk.Button(self,
                                             text=self.SQRT_SIGN,
                                             command=self.sqrt_of_expression,
                                             style="OperationButtonCalc.TButton")
        sqrt_button.grid(row=4, column=4, padx=2, pady=2)

        # sixth row (scrollbar)
        equation_display_entry_scrollbar: ttk.Scrollbar = ttk.Scrollbar(self,
                                                                        orient=tk.HORIZONTAL,
                                                                        command=self.equation_display_entry.xview)
        equation_display_entry_scrollbar.grid(row=5, column=0, sticky=tk.EW, columnspan=5, padx=2, pady=5)

        self.equation_display_entry.configure(xscrollcommand=equation_display_entry_scrollbar.set)

        self.general_methods: GeneralMethods = GeneralMethods(self.equation_var, self.equation_text, self.copy_result_button)

    # methods (belong to the buttons)
    def button_press(self, pressed_button):

        self.equation_text += str(pressed_button)

        self.equation_var.set(self.equation_text)

        self.copy_result_button.configure(state=tk.DISABLED)

    def perform_action(self):

        try:
            # Check if double asterisk or double slash is present in equation_text
            if "**" in self.equation_text or "//" in self.equation_text:
                self.general_methods.handle_error(syntax_error=True)

            self.calculation_of_expression()

            self.copy_result_button.configure(state=tk.NORMAL)

        except ZeroDivisionError:
            self.general_methods.handle_error(arithmetic_error=True)
        except SyntaxError:
            self.general_methods.handle_error(syntax_error=True)
        except ValueError:
            self.general_methods.handle_error(value_error=True)
        except TypeError:
            self.general_methods.handle_error(value_error=True)
        except Exception as E:
            # pass
            print(E)

    def calculation_of_expression(self):

        self.equation_text = self.equation_var.get()
        self.equation_text = self.general_methods.remove_leading_zeros_expression_start(self.equation_text)

        result = eval(str(self.equation_text))
        result = self.general_methods.round_result(result)

        self.equation_var.set(result)
        self.equation_text = result

    def square_of_expression(self):

        try:
            self.equation_text = self.equation_var.get()

            # operation
            result = (float(self.equation_text) * float(self.equation_text))
            result = self.general_methods.round_result(result)

            self.equation_var.set(result)
            self.equation_text = result

            self.copy_result_button.configure(state=tk.NORMAL)
        except ValueError:
            self.general_methods.handle_error(value_error=True)
        except Exception as E:
            # pass
            print(E)

    def sqrt_of_expression(self):

        try:
            self.equation_text = self.equation_var.get()

            # operation
            result = math.sqrt(float(self.equation_text))
            result = self.general_methods.round_result(result)

            self.equation_var.set(result)
            self.equation_text = result

            self.copy_result_button.configure(state=tk.NORMAL)

        except ValueError:
            self.general_methods.handle_error(value_error=True)
        except Exception as E:
            # pass
            print(E)

    def switch_mathematical_sign_of_expression(self):

        self.equation_text = self.equation_var.get()

        try:

            if self.equation_text[0] != "-":
                equation_text_reversed = self.equation_text[::-1]
                equation_text_reversed += "-"
                self.equation_text = equation_text_reversed[::-1]

                self.equation_var.set(self.equation_text)

            else:
                equation_text_reversed = self.equation_text[::-1]
                equation_text_reversed = equation_text_reversed[:-1]
                self.equation_text = equation_text_reversed[::-1]

                self.equation_var.set(self.equation_text)

        except IndexError:
            self.general_methods.handle_error(syntax_error=True)

    def delete_last(self):

        if self.general_methods.ERROR_SUFFIX in self.equation_var.get():
            self.equation_var.set("")
            self.equation_text = self.equation_var.get()
        else:
            self.equation_var.set(self.equation_var.get()[:-1])
            self.equation_text = self.equation_var.get()

    def all_clear(self):

        self.copy_result_button.configure(state=tk.DISABLED)

        self.equation_text = ""
        self.equation_var.set("")

    def copy_result(self):
        result = self.equation_var.get()
        pyperclip.copy(result)
