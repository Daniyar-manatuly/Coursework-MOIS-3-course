from tkinter import *
from tkinter import messagebox
import psycopg2 as pg
# Функция для подключения к базе данных
def create_connection():
    conn = pg.connect(host='localhost', database='Air_quality', port='5432', user='postgres', password='2802')
    return conn

# Функция для проверки учетных данных
def login_command():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Проверка учетных данных в базе данных
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute("SELECT username, password FROM login_page WHERE username=%s AND password=%s", (username, password))
        row = cur.fetchone()
        conn.close()

        if row:
            messagebox.showinfo("Success", "Login successful!")
            # Переход на главную страницу или другую страницу после успешного входа
            login_window.destroy()
            # Здесь используем нужный файл, например:
            # import main_page  # Замените на ваш основной интерфейс
            print("Login successful, transitioning to main page.")  # Для отладки
        else:
            messagebox.showerror("Error", "Invalid username or password!")
    except Exception as e:
        messagebox.showerror("Database Error", f"Error connecting to the database: {e}")

# Создание окна для входа
login_window = Tk()
login_window.geometry('800x600')
login_window.resizable(0, 0)
login_window.title("Login Page")
login_window.configure(bg="#F0F4F8")

# Добавление заголовка
title = Label(login_window, text="Login to Air Quality System", font=('Helvetica', 26, 'bold'), fg="#374151", bg="#F0F4F8")
title.pack(pady=40)

# Метки и поля ввода
username_label = Label(login_window, text="Username", font=('Helvetica', 14), bg='#F0F4F8', fg='#000000')
username_label.pack(pady=10)
usernameEntry = Entry(login_window, width=30, font=('Helvetica', 14), bd=2, relief='groove', highlightthickness=2, highlightbackground="#3B82F6")
usernameEntry.pack(pady=10)

password_label = Label(login_window, text="Password", font=('Helvetica', 14), bg='#F0F4F8', fg='#000000')
password_label.pack(pady=10)
passwordEntry = Entry(login_window, show="*", width=30, font=('Helvetica', 14), bd=2, relief='groove', highlightthickness=2, highlightbackground="#3B82F6")
passwordEntry.pack(pady=10)

# Кнопка для входа
loginButton = Button(login_window, text="Login", font=('Helvetica', 14, 'bold'), bg="#3B82F6", fg="white", bd=0, relief='flat',
                     width=15, height=2, command=login_command)
loginButton.pack(pady=20)

# Footer
footer = Label(login_window, text="© 2024 Air Quality Prediction System", font=('Helvetica', 10), bg="#F0F4F8", fg="#9CA3AF")
footer.pack(side=BOTTOM, pady=10)

# Запуск приложения
login_window.mainloop()
