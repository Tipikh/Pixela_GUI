from tkinter import *
from tkinter import ttk, messagebox
import my_funcs
from tkinter import font as tkfont


class WelcomePage(Frame):
    """
    A frame with three buttons, where the user can chose to log in,
    create an account or delete an account
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # UsernamePage Label
        self.welcome_label = ttk.Label(self, width=15, text="Welcome !", font=self.controller.title_font,
                                       foreground='#393E46', anchor='center')
        self.welcome_label.grid(column=1, row=0, columnspan=2, padx=10, pady=10)

        # Log in Button
        back_button = ttk.Button(self, text="Log in", command=lambda: controller.show_frame('LoginPage'),
                                 style='Accentbutton')
        back_button.grid(column=1, row=4, columnspan=2, padx=20, pady=20, ipadx=21, ipady=10)

        # Create Button
        back_button = ttk.Button(self, text="Create account",
                                 command=lambda: controller.show_frame('CreateAccountPage'), style='Accentbutton')
        back_button.grid(column=1, row=3, columnspan=2, padx=20, pady=20, ipadx=10, ipady=10)

        # Delete Account Button
        delete_button = ttk.Button(self, text="Delete Account",
                                   command=lambda: controller.show_frame('DeleteAccountPage'), style='Accentbutton')
        delete_button.grid(column=1, row=5, columnspan=2, padx=20, pady=20, ipadx=10, ipady=10)


class LoginPage(Frame):
    """ 
    A frame with 2 entry and 2 button where the user can log in
    with his username and password
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Username Label
        self.login_label = ttk.Label(self, width=20, text="Login Page", foreground='#393E46',
                                     font=self.controller.font, anchor='center')
        self.login_label.grid(column=1, row=0, columnspan=2, padx=10, pady=10)
        # self.username_label.place(x=120, y=200)

        # Username Entry
        username_label = ttk.Label(self, text='Username :')
        username_label.grid(column=1, row=1, padx=10, pady=10)
        self.username_entry = ttk.Entry(self, width=20)
        self.username_entry.grid(column=2, row=1, padx=10, pady=10)

        # Password Entry
        password_label = ttk.Label(self, text='Password :')
        password_label.grid(column=1, row=2, padx=10, pady=10)
        self.password_entry = ttk.Entry(self, width=20)
        self.password_entry.grid(column=2, row=2, padx=10, pady=10)

        # Log in Button
        change_user_button = ttk.Button(self, text="Log in", command=self.log_in,
                                        style='Accentbutton')
        change_user_button.grid(column=1, row=3, columnspan=2, padx=10, pady=10)

        # Back Home Button
        back_button = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame('UsernamePage'),
                                 style='Accentbutton')
        back_button.grid(column=1, row=4, columnspan=2, padx=10, pady=10)

    def log_in(self):
        password = self.password_entry.get()
        username = self.username_entry.get()

        # Check that the user doesn't leave an empty field
        if my_funcs.check_username_password(username, password):
            self.controller.current_user = username
            print(self.controller.current_user)
            self.controller.current_user_password = password
            self.controller.data = my_funcs.get_user_data(username, password)

            # Check if the user exists
            if type(self.controller.data) == dict:
                self.controller.show_frame('HomePage')

            else:
                self.controller.data = {}
                messagebox.showerror(title='Error', message=f"User {username} does not exist or the password is wrong")

        else:
            messagebox.showerror(title='Error', message=f"Please don't leave any empty field")


class CreateAccountPage(Frame):
    """ 
    A frame where the user can create a new account
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Header Label
        self.header_label = ttk.Label(self, width=20, text="Create an account", foreground='#393E46',
                                      font=self.controller.font, anchor='center')
        self.header_label.grid(column=1, row=0, columnspan=2, padx=10, pady=10)
        # self.username_label.place(x=120, y=200)

        # Username Entry
        username_label = ttk.Label(self, text='Username : [a-z][0-9]')
        username_label.grid(column=1, row=1, padx=10, pady=10)
        self.username_entry = ttk.Entry(self, width=20)
        self.username_entry.grid(column=2, row=1, padx=10, pady=10)

        # Password Entry
        password_label = ttk.Label(self, text='Password : [a-z][0-9]')
        password_label.grid(column=1, row=2, padx=10, pady=10)
        self.password_entry = ttk.Entry(self, width=20)
        self.password_entry.grid(column=2, row=2, padx=10, pady=10)

        # Create Button
        create_button = ttk.Button(self, text="Create account", command=self.create_account,
                                   style='Accentbutton')
        create_button.grid(column=1, row=3, columnspan=2, padx=10, pady=10)

        # Back Home Button
        back_button = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame('UsernamePage'),
                                 style='Accentbutton')
        back_button.grid(column=1, row=4, columnspan=2, padx=10, pady=10)

    def create_account(self):
        password = self.password_entry.get()
        username = self.username_entry.get()

        if my_funcs.check_username_password(username, password):
            params = my_funcs.format_user_params(password=password, username=username)
            response = my_funcs.create_account_request(params=params)

            if response['isSuccess']:
                messagebox.showinfo(title="Congrats", message=f"{response['message']}")
                self.controller.current_user = username
                self.controller.current_user_password = password
                self.controller.data = {}
                self.controller.show_frame('HomePage')
            else:
                messagebox.showerror(title='Error', message=f"{response['message']}")
        else:
            messagebox.showerror(title='Error', message="Please don't leave any empty field")


class DeleteAccountPage(Frame):
    """ A frame where the user can delete an account """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Header Label
        self.header_label = ttk.Label(self, width=20, text="Delete an account", font=self.controller.font,
                                      foreground='#393E46', anchor='center')
        self.header_label.grid(column=1, row=0, columnspan=2, padx=10, pady=10)

        # Username Entry
        username_label = ttk.Label(self, text='Username :')
        username_label.grid(column=1, row=1, padx=10, pady=10)
        self.username_entry = ttk.Entry(self, width=20)
        self.username_entry.grid(column=2, row=1, padx=10, pady=10)

        # Password Entry
        password_label = ttk.Label(self, text='Password :')
        password_label.grid(column=1, row=2, padx=10, pady=10)
        self.password_entry = ttk.Entry(self, width=20)
        self.password_entry.grid(column=2, row=2, padx=10, pady=10)

        # Create Button
        create_button = ttk.Button(self, text="Delete account", command=self.delete_account,
                                   style='Accentbutton')
        create_button.grid(column=1, row=3, columnspan=2, padx=10, pady=10)

        # Back Home Button
        back_button = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame('UsernamePage'),
                                 style='Accentbutton')
        back_button.grid(column=1, row=4, columnspan=2, padx=10, pady=10)

    def delete_account(self):
        password = self.password_entry.get()
        username = self.username_entry.get()

        if my_funcs.check_username_password(username, password):

            # Asks for confirmation
            answer = messagebox.askyesno(title='Are you sure ?',
                                         message=f"You are about to delete the {username} account"
                                                 f", are you sure ? ")
            if answer:
                response = my_funcs.delete_account(username, password)
                if response:
                    if response['isSuccess']:
                        messagebox.showinfo(title='Success !', message=f"{username} has been successfully deleted !")
                    else:
                        messagebox.showerror(title='Error', message=f"{response['message']}")
                else:
                    messagebox.showerror(title='Error', message="This account does not exist")
            else:
                messagebox.showinfo(title='Info', message="No account has been deleted")
        else:
            messagebox.showerror(title='Error', message="Please don't leave any empty field")
