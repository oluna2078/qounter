import tkinter as tk
from tkinter import ttk
import time
from src import brute_force as bf

sums: list[float] = [45.37, 28, 47, 35.4, 73.59, 35.56, 9.7, 38, 5, 4.67, 2.1, 11.87, 40.33, 111, 4036, 50.55, 6, 7, 3, 2, 300, 27.59]


def search():
    progress.start()
    button_print.config(text="hacker mode activated...")
    progress_label.config(text=f"0%")
    progress['value'] = 1
    root.update_idletasks()

    for i in range(len(sums)):
        bf.rec_sum_search(sums, 100, i)
        progress['value'] = 100 / (len(sums) - i)
        progress_made = round(progress['value'])
        progress_label.config(text=f"{progress_made}%")
        root.update_idletasks()
    print("FINISHED")

    button_print.config(text="hack the mainframe")
    progress_label.config(text="")
    root.update_idletasks()
    progress.stop()

root = tk.Tk()
label = tk.Label(root, text="qounter")
label.pack()

button_close = tk.Button(root, text="close", width=25, height=3, command=root.destroy)
button_close.pack(fill='both', side='bottom')

button_print = tk.Button(root, text="hack the mainframe", width=20, height=2, command=search)
button_print.pack(anchor='n')

progress = ttk.Progressbar(root, orient='horizontal', length=500, mode='determinate')
progress.pack(pady=20)

progress_label = tk.Label(root, text="")
progress_label.pack()

root.mainloop()
