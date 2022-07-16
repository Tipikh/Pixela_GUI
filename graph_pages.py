from tkinter import Frame, StringVar, ttk, messagebox
from tkcalendar import DateEntry
from datetime import date
import my_funcs
import random


class GraphPage(Frame):
    """ A frame where the user can create a graph by choosing a
    name (entry), a unit (entry) and a color (combobox) """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.colors = StringVar()

        # Create Graph Label
        self.create_label = ttk.Label(self, text="Create your graphs", font=self.controller.font,
                                      foreground='#393E46', anchor='center')
        self.create_label.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        # Graph Name Entry
        graph_name_label = ttk.Label(self, text='Graph Name :')
        graph_name_label.grid(column=1, row=2, padx=10, pady=10)
        self.graph_name_entry = ttk.Entry(self, width=20)
        self.graph_name_entry.grid(column=2, row=2, padx=10, pady=10)

        # Graph Unit Entry
        graph_unit_label = ttk.Label(self, text='Graph Unit :')
        graph_unit_label.grid(column=1, row=3, padx=10, pady=10)
        self.graph_unit_entry = ttk.Entry(self, width=20)
        self.graph_unit_entry.grid(column=2, row=3, padx=10, pady=10)

        # Graph Color Combobox
        graph_color_label = ttk.Label(self, text='Graph Color :')
        graph_color_label.grid(column=1, row=4, padx=10, pady=10)
        self.graph_color_combo = ttk.Combobox(self, textvariable=self.colors)
        self.graph_color_combo['values'] = (tuple(my_funcs.COLOR_NAMES.keys()))
        # Select randomly a default color
        self.colors.set(random.choice(self.graph_color_combo['values']))
        self.graph_color_combo.state(["readonly"])
        self.graph_color_combo.grid(column=2, row=4, padx=10, pady=10)

        # Create Graph Button
        create_button = ttk.Button(self, text="Create Graph", command=self.create_graph,
                                   style='Accentbutton')
        create_button.grid(column=1, row=5, columnspan=2, padx=10, pady=10)

        # Go Back Button
        back_button = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame('UserPage'),
                                 style='Accentbutton')
        back_button.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

    def create_graph(self):
        """ A function that take the parameters given by the user and
        send a request to the Pixela API in order to create a graph
        with the corresponding name, unit and color """

        username = self.controller.current_user
        graph_id = my_funcs.create_graph_id(self.controller.data)
        graph_name = self.graph_name_entry.get()
        graph_unit = self.graph_unit_entry.get()
        graph_color = my_funcs.COLOR_NAMES[self.graph_color_combo.get()]
        graph_params = my_funcs.format_graph_params(graph_id, graph_name, graph_unit, graph_color)
        header = {"X-USER-TOKEN": self.controller.current_user_password}

        if len(username) > 0 and len(graph_unit) > 0 and username.isspace() is False and graph_unit.isspace() is False:

            if graph_id in self.controller.data.keys():
                messagebox.showerror(title='Error', message=f"The graph {graph_name} already exist")

            elif my_funcs.check_entry(graph_unit):
                my_funcs.create_graph_request(graph_params, username, header)
                self.controller.update_data()
                messagebox.showinfo(title='Success ! ', message=f' The graph "{graph_name}" has been created !')

            else:
                messagebox.showerror(title='Error', message="The symbols '&', '<' and '>' are not authorized in unit")

        else:
            messagebox.showerror(title='Error', message="Please don't leave any empty field")


