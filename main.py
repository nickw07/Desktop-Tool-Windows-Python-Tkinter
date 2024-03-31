import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import datetime
import time
import subprocess

import pyautogui

import psutil
import platform
import wmi

from applications.calculator_app import Calculator
from applications.password_generator_app import RandomPasswordGenerator

from styling import MainWindowStylingDarkMode, MainWindowStylingLightMode


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # placing the GUI
        self.WIDTH: int = 900
        self.HEIGHT: int = 600

        self.MONITOR_CENTER_X: int = int(self.winfo_screenwidth() / 2 - (int(self.WIDTH) / 2))
        self.MONITOR_CENTER_Y: int = int(self.winfo_screenheight() / 2 - (int(self.HEIGHT) / 2))

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{self.MONITOR_CENTER_X}+{self.MONITOR_CENTER_Y}")
        self.resizable(False, False)

        # basic modification og GUI
        self.title("Desktop Tool")
        self.iconbitmap(r"graphics/window-icon-32x32px.ico")

        # GUI styling
        self.style: MainWindowStylingLightMode = MainWindowStylingLightMode(self)
        self.configure(background=self.style.BACKGROUND_COLOR)

        # creating frames to logically separate everything in the GUI
        self.body_frame: BodyFrame = BodyFrame(self,
                                               width=860,
                                               height=560,
                                               style="BodyFrame.TFrame")
        self.body_frame.place(x=20, y=20)

        date_time_frame: DateTimeFrame = DateTimeFrame(self.body_frame,
                                                       width=840,
                                                       height=50,
                                                       style="SectionFrame.TFrame")
        date_time_frame.place(x=10, y=10)
        date_time_frame.show_time()

        system_info_frame: SystemInfoFrame = SystemInfoFrame(self.body_frame,
                                                             width=625,
                                                             height=350,
                                                             style="SectionFrame.TFrame")
        system_info_frame.place(x=10, y=70)

        # implement switching between two frames
        self.frames: dict = {}

        quick_access_first_page_frame: QuickAccessFirst = QuickAccessFirst(self.body_frame,
                                                                           self,
                                                                           width=205,
                                                                           height=350,
                                                                           style="SectionFrame.TFrame")
        quick_access_first_page_frame.place(x=645, y=70)

        quick_access_second_page_frame: QuickAccessSecond = QuickAccessSecond(self.body_frame,
                                                                              self,
                                                                              width=205,
                                                                              height=350,
                                                                              style="SectionFrame.TFrame")
        quick_access_second_page_frame.place(x=645, y=70)

        self.frames[QuickAccessFirst] = quick_access_first_page_frame
        self.frames[QuickAccessSecond] = quick_access_second_page_frame

        self.change_window(QuickAccessFirst)

        applications_frame: ApplicationsFrame = ApplicationsFrame(self.body_frame,
                                                                  width=840,
                                                                  height=120,
                                                                  style="SectionFrame.TFrame")
        applications_frame.place(x=10, y=430)

    def change_window(self, container):
        frame = self.frames[container]
        frame.tkraise()


class BodyFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)


class DateTimeFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        # attributes
        self.date_var: tk.StringVar = tk.StringVar(value="date")
        self.time_var: tk.StringVar = tk.StringVar(value="time")

        self.button_mode: bool = True

        # widgets
        date_label: ttk.Label = ttk.Label(self,
                                          textvariable=self.date_var,
                                          style="DateTimeLabel.TLabel")
        date_label.place(x=10, y=10)

        time_label: ttk.Label = ttk.Label(self,
                                          textvariable=self.time_var,
                                          style="DateTimeLabel.TLabel")
        time_label.place(x=390, y=10)

        # switch mode
        self.switch_mode_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/date_time_frame/switch-mode-32x32px.png")
        switch_mode_button: ttk.Button = ttk.Button(self,
                                                    image=self.switch_mode_button_icon,
                                                    command=self.switch_mode,
                                                    style="AppButton.TButton")
        switch_mode_button.place(x=655, y=3)

        # show desktop
        self.show_desktop_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/date_time_frame/show-desktop-32x32px.png")
        show_desktop_button: ttk.Button = ttk.Button(self,
                                                     image=self.show_desktop_button_icon,
                                                     command=self.show_desktop,
                                                     style="AppButton.TButton")
        show_desktop_button.place(x=700, y=3)

        # lock screen
        self.lock_screen_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/date_time_frame/lock-screen-32x32px.png")
        lock_screen_button: ttk.Button = ttk.Button(self,
                                                    image=self.lock_screen_button_icon,
                                                    command=self.lock_screen,
                                                    style="AppButton.TButton")
        lock_screen_button.place(x=745, y=3)

        # close app
        self.close_app_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/date_time_frame/close-app-32x32px.png")
        close_app_button: ttk.Button = ttk.Button(self,
                                                  image=self.close_app_button_icon,
                                                  command=self.close_app,
                                                  style="AppButton.TButton")
        close_app_button.place(x=790, y=3)

    # methods
    def show_time(self):
        # get current date and time
        date_current = datetime.date.today()
        date_string = date_current.strftime("%B %d, %Y")
        self.date_var.set(date_string)

        time_current = datetime.datetime.now()
        time_string = time_current.strftime("%H:%M")  # :%S if seconds are required
        self.time_var.set(time_string)

        self.after(1000, self.show_time)

    def switch_mode(self):
        # switching between dark & light mode
        if self.button_mode:
            MainWindowStylingDarkMode()
            self.button_mode = False

        else:
            MainWindowStylingLightMode()
            self.button_mode = True

    @staticmethod
    def show_desktop():
        # minimize all windows -> Desktop
        pyautogui.hotkey("win", "d")

    @staticmethod
    def lock_screen():
        try:
            # bring user to lock screen -> re-enter password
            subprocess.run("rundll32.exe user32.dll,LockWorkStation")
        except Exception as E:
            print(f"{E} - Work Station could not be closed")

    @staticmethod
    def close_app():
        # destroy main window
        global root
        root.destroy()


class SystemInfoFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        # attributes
        self.ERROR: str = "Could not be read"
        self.INFO: str = "Press button for info"

        self.pc_name: tk.StringVar = tk.StringVar(value=self.INFO)
        self.pc_os: tk.StringVar = tk.StringVar(value=self.INFO)

        self.pc_cpu: tk.StringVar = tk.StringVar(value=self.INFO)
        self.pc_gpu: tk.StringVar = tk.StringVar(value=self.INFO)

        self.pc_ram: tk.StringVar = tk.StringVar(value=self.INFO)
        self.pc_drive: tk.StringVar = tk.StringVar(value=self.INFO)

        # widgets
        # description label
        frame_description_label: ttk.Label = ttk.Label(self,
                                                       text="Your System",
                                                       style="FrameDescriptionLabel.TLabel")
        frame_description_label.place(x=240, y=12)

        # load info button
        self.load_info_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/system_info_frame/load-info-32x32px.png")
        load_info_button: ttk.Button = ttk.Button(self,
                                                  image=self.load_info_button_icon,
                                                  command=self.load_all,
                                                  style="AppButton.TButton")
        load_info_button.place(x=365, y=4)

        # pc image
        self.pc_image: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/system_info_frame/laptop-image.png")
        pc_image: ttk.Label = ttk.Label(self,
                                        image=self.pc_image,
                                        style="Image.TLabel")
        pc_image.place(x=15, y=50)

        # processing unit info
        # heading
        processing_units_info_heading: ttk.Label = ttk.Label(self,
                                                             text="PROCESSING-UNIT INFORMATION:",
                                                             style="HardwareInfoHeading.TLabel")
        processing_units_info_heading.place(x=20, y=250)

        # cpu
        cpu_description_label: ttk.Label = ttk.Label(self,
                                                     text="CPU:",
                                                     style="DescriptionLabelSmaller.TLabel")
        cpu_description_label.place(x=20, y=285)

        cpu_info_label: ttk.Label = ttk.Label(self,
                                              textvariable=self.pc_cpu,
                                              style="HardwareComponentInfo.TLabel")
        cpu_info_label.place(x=67, y=285)

        # gpu
        gpu_description_label: ttk.Label = ttk.Label(self,
                                                     text="GPU:",
                                                     style="DescriptionLabelSmaller.TLabel")
        gpu_description_label.place(x=20, y=315)

        gpu_info_label: ttk.Label = ttk.Label(self,
                                              textvariable=self.pc_gpu,
                                              style="HardwareComponentInfo.TLabel")
        gpu_info_label.place(x=67, y=315)

        # software info
        # heading
        software_info_heading: ttk.Label = ttk.Label(self,
                                                     text="SOFTWARE INFORMATION:",
                                                     style="HardwareInfoHeading.TLabel")
        software_info_heading.place(x=335, y=70)

        # pc name
        name_description_label: ttk.Label = ttk.Label(self,
                                                      text="PC-NAME:",
                                                      style="DescriptionLabelSmaller.TLabel")
        name_description_label.place(x=335, y=105)

        name_info_label: ttk.Label = ttk.Label(self,
                                               textvariable=self.pc_name,
                                               style="HardwareComponentInfo.TLabel")
        name_info_label.place(x=422, y=105)

        # operating system
        os_description_label: ttk.Label = ttk.Label(self,
                                                    text="OS:",
                                                    style="DescriptionLabelSmaller.TLabel")
        os_description_label.place(x=335, y=135)

        os_info_label: ttk.Label = ttk.Label(self,
                                             textvariable=self.pc_os,
                                             style="HardwareComponentInfo.TLabel")
        os_info_label.place(x=370, y=135)

        # storage info
        # heading
        storage_info_heading: ttk.Label = ttk.Label(self,
                                                    text="STORAGE INFORMATION:",
                                                    style="HardwareInfoHeading.TLabel")
        storage_info_heading.place(x=335, y=180)

        # ram
        ram_description_label: ttk.Label = ttk.Label(self,
                                                     text="RAM:",
                                                     style="DescriptionLabelSmaller.TLabel")
        ram_description_label.place(x=335, y=215)

        ram_info_label: ttk.Label = ttk.Label(self,
                                              textvariable=self.pc_ram,
                                              style="HardwareComponentInfo.TLabel")
        ram_info_label.place(x=382, y=215)

        # drive
        drive_description_label: ttk.Label = ttk.Label(self,
                                                       text="DRIVE:",
                                                       style="DescriptionLabelSmaller.TLabel")
        drive_description_label.place(x=335, y=245)

        drive_info_label: ttk.Label = ttk.Label(self,
                                                textvariable=self.pc_drive,
                                                style="HardwareComponentInfo.TLabel")
        drive_info_label.place(x=395, y=245)

    # methods
    def load_general_info(self):
        # method to get all general information
        pc = wmi.WMI()

        # software information
        # name
        name_info = platform.node()
        self.pc_name.set(name_info)

        # os
        os_info = pc.Win32_OperatingSystem()[0].caption
        self.pc_os.set(os_info)

        # processing units info
        # cpu
        cpu_info = pc.Win32_Processor()[0].name
        self.pc_cpu.set(cpu_info)

        # gpu
        gpu_info = pc.Win32_VideoController()[0].name
        self.pc_gpu.set(gpu_info)

    def load_storage_info(self):
        # method to get all general information

        # get ram information
        try:
            ram_total_size = str(round((psutil.virtual_memory().total / 1024 / 1024 / 1024), 2))
            ram_currently_using_size = str(round((psutil.virtual_memory().used / 1024 / 1024 / 1024), 2))

            ram_info = f"{ram_total_size}GB, using {ram_currently_using_size}GB"
            self.pc_ram.set(ram_info)

        except PermissionError:
            self.pc_ram.set(self.ERROR)

        # get drive information
        try:
            first_partition = psutil.disk_partitions()[0]

            partition_usage = psutil.disk_usage(first_partition.mountpoint)

            drive_total_size = str(round((partition_usage.total / 1024 / 1024 / 1024), 2))
            drive_free_size = str(round((partition_usage.free / 1024 / 1024 / 1024), 2))

            drive_info = f"{drive_total_size}GB, {drive_free_size}GB free"
            self.pc_drive.set(drive_info)

        except PermissionError:
            self.pc_drive.set(self.ERROR)

    def load_all(self):
        try:
            # both methods are executed as soon as the method is used -> everything is loaded
            self.load_general_info()
            self.load_storage_info()
        except Exception as E:
            print(f"{E} - Information could not be read")
            self.pc_name.set(self.ERROR)
            self.pc_os.set(self.ERROR)
            self.pc_cpu.set(self.ERROR)
            self.pc_gpu.set(self.ERROR)
            self.pc_ram.set(self.ERROR)
            self.pc_drive.set(self.ERROR)


