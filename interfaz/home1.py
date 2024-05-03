import customtkinter

customtkinter.set_appearance_mode("dark")  # Login initial parameters
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    username = entry1.get()
    password = entry2.get()
    # Dummy authentication, replace with your actual authentication logic
    if username == "admin" and password == "password":
        tabhome()  # If authenticated, go to the home page
    else:
        print("Invalid credentials")

def tabhome():
    global frame_home
    frame.destroy()  # Destroy the login frame
    frame_home = customtkinter.CTkFrame(master=root)
    frame_home.pack(pady=20, padx=60, fill="both", expand=True)

    label_home = customtkinter.CTkLabel(master=frame_home, text="Control System", font=('roboto', 24))
    label_home.pack(pady=12, padx=10)

    button_change_user = customtkinter.CTkButton(master=frame_home, text="Change user", command=change_user)
    button_change_user.pack(pady=12, padx=10)

def change_user():
    global frame_home
    frame_home.destroy()  # Destroy the home frame
    tablogin()  # Go back to the login page

def tablogin():
    global frame, entry1, entry2  # Need to declare these as global to access them outside of this function
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Loggin System", font=('roboto', 24))
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)

# Initially, show the login page
tablogin()

root.mainloop()
