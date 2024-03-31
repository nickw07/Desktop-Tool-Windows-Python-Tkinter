
import tkinter as tk
from tkinter import ttk


# Main GUI
# light Mode
class MainWindowStylingLightMode(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # color system used for light mode
        self.BACKGROUND_COLOR: str = "#2b2b2b"
        self.BODY_COLOR: str = "#b1b3b5"
        self.PRIMARY_COLOR: str = "#434345"
        self.SECONDARY_COLOR: str = "#ffffff"

        # change the theme to be able to edit more
        self.theme_use("clam")

        # creating custom style classes
        # general style classes for applications
        self.configure("BodyFrame.TFrame",
                       relief=tk.SOLID,
                       background=self.BODY_COLOR)

        self.configure("SectionFrame.TFrame",
                       relief=tk.SOLID,
                       background=self.SECONDARY_COLOR)

        self.configure("FrameDescriptionLabel.TLabel",
                       font=("Arial", 14, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("DescriptionLabelSmaller.TLabel",
                       font=("Arial", 13, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("AppButton.TButton",
                       bordercolor=self.SECONDARY_COLOR,
                       borderwidth=0,
                       background=self.SECONDARY_COLOR)

        self.configure("Image.TLabel",
                       background=self.SECONDARY_COLOR)

        # for specific frames
        self.configure("DateTimeLabel.TLabel",
                       font=("Arial", 15, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("HardwareInfoHeading.TLabel",
                       font=("Arial", 13, "underline", "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("HardwareComponentInfo.TLabel",
                       font=("Arial", 13),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)


# dark mode
class MainWindowStylingDarkMode(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # color system used for light mode
        self.BACKGROUND_COLOR: str = "#2b2b2b"
        self.PRIMARY_COLOR: str = "#dddcde"
        self.SECONDARY_COLOR: str = "#434345"

        # change the theme to be able to edit more
        self.theme_use("clam")

        # creating custom style classes
        # general style classes for applications
        self.configure("BodyFrame.TFrame",
                       relief=tk.SOLID,
                       background=self.PRIMARY_COLOR)

        self.configure("SectionFrame.TFrame",
                       relief=tk.SOLID,
                       background=self.SECONDARY_COLOR)

        self.configure("FrameDescriptionLabel.TLabel",
                       font=("Arial", 14, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("DescriptionLabelSmaller.TLabel",
                       font=("Arial", 13, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR,)

        self.configure("AppButton.TButton",
                       bordercolor=self.SECONDARY_COLOR,
                       borderwidth=0,
                       background=self.SECONDARY_COLOR)

        self.configure("Image.TLabel",
                       background=self.SECONDARY_COLOR)

        # for specific frames
        self.configure("DateTimeLabel.TLabel",
                       font=("Arial", 15, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("HardwareInfoHeading.TLabel",
                       font=("Arial", 13, "underline", "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)

        self.configure("HardwareComponentInfo.TLabel",
                       font=("Arial", 13),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)


# Toplevel GUIs
# 1. App - Calculator
class CalculatorStyling(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # colors used in the program
        self.BACKGROUND_COLOR: str = "#2b2b2b"
        self.PRIMARY_COLOR: str = "#dddcde"
        self.SECONDARY_COLOR: str = "#434345"
        self.TERTIARY_COLOR: str = "#6d6d6e"
        self.ACCENT_COLOR: str = "#6e48e0"

        # change the theme to be able to edit more
        self.theme_use("clam")

        # creating custom style classes (using .map()-Method to customize even more precisely for ex. hovering)
        self.configure("BodyFrameCalc.TFrame",
                       background=self.BACKGROUND_COLOR)

        # display equation
        self.configure("EquationDisplayEntryCalc.TEntry",
                       bordercolor=self.PRIMARY_COLOR,
                       lightcolor=self.PRIMARY_COLOR,
                       darkcolor=self.PRIMARY_COLOR,
                       borderwitdh=1,
                       focusthickness=0,
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR,
                       fieldbackground=self.SECONDARY_COLOR)
        self.map("EquationDisplayEntryCalc.TEntry",
                 bordercolor=[("focus", self.PRIMARY_COLOR)],
                 lightcolor=[("focus", self.PRIMARY_COLOR)],
                 darkcolor=[("focus", self.PRIMARY_COLOR)])

        # buttons with numbers
        self.configure("BaseOptionButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       width=7,
                       background=self.TERTIARY_COLOR)
        self.map("BaseOptionButtonCalc.TButton",
                 foreground=[("active", self.BACKGROUND_COLOR)])

        # buttons with operations (+, -, ( ...)
        self.configure("OperationButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       width=7,
                       background=self.SECONDARY_COLOR)
        self.map("OperationButtonCalc.TButton",
                 foreground=[("active", self.BACKGROUND_COLOR)])

        self.configure("CopyResultButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       width=7,
                       background=self.SECONDARY_COLOR)

        # equals button custom color
        self.configure("EqualsButtonCalc.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       padding=7,
                       font=("Arial", 12, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       width=7,
                       background=self.ACCENT_COLOR)
        self.map("EqualsButtonCalc.TButton",
                 foreground=[("active", self.BACKGROUND_COLOR)])

        # default style classes
        # TScrollbar
        self.configure("TScrollbar",
                       bordercolor=self.TERTIARY_COLOR,
                       lightcolor=self.TERTIARY_COLOR,
                       darkcolor=self.TERTIARY_COLOR,
                       background=self.BACKGROUND_COLOR,
                       troughcolor=self.PRIMARY_COLOR,
                       arrowcolor=self.PRIMARY_COLOR)
        self.map("TScrollbar",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)],
                 slider=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)])


# 2. App - Password Generator
class RandomPasswordGeneratorStyling(ttk.Style):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # colors used in the program
        self.BACKGROUND_COLOR: str = "#2b2b2b"
        self.PRIMARY_COLOR: str = "#dddcde"
        self.SECONDARY_COLOR: str = "#434345"
        self.ACCENT_COLOR: str = "#6e48e0"

        # change the theme to be able to edit more
        self.theme_use("clam")

        # creating custom style classes (using .map()-Method to customize even more precisely for ex. hovering)
        self.configure("BodyFrameRPG.TFrame",
                       background=self.BACKGROUND_COLOR)

        # info labels
        self.configure("InfoLabelRPG.TLabel",
                       font=("Arial", 16, "bold"),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)

        # specification info labels
        self.configure("SpecificationInfoLabelRPG.TLabel",
                       font=("Arial", 14),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)

        # option checkbutton
        self.configure("OptionCheckbuttonRPG.TCheckbutton",
                       focusthickness=5,
                       font=("Arial", 12),
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)
        self.map("OptionCheckbuttonRPG.TCheckbutton",
                 foreground=[("active", self.PRIMARY_COLOR)],
                 background=[("active", self.SECONDARY_COLOR)],
                 indicatorbackground=[("selected", self.ACCENT_COLOR), ("!selected", self.PRIMARY_COLOR)],
                 indicatorcolor=[("selected", self.ACCENT_COLOR), ("!selected", self.PRIMARY_COLOR)])

        # buttons
        self.configure("PerformActionButtonRPG.TButton",
                       bordercolor=self.BACKGROUND_COLOR,
                       borderwidth=0,
                       font=("Arial", 14),
                       foreground=self.PRIMARY_COLOR,
                       background=self.SECONDARY_COLOR)
        self.map("PerformActionButtonRPG.TButton",
                 foreground=[("active", self.PRIMARY_COLOR)],
                 background=[("active", "#6d6d6e")])  # slightly brighter color SECONDARY_COLOR

        # separator
        self.configure("SeparatorRPG.TSeparator",
                       background=self.PRIMARY_COLOR)

        # display result
        self.configure("ResultEntryRPG.TEntry",
                       bordercolor=self.PRIMARY_COLOR,
                       lightcolor=self.PRIMARY_COLOR,
                       darkcolor=self.PRIMARY_COLOR,
                       borderwitdh=1,
                       focusthickness=0,
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR,
                       fieldbackground=self.SECONDARY_COLOR)
        self.map("ResultEntryRPG.TEntry",
                 bordercolor=[("focus", self.PRIMARY_COLOR)],
                 lightcolor=[("focus", self.PRIMARY_COLOR)],
                 darkcolor=[("focus", self.PRIMARY_COLOR)])

        # default style classes
        # TScrollbar
        self.configure("TScrollbar",
                       bordercolor=self.ACCENT_COLOR,
                       lightcolor=self.ACCENT_COLOR,
                       darkcolor=self.ACCENT_COLOR,
                       background=self.BACKGROUND_COLOR,
                       troughcolor=self.PRIMARY_COLOR,
                       arrowcolor=self.PRIMARY_COLOR)
        self.map("TScrollbar",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)],
                 slider=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)])

        # TScale
        self.configure("TScale",
                       bordercolor=self.ACCENT_COLOR,
                       lightcolor=self.ACCENT_COLOR,
                       darkcolor=self.ACCENT_COLOR,
                       focuscolor=self.PRIMARY_COLOR,
                       foreground=self.PRIMARY_COLOR,
                       background=self.BACKGROUND_COLOR)
        self.map("TScale",
                 background=[("active", self.BACKGROUND_COLOR), ("!active", self.BACKGROUND_COLOR)],
                 troughcolor=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)],
                 slider=[("active", self.PRIMARY_COLOR), ("!active", self.PRIMARY_COLOR)])