class QuickAccessFirst(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        # setup
        frame_description_label: ttk.Label = ttk.Label(self,
                                                       text="Quick Access",
                                                       style="FrameDescriptionLabel.TLabel")
        frame_description_label.place(x=40, y=12)

        # switch to second page
        self.switch_frame_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/quick_access_frames/down-arrow-32x32px.png")
        switch_frame_button: ttk.Button = ttk.Button(self,
                                                     image=self.switch_frame_button_icon,
                                                     command=lambda: controller.change_window(QuickAccessSecond),
                                                     style="AppButton.TButton")
        switch_frame_button.place(x=155, y=300)

        # letting the user open:
        # Task Manager
        self.open_task_manager_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/quick_access_frames/open-taskmanager-64x64px.png")
        open_task_manager_button: ttk.Button = ttk.Button(self,
                                                          image=self.open_task_manager_button_icon,
                                                          command=self.open_task_manager,
                                                          style="AppButton.TButton")
        open_task_manager_button.place(x=15, y=50)

        open_task_manager_label: ttk.Label = ttk.Label(self,
                                                       text="System",
                                                       style="DescriptionLabelSmaller.TLabel")
        open_task_manager_label.place(x=100, y=80)

        # Internet
        self.open_internet_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/quick_access_frames/open-internet-64x64px.png")
        open_internet_button: ttk.Button = ttk.Button(self,
                                                      image=self.open_internet_button_icon,
                                                      command=self.open_internet,
                                                      style="AppButton.TButton")
        open_internet_button.place(x=15, y=135)

        open_internet_label: ttk.Label = ttk.Label(self,
                                                   text="Internet",
                                                   style="DescriptionLabelSmaller.TLabel")
        open_internet_label.place(x=100, y=165)

        # Explorer
        self.open_explorer_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/quick_access_frames/open-explorer-64x64px.png")
        open_explorer_button: ttk.Button = ttk.Button(self,
                                                      image=self.open_explorer_button_icon,
                                                      command=self.open_explorer,
                                                      style="AppButton.TButton")
        open_explorer_button.place(x=15, y=220)

        open_explorer_label: ttk.Label = ttk.Label(self,
                                                   text="Explorer",
                                                   style="DescriptionLabelSmaller.TLabel")
        open_explorer_label.place(x=100, y=250)

    # methods
    @staticmethod
    def open_task_manager():
        command = "taskmgr.exe"

        try:
            # run
            subprocess.call([command], shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")

    @staticmethod
    def open_internet():
        url = "https://www.google.com"
        command = f"start {url}"

        try:
            # run
            subprocess.call(command, shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")

    @staticmethod
    def open_explorer():
        explorer_path = "explorer.exe"
        command = f"start {explorer_path}"

        try:
            # run
            subprocess.call(command, shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")


class QuickAccessSecond(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        # setup
        frame_description_label: ttk.Label = ttk.Label(self,
                                                       text="Quick Access",
                                                       style="FrameDescriptionLabel.TLabel")
        frame_description_label.place(x=40, y=12)

        # switch to second page
        self.switch_frame_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/quick_access_frames/up-arrow-32x32px.png")
        switch_frame_button: ttk.Button = ttk.Button(self,
                                                     image=self.switch_frame_button_icon,
                                                     command=lambda: controller.change_window(QuickAccessFirst),
                                                     style="AppButton.TButton")
        switch_frame_button.place(x=155, y=300)

        # letting the user open:
        # notepad
        self.open_notepad_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/quick_access_frames/open-notepad-64x64px.png")
        open_notepad_button: ttk.Button = ttk.Button(self,
                                                     image=self.open_notepad_button_icon,
                                                     command=self.open_notepad,
                                                     style="AppButton.TButton")
        open_notepad_button.place(x=15, y=50)

        open_notepad_label: ttk.Label = ttk.Label(self,
                                                  text="Notepad",
                                                  style="DescriptionLabelSmaller.TLabel")
        open_notepad_label.place(x=100, y=80)

        # settings
        self.open_settings_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/quick_access_frames/open-settings-64x64px.png")
        open_settings_button: ttk.Button = ttk.Button(self,
                                                      image=self.open_settings_button_icon,
                                                      command=self.open_settings,
                                                      style="AppButton.TButton")
        open_settings_button.place(x=15, y=135)

        open_settings_label: ttk.Label = ttk.Label(self,
                                                   text="Settings",
                                                   style="DescriptionLabelSmaller.TLabel")
        open_settings_label.place(x=100, y=165)

        # command line
        self.open_cmd_button_icon: tk.PhotoImage = tk.PhotoImage(
            file=r"graphics/quick_access_frames/open-cmd-64x64px.png")
        open_cmd_button: ttk.Button = ttk.Button(self,
                                                 image=self.open_cmd_button_icon,
                                                 command=self.open_cmd,
                                                 style="AppButton.TButton")
        open_cmd_button.place(x=15, y=220)

        open_cmd_label: ttk.Label = ttk.Label(self,
                                              text="CMD",
                                              style="DescriptionLabelSmaller.TLabel")
        open_cmd_label.place(x=100, y=250)

    # methods
    @staticmethod
    def open_notepad():
        notepad_path = "notepad.exe"
        command = f"start {notepad_path}"

        try:
            # run
            subprocess.call(command, shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")

    @staticmethod
    def open_settings():
        command = "start ms-settings:"

        try:
            # run
            subprocess.call(command, shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")

    @staticmethod
    def open_cmd():
        command = "start cmd"

        try:
            # run
            subprocess.call(command, shell=True)
        except Exception as E:
            print(f"{E} - Could not open {command}")


class ApplicationsFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        # letting user start 3 different applications:
        # app 1 - calculator
        self.calculator_app_icon: tk.PhotoImage = tk.PhotoImage(
            file="graphics/applications_frame/start-calculator-64x64px.png")
        calculator_app_button: ttk.Button = ttk.Button(self,
                                                       image=self.calculator_app_icon,
                                                       command=self.start_calculator,
                                                       style="AppButton.TButton")
        calculator_app_button.place(x=20, y=20)

        calculator_app_label: ttk.Label = ttk.Label(self,
                                                    text="Calculator",
                                                    style="FrameDescriptionLabel.TLabel")
        calculator_app_label.place(x=105, y=50)

        # app 2 - password generator
        self.password_generator_app_icon: tk.PhotoImage = tk.PhotoImage(
            file="graphics/applications_frame/start-generator-64x64px.png")
        password_generator_app_button: ttk.Button = ttk.Button(self,
                                                               image=self.password_generator_app_icon,
                                                               command=self.start_password_generator,
                                                               style="AppButton.TButton")
        password_generator_app_button.place(x=285, y=20)

        password_generator_app_label: ttk.Label = ttk.Label(self,
                                                            text="Key Generator",
                                                            style="FrameDescriptionLabel.TLabel")
        password_generator_app_label.place(x=370, y=50)

        # app 3 - screenshot
        self.take_screenshot_app_icon: tk.PhotoImage = tk.PhotoImage(
            file="graphics/applications_frame/take-screenshot-64x64px.png")
        take_screenshot_app_button: ttk.Button = ttk.Button(self,
                                                            image=self.take_screenshot_app_icon,
                                                            command=self.take_screenshot,
                                                            style="AppButton.TButton")
        take_screenshot_app_button.place(x=600, y=20)

        take_screenshot_app_label: ttk.Label = ttk.Label(self,
                                                         text="Screenshot",
                                                         style="FrameDescriptionLabel.TLabel")
        take_screenshot_app_label.place(x=685, y=50)

    # methods
    @staticmethod
    def start_password_generator():
        global root
        # creating Toplevel window
        password_generator: RandomPasswordGenerator = RandomPasswordGenerator(root)
        password_generator.grab_set()

    @staticmethod
    def start_calculator():
        global root
        # creating Toplevel window
        calculator: Calculator = Calculator(root)
        calculator.grab_set()

    @staticmethod
    def take_screenshot():
        global root

        root.iconify()
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        root.deiconify()

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if file_path:
            screenshot.save(file_path)
            messagebox.showinfo("Screenshot was taken!", f"Screenshot saved in {file_path}.")
        else:
            messagebox.showerror("Screenshot was not taken!", message="Screenshot not saved.")


if __name__ == "__main__":
    root: MainWindow = MainWindow()
    root.mainloop()
