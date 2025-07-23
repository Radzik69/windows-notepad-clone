import tkinter as tk
from tkinter import filedialog

class createGUI:
    def __init__(self):
        self.dont_save_button = None
        self.root = tk.Tk()
        self.root.geometry("800x1000")
        self.root.title("Notepad")

        frame = tk.Frame(self.root)
        frame.pack(fill='both', expand=True)

        self.text_field = tk.Text(frame, wrap='word', cursor="xterm", font=("Consolas", 11))
        self.text_field.pack(side='left', fill='both', expand=True)

        self.text_field_scrollbar = tk.Scrollbar(frame, orient='vertical', command=self.text_field.yview)
        self.text_field_scrollbar.pack(side='right', fill='y')
        self.text_field.config(yscrollcommand=self.text_field_scrollbar.set)
        print(self.text_field.get("1.0","end-1c"))

        self.menu = tk.Menu(self.root)
        self.create_top_menu()

        self.root.protocol("WM_DELETE_WINDOW",lambda: self.leave_save_question("leave_app"))

        self.root.mainloop()

    def leave_save_question(self,dont_save_status):
        self.leave_app_save_question_messagebox = tk.Toplevel()
        self.leave_app_save_question_messagebox.geometry("250x150")
        self.leave_app_save_question_messagebox.title("Unsaved Changes")

        label = tk.Label(self.leave_app_save_question_messagebox, text="Do you want to save changes?")
        label.pack(pady=10,padx=10)

        buttons_frame = tk.Frame(self.leave_app_save_question_messagebox)
        buttons_frame.pack(pady=10,padx=10)

        save_button = tk.Button(buttons_frame, text="Save",command=lambda: self.file_save_as(True))
        save_button.pack(side='left', pady=10,padx=10)

        self.dont_save_button = tk.Button(buttons_frame, text="Don't Save")
        self.dont_save_button.pack(side='left', pady=10, padx=10)

        cancel_button = tk.Button(buttons_frame, text="Cancel", command=self.leave_app_cancel)
        cancel_button.pack(side='left', pady=10, padx=10)

        if self.if_text_written()==True:
            if dont_save_status == "leave_app":
                self.dont_save_button.config(command=self.leave_app_dont_save)
            elif dont_save_status == "file_new":
                self.dont_save_button.config(command=self.text_field_delete)
            elif dont_save_status == "file_open":
                self.dont_save_button.config(command=self.open_file)
            else:
                print("Unknown Error")
        else:
            self.root.destroy()


    def leave_app_cancel(self):
        self.leave_app_save_question_messagebox.destroy()

    def leave_app_dont_save(self):
        self.root.destroy()

    def create_top_menu(self):
        file = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=file)
        file.add_command(label='New', command=self.file_new)
        file.add_command(label='New Window', command=None)
        file.add_command(label='Open...', command=self.file_open)
        file.add_command(label='Save', command=None)
        file.add_command(label='Save as', command=lambda: self.file_save_as(False))
        file.add_separator()
        file.add_command(label='Page setup...', command=None)
        file.add_command(label='Print...', command=None)
        file.add_separator()
        file.add_command(label='Exit', command=self.leave_save_question)

        self.root.config(menu = self.menu)

    def file_new(self):
        if self.if_text_written()==False:
            self.text_field_delete()
        elif self.if_text_written()==True:
            self.leave_save_question("file_new")
        else:
            print("Unknown Error")

    def file_new_windows(self):
        print("NEW WINDOW")

    def file_open(self):
        if self.if_text_written()==False:
            self.open_file()
        elif self.if_text_written()==True:
            self.leave_save_question("file_open")
        else:
            print("Unknown Error")

    def file_save_as(self,if_leave_app):
        try:
            self.leave_app_save_question_messagebox.destroy()
        except Exception:
            print(Exception)
        self.leave_app_save_filename = filedialog.asksaveasfilename(initialdir="/", title="Save as", initialfile=".txt",defaultextension=".txt",filetypes=(("Text Documents (*.txt)", "*.txt"), ("All Files", "*.*")))
        open(self.leave_app_save_filename, "x")
        with open(self.leave_app_save_filename, "w") as f:
            f.write(self.text_field.get("1.0", "end-1c"))
        if if_leave_app == True:
            self.root.destroy()

    def if_text_written(self):
        if self.text_field.get("1.0","end-1c")!="":
            return True
        else:
            return False

    def text_field_delete(self):
        self.text_field.delete("1.0", "end-1c")
        self.leave_app_save_question_messagebox.destroy()

    def open_file(self):
        self.open_file_filename = filedialog.askopenfilename(title="Open",initialdir='/',filetypes=(("Text Documents (*.txt)", "*.txt"), ("All Files", "*.*")))
        self.text_field_delete()
        with open(self.open_file_filename) as f:
            self.text_field.insert(tk.END, f.readline())
            f.close()


createGUI()
