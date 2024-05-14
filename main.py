import customtkinter as ctk

class App_Menu(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.logo = ctk.CTkLabel(root, text="Dear_Us")
        self.logo.grid(row=0, column=0, padx=10, pady=(10), sticky="new")

        self.account_create = ctk.CTkButton(self, text="Create Account")
        self.account_create.grid(row=1, column=0, padx=10, pady=(10), sticky="se")

        self.account_signin = ctk.CTkButton(self, text="Sign In")
        self.account_signin.grid(row=1, column=1, padx=10, pady=(10), sticky="sew")

        self.quit_app = ctk.CTkButton(self, text="Quit App")
        self.quit_app.grid(row=1, column=2, padx=10, pady=(10), sticky="sw")

class Menu_Choices(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

    

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dear_Us")
        self.geometry("1600x900")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_frame = App_Menu(self)
        self.menu_frame.grid(row=0, column=0, padx=10, pady=(10), sticky="ew")

app = App()
app.mainloop()