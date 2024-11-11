import tkinter as tk

def calculate_square():
    try:
        number = float(entry.get())
        result = number ** 2
        result_label.config(text=f"Квадрат числа: {result}")
    except ValueError:
        result_label.config(text="Пожалуйста, введите корректное число.")

root = tk.Tk()
root.title("Вычисление квадрата числа")

label = tk.Label(root, text="Введите число:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

calculate_button = tk.Button(root, text="Вычислить квадрат", command=calculate_square)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()
