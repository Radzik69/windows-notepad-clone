import tkinter as tk
from tkinter import filedialog


class createGUI:
    def __init__(self):
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

        self.root.protocol("WM_DELETE_WINDOW",self.leave_save_question)

        self.root.mainloop()

    def leave_save_question(self):
        self.leave_app_save_question_messagebox = tk.Toplevel()
        self.leave_app_save_question_messagebox.geometry("250x150")
        self.leave_app_save_question_messagebox.title("Unsaved Changes")

        label = tk.Label(self.leave_app_save_question_messagebox, text="Do you want to save changes?")
        label.pack(pady=10,padx=10)

        buttons_frame = tk.Frame(self.leave_app_save_question_messagebox)
        buttons_frame.pack(pady=10,padx=10)

        save_button = tk.Button(buttons_frame, text="Save",command=self.leave_app_save)
        save_button.pack(side='left', pady=10,padx=10)

        dont_save_button = tk.Button(buttons_frame, text="Don't Save",command=self.leave_app_dont_save)
        dont_save_button.pack(side='left', pady=10,padx=10)

        cancel_button = tk.Button(buttons_frame, text="Cancel",command=self.leave_app_cancel)
        cancel_button.pack(side='left', pady=10,padx=10)

    def leave_app_cancel(self):
        self.leave_app_save_question_messagebox.destroy()

    def leave_app_dont_save(self):
        self.root.destroy()

    def leave_app_save(self):
        #only create file, after opening files is implemented change so its detecting to create new file or override old
        self.filename = filedialog.asksaveasfilename(initialdir="/",title="Save as",initialfile=".txt",defaultextension=".txt",filetypes=(("Text Documents (*.txt)", "*.txt"), ("All Files", "*.*")))
        open(self.filename,"x")
        with open(self.filename,"w") as f:
            f.write(self.text_field.get("1.0","end-1c"))


createGUI()
