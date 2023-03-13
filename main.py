import tkinter as tk
import mysql.connector
import customtkinter as ctk

connection = mysql.connector.connect(host='localhost', user='root', password='mysql@23', port='3306',
                                     database='asap_database')
cursor = connection.cursor()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("800x500")
root.title("ASAP")

scrollable_frame = ctk.CTkScrollableFrame(master=root, width=200, height=200)
scrollable_frame.pack(pady=20, padx=60, fill="both", expand=True)

question = ""


def login():
    login_username = login_entry1.get().lower()
    login_username = login_username.replace(" ", "")
    user_present = user_exists(login_username)
    login_password = login_entry2.get()

    # password_match(login_username, login_password)

    if not user_present:
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        popup = ctk.CTkToplevel()
        popup.geometry("400x150")
        popup.title("Login status")
        popup.attributes('-topmost', True)
        frame = ctk.CTkScrollableFrame(master=popup)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = ctk.CTkLabel(master=frame, text="User not found\nSignup to create account", width=25,
                             font=('calibri', 20))
        label.pack(pady=12, padx=10)
        button = ctk.CTkButton(master=frame, text="OK", command=popup.destroy)
        button.pack(pady=12, padx=10)
    else:
        if not password_match(login_username, login_password):
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("green")
            popup = ctk.CTkToplevel()
            popup.geometry("500x200")
            popup.title("Login status")
            popup.attributes('-topmost', True)
            frame = ctk.CTkScrollableFrame(master=popup)
            frame.pack(pady=20, padx=60, fill="both", expand=True)
            label = ctk.CTkLabel(master=frame, text="Incorrect password\nNote: Password is case sensitive", width=25,
                                 font=('calibri', 20))
            label.pack(pady=12, padx=10)
            button = ctk.CTkButton(master=frame, text="OK", command=popup.destroy)
            button.pack(pady=12, padx=10)
            print("Login Unsuccessful")

        else:
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("green")
            popup = ctk.CTkToplevel()
            popup.geometry("400x150")
            popup.title("Signup status")
            popup.attributes('-topmost', True)
            frame = ctk.CTkScrollableFrame(master=popup)
            frame.pack(pady=20, padx=60, fill="both", expand=True)
            label = ctk.CTkLabel(master=frame, text="Login successful", width=25,
                                 font=('calibri', 20))
            label.pack(pady=12, padx=10)
            button = ctk.CTkButton(master=frame, text="OK", command=popup.destroy)
            button.pack(pady=12, padx=10)
            print("login successful")
            open_home()


def password_match(luname, lpass):
    select_query = f"SELECT password FROM asap_database.signup_table WHERE username = '{luname}';"
    # print(select_query)
    cursor.execute(select_query)
    db_pass = []
    for row in cursor:
        db_pass.append(row[0])
    # print(db_pass)

    if lpass == db_pass[0]:
        return True
    else:
        return False


def signup():
    global username
    firstname = signup_entry1.get()
    lastname = signup_entry2.get()
    username = signup_entry3.get().lower()
    username = username.replace(" ", "")
    password = signup_entry4.get()
    phone = signup_entry5.get()
    email = signup_entry6.get()

    if user_exists(username):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        popup = ctk.CTkToplevel()
        popup.geometry("400x150")
        popup.title("Signup status")
        popup.attributes('-topmost', True)
        frame = ctk.CTkScrollableFrame(master=popup)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = ctk.CTkLabel(master=frame, text="Username already taken\ntry another username", width=25,
                             font=('calibri', 20))
        label.pack(pady=12, padx=10)
        button = ctk.CTkButton(master=frame, text="OK", command=popup.destroy)
        button.pack(pady=12, padx=10)

    elif username == "":
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        popup = ctk.CTkToplevel()
        popup.geometry("350x250")
        popup.title("Username cannot be empty")
        popup.attributes('-topmost', True)
        frame = ctk.CTkScrollableFrame(master=popup)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = ctk.CTkLabel(master=frame,
                             text="Enter a valid username \n\n Username must be\nin lowercase and\n must not be empty \n\n(All the whitespaces\n are removed from the\n username)",
                             width=25, font=('calibri', 20))
        label.pack(pady=12, padx=10)
        button = ctk.CTkButton(master=frame, text="OK", command=popup.destroy)
        button.pack(pady=12, padx=10)
    else:
        # insertion of values to db
        insert_query = "INSERT INTO asap_database.signup_table (first_name, last_name, username, password, phone, email) VALUES (%s, %s, %s, %s, %s, %s);"
        values = (firstname, lastname, username, password, phone, email)
        cursor.execute(insert_query, values)
        connection.commit()
        print("Signup successful")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        popup = ctk.CTkToplevel()
        popup.geometry("350x250")
        popup.title("Signup status")
        popup.attributes('-topmost', True)
        frame = ctk.CTkScrollableFrame(master=popup)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = ctk.CTkLabel(master=frame,
                             text=f"Signup successful\nYour username:{username}",
                             width=25, font=('calibri', 20))
        label.pack(pady=12, padx=10)
        button = ctk.CTkButton(master=frame, text="OK", command=popup.destroy)
        button.pack(pady=12, padx=10)
        signup_window.destroy()


