
import tkinter as tk
from tkinter import ttk

import random
import string

import pyperclip

from styling import RandomPasswordGeneratorStyling


class RandomPasswordGenerator(tk.Toplevel):
    def __init__(self, parent: tk.Tk):
        super().__init__(parent)

        # placing the GUI
        self.root_x: int = parent.winfo_x()
        self.root_y: int = parent.winfo_y()

        self.geometry(f"+{self.root_x}+{self.root_y}")
        self.resizable(False, False)

        # basic modification of GUI
        self.title("Random password generator")
        self.iconbitmap(r"graphics/window-icon-32x32px.ico")

        # GUI styling
        self.style: RandomPasswordGeneratorStyling = RandomPasswordGeneratorStyling()
        self.configure(background=self.style.BACKGROUND_COLOR)

        # creating frames, info text, separator to logically separate everything in the GUI
        input_info_label: ttk.Label = ttk.Label(self,
                                                text="Create a random password",
                                                style="InfoLabelRPG.TLabel")
        input_info_label.grid(row=0, column=0, padx=10, pady=10)

        input_frame: InputFrame = InputFrame(self,
                                             style="BodyFrameRPG.TFrame")
        input_frame.grid(row=1, column=0)

        divider: ttk.Separator = ttk.Separator(self,
                                               style="SeparatorRPG.TSeparator")
        divider.grid(row=2, column=0, sticky=tk.EW, pady=5)

        output_info_label: ttk.Label = ttk.Label(self,
                                                 text="Your random password is:",
                                                 style="InfoLabelRPG.TLabel")
        output_info_label.grid(row=3, column=0, padx=5, pady=10)

        output_frame: OutputFrame = OutputFrame(self,
                                                input_frame.password_var,
                                                input_frame.ERROR,
                                                style="BodyFrameRPG.TFrame")
        output_frame.grid(row=4, column=0)


