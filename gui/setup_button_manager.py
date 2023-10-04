import tkinter as tk
from tkinter import ttk, messagebox
from utils.api_handler import OpenaiApiKeyHandler as OAKH
from title_page_controler import ButtonState as BS


class ApiKeySetupButtonOpenAi(ttk.Button):  
    def __init__(self, parent, select_openai_inst):
        super().__init__(parent, text="Add API key", command=self.manage_api_key)
        self.openai_inst = select_openai_inst
    def manage_api_key(self):
        if OAKH.ask_for_key():
            BS.openai_key_set = True
            self.openai_inst.set_openai_state(False)

class SelectOpenAiButton(ttk.Button):  
    def __init__(self, parent):
        super().__init__(parent, text="OpenAI", command=self.openai_selected)
        BS.check_openai_key()
        self.set_openai_state(False)

    def openai_selected(self):
        self.result = BS.toggle_openai_selected()
        self.select_alternative.set_alter_state(self.result)
        self.set_color(self.result)


    def set_color(self, state):
        style = ttk.Style()
        if state:
            style.configure("Alternative.TButton", background="green")
        else:
            style.configure("Alternative.TButton", background="gray90")
        self.config(style="Alternative.TButton")   

    def set_openai_state(self, state):
        if state is False and BS.openai_key_set:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)


class SelectAlternativeButton(ttk.Button):  
    def __init__(self, parent, ):
        super().__init__(parent, text="Alternative (in developement)", command=self.alter_selected)

    def alter_selected(self):
        self.result = BS.toggle_alter_selected()
        self.select_openai.set_openai_state(self.result)
        self.set_color(self.result)

    def set_color(self, state):
        style = ttk.Style()
        if state:
            style.configure("Alternative.TButton", background="green")
        else:
            style.configure("Alternative.TButton", background="gray90")
        self.config(style="Alternative.TButton")        

    def set_alter_state(self, state):
        if state is False:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)



class StartMainGuiButton(ttk.Button):  
    def __init__(self, parent, argi):
        super().__init__(parent, text="Start!", command=self.start_main_gui)
        self.argi = argi
        if BS.openai_selected:
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)
    
    def start_main_gui(self):
        if BS.openai_selected:
            BS.ready_to_start = True
        else:
            messagebox.showinfo("Info", "An alternative transcriber is under development")
        self.argi.destroy_all_widgets()
        self.argi.start_main_frame_and_widgets()