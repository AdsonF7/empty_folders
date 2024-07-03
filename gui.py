from tkinter import Tk, Button, Label, Entry, StringVar, Text, filedialog, messagebox, END

class GUI(Tk):

    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.str_folder = StringVar(self)
        lb_folder = Label(self, text="Folder")
        lb_folder.grid(column=0, row=0)
        et_folder = Entry(self, textvariable=self.str_folder, state="readonly")
        et_folder.grid(column=0, row=1)
        bt_folder = Button(self, text="Folder")
        bt_folder.grid(column=1, row=1)
        bt_folder.bind("<ButtonRelease>", lambda event: self.bt_folder_click(event))
        bt_find = Button(self, text="Find")
        bt_find.grid(column=0, row=2)
        bt_find.bind("<ButtonRelease>", lambda event: self.bt_find_click(event))
        self.tx_result = Text(self)
        self.tx_result.grid(column=0, row=3)
        bt_remove = Button(self, text="Remove")
        bt_remove.grid(column=0, row=4)
        bt_remove.bind("<ButtonRelease>", lambda event: self.bt_remove_click(event))

    def bt_find_click(self, event):
        self.clear_result()
        self.root.init_folder = self.str_folder.get()
        self.root.find_empty_folders()
        print(f"ok find in {self.str_folder.get()}")

    def bt_folder_click(self, event):
        result = filedialog.askdirectory()
        if result:
            self.str_folder.set(result)

    def bt_remove_click(self, event):
        answer = messagebox.askyesno("Proceed?", "Do you really want to delete the empty folders?")
        if answer:
            self.root.remove_empty_folders()

    def insert_result(self, text):
        self.tx_result.insert(END, str(text) + "\n")

    def clear_result(self):
        self.tx_result.delete("1.0", END)