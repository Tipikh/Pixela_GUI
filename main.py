from tkinter import Tk, Frame
from tkinter import font as tkfont
from user_pages import LoginPage, CreateAccountPage, WelcomePage, DeleteAccountPage, UserPage
from graph_pages import GraphPage, UpdatePage
from tkinter import ttk, messagebox
import my_funcs


class Controller(Tk):
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

        self.show_frame("WelcomePage")

    def show_frame(self, page_name):
        if page_name == 'UpdatePage' and len(self.data) == 0:
            messagebox.showerror(title='Error', message="You don't have any graph yet \n"
                                                        "Use the 'Create Graph' button to create a graph first")

        else:
            for frame in self.frames.values():
                frame.grid_remove()

            frame = self.frames[page_name]
            self.update_combobox()

            if page_name == 'UserPage':
                self.frames['UserPage'].link_var.set(f"https://pixe.la/@{self.current_user}")
                self.frames['UserPage'].greeting_text.set(f"Hello {self.current_user} !")

            elif page_name == 'UpdatePage':
                unit_name = my_funcs.get_unit_from_name(self.frames['UpdatePage'].chose_graph_combo.get(), self.data)
                self.frames['UpdatePage'].unit_var.set(unit_name)

            frame.grid()

    def update_combobox(self):
        """
        This function update the combobox in the UpdatePage
        to ensure that newly created graphs are displayed in it 
        """

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


if __name__ == "__main__":
    app = Controller()
    app.mainloop()
