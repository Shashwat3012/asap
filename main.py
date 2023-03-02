from tkinter import *

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x500")
root.title("ASAP")

scrollable_frame = ctk.CTkScrollableFrame(master=root, width=200, height=200)
scrollable_frame.pack(pady=20, padx=60, fill="both", expand=True)


def login():
    print("Login Successful")


def signup():
    print("Signup successful")


def open_signup():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    # registerPage = Toplevel(root)
    # registerPage.geometry("800x500")
    # registerPage.title("Register")

    signup_window = ctk.CTkToplevel()
    signup_window.geometry("800x500")
    signup_window.title("ASAP Signup")

    frame = ctk.CTkScrollableFrame(master=signup_window)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Signup System", width=25, font=('calibri',40))
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="First name")
    entry1.pack(pady=12, padx=10)

    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Last name")
    entry2.pack(pady=12, padx=10)

    entry3 = ctk.CTkEntry(master=frame, placeholder_text="Username")
    entry3.pack(pady=12, padx=10)

    entry4 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry4.pack(pady=12, padx=10)

    entry5 = ctk.CTkEntry(master=frame, placeholder_text="Contact number")
    entry5.pack(pady=12, padx=10)

    entry6 = ctk.CTkEntry(master=frame, placeholder_text="Email")
    entry6.pack(pady=12, padx=10)

    button= ctk.CTkButton(master=frame, text="Login", command=signup_window.destroy)
    button.pack(pady=12, padx=10)

    button= ctk.CTkButton(master=frame, text="Sign up", command=signup)
    button.pack(pady=12, padx=10)

    checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)


# def googleLogin():
#     print(pyautogui.position())
#     pyautogui.click(359, 100)
#     pyautogui.click(359, 100)
#     link = "https://accounts.google.com/signin"
#     pyautogui.typewrite(link)
#     pyautogui.press("enter")


label = ctk.CTkLabel(master=scrollable_frame, text="Login System", font=('calibri',40))
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=scrollable_frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=scrollable_frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=scrollable_frame, text="Login", command=login)
button.pack(pady=12, padx=10)

button = ctk.CTkButton(master=scrollable_frame, text="Sign up", command=open_signup)
button.pack(pady=12, padx=10)

# button = ctk.CTkButton(master=frame, text="Login with google", command=googleLogin)
# button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=scrollable_frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()

# vertical_scroll = Scrollbar(root)
# vertical_scroll.pack(side=RIGHT, fill=Y)
# vertical_scroll.config(command=root.frame)

# class MyFrame(ctk.CTkScrollableFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)
#
#         # add widgets onto the frame...
#         self.label = ctk.CTkLabel(self)
#         self.label.grid(row=0, column=0, padx=20)
#
#
# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)
#
#         self.my_frame = MyFrame(master=self, width=300, height=200, corner_radius=0, fg_color="transparent")
#         self.my_frame.grid(row=0, column=0, sticky="nsew")
#
#
# app = App()
# app.mainloop()
