import pathlib
import os
from gui import GUI

class App:

    def __init__(self):
        self.gui = GUI(self)
        self.init_folder = ""
        self.empty_folders = []
        self.gui.mainloop()

    @property
    def init_folder(self):
        return self._init_folder

    @init_folder.setter
    def init_folder(self, value):
        self._init_folder = pathlib.Path(value)
        #if self._init_folder.is_dir():
        #    self.find_empty_folders(self._init_folder)
        
    def find_empty_folders(self, folder=None):
        if folder == None:
            folder = self.init_folder
            self.empty_folders = []
        try: 
            if len(list(folder.iterdir())) == 0:
                self.gui.insert_result(folder)
                self.empty_folders.append(folder)
                return None
            else:
                for i in folder.iterdir():
                    if i.is_dir():
                        self.find_empty_folders(i)
        except WindowsError as e:
            print(e)

    def remove_empty_folders(self):
        for i in self.empty_folders:
            print(i)
            os.rmdir(i)