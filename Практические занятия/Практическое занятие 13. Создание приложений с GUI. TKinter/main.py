import tkinter as tk
import requests
from tkinter import messagebox

def get_fact():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Ошибка ввода", "Пожалуйста, введите название города!")
        return

    url = f"https://ru.wikipedia.org/api/rest_v1/page/summary/{city}"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            title = data.get('title', 'Нет названия')
            description = data.get('extract', 'Нет описания')
            result_label.config(text=f"Название: {title}\nОписание: {description}")
        else:
            messagebox.showerror("Ошибка", "Город не найден в Wikipedia.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка запроса", f"Произошла ошибка: {e}")

root = tk.Tk()
root.title("Поиск исторических фактов")

city_label = tk.Label(root, text="Введите название города:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Получить исторический факт", command=get_fact)
search_button.pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()
