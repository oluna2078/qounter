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

        root.geometry('700x500')

        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=3)
        root.rowconfigure(2, weight=3)
        root.rowconfigure(3, weight=1)
        root.rowconfigure(4, weight=15)
        root.rowconfigure(5, weight=2)

        root.columnconfigure(0, weight=3)
        root.columnconfigure(1, weight=3)
        root.columnconfigure(2, weight=3)
        root.columnconfigure(3, weight=3)
        root.columnconfigure(4, weight=1)

        label = tk.Label(
                root,
                text="qounter"
        ).grid(row=0, column=0, columnspan=5)


        button_close = tk.Button(
                root, 
                text="close", 
                width=25, 
                height=3, 
                command=root.destroy
        ).grid(row=5, column=0, columnspan=5, sticky='EW')


        button_open_file = tk.Button(
                root, 
                text="open file", 
                height=2, 
                command=self.upload_file
        ).grid(row=1, column=0, sticky='EW')


        self.file_label = tk.Label(
                root,
                text="No file selected"
        )
        self.file_label.grid(row=1, column=1, columnspan=4, sticky='EW')


        self.button_print = tk.Button(
                root, 
                text="hack the mainframe", 
                width=20, 
                height=2, 
                command=self.search
        )
        self.button_print.grid(row=3, column=0, columnspan=5)


        self.progress = ttk.Progressbar(
                root, 
                orient='horizontal', 
                length=500, 
                mode='determinate'
        )
        self.progress.grid(row=2, column=0, columnspan=4, sticky='EW')


        self.progress_label = tk.Label(
                root, 
                text=""
        )
        self.progress_label.grid(row=2, column=5)

    def search(self):
        sums: list[float] = csv_handler.csv_to_lst(self.filepath)

        calmness_val: int = random.randint(21, 29)
        self.progress.start()
        self.button_print.config(text="hacker mode activated...")
        self.progress['value'] = calmness_val / 3
        self.progress_label.config(text=f"{round(calmness_val / 3)}%")
        root.update_idletasks()

        for i in range(len(sums)):
            cf.rec_sum_search(sums, 421.24, i)
            self.progress['value'] = 100 / (len(sums) - i) + calmness_val
            progress_made = round(self.progress['value'])
            if progress_made > 100:
                progress_made = 100
            self.progress_label.config(text=f"{progress_made}%")
            root.update_idletasks()
        print("FINISHED")

        self.button_print.config(text="hack the mainframe")
        self.progress_label.config(text="")
        root.update_idletasks()
        self.progress.stop()


    def upload_file(self):
        filepath = filedialog.askopenfilename(title="Select a csv table", filetypes=[("CSV file", "*.csv"), ("All files", "*.*")])
        print("Selected File:", filepath)
        self.file_label.config(text=filepath)
        self.filepath = filepath



root = tk.Tk()

app = App(root)

root.mainloop()
