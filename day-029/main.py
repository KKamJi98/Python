import tkinter
import os

IMAGE_PATH = os.path.join(os.path.dirname(__file__), "logo.png")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_image = tkinter.PhotoImage(file=IMAGE_PATH)
image_width = logo_image.width()
image_height = logo_image.height()

canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Website
website_label = tkinter.Label(text="Website:", font="Courier")
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

# Email/Username
email_and_username_label = tkinter.Label(text="Email/Username:", font="Courier")
email_and_username_label.grid(column=0, row=2)

email_and_username_entry = tkinter.Entry(width=35)
email_and_username_entry.grid(column=1, row=2, columnspan=2)

# Password

def generate_password():
    pass

password_label = tkinter.Label(text="Password:", font="Courier")
password_label.grid(column=0, row=3)

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

# Add
def add_password():
    pass

add_button = tkinter.Button(text="Add", command=add_password, width=36)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()