import tkinter aspp tk
from tkinter import messagebox
import webbrowser, os, subprocess, sys, time

BASE_DIR = os.path.dirname(__file__)
HTML_FILE = os.path.join(BASE_DIR, "index.html")
SERVER_FILE = os.path.join(BASE_DIR, "server.py")
DESKTOP_FILE = os.path.join(BASE_DIR, "desktop_stt.py")
DB_GUI = os.path.join(BASE_DIR, "index.py")  # if user has GUI script for DB

def open_web_app():
    # Start server.py in background then open browser
    if os.path.exists(SERVER_FILE):
        # start Flask server
        subprocess.Popen([sys.executable, SERVER_FILE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.8)
    webbrowser.open_new_tab("file://" + HTML_FILE)

def open_desktop_app():
    subprocess.Popen([sys.executable, DESKTOP_FILE])

def open_db_gui():
    if os.path.exists(DB_GUI):
        subprocess.Popen([sys.executable, DB_GUI])
    else:
        messagebox.showinfo("Info", "Database GUI not found")

def login_success(root):
    root.destroy()
    choice = tk.Tk()
    choice.title("Choose Application")
    choice.geometry("320x200")
    tk.Label(choice, text="Select Application:", font=("Arial",12)).pack(pady=12)
    tk.Button(choice, text="🌐 Web App", width=18, command=open_web_app).pack(pady=6)
    tk.Button(choice, text="🖥 Desktop App", width=18, command=open_desktop_app).pack(pady=6)
    tk.Button(choice, text="📁 Database GUI", width=18, command=open_db_gui).pack(pady=6)
    choice.mainloop()

def try_login():
    user = user_entry.get()
    pwd = pwd_entry.get()
    if user == "Admin" and pwd == "123":
        login_success(root)
    else:
        messagebox.showerror("Login failed", "Invalid credentials")

# Login window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")
tk.Label(root, text="Username").pack(pady=6)
user_entry = tk.Entry(root); user_entry.pack(pady=6)
tk.Label(root, text="Password").pack(pady=6)
pwd_entry = tk.Entry(root, show="*"); pwd_entry.pack(pady=6)
tk.Button(root, text="Login", command=try_login).pack(pady=12)

root.mainloop()
