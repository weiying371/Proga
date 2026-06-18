import tkinter as tk
from tkinter import messagebox

def calculate_system():
    try:
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        c1 = float(entry_c1.get())

        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())
        c2 = float(entry_c2.get())

        D = a1 * b2 - b1 * a2

        if D != 0:
            x = (c1 * b2 - b1 * c2) / D
            y = (a1 * c2 - c1 * a2) / D

            label_result_x.config(text=f"x = {int(x) if x.is_integer() else round(x, 4)}")
            label_result_y.config(text=f"y = {int(y) if y.is_integer() else round(y, 4)}")
        else:
            Dx = c1 * b2 - b1 * c2
            if Dx == 0:
                messagebox.showinfo("Результат", "Система має безліч розв'язків")
            else:
                messagebox.showerror("Помилка", "Система не має розв'язків")

    except ValueError:
        messagebox.showwarning("Помилка введення", "Будь ласка, введіть коректні числа в усі поля!")




root = tk.Tk()
root.title("tk")
root.geometry("320x160")
root.resizable(False, False)

root.columnconfigure((0, 1, 2, 3, 4), pad=5)
root.rowconfigure((0, 1, 2, 3), pad=5)

entry_a1 = tk.Entry(root, width=5, justify="center")
entry_a1.grid(row=0, column=0, padx=(15, 0), pady=(10, 0))

lbl_x1 = tk.Label(root, text="x +")
lbl_x1.grid(row=0, column=1, pady=(10, 0))

entry_b1 = tk.Entry(root, width=5, justify="center")
entry_b1.grid(row=0, column=2, pady=(10, 0))

lbl_y1 = tk.Label(root, text="y =")
lbl_y1.grid(row=0, column=3, pady=(10, 0))

entry_c1 = tk.Entry(root, width=5, justify="center")
entry_c1.grid(row=0, column=4, padx=(0, 15), pady=(10, 0))


entry_a2 = tk.Entry(root, width=5, justify="center")
entry_a2.grid(row=1, column=0, padx=(15, 0))

lbl_x2 = tk.Label(root, text="x +")
lbl_x2.grid(row=1, column=1)

entry_b2 = tk.Entry(root, width=5, justify="center")
entry_b2.grid(row=1, column=2)

lbl_y2 = tk.Label(root, text="y =")
lbl_y2.grid(row=1, column=3)

entry_c2 = tk.Entry(root, width=5, justify="center")
entry_c2.grid(row=1, column=4, padx=(0, 15))


label_result_x = tk.Label(root, text="x = ", font=("Arial", 10))
label_result_x.grid(row=2, column=0, columnspan=2, pady=5)

label_result_y = tk.Label(root, text="y = ", font=("Arial", 10))
label_result_y.grid(row=2, column=2, columnspan=2, pady=5)


btn_calc = tk.Button(root, text="Обчислити", command=calculate_system)
btn_calc.grid(row=3, column=0, columnspan=2, padx=(15, 0), pady=(0, 10), sticky="we")

btn_close = tk.Button(root, text="Закрити", command=root.destroy)
btn_close.grid(row=3, column=3, columnspan=2, padx=(0, 15), pady=(0, 10), sticky="we")

root.mainloop()
