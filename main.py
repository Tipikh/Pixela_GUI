from tkinter import Tk, Frame, Label, StringVar
from tkinter import font as tkfont
from user_pages import LoginPage, CreateAccountPage, WelcomePage, DeleteAccountPage
from graph_pages import GraphPage, UpdatePage
from tkinter import ttk, messagebox
import my_funcs


class Control(Tk):
    """
    A class for managing the GUI frames
    Children of the Tk class from tkinter

    Attributes
    ----------

    current_user : str
        username of the currently logged user

    current_user_password : str
        password of the currently logged user
    
    data : dict
        datas (graphs) of the currently logged user

    container : tkinter.Frame()
        The container is where we'll stack all the frames
        on top of each other, then the one we want visible
        will be raised above the others

    Methods
    -------
    show_frame(page_name)
        Show the page given as parameter

    update_combobox() 
        Update the combobox in the UpdatePage to ensure that
        newly created graphs are displayed in it
    """

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.style = ttk.Style(self)
        self.tk.call('source', './azure/azure.tcl')
        self.style.theme_use('azure')
        self.font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.title_font = tkfont.Font(family='Helvetica', size=28, weight="bold")
        self.title('Pixela')
        self.config(padx=20, pady=20)
        self.current_user = None
        self.current_user_password = None
        self.data = {}

        # Increase button's font size
        buttons_font = tkfont.nametofont("TkDefaultFont")
        buttons_font.configure(size=12)

        # Prevent window resizing
        self.resizable(False, False) 

        # Create a container in which we'll put all the other frames
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        for F in (UserPage, WelcomePage, LoginPage, CreateAccountPage, GraphPage, UpdatePage, DeleteAccountPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("UsernamePage")

    def show_frame(self, page_name):
        if page_name == 'UpdatePage' and len(self.data) == 0:
            messagebox.showerror(title='Error', message="You don't have any graph yet \n"
                                                        "Use the 'Create Graph' button to create a graph first")

        else:
            for frame in self.frames.values():
                frame.grid_remove()

            frame = self.frames[page_name]
            self.update_combobox()

            if page_name == 'HomePage':
                self.frames['HomePage'].link_var.set(f"https://pixe.la/@{self.current_user}")
                self.frames['HomePage'].greeting_text.set(f"Hello {self.current_user} !")

            elif page_name == 'UpdatePage':
                unit_name = my_funcs.get_unit_from_name(self.frames['UpdatePage'].chose_graph_combo.get(), self.data)
                self.frames['UpdatePage'].unit_var.set(unit_name)

            frame.grid()

    def update_combobox(self):
        """
        This function update the combobox in the UpdatePage
        to ensure that newly created graphs are displayed in it 
        """
        
        print("J'exécute update_combobox")

        graph_list = [graph for graph in self.data.keys()]
        graph_names_list = [self.data[graphe]['name'] for graphe in graph_list]
        combo_values = tuple(graph_names_list)
        self.frames["UpdatePage"].chose_graph_combo['values'] = combo_values
        if len(graph_names_list) > 0:
            self.frames["UpdatePage"].chose_graph_combo.set(graph_names_list[0])
        else:
            self.frames["UpdatePage"].chose_graph_combo.set('There is no graph')

    def update_data(self):
        self.data = my_funcs.get_user_data(self.current_user, self.current_user_password)


class UserPage(Frame):
    """ 
    A frame whith 3 buttons, one to change the user, one to create 
    a new graph and one to update an existing graph
    Also contain a link to the user's Pixela page
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.link_var = StringVar()
        self.greeting_text = StringVar()

        # Greetings label
        greetings = ttk.Label(self, textvariable=self.greeting_text,
                              foreground='#393E46', font=self.controller.font, anchor='center')
        greetings.grid(row=0, column=1, padx=10, pady=15)

        # Greetings next label
        greetings_2 = ttk.Label(self, text="What do you want to do ?",
                                foreground='#393E46', font=self.controller.font, anchor='center')
        greetings_2.grid(row=1, column=1, padx=10, pady=15)

        # Change User Button
        change_user_button = ttk.Button(self, text="Change User", command=lambda: controller.show_frame('UsernamePage'),
                                        style='Accentbutton')
        change_user_button.grid(row=2, column=1, ipadx=22, ipady=10, padx=10, pady=15)

        # Graph Page Button
        graph_button = ttk.Button(self, text="Create Graph", command=lambda: controller.show_frame('GraphPage'),
                                  style='Accentbutton')
        graph_button.grid(row=3, column=1, ipadx=20, ipady=10, padx=10, pady=15)

        # Update Graph Page Button
        update_button = ttk.Button(self, text="Update Graphs", command=lambda: controller.show_frame('UpdatePage'),
                                   style='Accentbutton')
        update_button.grid(row=4, column=1, ipadx=12, ipady=10, padx=10, pady=15)

        # Visit label
        visit_label = ttk.Label(self, text='Visit your page :')
        visit_label.grid(column=1, row=5, padx=10, pady=(20, 0))

        # Link to the user's page
        link1 = Label(self, textvariable=self.link_var, fg='blue', cursor="hand2")
        link1.grid(row=6, column=1, ipadx=10, ipady=10, padx=10, pady=(0, 10))
        link1.bind("<Button-1>", lambda e: my_funcs.callback(f"https://pixe.la/@{self.controller.current_user}"))



if __name__ == "__main__":
    app = Control()
    app.mainloop()
