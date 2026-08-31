import tkinter as tk
from tkinter import ttk, filedialog
import random
from src import brute_force as bf
from src import categorised_force as cf
from src import csv_handler


class App:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('quonter')

        self.filepath: str = ""

        root.geometry('1000x500')
        root.config(bg='lightcyan3')

        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=7)
        root.rowconfigure(2, weight=2)
        root.rowconfigure(3, weight=2)
        root.rowconfigure(4, weight=1)
        root.rowconfigure(5, weight=10)

        root.columnconfigure(0, weight=3)
        root.columnconfigure(1, weight=3)
        root.columnconfigure(2, weight=3)
        root.columnconfigure(3, weight=2)
        root.columnconfigure(4, weight=2)


        # LABEL app_name
        tk.Label(
            root,
            text="qounter",
            bg='lightcyan2'
        ).grid(row=0, column=0, columnspan=6, ipady=5, sticky='ENW')


        # BUTTON close
        tk.Button(
            root, 
            text="X", 
            command=root.destroy,
            bg='lightcyan4',
            fg='white'
        ).grid(row=0, column=6, ipady=0, ipadx=0, sticky='ENW')


        # LABEL file_path_label
        tk.Label(
            root,
            text="selected CSV:",
            bg='lightcyan3'
        ).grid(row=1, column=1, columnspan=2, sticky='S')


        # LABEL sum_label
        tk.Label(
            root,
            text="sum:",
            bg='lightcyan3'
        ).grid(row=1, column=3, sticky='S')


        # LABEL margin_label
        tk.Label(
            root,
            text="margin:",
            bg='lightcyan3'
        ).grid(row=1, column=4, sticky='S')


        # BUTTON open_file
        tk.Button(
            root, 
            text="open file", 
            width=15,
            height=2, 
            command=self.upload_file,
            bg='white'
        ).grid(row=2, column=0)


        # LABEL file_path
        self.file_label = tk.Label(
            root,
            text="No file selected",
            bg='white'
        )
        self.file_label.grid(row=2, column=1, columnspan=2, ipady=5, sticky='EW')


        # ENTRY sum to calculate
        self.key_entry = tk.Entry(
            root,
            width=6,
        )
        self.key_entry.grid(row=2, column=3, ipady=4)


        # ENTRY +/- margin (optional)
        self.margin_entry = tk.Entry(
            root,
            width=6,
        )
        self.margin_entry.grid(row=2, column=4, ipady=4)


        # BUTTON run_calc
        self.button_run = tk.Button(
            root, 
            text="calculate", 
            width=15, 
            height=2, 
            command=self.search,
            bg='white'
        )
        self.button_run.grid(row=3, column=0)


        # PROGRESS BAR
        self.progress = ttk.Progressbar(
            root, 
            orient='horizontal', 
            mode='determinate'
        )
        self.progress.grid(row=3, column=1, columnspan=4, sticky='EW')


        # LABEL progress_percent
        self.progress_label = tk.Label(
            root, 
            text="",
            width=6,
            bg='lightcyan3'
        )
        self.progress_label.grid(row=3, column=5, sticky='W')


    def search(self):
        sums: list[float] = csv_handler.csv_to_lst(self.filepath)
        key: float = float(self.key_entry.get())
        margin: float

        if self.margin_entry.get() == '':
            margin = 0
        else:
            margin = float(self.margin_entry.get())

        calmness_val: int = random.randint(21, 29)
        self.progress.start()
        self.button_run.config(text="calculating...")
        self.progress['value'] = calmness_val / 3
        self.progress_label.config(text=f"{round(calmness_val / 3)}%")
        self.root.update_idletasks()

        for i in range(len(sums)):
            cf.rec_sum_search(sums, key, i, margin)
            self.progress['value'] = 100 / (len(sums) - i) + calmness_val
            progress_made = round(self.progress['value'])
            if progress_made > 100:
                progress_made = 100
            self.progress_label.config(text=f"{progress_made}%")
            self.root.update_idletasks()
        print("FINISHED\n")

        self.button_run.config(text="calculate")
        self.progress_label.config(text="")
        self.root.update_idletasks()
        self.progress.stop()


    def upload_file(self):
        filepath = filedialog.askopenfilename(title="Select a csv table", filetypes=[("CSV file", "*.csv"), ("All files", "*.*")])
        print("Selected File:", filepath)
        self.file_label.config(text=filepath)
        self.filepath = filepath

root = tk.Tk()
App(root)
root.mainloop()