class InputFrame(ttk.Frame):
    def __init__(self, container: tk.Toplevel, **kwargs):
        super().__init__(container, **kwargs)

        # attributes
        # length
        self.length_var: tk.IntVar = tk.IntVar(value=8)

        # content
        self.using_lowercase: tk.BooleanVar = tk.BooleanVar()
        self.using_uppercase: tk.BooleanVar = tk.BooleanVar()
        self.using_digits: tk.BooleanVar = tk.BooleanVar()
        self.using_punctuation: tk.BooleanVar = tk.BooleanVar()

        # storing result
        self.password_var: tk.StringVar = tk.StringVar()

        # constants / getting access to symbols
        self.LOWERCASE_LETTERS: str = string.ascii_lowercase
        self.UPPERCASE_LETTERS: str = string.ascii_uppercase
        self.DIGITS: str = string.digits
        self.PUNCTUATION: str = string.punctuation

        self.ERROR: str = "Select characters"

        # specifying the password length
        length_label: ttk.Label = ttk.Label(self,
                                            text="Length:",
                                            style="SpecificationInfoLabelRPG.TLabel")
        length_label.grid(row=0, column=0, sticky=tk.W, padx=12, pady=10)

        length_scale: ttk.Scale = ttk.Scale(self,
                                            length=100,
                                            from_=8,
                                            to=75,
                                            variable=self.length_var,
                                            command=self.update_value)
        length_scale.grid(row=0, column=1, sticky=tk.EW, columnspan=3, padx=12, pady=10)

        display_length_label: ttk.Label = ttk.Label(self,
                                                    textvariable=self.length_var,
                                                    style="SpecificationInfoLabelRPG.TLabel")
        display_length_label.grid(row=0, column=4)

        # specifying characters that should be included
        include_info_label: ttk.Label = ttk.Label(self,
                                                  text="Include:",
                                                  style="SpecificationInfoLabelRPG.TLabel")
        include_info_label.grid(row=1, column=0, padx=12, pady=10)

        # check buttons (4)
        uppercase_letters_checkbutton: ttk.Checkbutton = ttk.Checkbutton(self,
                                                                         text="ABC",
                                                                         variable=self.using_uppercase,
                                                                         style="OptionCheckbuttonRPG.TCheckbutton")
        uppercase_letters_checkbutton.grid(row=1, column=1, padx=10)

        lowercase_letters_checkbutton: ttk.Checkbutton = ttk.Checkbutton(self,
                                                                         text="abc",
                                                                         variable=self.using_lowercase,
                                                                         style="OptionCheckbuttonRPG.TCheckbutton")
        lowercase_letters_checkbutton.grid(row=1, column=2, padx=10)

        digits_checkbutton: ttk.Checkbutton = ttk.Checkbutton(self,
                                                              text="123",
                                                              variable=self.using_digits,
                                                              style="OptionCheckbuttonRPG.TCheckbutton")
        digits_checkbutton.grid(row=1, column=3, padx=10)

        punctuation_checkbutton: ttk.Checkbutton = ttk.Checkbutton(self,
                                                                   text="#!'",
                                                                   variable=self.using_punctuation,
                                                                   style="OptionCheckbuttonRPG.TCheckbutton")
        punctuation_checkbutton.grid(row=1, column=4, padx=10)

        # creating the password
        generate_pwd_button: ttk.Button = ttk.Button(self,
                                                     text="Generate password",
                                                     command=self.generate_password,
                                                     style="PerformActionButtonRPG.TButton")
        generate_pwd_button.grid(row=2, column=0, sticky=tk.EW, columnspan=5, padx=12, pady=10)

    # methods
    def update_value(self, value: str):
        # having even numbers on the scale
        self.length_var.set(int(float(value)))

    def generate_password(self):
        characters: str = ""

        # finding the characters that will be used
        pwd_length: int = self.length_var.get()
        lowercase: bool = self.using_lowercase.get()
        uppercase: bool = self.using_uppercase.get()
        digits: bool = self.using_digits.get()
        punctuation: bool = self.using_punctuation.get()

        if lowercase:
            characters += self.LOWERCASE_LETTERS
        if uppercase:
            characters += self.UPPERCASE_LETTERS
        if digits:
            characters += self.DIGITS
        if punctuation:
            characters += self.PUNCTUATION

        if not characters:
            self.password_var.set(f"{self.ERROR}")
            return None
        else:
            # creating password
            password = "".join(random.choices(characters, k=pwd_length))
            self.password_var.set(password)


class OutputFrame(ttk.Frame):
    def __init__(self, container: tk.Toplevel, password_var: tk.StringVar, error: str, **kwargs):
        super().__init__(container, **kwargs)

        # attributes
        # value transfer
        self.password_var: tk.StringVar = password_var

        # constants
        self.ERROR: str = error

        # displaying the password
        self.result_entry: ttk.Entry = ttk.Entry(self,
                                                 font=("Arial", 13),
                                                 state="readonly",
                                                 textvariable=self.password_var,
                                                 width=41,
                                                 style="ResultEntryRPG.TEntry")
        self.result_entry.grid(row=0, column=0, sticky=tk.EW, padx=12)

        # scrollbar (if result is large)
        self.result_entry_scrollbar: ttk.Scrollbar = ttk.Scrollbar(self,
                                                                   orient=tk.HORIZONTAL,
                                                                   command=self.result_entry.xview)
        self.result_entry_scrollbar.grid(row=1, column=0, sticky=tk.EW, padx=12, pady=7)
        self.result_entry.configure(xscrollcommand=self.result_entry_scrollbar.set)

        copy_result_button: ttk.Button = ttk.Button(self,
                                                    text="Copy result!",
                                                    command=self.copy_password,
                                                    style="PerformActionButtonRPG.TButton")
        copy_result_button.grid(row=2, column=0, sticky=tk.EW, padx=12, pady=10)

    # methods
    def copy_password(self):
        # copy result to clipboard
        if self.password_var.get() != self.ERROR:
            password = self.password_var.get()
            pyperclip.copy(password)
