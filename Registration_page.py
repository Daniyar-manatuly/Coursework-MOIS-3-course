from tkinter import *
from tkinter import messagebox
import psycopg2 as pg

def create_connection():
    conn = pg.connect(host='localhost', database='Air_quality', port='5432', user='postgres', password='2802')
    return conn

def register_command():
    username = usernameEntry.get()
    password = passwordEntry.get()
    birth_year = birthYearEntry.get()
    phone = phoneEntry.get()
    email = emailEntry.get()
    country = countryEntry.get()
    gender = genderVar.get()

    if not all([username, password, birth_year, phone, email, country, gender]):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        conn = create_connection()
        cur = conn.cursor()

        # Проверка на существование пользователя
        cur.execute("SELECT username FROM login_page WHERE username=%s", (username,))
        if cur.fetchone():
            messagebox.showerror("Error", "Username already exists!")
        else:
            # Вставка нового пользователя
            cur.execute("""
                INSERT INTO login_page (username, password, birth_year, phone, email, country, gender)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (username, password, birth_year, phone, email, country, gender))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            register_window.destroy()

        conn.close()
    except Exception as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")

register_window = Tk()
register_window.geometry('800x700')
register_window.resizable(0, 0)
register_window.title("Registration Page")
register_window.configure(bg="#F0F4F8")

title = Label(register_window, text="Register to Air Quality System", font=('Helvetica', 26, 'bold'), fg="#374151", bg="#F0F4F8")
title.pack(pady=20)

def create_label_entry(label_text, parent, entry_width=30, show=None):
    label = Label(parent, text=label_text, font=('Helvetica', 14), bg='#F0F4F8', fg='#000000')
    label.pack(pady=5)
    entry = Entry(parent, width=entry_width, font=('Helvetica', 14), bd=2, relief='groove', highlightthickness=2, highlightbackground="#3B82F6", show=show)
    entry.pack(pady=5)
    return entry

usernameEntry = create_label_entry("Username", register_window)
passwordEntry = create_label_entry("Password", register_window, show="*")
birthYearEntry = create_label_entry("Year of Birth", register_window)
phoneEntry = create_label_entry("Phone Number", register_window)
emailEntry = create_label_entry("Email", register_window)
countryEntry = create_label_entry("Country", register_window)

gender_label = Label(register_window, text="Gender", font=('Helvetica', 14), bg='#F0F4F8', fg='#000000')
gender_label.pack(pady=5)

genderVar = StringVar(value="None")
gender_frame = Frame(register_window, bg="#F0F4F8")
gender_frame.pack(pady=5)

maleRadio = Radiobutton(gender_frame, text="Male", variable=genderVar, value="Male", font=('Helvetica', 12), bg="#F0F4F8")
femaleRadio = Radiobutton(gender_frame, text="Female", variable=genderVar, value="Female", font=('Helvetica', 12), bg="#F0F4F8")
otherRadio = Radiobutton(gender_frame, text="Other", variable=genderVar, value="Other", font=('Helvetica', 12), bg="#F0F4F8")

maleRadio.pack(side=LEFT, padx=10)
femaleRadio.pack(side=LEFT, padx=10)
otherRadio.pack(side=LEFT, padx=10)

registerButton = Button(register_window, text="Register", font=('Helvetica', 14, 'bold'), bg="#10B981", fg="white", bd=0, relief='flat',
                        width=15, height=2, command=register_command)
registerButton.pack(pady=20)

footer = Label(register_window, text="© 2024 Air Quality Prediction System", font=('Helvetica', 10), bg="#F0F4F8", fg="#9CA3AF")
footer.pack(side=BOTTOM, pady=10)

register_window.mainloop()