def user_exists(uname):
    # if username == "":
    #     print("Username cannot be empty")
    #
    fetch_query = "SELECT username FROM asap_database.signup_table"
    cursor.execute(fetch_query)
    existing_users = []

    for row in cursor:
        existing_users.append(row[0])

    if uname in existing_users:
        return True
    else:
        return False


def open_home():
    scrollable_frame.destroy()
    home()


def home():
    home_frame = ctk.CTkScrollableFrame(master=root)

    # input_field = tk.Entry(master=root, bd=0, bg="#D6D6D6", font="Arial")
    # input_field.place(x=128, y=401, height=30, width=265)
    entry = ctk.CTkEntry(master=root,
                         placeholder_text="Chat with me",
                         width=500,
                         height=25,
                         border_width=2,
                         corner_radius=10,
                         # question=entry.get()
                         )
    entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    entry.pack()
    send_button = ctk.CTkButton(master=root, text="Send", command=send_message)
    send_button.pack(pady=12, padx=20)
    # home_frame.pack(pady=200, padx=60, fill="both", expand=True)


def send_message():
    pass


def open_signup():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    # registerPage = Toplevel(root)
    # registerPage.geometry("800x500")
    # registerPage.title("Register")
    global signup_entry1
    global signup_entry2
    global signup_entry3
    global signup_entry4
    global signup_entry5
    global signup_entry6

    global signup_window
    signup_window = ctk.CTkToplevel()
    signup_window.geometry("800x500")
    signup_window.title("ASAP Signup")
    signup_window.attributes('-topmost', True)

    frame = ctk.CTkScrollableFrame(master=signup_window)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Signup System", width=25, font=('calibri', 40))
    label.pack(pady=12, padx=10)

    signup_entry1 = ctk.CTkEntry(master=frame, placeholder_text="First name")
    signup_entry1.pack(pady=12, padx=10)

    signup_entry2 = ctk.CTkEntry(master=frame, placeholder_text="Last name")
    signup_entry2.pack(pady=12, padx=10)

    signup_entry3 = ctk.CTkEntry(master=frame, placeholder_text="Username")
    signup_entry3.pack(pady=12, padx=10)

    signup_entry4 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    signup_entry4.pack(pady=12, padx=10)

    signup_entry5 = ctk.CTkEntry(master=frame, placeholder_text="Contact number")
    signup_entry5.pack(pady=12, padx=10)

    signup_entry6 = ctk.CTkEntry(master=frame, placeholder_text="Email")
    signup_entry6.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text="Login", command=signup_window.destroy)
    button.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text="Sign up", command=signup)
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


label = ctk.CTkLabel(master=scrollable_frame, text="Login System", font=('calibri', 40))
label.pack(pady=12, padx=10)

login_entry1 = ctk.CTkEntry(master=scrollable_frame, placeholder_text="Username")
login_entry1.pack(pady=12, padx=10)

login_entry2 = ctk.CTkEntry(master=scrollable_frame, placeholder_text="Password", show="*")
login_entry2.pack(pady=12, padx=10)

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
