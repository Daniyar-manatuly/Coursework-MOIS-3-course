from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os


def open_login_page():
    try:
        os.system("python Login_page.py")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Login_page.py: {e}")


def open_register_page():
    try:
        os.system("python Registration_page.py")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Registration_page.py: {e}")


def open_dashboard():
    try:
        os.system("python Air_prediction.py")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Air_prediction.py: {e}")


def open_comparison_model():
    try:
        os.system("python comparison.py")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open comparison.py: {e}")


def show_contact_us():
    contact_text = (
        "You can contact us using the following details:\n"
        "Email: toleubai_dm@enu.kz\n"
        "Phone: +7 (7172) 709 500\n"
        "Address: 1 L.N. Gumilyov Eurasian National University,\n"
        "Information Systems Department,\n"
        "2, Satpayev Street, 010008 Astana, Kazakhstan."
    )
    contact_window = Toplevel(admin_window)
    contact_window.title("Contact Us")
    contact_window.geometry("600x400")

    # Set the background color for Contact Us window
    contact_window.configure(bg="#F0F9FF")

    Label(contact_window, text=contact_text, font=('Helvetica', 12), justify=LEFT, bg="#F0F9FF").pack(pady=10)

    # Email text box
    Label(contact_window, text="Write your message:", font=('Helvetica', 12), bg="#F0F9FF").pack(pady=10)

    message_box = Text(contact_window, height=8, width=50, font=('Helvetica', 12))
    message_box.pack(pady=10)

    # Send button
    Button(contact_window, text="Send", font=('Helvetica', 14), bg="#22C55E",
           command=lambda: messagebox.showinfo("Message", "Your message has been sent!")).pack(pady=10)


def show_about_project():
    project_text = (
        "The Air Quality Prediction project is designed to predict air quality in Astana\n"
        "by using machine learning models. The project includes user registration,\n"
        "login functionality, air quality predictions based on Astana, and model\n"
        "visualization features. The main goal is to help users understand the air\n"
        "quality in their make informed decisions."
    )

    # Create About Project window with a nice background color
    project_window = Toplevel(admin_window)
    project_window.title("About Project")
    project_window.geometry("600x400")

    # Set background color and center the title
    project_window.configure(bg="#D1FAE5")

    # Add a centered title at the top
    Label(project_window, text="About Project", font=('Helvetica', 18, 'bold'), fg="#374151", bg="#D1FAE5").pack(
        pady=20)

    # Add project description
    Label(project_window, text=project_text, font=('Helvetica', 12), justify=LEFT, bg="#D1FAE5").pack(pady=10)

    # Add Back button to go to Main Menu
    Button(project_window, text="Back", font=('Helvetica', 14), bg="#10B981", fg="white",
           command=project_window.destroy).pack(pady=20)


def show_about_model():
    try:
        os.system("python comparison.py")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open comparison.py: {e}")


def exit_application():
    admin_window.quit()


admin_window = Tk()
admin_window.attributes("-fullscreen", True)
admin_window.configure(bg="#F3F4F6")
admin_window.title("Main Menu")

canvas = Canvas(admin_window)
canvas.pack(fill=BOTH, expand=True)
canvas.create_rectangle(0, 0, 1920, 1080, fill="#6EE7B7", outline="#34D399")

# Add the image
image_path = r"C:\Users\opste\Desktop\aa.webp"
try:
    img = Image.open(image_path)
    img = img.resize((500, 400), Image.LANCZOS)  # Resize the image with LANCZOS filter
    img_tk = ImageTk.PhotoImage(img)
    img_label = Label(admin_window, image=img_tk, bg="#6EE7B7")
    img_label.image = img_tk  # Keep a reference to prevent garbage collection
    img_label.place(relx=0.5, rely=0.3, anchor=CENTER)  # Position image higher for better visual balance
except Exception as e:
    messagebox.showerror("Error", f"Failed to load the image: {e}")


def create_button(frame, text, command, color, width=15):
    return Button(frame, text=text, font=('Helvetica', 14, 'bold'), bg=color, fg="white", bd=0, relief='flat',
                  width=width, height=2, command=command,
                  activebackground=color, activeforeground="white",
                  highlightthickness=0)


menu_frame = Frame(admin_window, bg="#F3F4F6")
menu_frame.pack(pady=30)

loginButton = create_button(menu_frame, "Login", open_login_page, "#3B82F6")
loginButton.pack(side=LEFT, padx=10)

registerButton = create_button(menu_frame, "Register", open_register_page, "#10B981")
registerButton.pack(side=LEFT, padx=10)

contactButton = create_button(menu_frame, "Contact us", show_contact_us, "#6366F1")
contactButton.pack(side=LEFT, padx=10)

projectButton = create_button(menu_frame, "About project", show_about_project, "#A855F7")
projectButton.pack(side=LEFT, padx=10)

modelButton = create_button(menu_frame, "About Model", show_about_model, "#EC4899")
modelButton.pack(side=LEFT, padx=10)

dashboardButton = create_button(menu_frame, "Air prediction", open_dashboard, "#F59E0B")
dashboardButton.pack(side=LEFT, padx=10)

exitButton = create_button(menu_frame, "Exit", exit_application, "#EF4444")
exitButton.pack(side=LEFT, padx=10)

title = Label(admin_window, text="Air quality prediction in Astana", font=('Helvetica', 50, 'bold'), fg="#374151", bg="#F3F4F6")
title.pack(pady=50)

footer = Label(admin_window, text="© 2024 Air Quality Prediction System", font=('Helvetica', 10), bg="#F3F4F6",
               fg="#9CA3AF")
footer.pack(side=BOTTOM, pady=20)

admin_window.mainloop()