class UpdatePage(Frame):
    """ A frame where the user can update a graph """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.unit_var = StringVar()

        # Username Label
        self.username_label = ttk.Label(self, text="Update your graphs", font=self.controller.font,
                                        foreground='#393E46', anchor='center')
        self.username_label.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        # Chose Graph
        chose_graph_label = ttk.Label(self, text='Chose Graph :')
        chose_graph_label.grid(column=1, row=2, padx=10, pady=10)
        self.chose_graph_combo = ttk.Combobox(self, state='readonly')
        self.chose_graph_combo.grid(column=2, row=2, padx=10, pady=10)

        # Chose amount
        amount_label = ttk.Label(self, text='Amount :')
        amount_label.grid(column=1, row=3, padx=10, pady=10)
        self.amount_entry = ttk.Entry(self, width=20)
        self.amount_entry.grid(column=2, row=3, padx=10, pady=10)
        self.unit_var.set(self.chose_graph_combo.get())
        unit_label = ttk.Label(self, textvariable=self.unit_var)
        unit_label.grid(column=3, row=3, padx=(0, 50), pady=10)

        self.chose_graph_combo.bind("<<ComboboxSelected>>", lambda _: self.update_unit())

        # Chose date
        date_label = ttk.Label(self, text='Date :')
        date_label.grid(column=1, row=4, padx=10, pady=10)
        self.calendar = DateEntry(self, dateformat=3, width=12, background='blue',
                                  foreground='white', borderwidth=4, Calendar=2018, date_pattern='y/mm/dd')
        self.calendar.grid(row=4, column=2, columnspan=1, padx=10, pady=10)

        # Update Button
        back_button = ttk.Button(self, text="Update", command=self.update_graph,
                                 style='Accentbutton')
        back_button.grid(row=5, column=2, columnspan=1, padx=10, pady=10)

        # Go Back Button
        back_button = ttk.Button(self, text="Go Back", command=lambda: controller.show_frame('UserPage'),
                                 style='Accentbutton')
        back_button.grid(row=6, column=2, columnspan=1, padx=10, pady=10)

        # Delete Graph Button
        delete_graph_button = ttk.Button(self, text="Delete Graph", command=self.delete_graph,
                                         style='Accentbutton')
        delete_graph_button.grid(row=7, column=2, columnspan=1, padx=10, pady=10)

    def update_graph(self):
        """
        Method that take user's input from the Update Page and send
        a request to the Pixela API to update the graph accordingly
        """

        username = self.controller.current_user
        password = self.controller.current_user_password
        graph = self.chose_graph_combo.get()
        graph_id = my_funcs.get_graph_id_from_name(graph, self.controller.data)
        quantity = self.amount_entry.get()
        my_date = self.calendar.get_date().strftime('%Y%m%d')

        # Check that the selected date isn't in the future
        if int(my_date) > int(date.today().strftime('%Y%m%d')):
            messagebox.showerror(title='Error', message=f"Time travel is not available yet !")

        elif len(quantity) > 0:
            quantity = quantity.replace(" ", "")
            if quantity.isnumeric():
                my_funcs.request_update_graph(username, password, graph_id, quantity, my_date)
                messagebox.showinfo(title='Success !', message=f'The graph "{graph}" has been successfully updated !')
            else:
                messagebox.showerror(title='Error', message=f"Please enter an amount (numbers only)")

        else:
            messagebox.showerror(title='Error', message=f"Please enter an amount (numbers only)")

    def delete_graph(self):
        """ Delete the selected graph using the delete_graph function """

        username = self.controller.current_user
        password = self.controller.current_user_password
        graph = self.chose_graph_combo.get()
        graph_id = my_funcs.get_graph_id_from_name(graph, self.controller.data)
        response = my_funcs.delete_graph(username, password, graph_id)

        confirm = messagebox.askyesno(title='Are you sure ?',
                                      message=f'You are about to delete the "{graph}" graph'
                                              f", are you sure ? ")
        if confirm:
            if response['isSuccess']:
                self.controller.update_data()
                self.controller.update_combobox()
                messagebox.showinfo(title='Success !', message=f'The graph "{graph}" has been successfully deleted !')

            else:
                messagebox.showerror(title='Error', message=f"{response['message']}")

        else:
            messagebox.showinfo(title='Info', message="No graph has been deleted")

    def update_unit(self):
        """ Method that set the "unit_var" attribute in order to
        update the displayed unit on the graph page """

        unit_name = my_funcs.get_unit_from_name(self.chose_graph_combo.get(), self.controller.data)
        self.unit_var.set(unit_name)
